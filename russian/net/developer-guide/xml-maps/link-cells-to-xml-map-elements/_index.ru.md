---
title: Привязка ячеек к элементам XML отображения
type: docs
weight: 50
url: /ru/net/link-cells-to-xml-map-elements/
---

## **Возможные сценарии использования**

Вы можете связать ваши ячейки с элементами XML-карты, используя Aspose.Cells. Пожалуйста, используйте метод [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/linktoxmlmap) для этой цели.

## **Связать ячейки с элементами Xml-карты**

Следующий образец кода загружает [исходный Excel-файл](5115471.xlsx), который содержит XML-карту, затем связывает ячейки A1, B2, C3, D4, E5 и F6 с элементами XML-карты FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 и FIELD8 соответственно, а затем сохраняет книгу Excel в [выходной Excel-файл](5115467.xlsx).

Если вы откроете [выходной Excel-файл](5115467.xlsx) и нажмете кнопку Developer > Source, вы увидите, что ячейки связаны с элементами XML-карты, и они также будут выделены Microsoft Excel, как показано на этом изображении.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LinkCellsToXmlMapElements-LinkCellsToXmlMapElements.cs" >}}
{{< app/cells/assistant language="csharp" >}}
