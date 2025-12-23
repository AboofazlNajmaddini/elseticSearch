from elasticsearch import Elasticsearch

def get_client():
    return Elasticsearch("http://elasticsearch:9200")

def create_index_if_not_exists(es, index_name="books"):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

def index_document(es, index_name="books", doc_id=1, document=None):
    if document is None:
        document = {
            "title": "Learning DevOps",
            "author": "aboofazl najmaddini",
            "year": 2025
        }
    return es.index(index=index_name, id=doc_id, document=document)

def search_documents(es, index_name="books", author_name="aboofazl"):
    es.indices.refresh(index=index_name) 
    result = es.search(index=index_name, query={"match": {"author": author_name}})
    return result['hits']['hits']