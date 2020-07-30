---
title : "Access and Update the Portions of Rich Text of Cell" 
description : "" 
weight : 20407 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/stl-dtfmt/access+and+update+the+portions+of+rich+text+of+cell/
---

# Aspose.Cells for .NET : Access and Update the Portions of Rich Text of Cell


Aspose.Cells allows you to access and update the portions of the rich text of the cell. For this purpose, you can use [Cell.GetCharacters()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getcharacters/index) and [Cell.SetCharacters()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setcharacters) methods. These methods will return and accept the array of [FontSetting](https://apireference.aspose.com/net/cells/aspose.cells/fontsetting) objects which you can use to access and update various properties of font like font name, font color, boldness, etc.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Access and Update the Portions of Rich Text of Cell](#access-and-update-the-portions-of-rich-text-of-cell)
    *   1.1 [Console Output](#console-output)
{{< /panel >}}
 

 

## Access and Update the Portions of Rich Text of Cell

The following code demonstrates the usage of [Cell.GetCharacters()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getcharacters/index)and [Cell.SetCharacters()](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setcharacters) method using the [source excel file](https://docs2.aspose.com/cells/net/attachments/5017266/5112369.xlsx) which you can download from the provided link. The source excel file has a rich text in the cell A1. It has 3 portions and each portion has a different font. The following code snippet accesses these portions and updates the first portion with a new font name. Finally, it saves the workbook as [output excel file](https://docs2.aspose.com/cells/net/attachments/5017266/5112366.xlsx). When you will open it, you will find the font of the first portion of the text has changed to **"Arial"**.

### Console Output

Here is the console output of the above sample code using the [source excel file](https://docs2.aspose.com/cells/net/attachments/5017266/5112369.xlsx).

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

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [source.xlsx](https://docs2.aspose.com/cells/net/attachments/5017266/5112369.xlsx) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output.xlsx](https://docs2.aspose.com/cells/net/attachments/5017266/5112366.xlsx) (image/png)  

