---
title: Запрос областей ячеек, привязанных к пути XML отображения, с использованием метода Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ru/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Возможные сценарии использования**

Вы можете запросить области ячеек, отображаемые в пути XML-карты, с помощью Aspose.Cells для Python via .NET через метод [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query). Если путь существует, он вернёт список областей ячеек, связанных с этим путём внутри XML-карты. Первый параметр метода [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) задает путь к XML-элементу, а второй параметр — XML-карту, для которой хотите выполнить запрос.

## **Запрос областей ячеек, привязанных к пути XML-отображения, с использованием метода Worksheet.XmlMapQuery**

На следующем скриншоте показано, что Microsoft Excel отображает XML-карту внутри [образца Excel-файла](55541790.xlsx), используемого в коде. Код дважды обращается к XML-карте и печатает список областей ячеек, возвращенных методом [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query), в консоль, как показано ниже.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

Данные XML можно импортировать в листы. Иногда требуется указать путь XML из ListObjects листа. Эта функция доступна в Excel с помощью выражения вроде Sheet1.ListObjects(1).XmlMap.DataBinding. Такая же функция реализована в Aspose.Cells для Python via .NET вызовом метода [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url). Следующий пример демонстрирует эту функцию. Форматный файл и другие исходные файлы можно скачать по ссылкам:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

{{< app/cells/assistant language="python-net" >}}
