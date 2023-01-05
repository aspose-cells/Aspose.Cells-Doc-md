---
title: Автоматическое распространение формулы в таблице или объекте списка при вводе данных в новые строки
type: docs
weight: 980
url: /ru/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Возможные сценарии использования**
 Иногда вам нужно, чтобы формула в вашей таблице или объекте списка автоматически распространялась на новые строки при вводе новых данных. Это поведение по умолчанию для Microsoft Excel. Чтобы добиться того же с Aspose.Cells, используйте[СписокКолонка.Формула](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)имущество.
## **Автоматическое распространение формулы в таблице или объекте списка при вводе данных в новые строки**
Следующий пример кода создает объект Table или List таким образом, что формула в столбце B будет автоматически распространяться на новые строки при вводе новых данных. Пожалуйста, проверьте[выходной файл excel](5472519.xlsx) генерируется с помощью этого кода. Если вы введете любое число в ячейку A3, вы увидите, что формула в ячейке B2 автоматически распространяется на ячейку B3.
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
