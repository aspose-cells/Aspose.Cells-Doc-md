---
title: Add Custom XML Parts and Select Them by ID
type: docs
weight: 70
url: /net/add-custom-xml-parts-and-select-them-by-id/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Custom XML Parts are the XML data that are stored inside Microsoft Excel documents and are used by applications that work with them. There is no direct way of adding them using the Microsoft Excel UI at the moment. However, you can add them programmatically in various ways, e.g., using VSTO or using Aspose.Cells, etc. Please use **[Workbook.CustomXmlParts.Add()]**(https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) method if you want to add a Custom XML Part using the Aspose.Cells API. You can also set its ID using the **[CustomXmlPart.ID]**(https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) property. Similarly, if you want to select a Custom XML Part by ID, you can use **[Workbook.CustomXmlParts.SelectByID()]**(https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) method.

## **Add Custom XML Parts and Select Them by ID**

The following sample code first adds four Custom XML Parts using **[Workbook.CustomXmlParts.Add()]**(https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) method. It then sets their IDs using the **[CustomXmlPart.ID]**(https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) property. Finally, it finds or selects one of the added Custom XML Parts using **[Workbook.CustomXmlParts.SelectByID()]**(https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) method. Please also see the console output of the code given below for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Console Output**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
