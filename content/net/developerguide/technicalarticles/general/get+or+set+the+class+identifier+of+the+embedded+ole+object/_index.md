---
title : "Get or Set the Class Identifier of the Embedded OLE Object" 
description : "" 
weight : 16576 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/get+or+set+the+class+identifier+of+the+embedded+ole+object/
---

# Aspose.Cells for .NET : Get or Set the Class Identifier of the Embedded OLE Object


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Get or Set the Class Identifier of the Embedded OLE Object](#get-or-set-the-class-identifier-of-the-embedded-ole-object)
    *   2.1 [Sample Code](#sample-code)
    *   2.2 [Console Output](#console-output)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Aspose.Cells provides the [OleObject.ClassIdentifier](https://apireference.aspose.com/net/cells/aspose.cells.drawing/oleobject/properties/classidentifier) property which you can use to get or set the class identifier of embedded ole object. Ole Object Class Identifiers are actually GUIDs i.e Globally Unique Identifiers. GUID is always 16-bytes long, therefore Class Identifiers are also 16-bytes long. They are often found inside the Windows Registry and provide information to host application about how to open embedded ole object containing various embedded resources inside the client application.

## Get or Set the Class Identifier of the Embedded OLE Object

The following screenshot shows the Ole Object Class Identifier i.e GUID which has been read from the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5024988/5115190.xls) containing the embedded PowerPoint ole object.

![](https://docs2.aspose.com/cells/net/attachments/5024988/5115191.png)

### Sample Code

Please see the following sample code executed with [sample excel file](https://docs2.aspose.com/cells/net/attachments/5024988/5115190.xls) and its console output which prints the Class Identifier of Ole Object i.e GUID. The printed GUID is exactly same as shown inside the screenshot.

### Console Output

This is the console output of the above sample code when executed with the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5024988/5115190.xls).

{{< code lang="cs" >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sample.xls](https://docs2.aspose.com/cells/net/attachments/5024988/5115190.xls) (application/vnd.ms-excel)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [class-identifier-of-the-ole-object.png](https://docs2.aspose.com/cells/net/attachments/5024988/5115191.png) (image/png)  

