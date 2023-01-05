---
title: Найдите, находятся ли точки данных во втором круге или столбце круговой диаграммы или столбца круговой диаграммы
type: docs
weight: 910
url: /ru/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Возможные сценарии использования**
 Вы можете узнать, находятся ли точки данных ряда во втором круге на*пирог пирога* на графике или в баре*Бар пирога* график с использованием Aspose.Cells. Пожалуйста, используйте[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)свойство для его определения.

 Пожалуйста, загрузите[образец эксель файла](5473373.xlsx) используется в следующем примере кода и посмотрите его вывод на консоль. Если вы откроете[образец эксель файла](5473373.xlsx), вы обнаружите, что все точки данных, которые меньше 10, находятся внутри полосы*Бар пирога*график, также показанный выводом консоли.
## **Найдите, находятся ли точки данных во втором круге или столбце круговой диаграммы или столбца круговой диаграммы**
 В следующем примере кода показано, как определить, находятся ли точки данных во второй круговой диаграмме или столбце на*пирог пирога* или же*Бар пирога*диаграмма.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Консольный вывод**
 См. следующий вывод консоли, сгенерированный после выполнения приведенного выше примера кода с[образец эксель файла](5473373.xlsx) . Если[IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) является**ЛОЖЬ** , точка данных находится внутри круговой диаграммы или если она**истинный**, то точка данных находится внутри бара.

{{< highlight "java" >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
