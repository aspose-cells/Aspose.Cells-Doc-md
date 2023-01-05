---
title: Добавление настраиваемых свойств, видимых на панели сведений о документе
type: docs
weight: 500
url: /ru/java/adding-custom-properties-visible-inside-document-information-panel/
---
{{% alert color="primary" %}}

Aspose.Cells можно использовать для добавления настраиваемых свойств внутри объекта книги, которые видны на панели сведений о документе. Вы можете открыть панель информации о документе в Microsoft Excel, используя команды меню «Файл» > «Информация» > «Свойства» > «Показать панель документа».

 Пожалуйста, используйте[**Рабочая книга.getContentTypeProperties().добавить()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) метод добавления настраиваемого свойства, которое будет отображаться на панели сведений о документе.

{{% /alert %}}

## **Пример**

Следующий пример кода добавляет два настраиваемых свойства. Первое свойство не имеет никакого типа, а второе свойство имеет тип DateTime. После того, как вы откроете выходной файл Excel, сгенерированный этим кодом, вы увидите эти два свойства внутри панели информации о документе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских частей XML в Aspose.Cells](/cells/ru/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
