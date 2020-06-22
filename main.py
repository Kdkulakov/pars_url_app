# -*- coding: utf-8 -*-
from odoo import fields, models, api
from urllib.parse import urlparse, parse_qs


class ParseUrl(models.Model):
    _inherit = 'crm.lead'

    def set_campaign_id(self):
        if self.referred:
            url_parse = urlparse(self.referred)
            url_query = parse_qs(url_parse.query)
            value = url_query['campaign_id'][0]

            if "campaign_id" in self.referred:
                self.campaign_id = value
            else:
                self.campaign_id = "None"
        else:
            self.campaign_id = self.campaign_id

    def set_source_id(self):
        if self.referred:
            url_parse = urlparse(self.referred)
            url_query = parse_qs(url_parse.query)
            value = url_query['source_id'][0]

            if "source_id" in self.referred:
                self.source_id = value
            else:
                self.source_id = "None"
        else:
            self.source_id = self.source_id

    def set_medium_id(self):
        if self.referred:
            url_parse = urlparse(self.referred)
            url_query = parse_qs(url_parse.query)
            value = url_query['medium_id'][0]

            if "medium_id" in self.referred:
                self.medium_id = value
            else:
                self.medium_id = "None"
        else:
            self.medium_id = self.medium_id

    campaign_id = fields.Char(
        compute='set_campaign_id'
    )

    medium_id = fields.Char(
        compute='set_medium_id'
    )

    source_id = fields.Char(
        compute='set_source_id'
    )