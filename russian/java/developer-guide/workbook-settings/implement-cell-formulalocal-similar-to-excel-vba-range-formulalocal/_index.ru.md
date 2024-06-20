---
title: Реализуйте свойство Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /ru/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Возможные сценарии использования**
Формулы Microsoft Excel могут иметь разные названия в различных регионах или языках. Например, функция *SUM* называется *SUMME* на немецком. Aspose.Cells не может работать с функциями на не-английском языке. В Microsoft Excel VBA существует свойство *Range.FormulaLocal*, которое возвращает название функции в соответствии с его языком или регионом. Aspose.Cells также предоставляет свойство [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) для этой цели. Однако это свойство будет работать только при реализации метода [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)). 
## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**
В следующем примере кода объясняется, как реализовать метод [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)). Метод возвращает локальное название стандартной функции. Если стандартное название функции *SUM*, он возвращает *UserFormulaLocal_SUM*. Вы можете изменить код в соответствии с вашими потребностями и вернуть правильные локальные названия функций, например *SUM* является *SUMME* на немецком и *TEXT* является *ТЕКСТ* на русском. Также обратите внимание на консольный вывод приведенного ниже примера кода для справки.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Вывод в консоль**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
