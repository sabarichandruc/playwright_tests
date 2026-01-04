from playwright.sync_api import sync_playwright, APIRequestContext

def test_get_booking_ids():
    with sync_playwright() as p:
        request_context: APIRequestContext = p.request.new_context(base_url="https://restful-booker.herokuapp.com")
        response = request_context.get("https://restful-booker.herokuapp.com/booking/39")
        assert response.status == 200
        assert response.json() is not None
        print("Status Code:", response.status)
        print("Response Body:", response.json())
        
