---
title: Добавление пользовательских свойств, видимых внутри панели информации документа, с помощью Golang через C++
linktitle: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 300
url: /ru/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Изучить, как добавлять пользовательские свойства, видимые в панели информации документа, с помощью Aspose.Cells и Golang через C++.
---

## **Добавление пользовательских свойств, видимых в панели информации о документе**

Aspose.Cells можно использовать для добавления пользовательских свойств внутри объекта книги, которые видны внутри панели информации о документе. Вы можете открыть панель информации о документе в Microsoft Excel, используя команды меню Файл > Сведения > Свойства > Показать панель документа.

Пожалуйста, используйте метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) для добавления пользовательского свойства, которое будет отображаться в Панели информации о документе.

Следующий пример кода добавляет два пользовательских свойства. Первое свойство без типа, а второе с типом DateTime. После открытия созданного этим кодом файла Excel вы увидите эти два свойства в Панели информации о документе.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
