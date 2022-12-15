---
title: 处理字体设置
linktitle: 字体设置
type: docs
weight: 20
url: /zh/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

可以通过更改字体设置来控制文本的外观。这些字体设置可能包括字体的名称、样式、大小、颜色等效果，如下图所示：

**Microsoft Excel 中的字体设置** 

![待办事项：图像_替代_文本](dealing-with-font-settings_1.png)

与Microsoft Excel一样，Aspose.Cells也支持配置单元格的字体设置。

{{% /alert %}} 
## **配置字体设置**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合代表一个对象[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

Aspose.Cells 提供了[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级'[设置样式](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) 方法，用于设置单元格的格式。此外，对象的[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类提供用于配置字体设置的属性。

本文介绍如何：

- [将特定字体应用于文本。](/cells/zh/java/dealing-with-font-settings/)
- [将文本设置为粗体](/cells/zh/java/dealing-with-font-settings/).
- [设置字体大小](/cells/zh/java/dealing-with-font-settings/).
- [设置字体颜色](/cells/zh/java/dealing-with-font-settings/).
- [下划线文字](/cells/zh/java/dealing-with-font-settings/).
- [划线文字](/cells/zh/java/dealing-with-font-settings/).
- [将文本设置为下标](/cells/zh/java/dealing-with-font-settings/).
- [将文本设置为上标](/cells/zh/java/dealing-with-font-settings/).
### **设置字体名称**
使用特定字体将特定字体应用于单元格中的文本[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设定名称](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **将字体样式设置为粗体**
通过设置将文本设置为粗体[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置粗体](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold)财产给**真的**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **设置字体大小**
使用设置字体大小[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设定大小](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **设置字体下划线类型**
文本下划线[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置下划线](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline)财产。 Aspose.Cells 提供各种预定义的字体下划线类型[字体下划线类型](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)枚举。

|**字体下划线类型**|**描述**|
|:- |:- |
|[没有任何](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|无下划线|
|[单身的](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|单下划线|
|[双倍的](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|双下划线|
|[会计](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|单个会计下划线|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|双会计下划线|
|[短跑](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|虚线下划线|
|[短跑_点_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|粗点划线|
|[短跑_点_重的](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|粗点划线|
|[虚线_重](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|粗虚线下划线|
|[破折号_长](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|长虚线下划线|
|[短跑_长_重的](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|粗长虚线下划线|
|[点划线](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|点划线|
|[点_点_短跑](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|点划线下划线|
|[点缀](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|虚线下划线|
|[点重](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|粗点下划线|
|[重的](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|粗下划线|
|[海浪](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|波浪下划线|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|双波下划线|
|[波浪重](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|大浪下划线|
|` `[字](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|仅给非空格字符加下划线|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **设置字体颜色**
设置字体颜色[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置颜色](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color)财产。从中选择任何颜色[颜色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举并将所选颜色分配给[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置颜色](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **在文本上设置删除线效果**
带删除线的文本[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置删除线](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **设置下标**
使用[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置下标](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **设置上标**
将上标应用于文本[字体](https://reference.aspose.com/cells/java/com.aspose.cells/Font)对象的[设置上标](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **推进主题**
- [对字体应用上标和下标效果](/cells/zh/java/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
