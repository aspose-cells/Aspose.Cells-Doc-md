---
title: 管理文档属性
type: docs
weight: 30
url: /zh/go-cpp/managing-document-properties/
---

## **可能的使用场景**

Aspose.Cells 允许您使用内置和自定义文档属性。 这是打开这些 *文档属性* 的 Microsoft Excel 界面。 只需单击 *高级属性*，如此屏幕截图中所示，并查看它们。

![todo:image_alt_text](managing-document-properties_1.png)

## **管理文档属性**

以下示例代码加载[示例Excel文件](23166989.xlsx)，读取其内置文档属性（如标题和主题），并进行修改。还读取自定义文档属性（如MyCustom1），并添加新的自定义属性（MyCustom5），然后保存为输出Excel文件（23166986.xlsx）。截图展示了示例代码对样本Excel的效果。

![todo:image_alt_text](managing-document-properties_2.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **控制台输出**

以上示例代码在执行时输出的控制台内容，使用提供的[示例Excel文件](23166989.xlsx)。

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}
