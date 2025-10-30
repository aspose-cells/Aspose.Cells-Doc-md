---  
title: Proteger por contraseña el proyecto VBA del libro de trabajo de Excel con Node.js a través de C++  
linktitle: Proteger con contraseña el proyecto VBA del libro de Excel  
type: docs  
weight: 10  
url: /es/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Aprende cómo proteger con contraseña el proyecto VBA de un libro de Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Protege con contraseña el Proyecto VBA de un libro de Excel en Node.js**  

Puedes proteger con contraseña el Proyecto VBA (Visual Basic for Applications) de un libro usando Aspose.Cells con el método [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-).  

## **Código de muestra**  

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](43352067.xlsm), accede a su Proyecto VBA y lo protege con una contraseña. Finalmente, lo guarda como el [archivo de Excel de salida](43352068.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
