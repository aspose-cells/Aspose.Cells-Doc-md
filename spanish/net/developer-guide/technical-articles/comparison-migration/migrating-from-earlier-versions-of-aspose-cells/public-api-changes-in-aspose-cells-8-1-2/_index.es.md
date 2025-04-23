---
title: Cambios en la API pública en Aspose.Cells 8.1.2
type: docs
weight: 60
url: /es/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.1.1 a la 8.1.2, que pueden ser de interés para desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **Se agregó soporte para advertencias si se produce una sustitución de fuente**
Con Aspose.Cells for .NET 8.1.2, las clases WarningInfo, WarningType, la interfaz IWarningCallback y las propiedades SaveOptions.WarningCallback e ImageOrPrintOptions.WarningCallback han sido añadidas para facilitar al usuario recibir una advertencia si ocurre la sustitución de fuentes al convertir hojas de cálculo a imágenes o formato PDF. 

{{% alert color="primary" %}} 

Por favor revise el artículo detallado en [Obtener Advertencias por Sustitución de Fuentes al Renderizar Hojas de Cálculo](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Se eliminó la propiedad obsoleta PdfSaveOptions.ChartImageType**
Aspose.Cells for .NET 8.1.2 ha eliminado la propiedad obsoleta PdfSaveOptions.ChartImageType de la API pública.
{{< app/cells/assistant language="csharp" >}}
