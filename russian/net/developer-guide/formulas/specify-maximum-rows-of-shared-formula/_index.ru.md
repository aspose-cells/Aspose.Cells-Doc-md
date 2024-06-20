---
title: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/net/specify-maximum-rows-of-shared-formula/
---

## **Возможные сценарии использования**

По умолчанию максимальное количество строк общей формулы составляет 64. Оно может быть любым числом, например, оно может составлять 1000. Производительность общей формулы меняется при разном количестве строк. Поэтому Aspose.Cells предоставляет свойство [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula), которое можно использовать для указания максимального количества строк общей формулы. Общая формула будет разбита на несколько общих формул, если общее количество строк общей формулы больше указанного значения, как показано на следующем скриншоте.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Укажите максимальное количество строк общей формулы**

В следующем образце кода объясняется использование свойства [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula). Оно устанавливает максимальное количество строк общей формулы равным 5 и добавляет общую формулу в ячейку D1 на 100 строк и сохраняется в [файле Excel вывода](61767856.xlsx). Если извлечь содержимое файла Excel вывода и проверить *sheet1.xml*, то можно увидеть, что общая формула разбивается после каждых 5 строк, как показано на приведенном выше скриншоте.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
