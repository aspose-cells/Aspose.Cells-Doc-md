---
title: Укажите поля формулы при импорте данных на лист
type: docs
weight: 220
url: /ru/java/specify-formula-fields-while-importing-data-to-worksheet/
---
## **Возможные сценарии использования**

 Вы можете указать поля формулы при импорте данных на лист с помощью[**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas) метод. Этот метод принимает логический массив, в котором значение**истинный**означает, что поле является полем формулы. Например, если третье поле является полем формулы, то третье значение в массиве будет**истинный**.

## **Укажите поля формулы при импорте данных на лист**

 См. следующий пример кода, который объясняет, как указать поле формулы при импорте данных на лист. Пожалуйста, смотрите[выходной файл Excel](61767850.xlsx) сгенерированный кодом, и снимок экрана, показывающий влияние кода на выходной файл Excel.

![дело:изображение_альтернативный_текст](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
