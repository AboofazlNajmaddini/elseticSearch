import pytest
from elasticsearch_client import (
    get_client,
    create_index_if_not_exists,
    index_document,
    search_documents,
)

@pytest.fixture
def es_client():
    es = get_client()
    if not es.ping():
        pytest.fail("Error")
    yield es  

@pytest.fixture
def clean_index(es_client):
    index_name = "test_books"
    if es_client.indices.exists(index=index_name):
        es_client.indices.delete(index=index_name)
    yield index_name 
    if es_client.indices.exists(index=index_name):
        es_client.indices.delete(index=index_name)

def test_connection(es_client):
    assert es_client.ping() is True
    info = es_client.info()
    assert "cluster_name" in info

def test_create_index(es_client, clean_index):
    index_name = clean_index
    create_index_if_not_exists(es_client, index_name)
    assert es_client.indices.exists(index=index_name)

def test_index_and_search_single_document(es_client, clean_index):
    index_name = clean_index

    create_index_if_not_exists(es_client, index_name)

    test_doc = {
        "title": "DevOps",
        "author": "aboofazl",
        "year": 2025
    }

    index_document(es_client, index_name=index_name, doc_id=1, document=test_doc)

    results = search_documents(es_client, index_name=index_name, author_name="aboofazl")

    assert len(results) == 1
    assert results[0]['_source']['title'] == "DevOps"
    assert results[0]['_source']['author'] == "aboofazl"

def test_search_no_match(es_client, clean_index):
    index_name = clean_index

    create_index_if_not_exists(es_client, index_name)

    doc = {"title": "تست", "author": "someone_else", "year": 2024}
    index_document(es_client, index_name=index_name, doc_id=1, document=doc)

    results = search_documents(es_client, index_name=index_name, author_name="aboofazl")

    assert len(results) == 0 