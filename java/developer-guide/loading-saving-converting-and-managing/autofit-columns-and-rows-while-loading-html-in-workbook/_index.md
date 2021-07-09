---
title: AutoFit Columns and Rows while loading HTML in Workbook
type: docs
weight: 70
url: /java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Possible Usage Scenarios**

You can autofit columns and rows while loading your HTML file inside the **[Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook)** object. Please set the **[HtmlLoadOptions.AutoFitColsAndRows](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** property to **true** for this purpose.

## **AutoFit Columns and Rows while loading HTML in Workbook**

The following sample code first loads the sample HTML into Workbook without any load options and saves it in XLSX format. It then again loads the sample HTML into Workbook but this time, it loads the HTML after setting the **[HtmlLoadOptions.AutoFitColsAndRows](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** property to **true** and saves it in XLSX format. Please download both the output excel files i.e.[Output Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) and [Output Excel File With AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). The following screenshot shows the effect of **[HtmlLoadOptions.AutoFitColsAndRows](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** property on both output excel files.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
