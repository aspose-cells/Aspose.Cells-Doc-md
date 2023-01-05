---
title: Найдите, находятся ли точки данных во втором круге или столбце круговой диаграммы или столбца круговой диаграммы
type: docs
weight: 180
url: /ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Возможные сценарии использования**
 Вы можете узнать, находятся ли точки данных ряда во втором круге на*пирог пирога* на графике или в баре*Бар пирога* график с использованием Aspose.Cells. Пожалуйста, используйте[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)свойство для его определения.

 Пожалуйста, загрузите[образец эксель файла](5115193.xlsx) используется в следующем примере кода и посмотрите его вывод на консоль. Если вы откроете[образец эксель файла](5115193.xlsx) , вы обнаружите, что все точки данных, которые меньше 10, находятся внутри полосы*Бар пирога*график, также показанный выводом консоли.
## **Найдите, находятся ли точки данных во втором круге или столбце круговой диаграммы или столбца круговой диаграммы**
 В следующем примере кода показано, как определить, находятся ли точки данных во второй круговой диаграмме или столбце на*пирог пирога* или же*Бар пирога*диаграмма.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Консольный вывод**
 См. следующий вывод консоли, сгенерированный после выполнения приведенного выше примера кода с[образец эксель файла](5115193.xlsx) . Если[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) является**ЛОЖЬ** , точка данных находится внутри круговой диаграммы или если она**истинный**, то точка данных находится внутри бара.



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
