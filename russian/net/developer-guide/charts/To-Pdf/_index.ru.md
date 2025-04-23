---
title: Диаграмма в PDF 
description: Узнайте, как использовать Aspose.Cells for .NET для преобразования диаграммы в PDF документ. Наш руководство продемонстрирует, как экспортировать диаграмму из Microsoft Excel и сохранить ее в формате PDF для дальнейшего распространения и архивирования.
keywords: Aspose.Cells for .NET, Диаграмма в PDF, Microsoft Excel, Преобразование PDF, Экспорт, Распределение, Архивирование.
type: docs
weight: 47
url: /ru/net/chart-to-pdf/
---

## **Отображение диаграммы в формат PDF**

Для преобразования диаграммы в формат PDF API Aspose.Cells предоставляет метод [**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) с возможностью сохранения результирующего PDF по пути на диске или в потоке.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Создание PDF-файла диаграммы с выбранным размером страницы**
С помощью Aspose.Cells можно создать PDF с диаграммой с выбранным размером страницы и указать, как вы хотите выровнять диаграмму на странице: сверху, снизу, по центру, слева, справа и т. д. Кроме того, вывод диаграммы можно создать в потоке или на диске. Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, который загружает [образец файла Excel](64716906.xlsx), обращается к первой диаграмме в листе и затем преобразует ее в [выходной PDF](64716907.pdf) с выбранным размером страницы. На скриншоте показано, что размер страницы в выходном PDF составляет 7x7, как указано в коде, и диаграмма выровнена по центру как по горизонтали, так и по вертикали. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}

{{< app/cells/assistant language="csharp" >}}
