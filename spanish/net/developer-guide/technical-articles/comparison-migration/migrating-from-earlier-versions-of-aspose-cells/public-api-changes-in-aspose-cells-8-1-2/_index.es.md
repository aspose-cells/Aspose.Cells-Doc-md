---
title: Público API Cambios en Aspose.Cells 8.1.2
type: docs
weight: 60
url: /es/net/public-api-changes-in-aspose-cells-8-1-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.1.1 a la 8.1.2, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó soporte para advertencia si ocurre sustitución de fuente**
Con Aspose.Cells for .NET 8.1.2, las clases WarningInfo, WarningType, la interfaz IWarningCallback y las propiedades SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback se han agregado para facilitar que el usuario reciba una advertencia si se produce una sustitución de fuentes al convertir hojas de cálculo a imágenes o al formato PDF.

{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Obtención de advertencias para la sustitución de fuentes al renderizar hojas de cálculo](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Se eliminó la propiedad PdfSaveOptions.ChartImageType obsoleta**
Aspose.Cells for .NET 8.1.2 ha eliminado la propiedad obsoleta PdfSaveOptions.ChartImageType del público API.
