---
title: Aspose.Cells for Java 7.1.1 发行说明
type: docs
weight: 90
url: /zh/java/aspose-cells-for-java-7-1-1-release-notes/
---
{{% alert color="primary" %}} 

此页面包含发行说明[Aspose.Cells for Java 7.1.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.1.1/)

{{% /alert %}} 

我们是
很高兴宣布 Aspose.Cells for Java v7.1.1！

新功能

- 检查一列是否为空

增强功能

- 通过直接渲染到 OutputStream 使用 LightCells API 保存到 XLSX

例外情况

- Cell.setHtmlString() 方法抛出 NullPointerException
- 读取 XLSX 模板文件抛出 NullPointerException

虫子

- 散点图的二级分类轴成为文本轴
- 文本框中的内容未正确呈现
- ROUND 函数不能舍入大于 922337.20 的值
- 未从 ODStemplate 文件中正确读取图表
- 自定义数字格式：“dd.MM.yyyy”未正确保存为 ODS 文件
- 生成的 PDF 文档中的线形变短
