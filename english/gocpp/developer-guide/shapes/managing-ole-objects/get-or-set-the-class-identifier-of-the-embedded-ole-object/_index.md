---
title: Get or Set the Class Identifier of the Embedded OLE Object with Golang via C++
linktitle: Get or Set the Class Identifier of the Embedded OLE Object
type: docs
weight: 200
url: /go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Learn how to get or set the class identifier of embedded OLE objects using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**
Aspose.Cells provides the [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) property, which you can use to get or set the class identifier of an embedded OLE object. OLE object class identifiers are actually GUIDs, i.e., Globally Unique Identifiers. GUIDs are always 16 bytes long; therefore, class identifiers are also 16 bytes long. They are often found inside the Windows Registry and provide information to the host application about how to open embedded OLE objects containing various embedded resources inside the client application.

## **Get or Set the Class Identifier of the Embedded OLE Object**
The following screenshot shows the OLE object class identifier, i.e., GUID, which has been read from the [sample Excel file](5115190.xls) containing the embedded PowerPoint OLE object.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Sample Code**
Please see the following sample code, executed with the [sample Excel file](5115190.xls), and its console output, which prints the class identifier of the OLE object, i.e., GUID. The printed GUID is exactly the same as shown in the screenshot.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}

### **Console Output**
This is the console output of the above sample code when executed with the [sample Excel file](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}