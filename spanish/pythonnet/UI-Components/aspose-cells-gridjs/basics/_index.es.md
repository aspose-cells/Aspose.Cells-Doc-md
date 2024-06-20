---
title: Conceptos básicos de Aspose.Cells.GridJs
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## Fundamentos de GridJs

Aspose.Cells.GridJs es una biblioteca que permite a los usuarios desarrollar aplicaciones web multiplataforma para ver o editar archivos de hojas de cálculo de forma rápida y sencilla. 

## Por qué usar Aspose.Cells.GridJs


- Permite a los usuarios crear, editar, dar formato, colaborar y compartir hojas de cálculo de forma segura con actualizaciones en tiempo real, soporte para fórmulas y herramientas de visualización de datos enriquecidas, similares a las aplicaciones de escritorio tradicionales.
- Admite Entrada y Edición de Datos, Formato, Navegación por la Hoja de Cálculo, Cálculo de Fórmulas, Manipulación de Datos, Gráficos y Visualizaciones, Importación y Exportación, Seguridad, Complementos y Personalización para que los desarrolladores adapten el editor a las necesidades empresariales específicas.

## Características


- Importar, ver y editar los formatos de hojas de cálculo populares.
- Exportar las hojas de cálculo a varios formatos de archivo admitidos.
- Mostrar y gestionar archivos de imagen, formas o gráficos.
- Realizar la personalización del diseño y la disposición del Grid.
- Gestión de múltiples hojas de cálculo.
- Creación y cálculo de fórmulas de Excel®.

## Formatos de archivo compatibles

https://docs.aspose.com/cells/python-net/supported-file-formats/

## Uso General

A continuación se muestran los pasos básicos del proceso para desarrollar una aplicación web de GridJs.

- Establecer el directorio de almacenamiento en caché mediante Config.set_file_cache_directory(`su directorio de almacenamiento`)
- Establecer la Licencia mediante Config.set_license(`su ruta de licencia`)
- Establecer la URL de la ruta de la imagen GridJsWorkbook.set_image_url_base(`ruta para ver la imagen`);
- Configurar una acción de ruta para obtener `json` del archivo de hoja de cálculo. Puede utilizar las API `GridJsWorkbook.ImportExcelFile` y `GridJsWorkbook.ExportToJson`, `GridJs` almacenará automáticamente el archivo en caché.
- Configurar una acción de ruta para obtener `json` para la operación de actualización. Puede utilizar `GridJsWorkbook.UpdateCell` `API`, `GridJs` realizará la operación de actualización en caché y devolverá el 'json' actualizado.
- Configurar una acción de ruta para obtener el archivo en caché, de esta manera podemos obtener el archivo zip de imágenes/formas o el archivo de hoja de cálculo en caché.
- Configurar una acción de ruta para descargar la hoja de cálculo. Puede utilizar la API `GridJsWorkbook.SaveToCacheWithFileName`.

A continuación se muestra una demostración básica para mostrar el uso de Aspose.Cells.GridJs :

https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 

En la demostración utilizamos [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) para la renderización de la página del lado del cliente.

Si tiene alguna pregunta, requerimiento o necesita ayuda, por favor, envíe sus comentarios al siguiente sitio web https://forum.aspose.com/c/cells/9
