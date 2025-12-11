---
title: Access and Update the Portions of Rich Text of Cell
linktitle: Rich Formatting Text
type: docs
weight: 440
url: /java/access-and-update-the-portions-of-rich-text-of-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to access and update the portions of the rich text of a cell. For this purpose, you can use the `Cell.getCharacters()` and `Cell.setCharacters()` methods. These methods will return and accept an array of `FontSetting` objects, which you can use to access and update various properties of a font, such as font name, font color, boldness, etc.

{{% /alert %}} 
## **Access and Update the Portions of Rich Text of Cell**
The following code demonstrates the usage of `Cell.getCharacters()` and `Cell.setCharacters()` methods using the [source Excel file](5472937.xlsx), which you can download from the provided link. The source Excel file contains rich text in cell **A1**. It has three portions, each with a different font. We will access these portions and update the first portion with a new font name. Finally, it saves the workbook as the [output Excel file](5472930.xlsx). When you open it, you will find that the font of the first portion of the text has changed to **"Arial"**.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}



## **Console Output**
Here is the console output of the above sample code using the [source Excel file](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
