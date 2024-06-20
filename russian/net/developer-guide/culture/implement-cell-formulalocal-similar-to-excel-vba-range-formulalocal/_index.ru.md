---
title: Реализуйте свойство Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ru/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Возможные сценарии использования**

Формулы Microsoft Excel могут иметь разные названия в различных локалях, регионах или языках. Например, функция **SUM** называется **SUMME** на немецком. Aspose.Cells не может работать с именами функций на не-английском языке. В Microsoft Excel VBA есть свойство **Range.FormulaLocal**, которое возвращает название функции в соответствии с его языком или регионом. Aspose.Cells также предоставляет свойство [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) для этой цели. Однако это свойство будет работать только при реализации метода [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname).

## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**

Приведенный ниже образец кода объясняет, как реализовать метод [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname). Метод возвращает локальное название стандартной функции. Если стандартное название функции **SUM**, он возвращает **UserFormulaLocal_SUM**. Вы можете изменить код в соответствии с вашими потребностями и вернуть правильные локальные названия функций, например **SUM** - **SUMME** на немецком, а **TEXT** - **ТЕКСТ** на русском. Также ознакомьтесь с выводом консоли приведенного ниже образца кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
