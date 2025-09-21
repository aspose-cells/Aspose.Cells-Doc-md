---
title: Add Custom XML Parts and Select them by ID with Golang via C++
linktitle: Add Custom XML Parts and Select them by ID
type: docs
weight: 70
url: /go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Learn how to add and select custom XML parts in Excel files using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

Custom XML Parts are XML data stored inside Microsoft Excel documents and are used by applications that interact with them. There is no direct way to add them using the Microsoft Excel UI at the moment. However, you can add them programmatically in various ways, such as using VSTO or Aspose.Cells. Use the [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) method to add a Custom XML Part using the Aspose.Cells API. You can also set its ID using the [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/) property. Similarly, if you want to select a Custom XML Part by ID, you can use the [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/) method.

## **Add Custom XML Parts and Select them by ID**

The following sample code first adds four Custom XML Parts using the [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) method. It then sets their IDs using the [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/) property. Finally, it finds or selects one of the added Custom XML Parts using the [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/) method. Please also see the console output of the code given below for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Console Output**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}