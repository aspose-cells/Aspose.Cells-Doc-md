---
title: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона
description: Узнайте, как изменить источник данных диаграммы на целевой лист при копировании строк или диапазона в Aspose.Cells for .NET. Наш руководство покажет вам, как обновить диапазон данных диаграммы и связать его с целевым листом, обеспечивая точное отображение скопированных строк или диапазона в диаграмме.
keywords: Aspose.Cells for .NET, построение диаграмм, источник данных, целевой лист, строки, диапазон, копирование, обновление, диапазон данных, связь.
type: docs
weight: 440
url: /ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Возможные сценарии использования**

Когда вы копируете строки или диапазон, содержащий диаграммы, на новый лист, источник данных диаграммы не меняется. Например, если источником данных диаграммы является =Лист1!$A$1:$B$4, то после копирования строк или диапазона на новый лист, источник данных останется тем же, т.е. =Лист1!$A$1:$B$4. Это по-прежнему ссылается на старый лист, т.е. Лист1. Это также поведение в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый целевой лист, то, пожалуйста, используйте свойство [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) и установите его в **true** при вызове метода [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index). Теперь, если ваш целевой лист называется ЦелевойЛист, то источник данных вашей диаграммы изменится с =Лист1!$A$1:$B$4 на =ЦелевойЛист!$A$1:$B$4.

## **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**

В следующем образце кода поясняется использование свойства [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) при копировании строк или диапазона, содержащего диаграммы, на новый лист. Код использует [образец файла Excel](5113699.xlsx) и генерирует [файл Excel на выходе](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
