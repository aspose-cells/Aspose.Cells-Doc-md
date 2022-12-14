---
title: Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /ru/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Возможные сценарии использования**

 Microsoft Формулы Excel могут иметь разные названия в разных языковых стандартах, регионах или языках. Например,**СУММА**функция называется**СУММА** на немецком. Aspose.Cells не может работать с неанглийскими именами функций. В Microsoft Excel VBA есть**Range.FormulaLocal**свойство, которое возвращает имя функции в соответствии с ее языком или регионом. Aspose.Cells также предоставляет[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)имущество для этой цели. Однако это свойство будет работать только тогда, когда вы реализуете[**GlobalizationSettings.GetLocalFunctionName (стандартное имя строки)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)метод.

## **Реализовать Cell.FormulaLocal аналогично Excel VBA Range.FormulaLocal**

 В следующем примере кода объясняется, как реализовать[**GlobalizationSettings.GetLocalFunctionName (стандартное имя строки)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) метод. Метод возвращает локальное имя стандартной функции. Если стандартное имя функции**СУММА** , он возвращается**UserFormulaLocal_SUM** Вы можете изменить код в соответствии с вашими потребностями и вернуть правильные имена локальных функций, например**СУММА** является**СУММА** на немецком и**ТЕКСТ** является**ТЕКСТ**на русском. См. также вывод на консоль примера кода, приведенного ниже, для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
