---  
title: Cómo establecer la propiedad AutoRecover del Libro de trabajo con Node.js a través de C++  
linktitle: Cómo establecer la propiedad AutoRecover del Libro de trabajo  
type: docs  
weight: 220  
url: /es/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Aprende cómo establecer la propiedad AutoRecover de un libro de trabajo usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Puedes usar Aspose.Cells para establecer la propiedad AutoRecover del libro de trabajo. El valor predeterminado de esta propiedad es **true**. Cuando lo estableces en **falso** en un libro de trabajo, Microsoft Excel desactiva AutoRecover (Autosave) en ese archivo de Excel.  

Aspose.Cells proporciona la propiedad [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) para activar o desactivar esta opción.  
{{% /alert %}}  

El siguiente código explica cómo usar la propiedad [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad, que es **true**, luego lo establece como **falso** y guarda el libro de trabajo. Luego lee el libro de trabajo nuevamente y obtiene el valor de esta propiedad, que en ese momento es **falso**.  

## Código Node.js para establecer la propiedad AutoRecover del Libro de trabajo  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Salida**  

Aquí está la salida en consola del código de muestra anterior.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

