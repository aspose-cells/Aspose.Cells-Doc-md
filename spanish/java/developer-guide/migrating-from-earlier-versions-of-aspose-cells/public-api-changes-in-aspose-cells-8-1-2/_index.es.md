---
title: Cambios en la API pública en Aspose.Cells 8.1.2
type: docs
weight: 70
url: /es/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.1.1 a la 8.1.2, que pueden ser de interés para desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **Se agregó soporte para advertencias si se produce una sustitución de fuente**
Con Aspose.Cells for Java 8.1.2, se han agregado las clases WarningInfo y WarningType, la interfaz IWarningCallback, y las propiedades SaveOptions.WarningCallback e ImageOrPrintOptions.WarningCallback para permitir a los desarrolladores recibir advertencias cuando se produce una sustitución de fuente al convertir hojas de cálculo a imágenes, formatos XPS y PDF. 

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Obtención de advertencias por sustitución de fuente al representar hojas de cálculo](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) para obtener más información.

{{% /alert %}}
## **Se eliminó la propiedad obsoleta PdfSaveOptions.ChartImageType**
Aspose.Cells for Java 8.1.2 ha eliminado la propiedad obsoleta PdfSaveOptions.ChartImageType de la API pública.
