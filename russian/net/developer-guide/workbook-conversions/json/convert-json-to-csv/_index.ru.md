---
title: Преобразование JSON в CSV
type: docs
weight: 210
url: /ru/net/convert-json-to-csv/
---
## **Преобразование JSON в CSV**

Aspose.Cells поддерживает преобразование простых, а также вложенных JSON в CSV. Для этого API предоставляет**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** и**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** классы.**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**класс предоставляет параметры для макета JSON, например**[IgnoreArrayTitle] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(игнорирует заголовок, если массив является свойством объекта) или**[ArrayAsTable] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(обрабатывает массив как таблицу).**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**класс обрабатывает JSON, используя параметры макета, установленные с помощью**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**учебный класс.

В следующем примере кода показано использование**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**и**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** классы для загрузки[исходный файл JSON](104398869.json) и генерирует[выходной файл CSV](104398870.csv).

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
