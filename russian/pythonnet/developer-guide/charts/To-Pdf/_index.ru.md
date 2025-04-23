---
title: Диаграмма в PDF 
description: Узнайте, как использовать Aspose.Cells для Python via .NET для преобразования диаграммы в PDF документ. Наше руководство покажет, как экспортировать диаграмму из Microsoft Excel и сохранить её в виде PDF для дальнейшего распространения и архивации.
keywords: Aspose.Cells для Python via .NET, диаграмма в PDF, Microsoft Excel, преобразование в PDF, экспорт, распространение, архивация.
type: docs
weight: 47
url: /ru/python-net/chart-to-pdf/
---

## **Отображение диаграммы в формат PDF**

Чтобы вывести диаграмму в формате PDF, API Aspose.Cells для Python via .NET предоставили метод [**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf) с возможностью сохранять полученный PDF на диск или в поток.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **Создание PDF-файла диаграммы с выбранным размером страницы**
Вы можете создавать PDF-файлы диаграмм с желаемым размером страницы, используя Aspose.Cells для Python via .NET, и указывать, как вы хотите выровнять диаграмму внутри страницы, например, по верхнему, нижнему, центральному, левому, правому краю и т. д. Кроме того, выводная диаграмма может быть создана либо в поток, либо на диск. Ниже приведён пример кода, загружающий [образец Excel-файла](64716906.xlsx), получающий первую диаграмму в листе и затем преобразующий её в [выводной PDF](64716907.pdf) с желаемым размером страницы. Следующий скриншот показывает, что размер страницы в выводном PDF – 7x7, как указано в коде, а диаграмма выровнена по центру как по горизонтали, так и по вертикали. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}

