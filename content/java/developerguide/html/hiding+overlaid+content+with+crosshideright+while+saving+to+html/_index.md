---
title : "Hiding Overlaid Content with CrossHideRight while saving to HTML" 
description : "" 
weight : 12094 
toc : false
type: docs
url: /java/developerguide/html/hiding+overlaid+content+with+crosshideright+while+saving+to+html/
---

# Aspose.Cells for Java : Hiding Overlaid Content with CrossHideRight while saving to HTML


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Hiding Overlaid Content with CrossHideRight while saving to HTML](#hiding-overlaid-content-with-crosshideright-while-saving-to-html)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/javascript/cells/aspose.cells/htmlsaveoptions#HtmlCrossStringType) to [CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) then it hides all the strings at the right side of the cell which are overlaid or overlapping with cell string.

## Hiding Overlaid Content with CrossHideRight while saving to HTML

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/64456354/64716916.xlsx) and saves it to [output HTML](https://docs2.aspose.com/cells/java/attachments/64456354/64716915.zip) after setting the [HtmlSaveOptions.HtmlCrossStringType](https://apireference.aspose.com/javascript/cells/aspose.cells/htmlsaveoptions#HtmlCrossStringType) as [CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). The screenshot explains how [CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) affects the output HTML from default output.

![image](https://docs2.aspose.com/cells/java/attachments/64456354/64716914.png)

## Sample Code

