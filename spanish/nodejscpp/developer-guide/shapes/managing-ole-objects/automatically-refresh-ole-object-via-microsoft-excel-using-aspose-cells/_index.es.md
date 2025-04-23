---  
title: Actualice automáticamente el objeto OLE vía Microsoft Excel usando Aspose.Cells for Node.js via C++  
linktitle: Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells  
type: docs  
weight: 270  
url: /es/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Aprenda cómo actualizar automáticamente los objetos OLE en Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells proporciona la propiedad [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) para actualizar el objeto OLE cuando se abre el archivo de Excel en Microsoft Excel. Gracias a esta propiedad, el objeto OLE mostrará la imagen OLE correcta generada por Microsoft Excel.  
{{% /alert %}}  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115231.xlsx) que tiene una imagen OLE no real. El objeto OLE es en realidad un documento de Microsoft Word pero el archivo de Excel de muestra muestra la imagen de un animal en lugar de la imagen de Microsoft Word. Pero si abre el [archivo de Excel de salida](5115225.xlsx), verá que Microsoft Excel muestra la imagen OLE correcta.  

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
