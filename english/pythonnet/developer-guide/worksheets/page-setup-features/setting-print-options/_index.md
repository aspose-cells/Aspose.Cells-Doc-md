---
title: Setting Print Options
type: docs
weight: 40
url: /python-net/setting-print-options/
description: This article demonstrates how to programmatically set the Print Options of the Excel Worksheet Page Setup feature using the Aspose.Cells for Python via .NET API. You can set the Print Area, Print Titles and Page Order.
keywords: Python Excel Library, Python set excel print area, Python set excel print titles, Python how to set excel page order, Python How to Set Print Options, Python How to Set Print Area, Python How to Set Print Titles. 
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel's page setup settings provide several print options (also referred to as sheet options) that allow users to control how worksheet pages are printed.

{{% /alert %}}

## **How to Set Print Options**

These print options allow users to:

- Select a specific print area on a worksheet.
- Print titles.
- Print gridlines.
- Print row/column headings.
- Achieve draft quality.
- Print comments.
- Print cell errors.
- Define page ordering.

Aspose.Cells for Python via .NET supports all the print options offered by Microsoft Excel and developers can easily configure these options for worksheets using the properties offered by the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class. How these properties are used is discussed below in more detail.

## **How to Set Print Area**

By default, the print area incorporates all areas of the worksheet that contain data. Developers can establish a specific print area of the worksheet.

To select a specific print area, use the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class' [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) property. Assign a cell range that defines the print area to this property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **How to Set Print Titles**

Aspose.Cells for Python via .NET allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class' [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) and [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **How to Set Other Print Options**

The [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class also provides several other properties to set general print options as follows:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): a Boolean property that defines whether to print gridlines or not.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): a Boolean property that defines whether to print row and column headings or not.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): a Boolean property that defines whether to print the worksheet in black and white mode or not.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): defines whether to display the print comments on the worksheet or at the end of the worksheet.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): a Boolean property that defines whether to print the sheet without graphics.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): defines whether to print cell errors as displayed, blank, dash or N/A.

To set the [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) and [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) properties, Aspose.Cells also provides two enumerations, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype), and [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) that contain pre‑defined values to be assigned to the respective properties.

The pre‑defined values in the [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) enumeration are listed below with their descriptions.

|**Print Comments Types**|**Description**|
| :- | :- |
|PRINT_IN_PLACE|Specifies to print comments as displayed on the worksheet.|
|PRINT_NO_COMMENTS|Specifies not to print comments.|
|PRINT_SHEET_END|Specifies to print comments at the end of the worksheet.|

The pre‑defined values of the [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) enumeration are listed below with their descriptions.

|**Print Errors Types**|**Description**|
| :- | :- |
|PRINT_ERRORS_BLANK|Specifies not to print errors.|
|PRINT_ERRORS_DASH|Specifies to print errors as “--”.|
|PRINT_ERRORS_DISPLAYED|Specifies to print errors as displayed.|
|PRINT_ERRORS_NA|Specifies to print errors as “#N/A”.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **How to Set Page Order**

The [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class provides the [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) property that is used to order multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows.

- **Down then over:** prints all the pages down before printing any pages to the right.
- **Over then down:** prints pages left to right before printing the pages below.

Aspose.Cells provides an enumeration, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) that contains all pre‑defined order types.

The pre‑defined values of the [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) enumeration are listed below.

|**Print Order Types**|**Description**|
| :- | :- |
|DOWN_THEN_OVER|Represents printing order as down then over.|
|OVER_THEN_DOWN|Represents printing order as over then down.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
