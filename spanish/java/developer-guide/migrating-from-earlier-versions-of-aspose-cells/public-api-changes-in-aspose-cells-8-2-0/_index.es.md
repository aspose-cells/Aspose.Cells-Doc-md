---
title: Cambios en la API pública en Aspose.Cells 8.2.0
type: docs
weight: 80
url: /es/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.1.2 a la 8.2.0, que pueden ser de interés para desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad MultiThreadReading para la clase Cells**
Con Aspose.Cells for Java 8.2.0, la propiedad MultiThreadReading se ha agregado a la clase Cells para proporcionar un mecanismo más robusto para leer los valores de las celdas con varios hilos simultáneamente. Establecer la propiedad de tipo Boolean en true en la aplicación de varios hilos asegura que cada hilo reciba el valor correcto de las celdas.

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Lectura simultánea de los valores de las celdas en un entorno de múltiples hilos](/cells/es/java/reading-cell-values-in-multiple-threads-simultaneously/) para obtener más información.

{{% /alert %}}
## **Se agregaron sobrecargas para los métodos autoFitRows y autoFitColumns**
Se han agregado nuevas sobrecargas para los métodos autoFitRows y autoFitColumns a la clase Worksheet, lo que permite a los desarrolladores ajustar automáticamente las filas y columnas en función de sus rangos respectivos al pasar una instancia de la clase AutoFitterOptions. 

Las firmas de los métodos antes mencionados son las siguientes:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Por favor, consulte el artículo detallado sobre [Ajuste automático de filas y columnas](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
