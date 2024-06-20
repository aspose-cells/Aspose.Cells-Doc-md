---
title: Создание, изменение или удаление сценариев из листов
linktitle: Управление сценариями
type: docs
weight: 120
url: /ru/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

Иногда вам нужно создавать, изменять или удалять сценарии в электронных таблицах. Сценарий представляет собой именованную модель типа "что если", которая включает в себя переменные ввода, связанные между собой одним или несколькими формулами. Прежде чем создавать сценарий, разработайте лист так, чтобы он содержал как минимум одну формулу, зависящую от ячеек, в которые можно вводить различные значения. В следующем примере показано, как создавать и удалять сценарии на листе с использованием API Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет несколько полезных классов, например [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) и [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). Он также предоставляет свойство [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios). Приведенный ниже пример кода открывает файл Excel XLSX (содержащий некоторые сценарии) и удаляет существующий сценарий с листа. Перед сохранением Excel-файла также добавляется новый сценарий. В качестве простого шаблонного файла используется файл, содержащий сценарий.

После выполнения кода существующий сценарий удаляется, и новый сценарий добавляется на лист.

**Выходной файл**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
