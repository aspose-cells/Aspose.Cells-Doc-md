---  
title: Aggiorna automaticamente l OLE object tramite Microsoft Excel usando Aspose.Cells for Node.js via C++  
linktitle: Aggiorna automaticamente l oggetto OLE tramite Microsoft Excel utilizzando Aspose.Cells  
type: docs  
weight: 270  
url: /it/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Impara come aggiornare automaticamente gli OLE objects in Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells fornisce la proprietà [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) per aggiornare l'oggetto OLE quando il file Excel viene aperto in Microsoft Excel. Grazie a questa proprietà, l'oggetto OLE visualizzerà l'immagine OLE corretta generata da Microsoft Excel.  
{{% /alert %}}  

Il seguente codice di esempio carica il [file Excel di esempio](5115231.xlsx) che contiene un'immagine OLE non reale. L'oggetto OLE è effettivamente un documento di Microsoft Word ma il file Excel di esempio mostra l'immagine dell'animale invece dell'immagine di Microsoft Word. Ma se si apre il [file Excel di output](5115225.xlsx), si vedrà che Microsoft Excel mostra l'immagine OLE corretta.  

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
{{< app/cells/assistant language="nodejs-cpp" >}}
