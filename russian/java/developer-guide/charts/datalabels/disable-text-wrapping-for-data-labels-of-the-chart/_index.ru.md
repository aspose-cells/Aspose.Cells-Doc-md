---
title: Отключение переноса текста для меток данных диаграммы
type: docs
weight: 60
url: /ru/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 позволяет пользователям переносить или убирать перенос текста в метках данных диаграммы. По умолчанию текст метки данных переносится.

{{% /alert %}}

Aspose.Cells предоставляет метод [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Установите **True** или **False** для включения или отключения переноса текста в метках данных соответственно.

Точно так же используйте метод [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) чтобы узнать, перенесен ли уже текст метки данных.

Этот снимок экрана показывает образец файл Excel Microsoft, содержащий график, в котором текст меток данных перенесен. Как видите, вы можете проверить или очистить опцию **Переносить текст в форме** в разделе ВЫРАВНИВАНИЕ панели Формат меткам данных в Microsoft Excel 2013.

**Перенос меток данных**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

Приведенный ниже образец кода загружает образец файла Microsoft Excel с использованием Aspose.Cells и отключает перенос текста метки данных с помощью метода [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). При выполнении кода диаграмма выглядит следующим образом. Ранее перенесенный текст теперь не переносится.

**Показ только одной линии данных**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
