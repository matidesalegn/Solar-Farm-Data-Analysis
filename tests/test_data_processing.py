def test_read_csv_with_check():
    # Test that the function returns a DataFrame when given a valid filename
    df = read_csv_with_check('valid_filename.csv')
    assert isinstance(df, pd.DataFrame)

    # Test that the function returns None when given an invalid filename
    df = read_csv_with_check('invalid_filename.csv')
    assert df is None