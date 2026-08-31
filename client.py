class CorporateIdentityStationeryBusinessCardSynthesizerClient:
    def synthesize_stationery_suite(self, organization_name='AeroDynamics Autonomous Systems', individual_name='Alexander Cross', role_title='Chief Architect'):
        return {
            'stationery_suite_id': 'stn_syn_8812',
            'organization': organization_name,
            'business_card_nfc_vcard_encoded': True,
            'letterhead_bleed_grid_aligned': True,
            'vector_business_card_pdf_url': 'https://brand.genpark.ai/stationery/8812_card.pdf',
            'corporate_letterhead_docx_url': 'https://brand.genpark.ai/stationery/8812_letterhead.docx'
        }
