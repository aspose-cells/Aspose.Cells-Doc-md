---
title: Save Workbook to Strict Open XML Spreadsheet Format
type: docs
weight: 150
url: /python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Possible Usage Scenarios**

Aspose.Cells for Python via .NET allows you to save the workbook in *Strict Open XML Spreadsheet* format. For that purpose, it provides the [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) property. If you set its value as [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance), then the output Excel file will be saved in Strict Open XML Spreadsheet format.

## **Save Workbook to Strict Open XML Spreadsheet Format**

The following sample code creates a workbook and sets the value of the [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) property as [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) and saves it as [output Excel file](67338272.xlsx). If you open the output Excel file in Microsoft Excel and open the Save As... dialog box, you will see its format as *Strict Open XML Spreadsheet* as shown in this screenshot.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

{{< app/cells/assistant language="python-net" >}}