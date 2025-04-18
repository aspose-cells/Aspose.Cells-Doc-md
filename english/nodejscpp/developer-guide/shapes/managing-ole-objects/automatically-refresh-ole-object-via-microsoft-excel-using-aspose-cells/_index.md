---  
title: Automatically refresh OLE object via Microsoft Excel using Aspose.Cells for Node.js via C++  
linktitle: Automatically refresh OLE object via Microsoft Excel using Aspose.Cells  
type: docs  
weight: 270  
url: /nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Learn how to automatically refresh OLE objects in Excel using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells provides the [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) property to refresh the OLE object when the excel file is opened in Microsoft Excel. Because of this property, the OLE object will display the correct OLE image generated by Microsoft Excel.  
{{% /alert %}}  

The following sample code loads the [sample excel file](5115231.xlsx) which has a non-real OLE image. The OLE object is actually a Microsoft Word document but the sample excel file shows the animal image instead of Microsoft Word image. But if you open the [output excel file](5115225.xlsx), you will see Microsoft Excel displays the correct OLE image.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
