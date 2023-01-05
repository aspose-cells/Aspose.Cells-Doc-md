---
title: Использование маркеров изображений при группировке данных в смарт-маркерах
type: docs
weight: 630
url: /ru/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

В этой статье представлен пример, иллюстрирующий использование маркеров изображения при группировке данных в интеллектуальных маркерах.

{{% /alert %}} 
## **Использование маркеров изображений при группировке данных в смарт-маркерах**
Следующий пример кода создает книгу, а затем добавляет следующие теги смарт-маркеров в ячейки D2, E2 и F2 соответственно.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Затем он заполняет источник данных данными и вызывает[WorkbookDesigner.Процесс()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) для обработки тегов смарт-маркеров. Код использует эти изображения, т.е.[луна.png](5472549.png) и[луна2.png](5472548.png) но вы можете использовать любое изображение. На следующем снимке экрана показан вывод этого примера кода. Как видите, данные в столбцах E и F сгруппированы по отношению к данным в столбце D.

![дело:изображение_альтернативный_текст](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
