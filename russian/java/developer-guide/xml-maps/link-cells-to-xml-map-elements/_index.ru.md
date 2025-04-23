---
title: Привязка ячеек к элементам XML отображения
type: docs
weight: 50
url: /ru/java/link-cells-to-xml-map-elements/
---

## **Возможные сценарии использования**

Вы можете связать ваши ячейки с элементами XML-карты с помощью Aspose.Cells. Пожалуйста, используйте метод [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap-java.lang.String-int-int-java.lang.String-) для этой цели.

## **Привязка ячеек к элементам XML-отображения**

В следующем образце кода загружается [исходный файл Excel](5472518.xlsx), который содержит XML-отображение, затем привязываются ячейки A1, B2, C3, D4, E5 и F6 к элементам XML-отображения FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 и FIELD8 соответственно, после чего рабочая книга сохраняется в [файле Excel для вывода](5472517.xlsx).

Если вы откроете [файл Excel для вывода](5472517.xlsx) и нажмете кнопку *Разработчик > Источник*, вы увидите, что ячейки связаны с элементами XML-отображения, и они также будут выделены в Microsoft Excel, как показано на этом изображении.

![todo:image_alt_text](link-cells-to-xml-map-elements_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
{{< app/cells/assistant language="java" >}}
