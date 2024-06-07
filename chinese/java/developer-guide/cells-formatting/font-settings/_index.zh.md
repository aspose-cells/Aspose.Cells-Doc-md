---
title: 处理字体设置
linktitle: 字体设置
type: docs
weight: 20
url: /zh/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

可以通过更改其字体设置来控制文本的外观。 这些字体设置可能包括字体的名称、样式、大小、颜色以及字体的其他效果，如下图所示：

**Microsoft Excel中的字体设置** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

就像Microsoft Excel一样，Aspose.Cells还支持配置单元格的字体设置。

{{% /alert %}} 
## **配置字体设置**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，代表一个Microsoft Excel文件。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。 工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中的每个项目都代表[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

Aspose.Cells提供了[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\))方法，用于设置单元格的格式。 此外，[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类的对象提供了配置字体设置的属性。

本文将演示如何：

- [将特定字体应用于文本。](/cells/zh/java/dealing-with-font-settings/)
- [将文本设置为粗体](/cells/zh/java/dealing-with-font-settings/)
- [设置字体大小](/cells/zh/java/dealing-with-font-settings/)。
- [设置字体颜色](/cells/zh/java/dealing-with-font-settings/)。
- [给文本加下划线](/cells/zh/java/dealing-with-font-settings/)。
- [给文本加删除线](/cells/zh/java/dealing-with-font-settings/)。
- [将文本设置为下标](/cells/zh/java/dealing-with-font-settings/)。
- [将文本设置为上标](/cells/zh/java/dealing-with-font-settings/)。
### **设置字体名称**
使用 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) 属性，为单元格中的文本应用特定字体。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **将字体样式设置为粗体**
通过将 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) 属性设置为 **true**，将文本设置为加粗。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **设置字体大小**
使用 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) 属性设置字体大小。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **设置字体下划线类型**
使用 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) 属性为文本添加下划线。Aspose.Cells 提供了[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) 枚举中的各种预定义字体下划线类型。

|**字体下划线类型**|**描述**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|无下划线|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|单下划线|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|双下划线|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|单会计下划线|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|双会计下划线|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|虚线下划线|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|粗虚线-点-点下划线|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|粗虚线-点下划线|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|粗虚线下划线|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|长虚线下划线|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|粗长虚线下划线|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|破折号下划线|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|破折号点下划线|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|点下划线|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|粗点下划线|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|粗下划线|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|波浪线下划线|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|双波浪线下划线|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|重波浪线下划线|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|仅下划线非空格字符|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **设置字体颜色**
使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)属性设置字体颜色。从[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举中选择任何颜色，并将所选颜色赋给[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **在文本上设置删除线效果**
使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)属性为文本加删除线。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **设置下标**
通过使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)属性将文本设为下标。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **设置上标**
使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)属性将文本设为上标。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **高级主题**
- [在字体上应用上标和下标效果](/cells/zh/java/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
