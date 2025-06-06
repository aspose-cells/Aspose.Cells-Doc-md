---
title: Использование маркеров изображений при группировке данных в умных маркерах
type: docs
weight: 630
url: /ru/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

В этой статье представлен пример, иллюстрирующий использование изображений-маркеров при группировке данных в умных маркерах.

{{% /alert %}} 
## **Использование маркеров изображений при группировке данных в умных маркерах**
В следующем образце кода создается книга и затем добавляются следующие умные маркерные теги в ячейки D2, E2 и F2 соответственно.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Затем он заполняет источник данных данными и вызывает метод [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) для обработки тегов умных маркеров. В коде используются изображения, например [moon.png](5472549.png) и [moon2.png](5472548.png), но вы можете использовать любое изображение. Следующий скриншот показывает результат этого примера кода. Как видите, данные в столбцах E и F сгруппированы с учетом данных в столбце D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
