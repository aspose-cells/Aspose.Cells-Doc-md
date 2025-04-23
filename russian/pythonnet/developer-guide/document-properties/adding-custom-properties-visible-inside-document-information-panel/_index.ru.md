---
title: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 300
url: /ru/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **Добавление пользовательских свойств, видимых в панели информации о документе**

Aspose.Cells для Python via .NET можно использовать для добавления пользовательских свойств внутри объекта рабочей книги, которые отображаются в панели информации о документе. Открыть панель информации о документе в Microsoft Excel можно через меню Файл > Информация > Свойства > Показать панель документа.

Используйте метод [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) для добавления пользовательского свойства, которое будет видно в области информации о документе

В следующем образце кода добавляются два пользовательских свойства. Первое свойство не имеет типа, а второе свойство имеет тип DateTime. Когда вы откроете созданный этим кодом файл Excel, вы увидите эти два свойства в области информации о документе.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
