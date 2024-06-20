---
title: Implementar tamaño de papel personalizado de la hoja de cálculo para la representación
type: docs
weight: 30
url: /es/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **Escenarios de uso posibles**

No hay una opción directa disponible para crear tamaños de papel personalizados en MS Excel, sin embargo, puedes establecer el tamaño de papel personalizado de tus hojas de trabajo deseadas al renderizar el archivo de Excel al formato de archivo PDF. Este documento explica cómo establecer un tamaño de papel personalizado de una hoja de trabajo usando las APIs de Aspose.Cells.

## **Implementar Tamaño de Papel Personalizado de la Hoja de Cálculo para el Renderizado**

Aspose.Cells te permite implementar tu tamaño de papel deseado de la hoja de trabajo usando el método [**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize(double,%20double)) del [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup). El siguiente código de ejemplo ilustra cómo especificar un tamaño de papel personalizado para la primera hoja de trabajo en el libro. Por favor, revisa también el [PDF de salida](45056030.pdf) generado con el siguiente código como referencia.

## **Captura de pantalla**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
