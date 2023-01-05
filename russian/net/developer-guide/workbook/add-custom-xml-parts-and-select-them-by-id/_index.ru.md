---
title: Добавьте пользовательские части XML и выберите их по идентификатору
type: docs
weight: 70
url: /ru/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Возможные сценарии использования**

Пользовательские части XML — это данные XML, которые хранятся в документах Excel Microsoft и используются приложениями, которые с ними работают. На данный момент нет прямого способа добавить их с помощью пользовательского интерфейса Excel Microsoft. Однако вы можете добавить их программно различными способами, например, с помощью VSTO, используя Aspose.Cells и т. д. Пожалуйста, используйте[**Книга.CustomXmlParts.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)метод, если вы хотите добавить пользовательскую часть XML, используя Aspose.Cells API. Вы также можете установить его идентификатор, используя[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)имущество. Точно так же, если вы хотите выбрать Custom XML Part by ID, вы можете использовать[**Книга.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)метод.

## **Добавьте пользовательские части XML и выберите их по идентификатору**

В следующем примере кода сначала добавляются четыре настраиваемые части XML с помощью[**Книга.CustomXmlParts.Добавить()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)метод. Затем он устанавливает их идентификаторы, используя[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) имущество. Наконец, он находит или выбирает одну из добавленных пользовательских XML-частей, используя[**Книга.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)метод. Также см. консольный вывод кода, приведенного ниже для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
