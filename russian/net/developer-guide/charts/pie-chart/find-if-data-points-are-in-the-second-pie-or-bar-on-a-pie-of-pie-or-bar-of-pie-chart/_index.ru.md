---
title: Определите, находятся ли точки данных во второй круговой диаграмме или полосе круговой диаграммы.
description: Узнайте, как использовать Aspose.Cells for .NET, чтобы определить, находятся ли точки данных во второй круговой диаграмме или столбце круговой диаграммы. Наше руководство покажет, как идентифицировать вторичную круговую диаграмму или столбец на составной диаграмме и получить к ней доступ, что позволит вам эффективно анализировать данные и манипулировать ими.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Возможные сценарии использования**
 Вы можете узнать, находятся ли точки данных ряда на втором круге на*Пирог из пирогов* графике или в баре*Бар пирога* диаграмму, используя Aspose.Cells. Пожалуйста, используйте[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)свойство, позволяющее это определить.

 Пожалуйста, загрузите[образец файла Excel](5115193.xlsx)используется в следующем примере кода и посмотрите его вывод на консоль. Если вы откроете[образец файла Excel](5115193.xlsx) , вы обнаружите, что все точки данных меньше 10 находятся внутри полосы*Бар пирога*диаграмма, как также показано на выводе консоли.
##  **Определите, находятся ли точки данных во второй круговой диаграмме или полосе круговой диаграммы.**
 В следующем примере кода показано, как определить, находятся ли точки данных во второй круговой диаграмме или столбце диаграммы.*Пирог из пирогов* или*Бар пирога*диаграмма.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Консольный вывод**
 См. следующий вывод консоли, сгенерированный после выполнения приведенного выше примера кода с помощью[образец файла Excel](5115193.xlsx) . Если[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)имеет значение *false**, точка данных находится внутри круговой диаграммы, а если значение *true**, то точка данных находится внутри панели.



{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
