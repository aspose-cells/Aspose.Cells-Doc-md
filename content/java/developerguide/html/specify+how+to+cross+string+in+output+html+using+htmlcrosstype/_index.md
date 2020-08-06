---
title : "Specify how to cross string in output HTML using HtmlCrossType" 
description : "" 
weight : 12098 
toc : false
type: docs
url: /java/developerguide/html/specify+how+to+cross+string+in+output+html+using+htmlcrosstype/
---

# Aspose.Cells for Java : Specify how to cross string in output HTML using HtmlCrossType


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Specify how to cross string in output HTML using HtmlCrossType](#specify-how-to-cross-string-in-output-html-using-htmlcrosstype)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

When the cell contains text or string but it is larger than the width of the cell, then the string overflows if the next cell in the next column is null or empty. When you save your Excel file into HTML, you can control this overflow by specifying the cross type using the [HtmlCrossType](https://apireference.aspose.com/java/cells/com.aspose.cells/HtmlCrossType) enumeration. It has the following values

*   **[HtmlCrossType.DEFAULT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#DEFAULT)**

Display like MS Excel which depends on the next cell. If the next cell is null, the string will cross or it will be truncated.

*   **[HtmlCrossType.MS\_EXPORT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#MS_EXPORT)**

Display the string like MS Excel exporting HTML.

*   **[HtmlCrossType.CROSS](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#CROSS)**

Display HTML cross string, the performance for creating large HTML files will be more than ten times faster than setting the value to [DEFAULT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#DEFAULT) or [FIT\_TO\_CELL](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

*   **[HtmlCrossType.CROSS\_HIDE\_RIGHT](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)**

Display HTML cross string and hide the right string when the texts overlap.

*   **[HtmlCrossType.FIT\_TO\_CELL](https://apireference.aspose.com/java/cells/com.aspose.cells/htmlcrosstype#FIT_TO_CELL)**

Only displaying the string within the width of the cell.

## Specify how to cross string in output HTML using HtmlCrossType

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/51480080/51740747.xlsx) and saves it to HTML format by specifying different [HtmlCrossType](https://apireference.aspose.com/java/cells/com.aspose.cells/HtmlCrossType). Please download the [output HTML](https://docs2.aspose.com/cells/java/attachments/51480080/51740745.zip) files generated with this code. The sample Excel file contains the image bordered with red color as shown in this screenshot that shows the effect of the [HtmlCrossType](https://apireference.aspose.com/java/cells/com.aspose.cells/HtmlCrossType) values on output HTML.

![image](51740746.png)

## Sample Code

