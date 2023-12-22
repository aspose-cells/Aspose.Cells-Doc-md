---
title: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона
description: Узнайте, как изменить источник данных диаграммы на целевой лист при копировании строк или диапазона в Aspose.Cells for .NET. Наше руководство покажет вам, как обновить диапазон данных диаграммы и связать его с целевым листом, гарантируя, что скопированные строки или Диапазон точно отражен на графике.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Возможные сценарии использования**

Когда вы копируете строки или диапазон, содержащие диаграммы, на новый лист, источник данных диаграммы не меняется. Например, если источником данных диаграммы является =Sheet1!$A$1:$B$4, то после копирования строк или диапазона на новый лист источник данных останется прежним, т.е. =Sheet1!$A$1:$B$4. Это по-прежнему относится к старому листу, т.е. Листу1. То же самое происходит и в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый лист назначения, используйте[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)свойство и установите его в**истинный** во время звонка в[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)метод. Теперь, если вашим целевым листом является DestSheet, источник данных вашей диаграммы изменится с =Sheet1!$A$1:$B$4 на =DestSheet!$A$1:$B$4.

##  **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**

В следующем примере кода объясняется использование[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) свойство при копировании строк или диапазона, содержащего диаграммы, на новый лист. В коде используется[образец файла Excel](5113699.xlsx) и генерирует[выходной файл Excel](5113697.xlsx).

![задача: image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
