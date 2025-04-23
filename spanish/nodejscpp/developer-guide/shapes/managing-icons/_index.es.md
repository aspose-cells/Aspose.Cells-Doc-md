---  
title: Agregar íconos a la hoja de cálculo con Node.js a través de C++  
linktitle: Gestionar iconos  
type: docs  
weight: 100  
url: /es/nodejs-cpp/insert-svg-to-excel/  
---  

## Agregar íconos a la hoja de cálculo en Aspose.Cells for Node.js via C++

Si necesita usar [Aspose.Cells](https://products.aspose.com/cells/) para agregar 'iconos' en un archivo de Excel, este documento puede ofrecerle ayuda.

La interfaz de Excel correspondiente a la operación de insertar icono es la siguiente:

![](1.png)

- Seleccione la posición del icono a insertar en la hoja de cálculo
- Haga clic izquierdo *Insertar*->*Iconos*
- En la ventana que se abre, seleccione el icono en el rectángulo rojo en la figura anterior
- Haz clic izquierdo en *Insertar*, se insertará en el archivo de Excel.

El efecto es el siguiente:

![](2.png)

Aquí, hemos preparado *código de ejemplo* para ayudarte a insertar íconos usando [Aspose.Cells](https://products.aspose.com/cells/). También hay un [archivo de ejemplo](sample.xlsx) y un [archivo de recursos](icon.zip). Usamos la interfaz de Excel para insertar un ícono con el mismo efecto visual que el [archivo de recursos](icon.zip) en el [archivo de ejemplo](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Cuando ejecute el código anterior en su proyecto, obtendrá los siguientes resultados:

![](3.png)  

