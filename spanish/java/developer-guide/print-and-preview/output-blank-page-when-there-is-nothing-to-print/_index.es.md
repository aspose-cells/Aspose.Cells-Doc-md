---
title: Página en Blanco de Salida cuando no hay Nada que Imprimir
type: docs
weight: 80
url: /es/java/output-blank-page-when-there-is-nothing-to-print/
---

## **Escenarios de uso posibles**

Si la hoja está vacía, entonces Aspose.Cells no imprimirá nada cuando exportes la hoja de cálculo a imagen. Puedes cambiar este comportamiento utilizando la propiedad [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint). Cuando la establezcas en **true**, imprimirá la página en blanco.

## **Página en Blanco de Salida cuando no hay Nada que Imprimir**

El siguiente código de muestra crea el libro de trabajo vacío que tiene una hoja de cálculo vacía y renderiza la hoja de cálculo vacía a una imagen después de configurar la propiedad [**ImageOrPrintOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OutputBlankPageWhenNothingToPrint) como **true**. En consecuencia, genera la página en blanco ya que no hay nada que imprimir, lo cual puedes ver a continuación.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-OutputBlankPageWhenThereIsNothingToPrint-1.java" >}}
