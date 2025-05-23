---
title: Настройка общих формул
type: docs
weight: 10
url: /ru/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Если вы хотите добавить функцию в рабочую книгу, которая будет выполнять некоторые вычисления, в этой статье объясняется, как выполнить эту задачу с помощью Aspose.Cells.

{{% /alert %}}

## Установка общей формулы с использованием Aspose.Cells

Предположим, у вас есть лист с данными в формате, который выглядит как приведенный ниже образец листа.

|**Исходный файл с одним столбцом или данными**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Вы хотите добавить функцию в B2, которая будет вычислять налог с продаж для первой строки данных. Налог составляет **9%**. Формула, вычисляющая налог с продаж, такова: **"=A2*0.09"**. В этой статье объясняется, как применить эту формулу с помощью Aspose.Cells.

Aspose.Cells позволяет указывать формулу, используя свойство [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula). Для других ячеек (B3, B4, B5 и так далее) в столбце есть два варианта добавления формул.

Либо делайте то же самое, что и для первой ячейки, эффективно устанавливая формулу для каждой ячейки, соответственно обновляя ссылку на ячейку (A3*0.09, A4*0.09, A5*0.09 и так далее). Это требует обновления ссылок на ячейки для каждой строки. Также это требует анализа Aspose.Cells для каждой формулы индивидуально, что может занимать много времени для больших электронных таблиц и сложных формул. Это также добавляет дополнительные строки кода, хотя циклы могут уменьшить их до некоторой степени.

Другой подход - использовать **общую формулу**. С общей формулой формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы налог был рассчитан правильно. Метод [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) более эффективен, чем первый метод.

Приведенный ниже пример демонстрирует, как его использовать.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
