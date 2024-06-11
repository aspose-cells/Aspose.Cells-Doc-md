---
title: 向Excel备注添加图片
type: docs
weight: 60
url: /zh/java/add-a-picture-to-an-excel-comment/
---

{{% alert color="primary" %}}

Microsoft Excel允许用户在很大程度上自定义电子表格的外观和感觉。甚至可以向备注添加背景图片。

备注被添加到单元格中以记录评论，可以是关于公式运算细节、数值来源或审核者的问题等任何内容。添加背景图片可以是一种美学选择，也可以用于加强品牌。

{{% /alert %}}

## 使用Microsoft Excel向Excel备注中添加图片

在Microsoft Excel 2007中，可以将图像作为单元格备注的背景。在Excel 2007中，可以这样完成（假设已经添加了备注）：

1. 右键单击包含评论的单元格。
1. 选择**显示/隐藏评论**并清除评论中的任何文本。
1.选择**格式**，然后选择**注释**。
1. 选择**格式**，然后选择**评论**。
1. 在“颜色和线条”选项卡上，单击“颜色”的箭头。
1.单击**图片**选项卡。
1. 在“图片”选项卡上，单击**选择图片**。
1. 定位并选择图片
1. 点击**确定**。

## 向Excel评论中添加图片 Aspose.Cells

Aspose.Cells提供了这一宝贵的功能。

下面的示例代码从头创建一个XLSX文件，并向单元格A1添加带图片背景的评论。

执行代码后，A1将带有背景图片的评论。

**输出文件**

![todo:image_alt_text](add-a-picture-to-an-excel-comment_1.png)

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddPicturetoExcelComment-AddPicturetoExcelComment.java" >}}
