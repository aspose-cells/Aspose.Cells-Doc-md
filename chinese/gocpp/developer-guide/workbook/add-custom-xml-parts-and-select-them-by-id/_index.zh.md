---
title: 添加自定义XML部分并通过ID选择它们，使用Golang via C++
linktitle: 添加自定义XML部件并按ID选择
type: docs
weight: 70
url: /zh/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: 学习如何在Excel文件中添加和选择自定义XML部分，使用Aspose.Cells和Golang via C++
---

## **可能的使用场景**

自定义XML部件是存储在微软Excel文件中的XML数据，由与之交互的应用程序使用。目前没有直接通过Excel用户界面添加的方法，但可以通过编程实现，例如使用VSTO或Aspose.Cells。使用[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)方法以API添加自定义XML部分，也可以通过[**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)属性设置其ID。若要按ID选择自定义XML部件，可以使用[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)方法。

## **添加自定义XML部件并按ID选择**

以下示例代码先使用[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)方法添加了四个自定义XML部分，然后用[**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)属性设置它们的ID，最后用[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)方法查找或选择已添加的其中一个自定义XML部分。请参考下面的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **控制台输出**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
