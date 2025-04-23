---
title: Página en Blanco de Salida cuando no hay Nada que Imprimir
type: docs
weight: 90
url: /es/net/output-blank-page-when-there-is-nothing-to-print/
---

## **Escenarios de uso posibles**

Si la hoja está vacía, entonces Aspose.Cells no imprimirá nada al exportar la hoja de cálculo a imagen. Puedes cambiar este comportamiento utilizando la propiedad [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint). Cuando la establezcas como **true**, imprimirá la página en blanco.

## **Página en Blanco de Salida cuando no hay Nada que Imprimir**

El siguiente código de ejemplo crea el libro vacío que tiene una hoja de cálculo vacía y genera la hoja de cálculo vacía como una imagen después de establecer la propiedad [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/outputblankpagewhennothingtoprint) como **true**. Como resultado, genera la página en blanco al no haber nada que imprimir, lo que se puede ver en la imagen a continuación.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
