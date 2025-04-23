---
title: Добавление пользовательских меток к данным точек в серии диаграммы
type: docs
weight: 380
url: /ru/java/adding-custom-labels-to-data-points-in-the-series-of-the-chart/
---

{{% alert color="primary" %}} 

Вы можете добавлять пользовательские метки к данным точек в серии диаграммы. Aspose.Cells предоставляет свойство [ChartPoint.getDataLabels().setText()](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) для добавления этих пользовательских меток. В этой статье будет объяснено, как использовать это свойство для добавления пользовательских меток к данным точек в серии диаграммы.

{{% /alert %}} 
## **Добавление пользовательских меток к данным точек в серии диаграммы**
Приведенный ниже код создает линейно-связанную диаграмму рассеяния с маркерами данных, а затем добавляет пользовательские метки к данным точек в серии диаграммы. Каждая пользовательская метка показывает имя серии и имя точки. Вы можете использовать любой другой текст вместо него. После выполнения кода создается следующий файл Excel. Как вы можете видеть внутри диаграммы, каждая точка данных имеет установленную пользовательскую метку.

![todo:image_alt_text](adding-custom-labels-to-data-points-in-the-series-of-the-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddCustomLabelsToDataPoints-AddCustomLabelsToDataPoints.java" >}}
{{< app/cells/assistant language="java" >}}
