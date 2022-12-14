---
title: Запрос Cell Области, сопоставленные с путем карты XML с использованием метода Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ru/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Возможные сценарии использования**

Вы можете запросить области ячеек, сопоставленные с путем карты XML, с помощью Aspose.Cells, используя[**Рабочий лист.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)метод. Если путь существует, он вернет список областей ячеек, связанных с этим путем, внутри карты XML. Первый параметр[**Рабочий лист.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)Метод указывает путь к элементу XML, а второй параметр указывает карту XML, которую вы хотите запросить.

## **Запрос Cell Области, сопоставленные с путем карты XML с использованием метода Worksheet.XmlMapQuery**

 На следующем снимке экрана показано, как Microsoft Excel отображает XML-карту внутри[образец файла Excel](55541790.xlsx) используется в коде. Код дважды запрашивает карту XML и печатает список областей ячеек, возвращенный[**Рабочий лист.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)на консоли, как показано ниже.

![дело:изображение_альтернативный_текст](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Консольный вывод**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Получить путь XML из объекта/таблицы списка**

XML-данные можно импортировать в рабочие листы. Иногда требуется путь XML из ListObjects рабочего листа. Эта функция доступна в Excel с помощью такого выражения, как Sheet1.ListObjects(1).XmlMap.DataBinding. Эта же функция доступна в Aspose.Cells по телефону[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). Следующий пример демонстрирует эту функцию. Файл шаблона и другие исходные файлы можно скачать по следующим ссылкам:

1. [XML-данные.xlsx](72417285.xlsx)
1. [Список стран.xml](72417287.xml)
1. [Список продуктов питания.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
