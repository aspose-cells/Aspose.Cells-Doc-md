---
title: Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /ru/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Возможные сценарии использования**
Microsoft Формулы Excel могут иметь разные названия в разных языковых стандартах, регионах или языках. Например,*СУММА*функция называется*СУММА*в*Немецкий*Aspose.Cells не может работать с неанглийскими именами функций. В*Microsoft Excel VBA*, есть* *а*Range.FormulaLocal*свойство, которое возвращает имя функции в соответствии с ее языком или регионом. Aspose.Cells также предоставляет[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)имущество для этой цели. Однако это свойство будет работать только тогда, когда вы реализуете[GlobalizationSettings.getLocalFunctionName (стандартное имя строки)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) метод.
## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**
В следующем примере кода объясняется, как реализовать[GlobalizationSettings.getLocalFunctionName (стандартное имя строки)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) метод. Метод возвращает локальное имя стандартной функции. Если стандартное имя функции*СУММА*, он возвращается*UserFormulaLocal_SUM*. Вы можете изменить код в соответствии с вашими потребностями и вернуть правильные имена локальных функций, например*СУММА*является*СУММА*в*Немецкий*и*ТЕКСТ*является*ТЕКСТ*в*Русский*. См. также вывод на консоль примера кода, приведенного ниже, для справки.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Консольный вывод**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
