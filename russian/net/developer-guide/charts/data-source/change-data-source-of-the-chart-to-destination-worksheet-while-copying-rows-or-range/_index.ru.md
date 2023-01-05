---
title: Измените источник данных диаграммы на рабочий лист назначения при копировании строк или диапазона
type: docs
weight: 440
url: /ru/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Возможные сценарии использования**

Когда вы копируете строки или диапазоны, содержащие диаграммы, на новый лист, источник данных диаграммы не изменяется. Например, если источником данных диаграммы является =Лист1!$А$1:$В$4, то после копирования строк или диапазона на новый лист источник данных останется прежним, т.е. =Лист1!$А$1:$В$4. Он по-прежнему относится к старому рабочему листу, т.е. Sheet1. Это также поведение в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый рабочий лист назначения, используйте[**Копипоптионс.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)свойство и установите его в**истинный** во время звонка[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)метод. Теперь, если целевым рабочим листом является DestSheet, источник данных вашей диаграммы изменится с =Sheet1!$A$1:$B$4 на =DestSheet!$A$1:$B$4.

## **Измените источник данных диаграммы на рабочий лист назначения при копировании строк или диапазона**

 В следующем примере кода объясняется использование[**Копипоптионс.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) при копировании строк или диапазонов, содержащих диаграммы, на новый лист. В коде используется[образец эксель файла](5113699.xlsx) и генерирует[выходной файл excel](5113697.xlsx).

![дело:изображение_альтернативный_текст](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
