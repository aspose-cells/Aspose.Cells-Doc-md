---
title: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 500
url: /ru/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells можно использовать для добавления пользовательских свойств внутри объекта книги, которые видны внутри панели информации о документе. Вы можете открыть панель информации о документе в Microsoft Excel, используя команды меню Файл > Сведения > Свойства > Показать панель документа.

Пожалуйста, используйте метод [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) для добавления пользовательского свойства, которое будет видно в панели информации о документе.

{{% /alert %}}

## **Пример**

В следующем образце кода добавляются два пользовательских свойства. Первое свойство не имеет типа, а второе свойство имеет тип DateTime. Когда вы откроете созданный этим кодом файл Excel, вы увидите эти два свойства в области информации о документе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
