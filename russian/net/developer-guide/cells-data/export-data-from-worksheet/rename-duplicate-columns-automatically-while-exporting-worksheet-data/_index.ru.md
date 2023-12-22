---
title: Автоматическое переименование повторяющихся столбцов при экспорте данных листа
type: docs
weight: 250
url: /ru/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Узнайте, как автоматически переименовывать повторяющиеся столбцы при экспорте данных листа через код Aspose.Cells for .NET API.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Возможные сценарии использования**

 Иногда пользователь сталкивается с проблемой дублирования столбцов при экспорте данных из листа в таблицу данных. DataTable не может иметь повторяющиеся столбцы, поэтому повторяющиеся столбцы необходимо переименовать, прежде чем вы сможете экспортировать данные листа в таблицу данных. Aspose.Cells может автоматически переименовывать повторяющиеся столбцы в соответствии со стратегией, указанной вами с помощью[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) свойство. Если вы укажете[**Переименовать стратегию**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, столбцы будут переименованы как столбец1, столбец2, столбец3 и т. д., и если вы укажете[**Переименовать стратегию**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, тогда столбцы будут переименованы, например, столбец A, столбец B, столбец C и т. д.

##  **Автоматическое переименование повторяющихся столбцов при экспорте данных листа**

Следующий пример кода добавляет некоторые данные в первые три столбца листа, но все столбцы имеют одно и то же имя, т. е. *Люди*. Затем он экспортирует данные из листа в таблицу данных, указав[**Переименовать стратегию**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Письменная стратегия. Затем он печатает имена столбцов таблицы данных, созданной с помощью Aspose.Cells. На следующем снимке экрана показана таблица данных с экспортированными данными в визуализаторе. Как видите, повторяющиеся столбцы были переименованы в PeopleA, PeopleB и т. д.

![задача: image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Консольный вывод**

Вот консольный вывод приведенного выше примера кода для справки.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
