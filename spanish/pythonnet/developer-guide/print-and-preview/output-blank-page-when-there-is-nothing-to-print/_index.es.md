---
title: Página en Blanco de Salida cuando no hay Nada que Imprimir
type: docs
weight: 90
url: /es/python-net/output-blank-page-when-there-is-nothing-to-print/
---

## **Escenarios de uso posibles**

Si la hoja está vacía, entonces Aspose.Cells para Python via .NET no imprimirá nada cuando exportes la hoja de cálculo a imagen. Puedes cambiar este comportamiento usando la propiedad [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print). Cuando la configures en **true**, imprimirá la página en blanco.

## **Página en Blanco de Salida cuando no hay Nada que Imprimir**

El siguiente código de ejemplo crea el libro vacío que tiene una hoja de cálculo vacía y genera la hoja de cálculo vacía como una imagen después de establecer la propiedad [**ImageOrPrintOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/output_blank_page_when_nothing_to_print) como **true**. Como resultado, genera la página en blanco al no haber nada que imprimir, lo que se puede ver en la imagen a continuación.

![todo:image_alt_text](1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-OutputBlankPageWhenThereIsNothingToPrint-1.py" >}}

