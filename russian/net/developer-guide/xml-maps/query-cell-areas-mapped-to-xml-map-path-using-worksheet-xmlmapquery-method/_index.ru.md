---
title: Запрос областей ячеек, привязанных к пути XML отображения, с использованием метода Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ru/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Возможные сценарии использования**

Вы можете запросить области ячеек, сопоставленных пути XML-карты, с помощью метода [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) из Aspose.Cells. Если путь существует, он вернет список областей ячеек, связанных с этим путем внутри XML-карты. Первый параметр метода [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) указывает путь элемента XML, а второй параметр указывает XML-карту, которую вы хотите запросить.

## **Запрос областей ячеек, привязанных к пути XML-отображения, с использованием метода Worksheet.XmlMapQuery**

На следующем скриншоте показано, что Microsoft Excel отображает XML-карту внутри [образца Excel-файла](55541790.xlsx), используемого в коде. Код дважды обращается к XML-карте и печатает список областей ячеек, возвращенных методом [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery), в консоль, как показано ниже.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Вывод в консоль**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **Получение пути XML из объекта списка/таблицы**

Данные XML могут быть импортированы в листы Excel. Иногда требуется получить XML-путь из ListObjects в листе Excel. Эта функция доступна в Excel при использовании выражения вроде Sheet1.ListObjects(1).XmlMap.DataBinding. Та же функция доступна в Aspose.Cells при вызове [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). Приведенный ниже пример демонстрирует эту функцию. Файл шаблона и другие исходные файлы можно загрузить по следующим ссылкам:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
