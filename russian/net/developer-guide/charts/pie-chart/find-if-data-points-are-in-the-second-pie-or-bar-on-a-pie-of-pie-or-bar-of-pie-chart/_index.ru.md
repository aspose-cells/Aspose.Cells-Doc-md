---
title: Определите, находятся ли данные во второй круговой или столбчатой диаграмме на круговой диаграмме с обрывным или столбчатой диаграмме
description: Узнайте, как использовать Aspose.Cells for .NET, чтобы найти, находятся ли точки данных во втором круге или столбе на диаграмме Круг на круге или Столбец на круге . Наш руководство покажет, как определить и получить доступ к вторичному кругу или столбу на составной диаграмме, что позволит вам эффективно анализировать и обрабатывать данные.
keywords: Aspose.Cells for .NET, Диаграмма Круг на круге , Диаграмма Столбец на круге , Вторичный круг, Вторичный столб, Анализ данных, Обработка данных.
type: docs
weight: 180
url: /ru/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Возможные сценарии использования**
Вы можете определить, находятся ли точки данных серии во втором круге на диаграмме 'Круг на круге' или в столбе диаграммы 'Столбец на круге' с помощью Aspose.Cells. Используйте свойство [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot), чтобы определить это.

Пожалуйста, загрузите [образец excel-файла](5115193.xlsx), используемый в следующем образце кода, и проверьте его вывод в консоль. Если вы откроете [образец excel-файла](5115193.xlsx), вы увидите, что все точки данных, которые меньше 10, находятся внутри столба 'Столбец на круге', как показано в выводе консоли.
## **Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме**
В следующем образце кода показано, как определить, находятся ли точки данных во втором сегменте или в столбце на диаграмме *Круговой из кругов* или *Столбчатая из кругов*.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Вывод в консоль**
Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным после выполнения вышеуказанного образца кода с [образцом excel-файла](5115193.xlsx). Если [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) равно **false**, то точка данных внутри круга, а если **true**, то точка данных внутри столба.



{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
