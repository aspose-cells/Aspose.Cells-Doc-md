---
title: 处理字体设置
linktitle: 字体设置
type: docs
weight: 20
url: /zh/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

可以通过更改字体设置来控制文本的外观和感觉。这些字体设置可能包括字体的名称、样式、大小、颜色和其他效果，如下图所示：

**Microsoft Excel 中的字体设置** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

与Microsoft Excel一样，Aspose.Cells也支持配置单元格的字体设置。

{{% /alert %}} 
## **配置字体设置**
Aspose.Cells提供了一个[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类，代表一个Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中的每个项目都表示[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

Aspose.Cells 提供 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的 [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) 方法，用于设置单元格的格式，还， [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 类的对象提供了配置字体设置的属性。

本文介绍如何：

- [应用特定的字体到文本。](/cells/zh/java/dealing-with-font-settings/)
- [将文本设置为粗体](/cells/zh/java/dealing-with-font-settings/)。
- [设置字体大小](/cells/zh/java/dealing-with-font-settings/)。
- [设置字体颜色](/cells/zh/java/dealing-with-font-settings/)。
- [给文本添加下划线](/cells/zh/java/dealing-with-font-settings/)。
- [删除线文字](/cells/zh/java/dealing-with-font-settings/).
- [将文本设置为下标](/cells/zh/java/dealing-with-font-settings/).
- [将文本设置为上标](/cells/zh/java/dealing-with-font-settings/).
### **设置字体名称**
使用 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) 属性在单元格中应用特定字体。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **将字体样式设置为粗体**
通过将 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) 属性设置为 **true** 来将文本设置为粗体。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **设置字体大小**
使用 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) 属性设置字体大小。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **设置字体下划线类型**
使用 [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) 对象的 [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) 属性给文本添加下划线。Aspose.Cells 在 [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) 枚举中提供各种预定义的字体下划线类型。

|**字体下划线类型**|**描述**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|无下划线|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|单下划线|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|双下划线|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|单会计下划线|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE-ACCOUNTING)|双重会计下划线|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|虚线下划线|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-DOT-HEAVY)|粗虚线点点下划线|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-HEAVY)|粗虚线点线下划线|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED-HEAVY)|粗虚线下划线|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG)|长虚线下划线|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG-HEAVY)|粗长虚线下划线|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DASH)|虚线点划线|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DOT-DASH)|虚线点点划线|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|点线下划线|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED-HEAVY)|粗点线下划线|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|粗下划线|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|波浪线下划线|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-DOUBLE)|双波纹下划线|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-HEAVY)|粗波纹下划线|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|仅对非空格字符下划线|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **设置字体颜色**
使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)属性设置字体颜色。从[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举中选择任何颜色，并将所选颜色分配给[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **在文本上设置删除线效果**
使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)属性划掉文本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **设置下标**
通过使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)属性使文本成为上标。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **设置上标**
使用[Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)属性将上标应用于文本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **高级主题**
- [在字体上应用上标和下标效果](/cells/zh/java/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="java" >}}
