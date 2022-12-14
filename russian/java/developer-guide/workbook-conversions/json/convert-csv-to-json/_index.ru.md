---
title: Конвертировать CSV в JSON
type: docs
weight: 170
url: /ru/java/convert-csv-to-json/
---
## **Конвертировать CSV в JSON**

Aspose.Cells поддерживает преобразование CSV в JSON. Для этого API предоставляет[**Экспортранжетоджсоноптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)а также[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)классы.[**Экспортранжетоджсоноптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)class предоставляет параметры для экспорта диапазона в JSON.[**Экспортранжетоджсоноптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)класс имеет следующие свойства.

- [**Экспорткак строка**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)это экспортирует строковое значение ячеек в JSON.
- [**Хасхеадерров**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): указывает, содержит ли диапазон строку заголовка.
- [**Отступ**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): указывает отступ.

[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)class экспортирует JSON, используя параметры экспорта, установленные с помощью[**Экспортранжетоджсоноптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)учебный класс.

В следующем примере кода показано использование[**Экспортранжетоджсоноптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)а также[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)классы для загрузки[исходный CSV-файл](SampleCsv.csv)и печатает[JSON](SampleJson_out.csv) вывод в консоль.

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Консольный вывод**

[ { "id": 1, "language": "Java", "издание": "третье", "автор": "Герберт Шильдт", "улицаАдрес": 126, "город": "Сан-Джон", "штат": "CA", "почтовый индекс": 394221 }, { "id": 2, "язык": "C++", "издание": "второй", "автор": "EAAAA", "streetAddress": 126, "город": "Сан-Джон", "штат": "CA", "почтовый индекс": 394221 }, { "id": 3 , "язык": ".Net", "издание": "второй", "автор": "Е.Балагарусамы", "улицаАдрес": 126, "город": "Сан-Джон", " состояние": "CA", "почтовый индекс": 394221 } ]