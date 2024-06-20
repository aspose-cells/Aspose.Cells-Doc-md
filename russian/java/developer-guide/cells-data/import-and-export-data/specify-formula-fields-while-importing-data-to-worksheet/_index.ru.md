---
title: Указание формульных полей при импорте данных в рабочий лист
type: docs
weight: 220
url: /ru/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **Возможные сценарии использования**

Вы можете указать формульные поля при импорте данных в свой рабочий лист, используя метод [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas). Этот метод принимает логический массив, где значение **true** означает, что поле является формульным. Например, если третье поле является формульным, то третье значение в массиве будет **true**.

## **Указание формульных полей при импорте данных в рабочий лист**

Пожалуйста, ознакомьтесь с следующим образцом кода, который объясняет, как указать формульное поле при импорте данных в рабочий лист. Пожалуйста, ознакомьтесь с [выходным файлом Excel](61767850.xlsx), сгенерированным кодом, и скриншотом, показывающим воздействие кода на выходной файл Excel.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
