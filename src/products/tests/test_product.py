import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def category(mixer):
    return mixer.blend("products.Category", name="Игрушки")


@pytest.fixture
def product(mixer, category):
    return mixer.blend("products.Product", category=category, name="Зелебоба")


def test_product_list(api, product, category):
    result = api.get("/api/v1/products/")

    assert result[0]["id"] == product.id
    assert result[0]["name"] == "Зелебоба"
    assert result[0]["category"]["id"] == category.id
    assert result[0]["category"]["name"] == "Игрушки"


def test_product_retrive(api, product, category):
    result = api.get(f"/api/v1/products/{product.id}/")

    assert result["id"] == product.id
    assert result["name"] == "Зелебоба"
    assert result["category"]["id"] == category.id
    assert result["category"]["name"] == "Игрушки"
