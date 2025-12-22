from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

if es.ping():
    print("conection Elasticsearch is secure!")

    if not es.indices.exists(index="books"):
        es.indices.create(index="books")

    # داکیومنت جدید
    doc = {
        "title": "learning DevOps",
        "author": "aboofazl najmaddini", 
        "year": 2025
    }

    es.index(index="books", id=1, document=doc)
    print("document saved sucsessfully!")

    es.indices.refresh(index="books")

    response = es.get(index="books", id=1)
    print("document has been saved:", response['_source'])

    result = es.search(index="books", query={"match": {"author": "aboofazl"}})
    print("NUMBER OF RESULTS:", result['hits']['total']['value'])
    print("RESULT:")
    for hit in result['hits']['hits']:
        print(hit['_source'])

else:
    print("not connected!")