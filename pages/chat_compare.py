from model.chat import Chat


class ChatComparePage:

    def __init__(self, app):
        self.app = app
        self.header = app.wd.find_element_by_css_selector('.masthead-product')
        self.hero_section = app.wd.find_element_by_css_selector('.chat-hero')
        self.sticky_menu = app.wd.find_element_by_css_selector('.nav-sticky-menu')
        self.compare_table = app.wd.find_element_by_css_selector('.compare-table')
        self.trial_section = app.wd.find_element_by_css_selector('.cta-section')
        self.footer = app.wd.find_element_by_css_selector('.mega-footer')
        self.legal_section = app.wd.find_element_by_css_selector('.legal')

    def get_chat_prices(self, plan):

        if plan == 'lite':
            column_number = 2
        elif plan == 'team':
            column_number = 3
        elif plan == 'professional':
            column_number = 4
        elif plan == 'enterprise':
            column_number = 5
        else:
            raise ValueError('Unrecognized chat plan "%s"' % plan)

        prices = []
        # get only 3 first cells which belong to "Zendesk Chat Pricing" section
        column_selector = 'tr:not(.compare-table-key):not(.compare-table-header) td:nth-of-type(%s) span' % column_number
        price_column = self.app.wd.find_elements_by_css_selector(column_selector)[:3]

        for cell in price_column:
            prices.append(cell.text)

        # string slicing is needed to remove currency sign (it is user locale dependant)
        return Chat(yr_price=prices[0][1:], mnth_price=prices[1][1:], agents=prices[2])
