---
title: Конвертировать JSON в CSV
type: docs
weight: 210
url: /ru/net/convert-json-to-csv/
---

## **Преобразовать JSON в CSV**

Aspose.Cells поддерживает преобразование простого и вложенного JSON в CSV. Для этого API предоставляет классы [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) и [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) предоставляет параметры макета JSON, такие как [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)(игнорирует заголовок, если массив является свойством объекта) или [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)(обрабатывает массив как таблицу). Класс [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) обрабатывает JSON с установленными параметрами макета с помощью класса  [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions).

Приведенный ниже образец кода демонстрирует использование классов [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) и [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) для загрузки [исходного файла JSON](104398869.json) и генерации [выходного файла CSV](104398870.csv).

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
