---  
title: Verificar contraseña para modificar usando Aspose.Cells for Node.js via C++  
linktitle: Verificar contraseña para modificar  
type: docs  
weight: 2400  
url: /es/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Aprende cómo verificar si una contraseña para modificar coincide usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A veces, necesitas verificar programáticamente si la contraseña dada coincide con la **Contraseña para modificar**. Aspose.Cells proporciona el método `WorkbookSettings.writeProtection.validatePassword()` que puedes usar para verificar si la contraseña dada es correcta o no.  
{{% /alert %}}  

## **Verificar Contraseña para modificar en Microsoft Excel**  

Puedes asignar **Contraseña para abrir** y **Contraseña para modificar** al crear tus libros de trabajo en Microsoft Excel. Por favor, mira esta captura de pantalla que muestra la interfaz que Microsoft Excel proporciona para especificar estas contraseñas.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Verificar contraseña para modificar usando Aspose.Cells for Node.js via C++**  

Los siguientes códigos de ejemplo cargan el archivo de [origen de Excel](5112232.xlsx). Tiene una contraseña para abrirla 1234 y una contraseña para modificarla 5678. Primero comprueba si 567 es la contraseña correcta para modificar y devuelve falso, luego verifica si 5678 es la contraseña y devuelve verdadero.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **Salida de la consola**  

Aquí está la salida de la consola del código de muestra anterior después de cargar el archivo de Excel fuente.  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
