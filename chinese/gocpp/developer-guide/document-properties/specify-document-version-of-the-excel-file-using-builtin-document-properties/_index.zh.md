---
title: 使用C++中的Golang通过内置文档属性指定Excel文件的版本
linktitle: 指定文档版本
type: docs
weight: 20
url: /zh/go-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: 学习如何使用 Aspose.Cells for C++ 通过内置文档属性指定Excel文件的版本。
---

## **可能的使用场景**

你可以通过右键点击文件，然后选择 属性 > 详细信息并编辑“版本号”字段，来更改Excel文件的**版本号**。请使用 [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/) 属性通过 Aspose.Cells API 以编程方式更改。

## **使用内置文档属性指定Excel文件的文档版本**

以下示例代码创建一个工作簿并更改其内置文档属性，包括标题、作者和版本号。请查看由此代码生成的[输出Excel文件](64716811.xlsx)和截图，显示通过 [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/) 属性修改的版本号。

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyDocumentVersionOfTheExcelFileUsingBuiltinDocumentProperties.go" >}}
