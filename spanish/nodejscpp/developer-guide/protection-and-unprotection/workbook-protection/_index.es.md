---  
title: Proteger y desbloquear la estructura del libro con Node.js via C++  
linktitle: Proteger y desproteger la estructura del libro  
type: docs  
weight: 40  
url: /es/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Proteger y desproteger la estructura del libro de archivos Excel usando Node.js via C++.  
---  


{{% alert color="primary" %}}  
Para evitar que otros usuarios vean hojas de cálculo ocultas, agreguen, muevan, eliminen u oculten hojas de cálculo, y cambien el nombre de las hojas de cálculo, puede proteger la estructura de su libro de Excel con una contraseña.  
{{% /alert %}}  


## **Proteger y desproteger la estructura del libro en MS Excel**  

**![proteger y desproteger la estructura del libro](proteger-y-desproteger-la-estructura-del-libro.png)**  

1. Haga clic en **Revisar > Proteger libro**.  
1. Ingrese una contraseña en **el cuadro de Contraseña**.  
1. Seleccione **Aceptar**, vuelva a ingresar la contraseña para confirmarla y luego seleccione **Aceptar** nuevamente.  


## **Proteger estructura del libro usando Aspose.Cells for Node.js via C++**  
Solo necesitas las siguientes líneas de código simples para implementar la protección de la estructura del libro de trabajo de archivos de Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Desproteger estructura del libro usando Aspose.Cells for Node.js via C++**  
Desproteger la estructura del libro es fácil con la API de Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Nota: se requiere una contraseña correcta.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
