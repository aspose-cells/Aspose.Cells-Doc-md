---
title: Преобразование JSON в CSV
type: docs
weight: 160
url: /ru/java/convert-json-to-csv/
---
Aspose.Cells поддерживает преобразование простых, а также вложенных JSON в CSV. Для этого API предоставляет[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)и[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)классы.[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)класс предоставляет параметры для макета JSON, например[**Игнораррайтитле**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(игнорирует заголовок, если массив является свойством объекта) или[**Массив как таблица**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(обрабатывает массив как таблицу).[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)класс обрабатывает JSON, используя параметры макета, установленные с помощью[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)учебный класс.

В следующем примере кода показано использование[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)и[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)классы для загрузки[исходный файл JSON](SampleJson.json)и генерирует[выходной файл CSV](SampleJson_out.csv).

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
