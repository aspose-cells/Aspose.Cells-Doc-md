---
title: Добавление пользовательских XML частей и выбор их по идентификатору
type: docs
weight: 70
url: /ru/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Возможные сценарии использования**

Пользовательские XML-части — это XML-данные, хранящиеся внутри документов Microsoft Excel и используемые приложениями, с ними работающими. В настоящее время нет прямого способа их добавить через интерфейс Microsoft Excel. Однако их можно добавить программно разными способами, например, с помощью VSTO, Aspose.Cells и других. Используйте метод [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes), если хотите добавить пользовательскую XML-часть с помощью API Aspose.Cells для Python via .NET. Также можно установить его ID через свойство [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Если нужно выбрать пользовательскую XML-часть по ID, используйте метод [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str).

## **Добавление пользовательских XML-частей и выбор их по идентификатору**

В следующем примере код сначала добавляет четыре пользовательские части XML, используя метод [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes). Затем он устанавливает их идентификаторы с использованием свойства [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Наконец, он находит или выбирает одну из добавленных пользовательских частей XML с использованием метода [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str). Пожалуйста, обратите также внимание на вывод консоли приведенного ниже кода для ссылки.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

