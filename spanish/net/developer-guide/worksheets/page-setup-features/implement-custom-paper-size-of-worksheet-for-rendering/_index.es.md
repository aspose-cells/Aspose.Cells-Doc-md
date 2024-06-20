---
title: Implementar tamaño de papel personalizado de la hoja de cálculo para la representación
type: docs
weight: 70
url: /es/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Este artículo explica cómo utilizar el código de muestra de la API de C# o biblioteca .NET para establecer el tamaño de papel personalizado de las hojas de cálculo deseadas al convertir un archivo de Excel a formato de archivo PDF de forma programática.
keywords: establecer tamaño de papel personalizado al renderizar excel a pdf c#
---

## **Escenarios de uso posibles**

No hay una opción directa disponible para crear tamaños de papel personalizados en MS Excel, sin embargo, puede establecer el tamaño de papel personalizado de sus hojas de cálculo deseadas al renderizar el archivo de Excel al formato de archivo PDF. Este documento explica cómo establecer un tamaño de papel personalizado de una hoja de cálculo utilizando las APIs de Aspose.Cells.

## **Implementar Tamaño de Papel Personalizado de la Hoja de Cálculo para el Renderizado**

Aspose.Cells le permite implementar el tamaño de papel deseado de la hoja de cálculo. Puede usar el método [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) para especificar un tamaño de página personalizado. El siguiente código de muestra ilustra cómo especificar un tamaño de papel personalizado para la primera hoja de trabajo en el libro. Consulte también el [PDF de salida](45056028.pdf) generado con el siguiente código como referencia.

## **Captura de pantalla**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
