---
title: Привязка ячеек к элементам XML отображения
type: docs
weight: 50
url: /ru/python-net/link-cells-to-xml-map-elements/
---

## **Возможные сценарии использования**

Вы можете связать ячейки с элементами XML-карты, используя Aspose.Cells для Python via .NET. Для этого используйте метод [**Cells.link_to_xml_map()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/link_to_xml_map).

## **Связать ячейки с элементами Xml-карты**

Следующий образец кода загружает [исходный Excel-файл](5115471.xlsx), который содержит XML-карту, затем связывает ячейки A1, B2, C3, D4, E5 и F6 с элементами XML-карты FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 и FIELD8 соответственно, а затем сохраняет книгу Excel в [выходной Excel-файл](5115467.xlsx).

Если вы откроете [выходной Excel-файл](5115467.xlsx) и нажмете кнопку Developer > Source, вы увидите, что ячейки связаны с элементами XML-карты, и они также будут выделены Microsoft Excel, как показано на этом изображении.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-LinkCellsToXmlMapElements.py" >}}

{{< app/cells/assistant language="python-net" >}}
