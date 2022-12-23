---
title: Создавайте, манипулируйте или удаляйте сценарии из рабочих листов
linktitle: Управление сценариями
type: docs
weight: 120
url: /ru/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Иногда вам нужно создавать, изменять или удалять сценарии в электронных таблицах. Сценарий — это именованная модель «что, если», которая включает переменные входные ячейки, связанные между собой одной или несколькими формулами. Перед созданием сценария спроектируйте рабочий лист так, чтобы он содержал хотя бы одну формулу, зависящую от ячеек, в которые можно вставлять разные значения. В следующем примере показано, как создавать и удалять сценарии с рабочего листа с помощью API Aspose.Cells.

{{% /alert %}}

 Aspose.Cells предоставляет некоторые полезные классы, например[**СценарийКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Сценарий**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**СценарийInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) и[**СценарийInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . Он также обеспечивает[**Рабочий лист. Сценарии**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)имущество. Приведенный ниже пример кода открывает файл Excel XLSX (который содержит несколько сценариев) и удаляет существующий сценарий с рабочего листа. Он также добавляет новый сценарий перед сохранением файла Excel. Он использует очень простой файл шаблона, который содержит сценарий.

После выполнения кода существующий сценарий удаляется, а на рабочий лист добавляется новый сценарий.

**Выходной файл**

![дело:изображение_альтернативный_текст](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
