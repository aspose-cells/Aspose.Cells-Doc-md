---
title: Управление размером позиции и диаграммой дизайнера
description: Узнайте, как использовать Aspose.Cells for .NET для эффективного управления положением, размером и дизайнерской диаграммой в Microsoft Excel. Наше руководство покажет, как настроить эти свойства для улучшения макета и визуализации.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /ru/net/manipulate-position-size-and-designer-chart/
---
##  **Положение и размер диаграммы**
 Иногда вам нужно изменить положение или размер новой или существующей диаграммы на листе. Aspose.Cells обеспечивает[Диаграмма.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) собственность для достижения этой цели. Вы можете использовать его подсвойства, чтобы изменить размер диаграммы с помощью новых**высота** и**ширина** или перепозиционируйте его с новым**Х** и **Y** координаты.
###  **Управление положением и размером диаграммы**
Чтобы изменить положение диаграммы (координаты X, Y) или размер (высота, ширина), используйте эти свойства:

1. [Диаграмма.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Диаграмма.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

В следующем примере объясняется использование вышеуказанных API. Он загружает существующую книгу, содержащую диаграмму на первом листе. Затем он изменяет размер и положение диаграммы, используя Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **Манипулирование диаграммами конструктора**
Бывают случаи, когда вам необходимо манипулировать или изменять диаграммы в файлах шаблонов дизайнера. Aspose.Cells полностью поддерживает управление содержимым и элементами диаграмм дизайнера. Данные, содержимое диаграммы, фоновое изображение и форматирование могут быть точно сохранены.
###  **Управление диаграммами конструктора в файлах шаблонов**
Для управления диаграммами дизайнера в файлах шаблонов используйте связанную диаграмму API. Например, вы можете использовать свойство Worksheet.Charts, чтобы получить существующую коллекцию диаграмм в файле шаблона.
####  **Создание диаграммы**
В следующем примере показано, как создать пирамидальную диаграмму. Мы будем манипулировать этой диаграммой позже.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **Манипулирование диаграммой**
В следующем примере показано, как манипулировать существующей диаграммой. В этом примере мы модифицируем диаграмму, созданную выше. Обратите внимание, что в сгенерированных выходных данных метка даты для одной точки данных установлена на «Великобритания, 30 тыс.».



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **Управление линейным графиком в шаблоне дизайнера**
В этом примере мы будем манипулировать линейным графиком. Мы добавим несколько рядов данных в существующую диаграмму и изменим цвета их линий.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

