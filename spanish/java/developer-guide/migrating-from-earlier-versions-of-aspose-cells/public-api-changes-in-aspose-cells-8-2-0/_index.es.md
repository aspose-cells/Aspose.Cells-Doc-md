---
title: Público API Cambios en Aspose.Cells 8.2.0
type: docs
weight: 80
url: /es/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.1.2 a la 8.2.0, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad MultiThreadReading para la clase Cells**
Con Aspose.Cells for Java 8.2.0, la propiedad MultiThreadReading se ha agregado a la clase Cells para proporcionar un mecanismo más sólido para leer valores de celdas con múltiples subprocesos simultáneamente. Establecer la propiedad de tipo booleano en verdadero en la aplicación de subprocesos múltiples asegura que cada subproceso recibirá el valor de celdas correcto.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Lectura simultánea de valores Cells en un entorno de subprocesos múltiples](/cells/es/java/reading-cell-values-in-multiple-threads-simultaneously/) para más información.

{{% /alert %}}
## **Se agregaron sobrecargas para los métodos autoFitRows y autoFitColumns**
 Se agregaron nuevas sobrecargas para autoFitRows y autoFitColumns a la clase Worksheet, lo que permite a los desarrolladores ajustar automáticamente las filas y columnas en función de sus respectivos rangos al pasar una instancia de la clase AutoFitterOptions.

Las firmas de los métodos antes mencionados son las siguientes:

1. autoFitRows(int startRow, int endRow, opciones de AutoFitterOptions)
1. autoFitColumns(int firstColumn, int lastColumn, opciones de AutoFitterOptions)

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Filas y columnas de ajuste automático](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
