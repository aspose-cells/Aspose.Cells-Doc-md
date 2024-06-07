---
title: 为多个文档添加页脚
type: docs
weight: 80
url: /zh/sharepoint/add-footer-to-multiple-documents/
---

如果您想在多个Excel文件中添加页脚，请在功能区中选择“使用Aspose.Cells添加页脚”选项。

![todo:image_alt_text](add-footer-to-multiple-documents_1.png)



从数据源文件夹获取所有Excel文件并创建文件列表表。

选择需要添加页脚的文件，单击**添加页脚**按钮来为所选文件添加页脚。 

![todo:image_alt_text](add-footer-to-multiple-documents_2.png)



在添加页脚设置时可以选择以下选项:

**版块**

添加页脚位置：左侧区域、中间区域和右侧区域。

**页脚脚本**

It represents Footer formatting script. Script commands: Command | Description| &P Current page number| &N Page count|&D Current date| &T Current time &A Sheet name &F File name without path &"<FontName>" Font name, for example: &"Arial" &"<FontName>, <FontStyle>" Font name and font style, for example: &"Arial,Bold" &<FontSize> Font size. If this command is followed by a plain number to be printed in the header, it will be separated from the font height with a space character. &G Image script For example: "&Arial,Bold&8Footer Note".
