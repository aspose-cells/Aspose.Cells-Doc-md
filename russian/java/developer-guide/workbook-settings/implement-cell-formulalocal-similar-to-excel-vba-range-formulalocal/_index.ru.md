---
title: Реализуйте свойство Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /ru/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Возможные сценарии использования**
Множество локализаций функций Microsoft Excel могут иметь разные названия в разных регионах или языках. Например, функция *SUM* называется *SUMME* в *немецком*. Aspose.Cells не работает с неанглийскими названиями функций. В *Microsoft Excel VBA* есть свойство *Range.FormulaLocal*, которое возвращает название функции в соответствии с языком или регионом. Aspose.Cells также предоставляет свойство [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) для этой цели. Однако это свойство работает только при реализации метода [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) 
## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**
Следующий пример кода объясняет, как реализовать метод [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-). Он возвращает локализованное название стандартной функции. Если стандартное название функции *SUM*, он возвращает *UserFormulaLocal_SUM*. Вы можете изменить код в соответствии с вашими потребностями, чтобы возвращать правильные локальные имена функций, например *SUM* — *SUMME* в *немецком* и *TEXT* — *ТЕКСТ* в *русском*. Также ознакомьтесь с примером вывода в консоль для кода ниже.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Вывод в консоль**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
