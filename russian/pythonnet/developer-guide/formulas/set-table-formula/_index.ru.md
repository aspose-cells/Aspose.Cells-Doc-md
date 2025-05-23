---
title: Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки
linktitle: Устанавливает формулу таблицы
type: docs
weight: 260
url: /ru/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Возможные сценарии использования**
Иногда вы хотите, чтобы формула в таблице или списке автоматически распространялась на новые строки при вводе новых данных. Это поведение по умолчанию в Microsoft Excel. Чтобы добиться того же в Aspose.Cells для Python via .NET, используйте свойство [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula).

## **Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки**
Приведенный ниже образец кода создает таблицу или объект списка таким образом, что формула в столбце B будет автоматически распространяться на новые строки при вводе новых данных. Пожалуйста, проверьте [выходной файл Excel](5115469.xlsx), сгенерированный этим кодом. Если вы введете любое число в ячейку A3, то увидите, что формула в ячейке B2 автоматически распространится на ячейку B3.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

