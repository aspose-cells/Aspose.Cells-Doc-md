---  
title: Gestión de objetos OLE con Node.js a través de C++  
linktitle: Gestión de objetos OLE  
type: docs  
weight: 50  
url: /es/nodejs-cpp/managing-ole-objects/  
description: Aprende cómo gestionar objetos OLE en Aspose.Cells for Node.js via C++. Agrega, extrae y manipula objetos OLE dentro de hojas de cálculo.  
---  

## **Introducción**  

OLE (Objeto Enlazado e Inserto) es un marco para la tecnología de documentos compuestos. En pocas palabras, un documento compuesto es algo como un escritorio de visualización que puede contener objetos visuales e informativos de todo tipo: texto, calendarios, animaciones, sonido, video en movimiento, 3D, noticias actualizadas continuamente, controles, etc. Cada objeto del escritorio es una entidad de programa independiente que puede interactuar con un usuario y también comunicarse con otros objetos en el escritorio.  

OLE es compatible con muchos programas diferentes y se usa para hacer que el contenido creado en un programa esté disponible en otro. Por ejemplo, puedes insertar un documento de Microsoft Word en Microsoft Excel. Para ver qué tipos de contenido puedes insertar, haz clic en **Objeto** en el menú **Insertar**. Solo aparecen en el cuadro **Tipo de objeto** los programas que están instalados en la computadora y que soportan objetos OLE.  

### **Inserción de objetos OLE en la hoja de cálculo**  

Aspose.Cells for Node.js via C++ soporta agregar, extraer y manipular objetos OLE en hojas de cálculo. Por esta razón, Aspose.Cells tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), utilizada para agregar un nuevo objeto OLE a la colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:  

- La propiedad [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) especifica los datos de la imagen (ícono) de tipo arreglo de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.  
- La propiedad [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) especifica los datos del objeto en forma de un arreglo de bytes. Estos datos se mostrarán en su programa relacionado cuando hagas doble clic en el ícono del objeto OLE.  

El siguiente ejemplo muestra cómo agregar un objeto(s) OLE a una hoja de cálculo.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Extracción de objetos OLE en el libro de trabajo**  

El siguiente ejemplo muestra cómo extraer objetos OLE en un libro de trabajo. El ejemplo obtiene diferentes objetos OLE de un archivo XLS existente y guarda diferentes archivos (DOC, XLS, PPT, PDF, etc.) basándose en el tipo de formato de archivo del objeto OLE.  

Después de ejecutar el código, podemos guardar diferentes archivos basados en sus respectivos tipos de formato de objetos OLE.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Extrayendo archivo MOL incrustado**  

Aspose.Cells for Node.js via C++ soporta extraer objetos de tipos poco comunes como MOL (archivo de datos moleculares que contiene información sobre átomos y enlaces). El siguiente fragmento de código demuestra cómo extraer un archivo MOL incrustado y guardarlo en disco usando este [archivo de ejemplo de Excel](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Temas avanzados**  
- [Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado](/cells/es/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells](/cells/es/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extraer objetos OLE del libro de trabajo](/cells/es/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Obtener o establecer el identificador de clase del objeto OLE incrustado](/cells/es/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Insertar un archivo WAV como un objeto OLE](/cells/es/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
