from kep import KEP()
  
kep = KEP()
kep.__update_from_current_month__()

def test_current_month_row_system():
    assert kep.__rs__.__len__()['datapoints'] > 0 

def test_kep():
    assert a.len() > 0 
    dfm = kep.monthly_df()
    dfa = kep.annual_df()
    dfq = kep.quarter_df()
    # somethign else here - maybe from final use examples?    

def test_fiscal_inidciators_present():
    #WARNING: labels do not quarantee proper data in dataset  
    for lab in ['GOV_CONSOLIDATED_EXPENSE_ACCUM', 'GOV_CONSOLIDATED_REVENUE_ACCUM', 
                'GOV_FEDERAL_EXPENSE_ACCUM', 'GOV_FEDERAL_REVENUE_ACCUM', 'GOV_FEDERAL_SURPLUS_ACCUM', 
                'GOV_SUBFEDERAL_EXPENSE_ACCUM', 'GOV_SUBFEDERAL_REVENUE_ACCUM', 'GOV_SUBFEDERAL_SURPLUS_ACCUM']:
        assert lab in a.head_labels()  
   
if '__main__' = __name__:   
   kep.publish()