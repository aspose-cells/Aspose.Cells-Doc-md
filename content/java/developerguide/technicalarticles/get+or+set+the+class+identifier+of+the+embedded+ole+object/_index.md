---
title : "Get or Set the Class Identifier of the Embedded OLE Object" 
description : "" 
weight : 12559 
toc : false
type: docs
url: /java/developerguide/technicalarticles/get+or+set+the+class+identifier+of+the+embedded+ole+object/
---

# Aspose.Cells for Java : Get or Set the Class Identifier of the Embedded OLE Object


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Get or Set the Class Identifier of the Embedded OLE Object](#get-or-set-the-class-identifier-of-the-embedded-ole-object)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

 


## Possible Usage Scenarios

Aspose.Cells provides the [OleObject.ClassIdentifier](https://apireference.aspose.com/java/cells/com.aspose.cells/oleobject#ClassIdentifier) property which you can use to get or set the class identifier of an embedded ole object. Ole Object Class Identifiers are actually GUIDs i.e Globally Unique Identifiers. GUID is always 16-bytes long, therefore Class Identifiers are also 16-bytes long. They are often found inside the Windows Registry and provide information to host application about how to open embedded ole object containing various embedded resources inside the client application.

## Get or Set the Class Identifier of the Embedded OLE Object

The following screenshot shows the Ole Object Class Identifier i.e GUID which has been read from the [sample excel file](https://docs2.aspose.com/cells/java/attachments/5276174/5473378.xls) containing the embedded PowerPoint ole object.

![](https://docs2.aspose.com/cells/java/attachments/5276174/5473377.png)

## Sample Code

Please see the following sample code executed with [sample excel file](https://docs2.aspose.com/cells/java/attachments/5276174/5473378.xls) and its console output which prints the *Class Identifier* of Ole Object i.e GUID. The printed GUID is exactly same as shown inside the screenshot.

## Console Output

This is the console output of the above sample code when executed with the [sample excel file](https://docs2.aspose.com/cells/java/attachments/5276174/5473378.xls).

{{< code lang="cs" >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /code >}}

