---
title: Conceptos básicos de Aspose.Cells.GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: Este artículo introduce los pasos básicos para configurar una aplicación web para GridJs.
---

## Fundamentos de GridJs

Aspose.Cells.GridJs es una biblioteca estándar de .NET que permite a los usuarios desarrollar aplicaciones web para mostrar/editar hojas de cálculo de forma rápida y sencilla. 

Aspose.Cells.GridJs admite la importación de los formatos de archivo de hojas de cálculo populares (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

También permite exportar archivos de Excel a PDF, HTML, etc. A continuación se muestran los pasos básicos del proceso para desarrollar una aplicación web de GridJs.

- Implementar GridCacheForStream para escribir tu propia lógica empresarial para el almacenamiento en caché.
- Configurar una acción del controlador para obtener json del archivo de hoja de cálculo. Puedes utilizar las APIs GridJsWorkbook.ImportExcelFile y GridJsWorkbook.ExportToJson, GridJs almacenará automáticamente el archivo de cálculo en caché.
- Configurar una acción del controlador para obtener JSON para la operación de actualización. Puede utilizar la API GridJsWorkbook.UpdateCell, GridJs realizará la operación de actualización en caché y devolverá el JSON actualizado.
- Configurar una acción del controlador para obtener la URL de archivos de imágenes/formas en la hoja de cálculo, GridJs automáticamente comprimirá todas las imágenes/formas en caché. Se utilizará la API GridCacheForStream.GetFileUrl.
- Configurar una acción del controlador para obtener un archivo en caché, así podremos obtener el archivo zip de imágenes/formas o el archivo de la hoja de cálculo en caché. Se utilizará la API GridCacheForStream.LoadStream.
- Configurar una acción del controlador para descargar la hoja de cálculo. Puede utilizar la API GridJsWorkbook.SaveToCacheWithFileName.

A continuación, una demostración básica para mostrar el uso de Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs


Si tiene alguna pregunta, requerimiento o necesita ayuda, por favor, envíe sus comentarios al siguiente sitio web https://forum.aspose.com/c/cells/9
