---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal con Golang a través de C++
linktitle: Implementar Cell.FormulaLocal
type: docs
weight: 30
url: /es/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aprenda cómo implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal usando Aspose.Cells con Golang a través de C++
---

## **Escenarios de uso posibles**

Las fórmulas de Microsoft Excel pueden tener diferentes nombres en diferentes lugares o regiones o idiomas. Por ejemplo, la función **SUMA** se llama **SUMME** en alemán. Aspose.Cells no puede trabajar con nombres de función no-ingleses. En Microsoft Excel VBA, hay una propiedad **Range.FormulaLocal** que devuelve el nombre de la función según su idioma o región. Aspose.Cells también proporciona la propiedad [**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/) para este propósito. Sin embargo, esta propiedad solo funcionará cuando implemente el método [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**

El siguiente código de ejemplo explica cómo implementar el método [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/). El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es **SUM**, devuelve **UserFormulaLocal_SUM**. Puede cambiar el código según sus necesidades y devolver los nombres de función locales correctos, por ejemplo **SUMA** es **SUMME** en alemán y **TEXTO** es **ТЕКСТ** en ruso. Por favor, consulte también la salida de consola del código de ejemplo dado abajo para referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **Salida de la consola**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
