---
title: Конвертировать JSON в CSV
type: docs
weight: 160
url: /ru/java/convert-json-to-csv/
---

Aspose.Cells поддерживает преобразование как простого, так и вложенного JSON в CSV. Для этого API предоставляет классы [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) и [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) предоставляет параметры для макета JSON, такие как [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (игнорирует заголовок, если массив является свойством объекта) или [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (обрабатывает массив как таблицу). Класс [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) обрабатывает JSON, используя заданные параметры макета с помощью класса [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions).

В следующем образце кода демонстрируется использование классов [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) и [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) для загрузки [исходного JSON-файла](SampleJson.json) и генерации [файла CSV-вывода](SampleJson_out.csv).

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
