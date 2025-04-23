---
title: Управление свойствами документа
linktitle: Свойства документа
type: docs
weight: 80
url: /ru/python-net/managing-document-properties/
description: Изучите, как управлять свойствами документа через API Aspose.Cells для Python via .NET.
keywords: Как управлять свойствами документа в C#, получать или устанавливать свойства документа, добавлять или удалять свойства документа через C#, вставлять или удалять свойства документа через C#, как получить доступ к свойствам документа с помощью Aspose.Cells для Python via .NET.
---


## **Введение**

Microsoft Excel предоставляет возможность добавлять свойства к файлам электронных таблиц. Эти свойства документов предоставляют полезную информацию и делятся на 2 категории, как описано ниже.

- Системные (встроенные) свойства: Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (пользовательские) свойства: Пользовательские свойства, определенные конечным пользователем в виде пары имя-значение.

{{% alert color="primary" %}}

Самый важный момент, который нужно знать о встроенных и пользовательских свойствах, заключается в том, что встроенные свойства можно получить доступ, изменить, но не создать или удалить. Однако пользовательские свойства можно создавать и управлять ими.

{{% /alert %}}

## **Как управлять свойствами документа с помощью Microsoft Excel**

Microsoft Excel позволяет управлять свойствами документов файлов Excel в режиме WYSIWYG. Пожалуйста, следуйте нижеуказанным шагам, чтобы открыть диалоговое окно **Свойства** в Excel 2016.

1. В меню **Файл** выберите **Сведения**.

|**Выбор меню Сведения**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Нажмите на заголовок **Свойства** и выберите "Расширенные свойства".

|**Нажмите на выбор расширенных свойств**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Управляйте свойствами документа файла.

|**Диалоговое окно свойств**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
В диалоговом окне свойств есть различные вкладки, такие как Общее, Резюме, Статистика, Содержание и Пользовательские. Каждая вкладка помогает настраивать различные виды информации, связанные с файлом. Вкладка Пользовательские используется для управления пользовательскими свойствами.

## **Как работать со свойствами документа с помощью Aspose.Cells**

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells для Python via .NET. Эта функция помогает разработчикам сохранять полезную информацию вместе с файлом, например, дату получения, обработки, временные метки и т. д.

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET напрямую записывает информацию о версии API и номере версии в выводимые документы. Например, при преобразовании документа в PDF Aspose.Cells для Python via .NET заполняет поле **Application** значением 'Aspose.Cells' и поле **PDF Producer** значением, например 'Aspose.Cells for Python via .NET v17.9'.

Обратите внимание, что вы не можете указать Aspose.Cells для Python via .NET изменять или удалять эту информацию из выходных документов.

{{% /alert %}}


### **Как добавить или удалить пользовательские свойства документа**

Как мы уже описывали ранее в начале этой темы, разработчики не могут добавлять или удалять встроенные свойства, потому что эти свойства определены системой, но возможно добавить или удалить пользовательские свойства, потому что они определены пользователем.

### **Как добавить пользовательские свойства**

API Aspose.Cells для Python via .NET предоставил метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) для класса [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) для добавления пользовательских свойств в коллекцию. Метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде объекта [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Продвинутые темы**
- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа](/cells/ru/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Указание версии документа Excel с использованием встроенных свойств документа](/cells/ru/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Указание языка файла Excel с использованием встроенных свойств документа](/cells/ru/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

