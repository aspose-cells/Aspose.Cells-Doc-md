import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)