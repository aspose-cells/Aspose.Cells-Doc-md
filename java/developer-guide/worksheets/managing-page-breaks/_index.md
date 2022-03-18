---
title: Managing Page Breaks
type: docs
weight: 30
url: /java/managing-page-breaks/
---

{{% alert color="primary" %}}

A page break is a place in the text where one page ends and the next one begins. Microsoft Excel can add page breaks at any selected cell in a worksheet.
The page ends at the cell where the page break is added and all the data after the page break is printed on the next page. In simple words, page breaks split worksheets into multiple pages. It is also possible to add page breaks to worksheets at runtime using Aspose.Cells. Aspose.Cells supports two kinds of page break:

- horizontal
- vertical.

This article describes that how to add horizontal or vertical page breaks into worksheets using Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells & Page Breaks**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) that represents an Excel file. The [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**WorksheetCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet) class which provides a wide range of properties and methods for managing worksheets. To add the page breaks, use the [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet) class' [**HorizontalPageBreaks**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) and [**VerticalPageBreaks**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) properties.

The [**HorizontalPageBreaks**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) and [**VerticalPageBreaks**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) properties are in fact collections that may contain several page breaks. Each collection contains several methods for managing horizontal and vertical page breaks. How these methods are used is discussed below.

## **Adding Page Breaks**

To add a page break in a worksheet, insert vertical and horizontal page breaks at the specified cell by calling the [**HorizontalPageBreaks**](https://apireference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) and [**VerticalPageBreaks**](https://apireference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collections' **Add** methods. Each **Add** method takes the cell name where the page break is to be added.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

In page break preview or print preview modes, you can see how these page breaks work.

{{% /alert %}}

## **Clearing All Page Breaks**

To clear all page breaks in a worksheet, call the [**HorizontalPageBreakCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) and [**VerticalPageBreakCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collections' **Clear** methods.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Removing Specific Page Break**

To remove a specific page break in the worksheet, call the [**HorizontalPageBreakCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) and [**VerticalPageBreakCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collections' **removeAt** methods. Each **removeAt** method will take the index of the page break to be removed.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Important to know**: When you set the fit to page properties (that is [**FitToPagesTall**](https://apireference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) and [**FitToPagesWide**](https://apireference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) in the page setup settings, the page break settings are affected, so, if you print the worksheet, the page break settings are not considered although they still exist in the file.

{{% /alert %}}
