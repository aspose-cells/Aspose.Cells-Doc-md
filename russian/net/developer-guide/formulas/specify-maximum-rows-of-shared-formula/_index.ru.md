---
title: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/net/specify-maximum-rows-of-shared-formula/
---
## **Возможные сценарии использования**

Максимальное количество строк общей формулы по умолчанию — 64. Это может быть любое число, например 1000. Производительность общей формулы изменяется при изменении количества строк. Таким образом, Aspose.Cells обеспечивает[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)свойство, которое можно использовать для указания максимального количества строк общей формулы. Общая формула будет разделена на несколько общих формул, если общее количество строк общей формулы больше ее, как показано на следующем снимке экрана.

![дело:изображение_альтернативный_текст](specify-maximum-rows-of-shared-formula_1.png)

## **Укажите максимальное количество строк общей формулы**

Следующий пример кода объясняет использование[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) имущество. Он устанавливает максимальное количество строк общей формулы на 5 и добавляет общую формулу в ячейку D1 для 100 строк и сохраняет в[выходной файл Excel](61767856.xlsx). Если вы извлечете содержимое выходного файла Excel и проверите*лист1.xml*, вы увидите, что общая формула разбивается через каждые 5 строк, как показано на снимке экрана выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
