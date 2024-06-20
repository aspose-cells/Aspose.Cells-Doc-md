---
title: Изменение формы метки данных диаграммы для подгонки текста
type: docs
weight: 190
url: /ru/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

Приложение Excel предоставляет опцию **Изменить форму для подгонки размера** для меток данных диаграммы с целью увеличения размера формы, чтобы текст поместился внутри нее. Эту опцию можно получить в интерфейсе Excel, выбрав любую из меток данных на диаграмме. Щелкните правой кнопкой мыши и выберите меню **Формат меток данных**. Вкладка **Размер и свойства**, разверните **Выравнивание**, чтобы отобразить соответствующие свойства, включая опцию **Изменить форму для подгонки размера**.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Изменение формы метки данных диаграммы для подгонки текста**

Для имитации функции Excel по изменению форм меток данных для подгонки текста, API Aspose.Cells предоставляют свойство типа булево [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText). В следующем фрагменте кода показан простой сценарий использования свойства [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText).

Диаграмма выглядит следующим образом до выполнения кода.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

Диаграмма выглядит следующим образом после выполнения кода.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
