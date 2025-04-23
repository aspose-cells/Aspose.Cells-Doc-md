---
title: Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки
type: docs
weight: 980
url: /ru/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Возможные сценарии использования**
Иногда вам нужна формула в вашей таблице или объекте списка автоматически распространяется на новые строки при вводе новых данных. Это поведение по умолчанию в Microsoft Excel. Чтобы достичь того же с Aspose.Cells, используйте [ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula) свойство.
## **Распространить формулу в таблице или объекте списка автоматически при вводе данных в новые строки**
В следующем образце кода создается таблица или объект списка таким образом, что формула в столбце B будет автоматически распространяться на новые строки, когда вы введете новые данные. Пожалуйста, проверьте [выходной файл Excel](5472519.xlsx), созданный с помощью этого кода. Если вы введете любое число в ячейку A3, вы увидите, что формула в ячейке B2 автоматически распространяется на ячейку B3.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
{{< app/cells/assistant language="java" >}}
