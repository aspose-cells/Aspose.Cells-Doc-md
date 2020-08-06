---
title: Conditional Formatting
type: docs
weight: 40
url: /java/conditional-formatting/
---

{{% alert color="primary" %}} 

Conditional formatting is an advanced Microsoft Excel feature that allows you to apply formats to a cell or range of cells and have that formatting change depending on the value of the cell or the value of a formula. For example, you can have a cell appear bold only when the value of the cell is greater than 500. When the value of the cell meets the condition, the specified format is applied to the cell. If the value of the cell does not meet the condition, the default formatting is used. In Microsoft Excel, select **Format**, then **Conditional Formatting** to open the Conditional Formatting dialog.

**Conditional formatting in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells supports applying conditional formatting to cells at runtime. This article explains how.

{{% /alert %}} 
### **Applying Conditional Formatting**
Aspose.Cells supports conditional formatting in two ways:

- [Using a designer spreadsheet](/cells/java/conditional-formatting-html/).
- [Creating conditional formatting at runtime](/cells/java/conditional-formatting-html/).
#### **Using Designer Spreadsheet**
Developers can create a designer spreadsheet that contains conditional formatting in Microsoft Excel and then open that spreadsheet with Aspose.Cells. Aspose.Cells loads and saves the designer spreadsheet, keeping any conditional formatting setting. To find out more about designer spreadsheets, read [What is a Designer Spreadsheet](/cells/java/what-is-a-designer-spreadsheet-html/).
### **Applying Conditional Formatting at Runtime**
Aspose.Cells supports applying conditional formatting at runtime.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
#### **Set Font**
**Setting fonts in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
#### **Set Border**
**Setting borders in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
#### **Set Pattern**
**Setting a cell pattern in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}
