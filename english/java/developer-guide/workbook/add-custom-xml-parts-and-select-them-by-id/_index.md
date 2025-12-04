---
title: Add Custom XML Parts and Select them by ID
type: docs
weight: 10
url: /java/add-custom-xml-parts-and-select-them-by-id/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Custom XML Parts are the XML data that is stored inside the Microsoft Excel documents and are used by the applications that deal with them. There is no direct way of adding them using Microsoft Excel UI at the moment. However, you can add them programmatically in various ways e.g. using *VSTO*, using *Aspose.Cells* etc. Please use [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-) method if you want to add Custom XML Part using Aspose.Cells API. You can also set its ID, using the [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#setID-java.lang.String-) property. Similarly, if you want to select Custom XML Part by ID, you can use [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-) method.

## **Add Custom XML Parts and Select them by ID**

The following sample code first adds four Custom XML Parts using [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-) method. It then set their IDs using [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#setID-java.lang.String-) property. Finally, it finds or selects one of the added Custom XML Part using [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-) method. Please also see the console output of the code given below for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Console Output**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
