---
title: Get or Set the Class Identifier of the Embedded OLE Object
type: docs
weight: 920
url: /java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Possible Usage Scenarios**
Aspose.Cells provides the [OleObject.ClassIdentifier](https://apireference.aspose.com/java/cells/com.aspose.cells/oleobject#ClassIdentifier) property which you can use to get or set the class identifier of an embedded ole object. Ole Object Class Identifiers are actually GUIDs i.e Globally Unique Identifiers. GUID is always 16-bytes long, therefore Class Identifiers are also 16-bytes long. They are often found inside the Windows Registry and provide information to host application about how to open embedded ole object containing various embedded resources inside the client application.
## **Get or Set the Class Identifier of the Embedded OLE Object**
The following screenshot shows the Ole Object Class Identifier i.e GUID which has been read from the [sample excel file](attachments/5276174/5473378.xls) containing the embedded PowerPoint ole object.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Sample Code**
Please see the following sample code executed with [sample excel file](attachments/5276174/5473378.xls) and its console output which prints the *Class Identifier* of Ole Object i.e GUID. The printed GUID is exactly same as shown inside the screenshot.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Console Output**
This is the console output of the above sample code when executed with the [sample excel file](attachments/5276174/5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
