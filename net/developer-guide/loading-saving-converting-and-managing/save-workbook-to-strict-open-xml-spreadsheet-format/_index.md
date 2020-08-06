---
title: Save Workbook to Strict Open XML Spreadsheet Format
type: docs
weight: 150
url: /net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to save the workbook in *Strict Open XML Spreadsheet* format. For that purpose, it provides the [Workbook.Settings.Compliance](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/compliance) property. If you set its value as [OoxmlCompliance.Iso29500_2008_Strict](https://apireference.aspose.com/net/cells/aspose.cells/ooxmlcompliance), then the output Excel file will be saved in Strict Open XML Spreadsheet format.
## **Save Workbook to Strict Open XML Spreadsheet Format**
The following sample code creates a workbook and sets the value of the [Workbook.Settings.Compliance](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/compliance) property as [OoxmlCompliance.Iso29500_2008_Strict](https://apireference.aspose.com/net/cells/aspose.cells/ooxmlcompliance) and saves it as [output Excel file](attachments/66945466/67338272.xlsx). If you open the output Excel file in Microsoft Excel and open the Save As... dialog box, you will see its format as *Strict Open XML Spreadsheet* as shown in this screenshot.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}