---
title: AutoFit Columns and Rows while loading HTML in Workbook
type: docs
weight: 120
url: /net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Possible Usage Scenarios**

You can autofit columns and rows while loading your HTML file inside the Workbook object. Please set the **[HtmlLoadOptions.AutoFitColsAndRows](https://apireference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** property to **true** for this purpose.

## **AutoFit Columns and Rows while loading HTML in Workbook**

The following sample code first loads the sample HTML into Workbook without any load options and saves it in XLSX format. It then again loads the sample HTML into Workbook but this time, it loads the HTML after setting the **[HtmlLoadOptions.AutoFitColsAndRows](https://apireference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** property to **true** and saves it in XLSX format. Please download both the output excel files i.e.[Output Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) and [Output Excel File With AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). The following screenshot shows the effect of **[HtmlLoadOptions.AutoFitColsAndRows](https://apireference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** property on both output excel files.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Sample Code**

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}
