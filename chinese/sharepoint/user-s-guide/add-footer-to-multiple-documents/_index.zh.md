---
title: 向多个文档添加页脚
type: docs
weight: 80
url: /zh/sharepoint/add-footer-to-multiple-documents/
---

如果您想要在多个 Excel 文件中添加页脚，请在功能区中选择“使用 Aspose.Cells 添加页脚”选项。

![todo:image_alt_text](add-footer-to-multiple-documents_1.png)



从数据源文件夹中获取所有Excel文件并创建文件列表表格。

选择需要添加页脚的文件，单击**添加页脚**按钮以为所选文件添加页脚。 

![todo:image_alt_text](add-footer-to-multiple-documents_2.png)



在添加页脚设置期间提供以下选项：

**章节**

添加页脚位置：左侧章节、中心章节和右侧章节。

**页脚脚本**

It represents Footer formatting script. Script commands: Command | Description| &P Current page number| &N Page count|&D Current date| &T Current time &A Sheet name &F File name without path &"<FontName>" Font name, for example: &"Arial" &"<FontName>, <FontStyle>" Font name and font style, for example: &"Arial,Bold" &<FontSize> Font size. If this command is followed by a plain number to be printed in the header, it will be separated from the font height with a space character. &G Image script For example: "&Arial,Bold&8Footer Note".
