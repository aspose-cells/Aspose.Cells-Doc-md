---
title: Добавьте пользовательские части XML и выберите их по идентификатору
type: docs
weight: 10
url: /ru/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Возможные сценарии использования**

Пользовательские части XML — это данные XML, которые хранятся в документах Excel Microsoft и используются приложениями, которые с ними работают. На данный момент нет прямого способа добавить их с помощью пользовательского интерфейса Excel Microsoft. Однако вы можете добавить их программно различными способами, например, используя*ВСТО*, с использованием*Aspose.Cells*и т.д. Пожалуйста, используйте[**Книга.getCustomXmlParts().Добавить()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)), если вы хотите добавить пользовательскую часть XML, используя Aspose.Cells API. Вы также можете установить его идентификатор, используя[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)имущество. Точно так же, если вы хотите выбрать Custom XML Part by ID, вы можете использовать[**Рабочая книга.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) метод.

## **Добавьте пользовательские части XML и выберите их по идентификатору**

В следующем примере кода сначала добавляются четыре настраиваемые части XML с помощью[**Книга.getCustomXmlParts().Добавить()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) метод. Затем он устанавливает их идентификаторы, используя[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)имущество. Наконец, он находит или выбирает одну из добавленных пользовательских XML-частей, используя[**Рабочая книга.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) метод. Также см. консольный вывод кода, приведенного ниже, для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
