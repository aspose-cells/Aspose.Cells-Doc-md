---
title: Импорт XML в книгу Excel 
linktitle: Сопоставления XML
type: docs
weight: 210
url: /ru/python-net/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Импорт данных из файлов XML в Microsoft Excel.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET позволяет импортировать карту XML внутри рабочей книги, используя метод [**Workbook.import_xml()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/import_xml/#str-str-int-int). Вы можете импортировать XML карту с помощью Microsoft Excel с следующими шагами

- Выберите вкладку **Разработчик**
- Нажмите **Импорт** в разделе XML и следуйте необходимым шагам.

Для завершения импорта вам потребуется предоставить свои XML-данные. Вот [пример XML-данных](5115037.txt), который вы можете использовать для тестирования.

{{% /alert %}}

## **Импорт XML-схемы с использованием Microsoft Excel**

На следующем скриншоте показано, как импортировать XML-схему с использованием Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Импорт XML карты с помощью Aspose.Cells для Python via .NET**

В следующем примере кода показано, как использовать [**Workbook.import_xml()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/import_xml/#str-str-int-int). Это генерирует [выходной файл Excel](5115036.xlsx), как показано на этом снимке экрана.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-ImportXmlDataIntoWorkbook.py" >}}

## **Продвинутые темы**
- [Добавить XML-отображение внутри книги с использованием метода XmlMapCollection.Add](/cells/ru/python-net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Экспорт XML-данных, связанных с XML-схемой, внутри книги](/cells/ru/python-net/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Найдите имя корневого элемента XML-карты.](/cells/ru/python-net/find-the-root-element-name-of-xml-map/)
- [Привязка ячеек к элементам XML-отображения](/cells/ru/python-net/link-cells-to-xml-map-elements/)
- [Запрос областей ячеек, привязанных к пути XML-отображения, с использованием метода Worksheet.XmlMapQuery](/cells/ru/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)


{{< app/cells/assistant language="python-net" >}}
