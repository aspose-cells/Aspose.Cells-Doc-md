---
title: Добавление пользовательских XML частей и выбор их по идентификатору
type: docs
weight: 70
url: /ru/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Возможные сценарии использования**

Пользовательские части XML - это XML-данные, которые хранятся в документах Microsoft Excel и используются приложениями, которые работают с ними. В настоящее время нет прямого способа добавить их с помощью пользовательского инструментария Microsoft Excel. Тем не менее, вы можете добавить их программно различными способами, например, используя VSTO, используя Aspose.Cells и т. д. Пожалуйста, используйте метод [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add), если вы хотите добавить пользовательскую часть XML с использованием API Aspose.Cells. Вы также можете установить ее идентификатор, используя свойство [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Аналогично, если вы хотите выбрать пользовательскую часть XML по идентификатору, вы можете использовать метод [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid).

## **Добавление пользовательских XML-частей и выбор их по идентификатору**

В следующем примере код сначала добавляет четыре пользовательские части XML, используя метод [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add). Затем он устанавливает их идентификаторы с использованием свойства [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Наконец, он находит или выбирает одну из добавленных пользовательских частей XML с использованием метода [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid). Пожалуйста, обратите также внимание на вывод консоли приведенного ниже кода для ссылки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
