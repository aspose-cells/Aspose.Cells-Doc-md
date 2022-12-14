---
title: Создавайте, манипулируйте или удаляйте сценарии из рабочих листов
linktitle: Управление сценариями
type: docs
weight: 190
url: /ru/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Иногда вам нужно создавать, изменять или удалять сценарии в электронных таблицах. Сценарий называется «что, если?» модель, которая включает переменные входные ячейки, связанные одной или несколькими формулами. Перед созданием сценария спроектируйте лист так, чтобы он содержал хотя бы одну формулу, зависящую от ячеек, в которые можно вставлять разные значения. В следующем примере показано, как создавать и удалять сценарии из рабочего листа в рабочей книге с помощью API-интерфейсов Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет несколько полезных классов, например,[**СценарийКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Сценарий**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**СценарийInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , а также[**СценарийInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) классы. Он также обеспечивает[**Рабочий лист. Сценарии**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)имущество. Приведенный ниже пример кода открывает файл XLSX Excel, содержащий несколько сценариев, и удаляет существующий сценарий. Он также добавляет новый сценарий на лист перед сохранением файла Excel. В примере используется очень простой файл шаблона, содержащий сценарий.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
