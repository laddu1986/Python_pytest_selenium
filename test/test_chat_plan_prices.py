from data.generator import expected_data
from pages.chat_compare import ChatComparePage


def test_chat_plan_prices(app):
    app.navigate_to_chat_compare_page()
    chat_compare_page = ChatComparePage(app)
    lite_plan = chat_compare_page.get_chat_prices('lite')
    team_plan = chat_compare_page.get_chat_prices('team')
    professional_plan = chat_compare_page.get_chat_prices('professional')
    enterprise_plan = chat_compare_page.get_chat_prices('enterprise')
    assert lite_plan == expected_data['lite']
    assert team_plan == expected_data['team']
    assert professional_plan == expected_data['professional']
    assert enterprise_plan == expected_data['enterprise']
