---  
title: Convert Excel to CSV, TSV, and TXT  
linktitle: Save as CSV, TSV, and TXT  
type: docs  
weight: 40  
url: /python-net/convert-excel-to-csv-tsv-and-txt/  
description: Convert Excel to CSV, TSV, and TXT by using Aspose.Cells for Python via .NET API.  
keywords: Python Convert Excel to CSV, TSV, and TXT, Convert Excel to CSV, TSV, and TXT in Python via .NET, Python Convert Workbook to CSV, TSV, and TXT.  
ai_search_scope: cells_pythonnet  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask" 
---  

{{% alert color="primary" %}}  

Aspose.Cells for Python via .NET makes it possible to convert Excel, ODS, JSON, and other format files to CSV, TSV, and TXT.  

{{% /alert %}}  

## **Saving Workbook to Text or CSV Format**  

Sometimes, you want to convert or save a workbook with multiple worksheets into a text format. For text formats (for example, TXT, tab‑delimited, CSV, etc.), by default both Microsoft Excel and Aspose.Cells for Python via .NET save the contents of the active worksheet only.  

The following code example explains how to save an entire workbook into a text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (e.g., XLS, XLSX, XLSM, XLSB, ODS, and so on) with any number of worksheets.  

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.  

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) is a comma, so do not specify a separator if saving to CSV format.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}  

## **Saving Text Files with Custom Separator**  

Text files contain spreadsheet data without formatting. The file is a plain‑text file that can have customized delimiters between its data.  

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}  

## **Advanced topics**  
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](/cells/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)  
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)  
{{< app/cells/assistant language="python-net" >}}
