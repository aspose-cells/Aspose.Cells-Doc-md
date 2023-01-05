---
title: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/java/specify-maximum-rows-of-shared-formula/
---
## **Возможные сценарии использования**

Максимальное количество строк общей формулы по умолчанию — 64. Это может быть любое число, например 1000. Производительность общей формулы изменяется при изменении количества строк. Таким образом, Aspose.Cells обеспечивает[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)свойство, которое можно использовать для указания максимального количества строк общей формулы. Общая формула будет разделена на несколько общих формул, если общее количество строк общей формулы больше ее, как показано на следующем снимке экрана.

![дело:изображение_альтернативный_текст](specify-maximum-rows-of-shared-formula_1.png)

## **Укажите максимальное количество строк общей формулы**

Следующий пример кода объясняет использование[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)имущество. Он устанавливает максимальное количество строк общей формулы на 5 и добавляет общую формулу в ячейку D1 для 100 строк и сохраняет в[выходной файл Excel](61767869.xlsx). Если вы извлечете содержимое выходного файла Excel и проверите*лист1.xml*, вы увидите, что общая формула разбивается через каждые 5 строк, как показано на снимке экрана выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
