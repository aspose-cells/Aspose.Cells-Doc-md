---  
title: Изменить источник данных графика на целевой лист при копировании строк или диапазонов с помощью Golang через C++  
description: Узнайте, как изменить источник данных диаграммы на целевой лист при копировании строк или диапазона в Aspose.Cells for C++. Наш практи guide покажет, как обновлять диапазон данных диаграммы и связывать его с целевым листом, обеспечивая точное отображение скопированных строк или диапазона в диаграмме.  
keywords: Aspose.Cells for C++, построение диаграмм, источник данных, целевой лист, строки, диапазон, копирование, обновление, диапазон данных, связывание.  
type: docs  
weight: 440  
url: /ru/go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Возможные сценарии использования**

Когда вы копируете строки или диапазон с диаграммами в новый лист, источник данных диаграммы не меняется. Например, если источник данных диаграммы =Sheet1!$A$1:$B$4, то после копирования строк или диапазона на новый лист источник данных останется прежним, то есть =Sheet1!$A$1:$B$4. Он по-прежнему ссылается на старый лист, то есть Sheet1. Это также поведение в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый лист назначения, используйте свойство [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) и установите его в значение **true** при вызове метода [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Тогда, если ваш лист назначения — DestSheet, источник данных для вашей диаграммы изменится с =Sheet1!$A$1:$B$4 на =DestSheet!$A$1:$B$4.

## **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**

Следующий пример кода объясняет использование свойства [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) при копировании строк или диапазона с диаграммами на новый лист. Код использует [образец файла Excel](5113699.xlsx) и создает [выходной файл Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}
