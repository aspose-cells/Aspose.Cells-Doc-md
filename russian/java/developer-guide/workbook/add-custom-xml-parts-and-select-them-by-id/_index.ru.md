---
title: Добавление пользовательских XML частей и выбор их по идентификатору
type: docs
weight: 10
url: /ru/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Возможные сценарии использования**

Пользовательские XML-части - это XML-данные, которые хранятся в документах Microsoft Excel и используются приложениями, которые работают с ними. На данный момент нет прямого способа добавления их с помощью пользовательского интерфейса Microsoft Excel. Однако вы можете добавить их программным способом различными способами, например, с помощью *VSTO*, с использованием *Aspose.Cells* и т. д. Если вы хотите добавить пользовательскую XML-часть с использованием API Aspose.Cells, используйте метод [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)). Вы также можете установить его ID с помощью свойства [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Аналогично, если вы хотите выбрать пользовательскую XML-часть по ID, вы можете использовать метод [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)).

## **Добавление пользовательских XML-частей и выбор их по идентификатору**

Нижеприведенный образец кода сначала добавляет четыре пользоватские XML-части с использованием метода [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)). Затем устанавливает их ID с использованием свойства [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Наконец, он находит или выбирает одну из добавленных пользоватских XML-частей с использованием метода [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)). Пожалуйста, также посмотрите консольный вывод ниже приведенного кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
