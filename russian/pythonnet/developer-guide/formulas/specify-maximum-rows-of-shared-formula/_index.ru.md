---
title: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/python-net/specify-maximum-rows-of-shared-formula/
---

## **Возможные сценарии использования**

По умолчанию максимальное число строк для общей формулы — 64. Можно установить любое число, например, 1000. Производительность общей формулы меняется в зависимости от количества строк. Поэтому Aspose.Cells для Python via .NET предоставляет свойство [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula), позволяющее указать максимальное число строк для общей формулы. Если количество строк превышает это, формула будет разбита на несколько разделяемых формул, как показано на следующем скриншоте.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Укажите максимальное количество строк общей формулы**

В следующем образце кода объясняется использование свойства [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula). Оно устанавливает максимальное количество строк общей формулы равным 5 и добавляет общую формулу в ячейку D1 на 100 строк и сохраняется в [файле Excel вывода](61767856.xlsx). Если извлечь содержимое файла Excel вывода и проверить *sheet1.xml*, то можно увидеть, что общая формула разбивается после каждых 5 строк, как показано на приведенном выше скриншоте.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

{{< app/cells/assistant language="python-net" >}}
