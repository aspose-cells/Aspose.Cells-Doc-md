---
title: Cambios en la API pública en Aspose.Cells 8.2.0
type: docs
weight: 70
url: /es/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.1.2 a la 8.2.0, que pueden ser de interés para desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad MultiThreadReading para la clase Cells**
Con Aspose.Cells for .NET 8.2.0, se ha añadido la propiedad MultiThreadReading a la clase Cells para proporcionar un mecanismo más robusto para leer los valores de las celdas con múltiples hilos simultáneamente. Establecer la propiedad de tipo Booleano en true en la aplicación multi-hilo garantiza que cada hilo reciba el valor correcto de las celdas.

{{% alert color="primary" %}} 

Por favor revise el artículo detallado en [Leer Valores de las Celdas Simultáneamente en un Entorno Multi-hilo](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) para obtener más información.

{{% /alert %}}
## **Añadidos sobrecargas para los métodos AutoFitRows y AutoFitColumns**
Se han añadido nuevas sobrecargas para AutoFitRows y AutoFitColumns a la clase Worksheet, permitiendo a los desarrolladores ajustar automáticamente las filas y columnas en función de sus respectivos rangos al pasar una instancia de la clase AutoFitterOptions. 

Las firmas de los métodos antes mencionados son las siguientes:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Por favor revise el artículo detallado en [Ajuste Automático de Filas y Columnas](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns)

{{% /alert %}}
