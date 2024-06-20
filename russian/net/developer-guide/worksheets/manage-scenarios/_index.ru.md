---
title: Создание, изменение или удаление сценариев из листов
linktitle: Управление сценариями
type: docs
weight: 190
url: /ru/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: В данной статье вы узнаете, как создавать, изменять или удалять сценарии из листов книги Excel программно с использованием библиотеки C# и .NET API.
keywords: создание сценария листа книги c#, удаление сценария листа книги Excel c#, изменение сценария листа книги c#
---

{{% alert color="primary" %}}

Иногда вам может понадобиться создавать, изменять или удалять сценарии в электронных таблицах. Сценарий - это именованная модель «что если?», которая включает в себя переменные ввода, связанные одной или несколькими формулами. Перед созданием сценария разработайте лист книги так, чтобы в нем была по крайней мере одна формула, зависимая от ячеек, в которые можно вводить различные значения. В следующем примере показано, как создавать и удалять сценарии из листа книги в книге с помощью API Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет некоторые полезные классы, например, классы [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) и [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell). Он также предоставляет свойство [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios). Приведенный ниже пример кода открывает файл Excel XLSX, содержащий несколько сценариев, удаляет существующий сценарий и добавляет новый сценарий на лист перед сохранением файла Excel. Пример использует очень простой файл шаблона, содержащий сценарий.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
