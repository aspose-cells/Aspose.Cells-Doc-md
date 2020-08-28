---
title: Hiding Overlaid Content with CrossHideRight while saving to HTML
type: docs
weight: 100
url: /java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Possible Usage Scenarios**

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the [**HtmlSaveOptions.HtmlCrossStringType**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) to [**CROSS_HIDE_RIGHT**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

## **Hiding Overlaid Content with CrossHideRight while saving to HTML**

The following sample code loads the [sample Excel file](64716916.xlsx) and saves it to [output HTML](64716915.zip) after setting the [**HtmlSaveOptions.HtmlCrossStringType**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) as [**CROSS_HIDE_RIGHT**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). The screenshot explains how [**CROSS_HIDE_RIGHT**](https://apireference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) affects the output HTML from default output.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Sample Code**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
