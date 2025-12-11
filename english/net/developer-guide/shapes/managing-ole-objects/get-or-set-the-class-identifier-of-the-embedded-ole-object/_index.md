---
title: Get or Set the Class Identifier of the Embedded OLE Object
type: docs
weight: 200
url: /net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells provides the [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) property which you can use to get or set the class identifier of an embedded OLE object. OLE object class identifiers are actually GUIDs, i.e., globally unique identifiers. A GUID is always 16 bytes long; therefore, class identifiers are also 16 bytes long. They are often found inside the Windows Registry and provide information to the host application about how to open an embedded OLE object containing various embedded resources inside the client application.

## **Get or Set the Class Identifier of the Embedded OLE Object**
The following screenshot shows the OLE object class identifier, i.e., GUID, which has been read from the [sample Excel file](5115190.xls) containing the embedded PowerPoint OLE object.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Sample Code**
Please see the following sample code executed with the [sample Excel file](5115190.xls) and its console output, which prints the class identifier of the OLE object, i.e., GUID. The printed GUID is exactly the same as shown in the screenshot.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}

### **Console Output**
This is the console output of the above sample code when executed with the [sample Excel file](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}

{{< app/cells/assistant language="csharp" >}}
