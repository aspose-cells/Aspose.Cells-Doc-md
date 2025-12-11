---
title: Add Custom XML Parts and Select Them by ID
type: docs
weight: 70
url: /python-net/add-custom-xml-parts-and-select-them-by-id/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Custom XML Parts are the XML data that is stored inside Microsoft Excel documents and are used by the applications that work with them. There is no direct way of adding them using the Microsoft Excel UI at the moment. However, you can add them programmatically in various ways, e.g., using VSTO, Aspose.Cells, etc. Please use **[Workbook.custom_xml_parts.add()](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)** if you want to add a Custom XML Part using Aspose.Cells for Python via .NET API. You can also set its ID using the **[CustomXmlPart.id](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id)** property. Similarly, if you want to select a Custom XML Part by ID, you can use **[Workbook.custom_xml_parts.select_by_id()](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)**.

## **Add Custom XML Parts and Select Them by ID**

The following sample code first adds four Custom XML Parts using **[Workbook.custom_xml_parts.add()](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)**. It then sets their IDs using the **[CustomXmlPart.id](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id)** property. Finally, it finds or selects one of the added Custom XML Parts using **[Workbook.custom_xml_parts.select_by_id()](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)**. Please also see the console output of the code below for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Console Output**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
