---  
title: Proteger y desbloquear la hoja de trabajo con Node.js via C++  
linktitle: Proteger y Desproteger Hoja de Cálculo  
type: docs  
weight: 40  
url: /es/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Proteger y desproteger hojas de trabajo de archivos Excel con Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Para evitar que otros usuarios cambien, muevan o eliminen datos en una hoja de cálculo de forma accidental o deliberada, puede bloquear las celdas en su hoja de cálculo de Excel y luego proteger la hoja con una contraseña.  
{{% /alert %}}  

## **Proteger y desproteger Hoja de Cálculo en MS Excel**  

**![proteger y desproteger Hoja de Cálculo](protect-and-unprotect-worksheet.png)**  

1. Haga clic en **Revisar > Proteger Hoja**.  
1. Ingrese una contraseña en **el cuadro de Contraseña**.  
1. Seleccione las opciones de **permitir**.  
1. Seleccione **Aceptar**, vuelva a ingresar la contraseña para confirmarla y luego seleccione **Aceptar** nuevamente.  

## **Proteger hoja de trabajo usando Aspose.Cells for Node.js via C++**  
Solo necesitas las siguientes líneas de código simples para implementar la protección de la estructura del libro de trabajo de archivos de Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Desproteger hoja de trabajo usando Aspose.Cells for Node.js via C++**  
Desproteger la hoja de trabajo es fácil con la API Aspose.Cells. Si la hoja está protegida por contraseña, se requiere una contraseña correcta.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Temas avanzados**  
- [Configuración de Protección Avanzada desde Excel XP](/cells/es/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Detectar si la hoja de cálculo está protegida con contraseña](/cells/es/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Protección de Hojas de Cálculo](/cells/es/nodejs-cpp/protecting-worksheets/)  
- [Desproteger una Hoja de Cálculo](/cells/es/nodejs-cpp/unprotect-a-worksheet/)  
- [Verificar la Contraseña Utilizada para Proteger la Hoja de Cálculo](/cells/es/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

