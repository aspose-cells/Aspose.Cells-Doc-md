---
title : "Access and Update the Portions of Rich Text of Cell" 
description : "" 
weight : 12510 
toc : false
type: docs
url: /java/developerguide/technicalarticles/access+and+update+the+portions+of+rich+text+of+cell/
---

# Aspose.Cells for Java : Access and Update the Portions of Rich Text of Cell


Aspose.Cells allows you to access and update the portions of the rich text of cell. For this purpose, you can use `Cell.getCharacters()` and `Cell.setCharacters()` methods. These methods will return and accept the array of `FontSetting` objects which you can use to access and update various properties of font like font name, font color, boldness etc.

#### Access and Update the Portions of Rich Text of Cell

The following code demonstrates the usage of `Cell.getCharacters()` and `Cell.setCharacters()` method using the [source excel file](https://docs2.aspose.com/cells/java/attachments/5276482/5472937.xlsx) which you can download from the provided link. The source excel file has a rich text in the cell A1. It has 3 portions and each portion has different font. We will access these portions and update the first portion with new font name. Finally it saves the workbook as [output excel file](https://docs2.aspose.com/cells/java/attachments/5276482/5472930.xlsx). When you will open it, you will find the font of the first portion of the text has changed to **"Arial"**.


#### Console Output

Here is the console output of the above sample code using the [source excel file](https://docs2.aspose.com/cells/java/attachments/5276482/5472937.xlsx).

{{< code lang="cs" >}}
Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana
{{< /code >}}

