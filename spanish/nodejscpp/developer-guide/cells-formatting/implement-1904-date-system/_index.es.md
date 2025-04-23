---
title: Implementar el Sistema de Fechas 1904 con Node.js a través de C++
description: Aspose.Cells es una biblioteca de Node.js para trabajar con archivos de hojas de cálculo. Soporta la implementación del sistema de fechas 1904, permitiendo a los usuarios calcular y formatear en función del sistema de fechas del 1 de enero de 1904. Este artículo describe cómo implementar el sistema de fechas 1904 utilizando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, sistema de fechas 1904, hoja de cálculo, cálculo, formateo, Node.js a través de C++
type: docs
weight: 7000
url: /es/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel soporta dos sistemas de fechas: sistema de fechas 1900 (el sistema predeterminado implementado en Excel para Windows) y sistema de fechas 1904. El sistema de fechas 1904 se usa normalmente para garantizar compatibilidad con archivos de Excel en Macintosh y es el sistema predeterminado si usas Excel para Macintosh. Puedes configurar el sistema de fechas 1904 para archivos de Excel usando Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

Para implementar el sistema de fechas 1904 en Microsoft Excel (por ejemplo, Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**, y elige la pestaña **Cálculo**.
1. Selecciona la opción **Sistema de fecha 1904**.
1. Haz clic en **Aceptar**.

|**Seleccionar el sistema de fecha 1904 en Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Consulta el siguiente código de muestra sobre cómo lograr esto usando las API de Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
