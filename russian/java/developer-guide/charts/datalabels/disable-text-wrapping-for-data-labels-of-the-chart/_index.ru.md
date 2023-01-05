---
title: Отключить перенос текста для меток данных диаграммы
type: docs
weight: 60
url: /ru/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 позволяет пользователям переносить или разворачивать текст внутри меток данных диаграммы. По умолчанию текст метки данных переносится.

{{% /alert %}}

Aspose.Cells обеспечивает[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) метод. Установлен в**Истинный** или же**ЛОЖЬ** чтобы включить или отключить перенос текста на метках данных соответственно.

 Аналогичным образом используйте[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)метод, чтобы узнать, упакована ли уже метка данных.

На этом снимке экрана показан пример файла Excel Microsoft, содержащего диаграмму, в которой заключен текст меток данных. Как видите, вы можете проверить или очистить**Обтекание текста по форме** в разделе ВЫРАВНИВАНИЕ панели «Формат меток данных» в Microsoft Excel 2013.

**Обтекание меток данных**

![дело:изображение_альтернативный_текст](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 В приведенном ниже примере кода загружается пример файла Excel Microsoft с использованием Aspose.Cells и отключается перенос текста метки данных с помощью[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)метод. Когда код выполняется, диаграмма выглядит так. Ранее обернутый текст теперь развернут.

**Отображение меток данных только в одной строке**

![дело:изображение_альтернативный_текст](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
