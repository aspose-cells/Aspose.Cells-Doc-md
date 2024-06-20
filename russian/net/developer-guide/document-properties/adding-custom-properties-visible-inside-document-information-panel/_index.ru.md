---
title: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 300
url: /ru/net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Добавление пользовательских свойств, видимых в панели информации о документе**

Aspose.Cells можно использовать для добавления пользовательских свойств внутри объекта книги, которые видны внутри панели информации о документе. Вы можете открыть панель информации о документе в Microsoft Excel, используя команды меню Файл > Сведения > Свойства > Показать панель документа.

Используйте метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) для добавления пользовательского свойства, которое будет видно в области информации о документе

В следующем образце кода добавляются два пользовательских свойства. Первое свойство не имеет типа, а второе свойство имеет тип DateTime. Когда вы откроете созданный этим кодом файл Excel, вы увидите эти два свойства в области информации о документе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddingCustomPropertiesVisible-1.cs" >}}

### **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
