---
title: Укажите максимальное количество строк общей формулы
type: docs
weight: 40
url: /ru/java/specify-maximum-rows-of-shared-formula/
---

## **Возможные сценарии использования**

По умолчанию максимальное количество строк общей формулы составляет 64. Оно может быть любым числом, например, 1000. Производительность общей формулы меняется в зависимости от количества строк. Поэтому Aspose.Cells предоставляет свойство  [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula), которое можно использовать для указания максимального количества строк общей формулы. Общая формула будет разделена на несколько общих формул, если общее количество строк общей формулы больше, чем показано на следующем снимке экрана.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Укажите максимальное количество строк общей формулы**

В следующем примере кода объясняется использование свойства [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula). Оно устанавливает максимальное количество строк общей формулы равным 5, добавляет общую формулу в ячейке D1 для 100 строк и сохраняет в файл Excel [output Excel file](61767869.xlsx). Если извлечете содержимое файла Excel и проверите *sheet1.xml*, вы увидите, что общая формула разделяется после каждых 5 строк, как показано на снимке экрана выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
