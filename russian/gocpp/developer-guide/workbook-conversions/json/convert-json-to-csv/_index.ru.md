---
title: Конвертировать JSON в CSV с помощью Golang через C++
linktitle: Конвертировать JSON в CSV
type: docs
weight: 210
url: /ru/go-cpp/convert-json-to-csv/
description: Узнайте, как преобразовать JSON в CSV с помощью Aspose.Cells for C++, используя простые и вложенные примеры JSON.
---

## **Преобразовать JSON в CSV**

Поддержка Aspose.Cells для преобразования простого и вложенного JSON в CSV. Для этого API предоставляет классы [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). Класс [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) задаёт параметры для форматирования JSON, такие как [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (игнорирует заголовок, если массив является свойством объекта) или [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (обрабатывает массив как таблицу). Класс [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) обрабатывает JSON, используя установленные параметры разметки с помощью класса [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/).

Следующий пример демонстрирует использование классов [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) для загрузки [исходного JSON файла](104398869.json) и генерации [выходного CSV файла](104398870.csv).

### **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
