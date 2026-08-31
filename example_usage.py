from client import CorporateIdentityStationeryBusinessCardSynthesizerClient

def main():
    client = CorporateIdentityStationeryBusinessCardSynthesizerClient()
    res = client.synthesize_stationery_suite('Quantum Dynamics Lab', 'Dr. Sarah Connor', 'VP of Research')
    print('Stationery Suite Synthesizer: ' + res['stationery_suite_id'] + ' (' + res['organization'] + ')')
    print('NFC vCard: ' + str(res['business_card_nfc_vcard_encoded']) + ' | Grid Aligned: ' + str(res['letterhead_bleed_grid_aligned']))
    print('Business Card PDF: ' + res['vector_business_card_pdf_url'])
    print('Letterhead DOCX: ' + res['corporate_letterhead_docx_url'])

if __name__ == '__main__':
    main()
