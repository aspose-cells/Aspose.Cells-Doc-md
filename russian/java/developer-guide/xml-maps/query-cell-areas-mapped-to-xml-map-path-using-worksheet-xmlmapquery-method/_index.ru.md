---
title: Запрос областей ячеек, привязанных к пути XML отображения, с использованием метода Worksheet.XmlMapQuery
type: docs
weight: 60
url: /ru/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Возможные сценарии использования**

Вы можете запрашивать области ячеек, сопоставленные пути XML-карты, с помощью метода [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)). Если путь существует, он вернет список областей ячеек, связанных с этим путем внутри XML-карты. Первый параметр метода [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) указывает путь элемента XML и второй параметр указывает XML-карту, которую вы хотите запросить.

## **Запрос областей ячеек, привязанных к пути XML-отображения, с использованием метода Worksheet.XmlMapQuery**

На следующем снимке экрана показан Microsoft Excel, отображающий XML-карту внутри [образцового файла Excel](55541818.xlsx), использованного в коде. Код запрашивает XML-карту два раза и печатает список областей ячеек, возвращенных методом [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)), на консоль, как показано ниже.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Вывод в консоль**

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

XML-данные могут быть импортированы в листы. Иногда требуется путь XML из ListObjects листа. Эта функция доступна в Excel с помощью выражения вроде Sheet1.ListObjects(1).XmlMap.DataBinding. Та же функция доступна в Aspose.Cells при вызове [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). Следующий пример демонстрирует эту функцию. Файл шаблона и другие исходные файлы можно загрузить по следующим ссылкам:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
