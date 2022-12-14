---
title: Aspose.Cells. Conceptos básicos de GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/basics/
---
## Conceptos básicos de GridJs

 Aspose.Cells.GridJs es una biblioteca estándar .NET que permite a los usuarios desarrollar aplicaciones web para mostrar/editar hojas de cálculo de forma rápida y sencilla.

Aspose.Cells.GridJs admite la importación de los formatos de archivo de hoja de cálculo populares (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

También permite exportar archivos de Excel a PDF, HTML, etc. A continuación se muestran los pasos básicos del proceso para desarrollar una aplicación web de GridJs.

- Implemente GridCacheForStream para escribir su propia lógica comercial para el almacenamiento en caché.
- Configure una acción de controlador para obtener json del archivo de hoja de cálculo. Puede usar las API GridJsWorkbook.ImportExcelFile y GridJsWorkbook.ExportToJson, GridJs almacenará automáticamente el archivo de distribución en caché.
- Configure una acción de controlador para obtener json para la operación de actualización. Puede usar GridJsWorkbook.UpdateCell API, GridJs realizará la operación de actualización en caché y devolverá el json actualizado.
- Configure una acción de controlador para obtener la URL de los archivos de imágenes/formas en la hoja de cálculo, GridJs comprimirá automáticamente todas las imágenes/formas en caché. Utilizará GridCacheForStream.GetFileUrl API.
- Configure una acción de controlador para obtener el archivo en caché, por lo que podemos obtener el archivo zip de imágenes/formas o el archivo de hoja de cálculo en caché. Utilizará GridCacheForStream.LoadStream API.
- Configure una acción de controlador para descargar la hoja de cálculo. Puede usar GridJsWorkbook.SaveToCacheWithFileName API.

 A continuación hay una demostración básica para mostrar el uso de Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

Si tiene alguna pregunta, requisitos o necesita ayuda, envíe sus comentarios al siguiente sitio web https://forum.aspose.com/c/cells/9