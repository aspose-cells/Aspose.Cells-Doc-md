---
title: 在 Aspose.Cells 中使用 Golang 通过 C++ 处理自定义 XML 部分
linktitle: 使用自定义XML部分
type: docs
weight: 390
url: /zh/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: 学习如何使用 Aspose.Cells 通过 C++ 在 Golang 中以程序方式在 Excel 文件中使用自定义 XML 部分。
---

## 在Aspose.Cells中使用自定义XML部件

自定义XML部分是由不同应用程序（如SharePoint）存储在Excel文件内的XML数据。这些数据由需要的应用程序使用。Microsoft Excel不使用这些数据，因此没有GUI来添加它。你可以通过将**.xlsx**的扩展名改为**.zip**，然后用**WinZip**打开，查看此数据。你也可以用第三方Windows压缩工具（如WinRAR或WinZip）打开ZIP文件。数据在**customXml**文件夹内。

你可以通过调用[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)方法，使用Aspose.Cells添加自定义XML部分。

以下示例代码使用[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)方法添加了名为**Book Store**的**Book Catalog XML**，其效果如下图所示。你可以看到，Book Catalog XML被加入至BookStore节点中，这是此属性的名称。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## 使用C++的自定义XML部分的代码示例

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## 相关文章

- [在文档信息面板中添加可见的自定义属性](/cells/zh/cpp/adding-custom-properties-visible-inside-document-information-panel/)
