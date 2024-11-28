---
title: Add Custom XML Parts and Select them by ID
type: docs
weight: 70
url: /python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Possible Usage Scenarios**

Custom XML Parts are the XML data that is stored inside the Microsoft Excel documents and are used by the applications that deal with them. There is no direct way of adding them using Microsoft Excel UI at the moment. However, you can add them programmatically in various ways e.g. using VSTO, using Aspose.Cells etc. Please use [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) method if you want to add Custom XML Part using Aspose.Cells for Python via .NET API. You can also set its ID, using the [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id) property. Similarly, if you want to select Custom XML Part by ID, you can use [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str) method.

## **Add Custom XML Parts and Select them by ID**

The following sample code first adds four Custom XML Parts using [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) method. It then sets their IDs using [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id) property. Finally, it finds or selects one of the added Custom XML Part using [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str) method. Please also see the console output of the code given below for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Console Output**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

