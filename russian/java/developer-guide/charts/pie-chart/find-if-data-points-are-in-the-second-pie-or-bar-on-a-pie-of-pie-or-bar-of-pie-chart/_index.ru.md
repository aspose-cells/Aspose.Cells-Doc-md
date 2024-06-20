---
title: Определите, находятся ли данные во второй круговой или столбчатой диаграмме на круговой диаграмме с обрывным или столбчатой диаграмме
type: docs
weight: 910
url: /ru/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Возможные сценарии использования**
Вы можете определить, находятся ли точки данных серии во втором сегменте на диаграмме *Круговой из кругов* или в столбце на диаграмме *Столбчатая из кругов* с помощью Aspose.Cells. Пожалуйста, используйте свойство [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot), чтобы определить это.

Пожалуйста, скачайте [образец файл Excel](5473373.xlsx), используемый в следующем примере кода, и посмотрите его вывод в консоли. Если вы откроете [образец файл Excel](5473373.xlsx), вы увидите, что все точки данных, которые меньше 10, находятся внутри столбца на диаграмме *Столбчатая из кругов*, как показано также в выводе консоли.
## **Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме**
В следующем образце кода показано, как определить, находятся ли точки данных во втором сегменте или в столбце на диаграмме *Круговой из кругов* или *Столбчатая из кругов*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Вывод в консоль**
Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным после выполнения вышеуказанного образца кода с [образцом файла Excel](5473373.xlsx). Если [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) равно **false**,точка данных находится внутри круга, а если оно равно **true**, то точка данных находится внутри столбца.

{{< highlight java >}}

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
