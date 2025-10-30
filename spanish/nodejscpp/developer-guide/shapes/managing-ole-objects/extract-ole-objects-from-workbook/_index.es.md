---  
title: Extraer objetos OLE del libro de trabajo con Node.js vía C++  
linktitle: Extraer objetos OLE del libro de trabajo  
type: docs  
weight: 110  
url: /es/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
A veces, necesita extraer objetos OLE de un libro de trabajo. Aspose.Cells soporta la extracción y guardado de esos objetos OLE.

Este artículo muestra cómo crear una aplicación de consola en Node.js a través de C++ y extraer diferentes objetos OLE de un libro de trabajo con unas pocas líneas de código.  
{{% /alert %}}  

## **Extraer objetos OLE de un libro de trabajo**  

### **Crear un libro de trabajo de plantilla**  

1. Crea un libro de trabajo en Microsoft Excel.  
1. Agrega un documento de Microsoft Word, un libro de Excel y un documento PDF como objetos OLE en la primera hoja de trabajo.  

| **Documento de plantilla con objetos OLE (OleFile.xls)** |  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

Luego, extrae los objetos OLE y guárdalos en el disco duro con sus respectivos tipos de archivo.  

### **Descargar e instalar Aspose.Cells**  

1. [Descarga Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Instálelo en su equipo de desarrollo.  

Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.  

### **Crear un proyecto**  

Inicie **Node.js** y cree una nueva aplicación de consola. Este ejemplo mostrará una aplicación de consola Node.js, pero también puede usar cualquier entorno compatible con JavaScript.  

1. Agregar Dependencias  
   1. Agregue una referencia al componente Aspose.Cells a su proyecto, por ejemplo, incluya el paquete usando la función `require`:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **Extraer objetos OLE**  

El código a continuación realiza la tarea de encontrar y extraer objetos OLE. Los objetos OLE (archivos DOC, XLS y PDF) se guardan en el disco.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
