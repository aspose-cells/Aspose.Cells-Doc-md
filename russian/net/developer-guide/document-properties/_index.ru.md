---
title: Управление свойствами документа
linktitle: Свойства документа
type: docs
weight: 80
url: /ru/net/managing-document-properties/
description: Узнайте, как управлять свойствами документа с помощью API Aspose.Cells для NET.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **Введение**

Microsoft Excel предоставляет возможность добавлять свойства в файлы электронных таблиц. Эти свойства документа предоставляют полезную информацию и разделены на две категории, как описано ниже.

- Системные (встроенные) свойства. Встроенные свойства содержат общую информацию о документе, например название документа, имя автора, статистику документа и т. д.
- Пользовательские (настраиваемые) свойства: пользовательские свойства, определенные конечным пользователем в форме пары имя-значение.

{{% alert color="primary" %}}

Самый важный момент, который нужно знать о встроенных и настраиваемых свойствах, заключается в том, что к встроенным свойствам можно получить доступ и изменить их, но нельзя создать или удалить. Однако можно создавать и управлять настраиваемыми свойствами.

{{% /alert %}}

##  **Как управлять свойствами документа с помощью Microsoft Excel**

 Microsoft Excel позволяет управлять свойствами файлов Excel в режиме WYSIWYG. Пожалуйста, следуйте инструкциям ниже, чтобы открыть**Характеристики** диалог в Excel 2016.

1.  Из**Файл** меню выберите *Информация**.

|**Выбор информационного меню**|
| :- |
|![задача: image_alt_text](managing-document-properties_1.png)|
1.  Нажмите на**Характеристики** заголовок и выберите «Дополнительные свойства».

|**Нажатие кнопки «Выбор дополнительных свойств»**|
| :- |
|![задача: image_alt_text](managing-document-properties_2.png)|
1. Управляйте свойствами документа файла.

|**Диалог свойств**|
| :- |
|![задача: image_alt_text](managing-document-properties_3.png)|
В диалоговом окне «Свойства» есть различные вкладки, такие как «Общие», «Сводка», «Статистика», «Содержимое» и «Пользовательские». Каждая вкладка помогает настроить различные виды информации, связанной с файлом. Вкладка «Пользовательские» используется для управления пользовательскими свойствами.

##  **Как работать со свойствами документа с помощью Aspose.Cells**

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells. Эта функция помогает разработчикам хранить полезную информацию вместе с файлом, например, когда файл был получен, обработан, с отметкой времени и т. д.

{{% alert color="primary" %}}

 Aspose.Cells for .NET напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF, Aspose.Cells for .NET заполняется**Приложение** поле со значением «Aspose.Cells» и**PDF Производитель** поле со значением, например, «Aspose.Cells v17.9».

Обратите внимание, что вы не можете дать указание Aspose.Cells for .NET изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

###  **Как получить доступ к свойствам документа**

 Aspose.Cells API поддерживают оба типа свойств документа: встроенные и настраиваемые. Aspose.Cells'[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс представляет файл Excel и, как и файл Excel,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс может содержать несколько листов, каждый из которых представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс, тогда как коллекция рабочих листов представлена классом[**Рабочий ЛистКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)сорт.

 Использовать[**Рабочий ЛистКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)для доступа к свойствам документа файла, как описано ниже.

- Чтобы получить доступ к встроенным свойствам документа, используйте[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Чтобы получить доступ к пользовательским свойствам документа, используйте[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Оба[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) и[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) вернуть экземпляр[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Эта коллекция содержит[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)объекты, каждый из которых представляет одно встроенное или настраиваемое свойство документа.

 То, как получить доступ к свойству, зависит от требований приложения; используя индекс или имя свойства из[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)как показано в примере ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Класс позволяет получить имя, значение и тип свойства документа:

-  Чтобы получить имя свойства, используйте[**ДокументСвойство.Имя**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Чтобы получить значение свойства, используйте[**ДокументСвойство.Значение**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**ДокументСвойство.Значение**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)возвращает значение как объект.
-  Чтобы получить тип свойства, используйте[**ДокументСвойство.Тип**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Это возвращает один из[**Тип собственности**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)значения перечисления. После получения типа свойства используйте один из**ДокументПроперти.ToXXX** методы для получения значения соответствующего типа вместо использования[**ДокументСвойство.Значение**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) .**ДокументПроперти.ToXXX**методы описаны в таблице ниже.

{{% alert color="primary" %}}

[**ДокументСвойство**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Класс также предоставляет набор методов, которые возвращают значения других типов данных.

{{% /alert %}}

|**Имя участника**|**Описание**|**Метод ToXXX**|
| :- | :- | :- |
|логическое значение|Тип данных свойства — логический.|ТоБул|
|Дата| Тип данных свойства — DateTime. Обратите внимание, что Microsoft Excel хранит только<br>часть даты, время не может быть сохранено в настраиваемом свойстве этого типа|Тодатевремя|
|Плавать|Тип данных свойства — Double.|Удвоить|
|Число|Тип данных свойства — Int32.|ТоИнт|
|String|Тип данных свойства — String.|Нанизывать|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **Как добавить или удалить пользовательские свойства документа**

Как мы описывали ранее в начале этой темы, разработчики не могут добавлять или удалять встроенные свойства, поскольку эти свойства определяются системой, но можно добавлять или удалять пользовательские свойства, поскольку они определяются пользователем.

###  **Как добавить пользовательские свойства**

 Aspose.Cells API раскрыли[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) метод для[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) class, чтобы добавить в коллекцию пользовательские свойства.[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) метод добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **Как настроить настраиваемое свойство «Ссылка на контент»**

 Чтобы создать настраиваемое свойство, связанное с содержимым заданного диапазона, вызовите метод[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) метод и передайте имя и источник свойства. Вы можете проверить, настроено ли свойство как связанное с контентом, используя[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) свойство. Более того, также возможно получить исходный диапазон, используя[**Источник**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) собственность[**ДокументСвойство**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)сорт.

В примере мы используем простой шаблон Microsoft файла Excel. В рабочей книге есть определенный именованный диапазон с меткой**Мойдиапазон** который относится к значению ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **Как удалить пользовательские свойства**

 Чтобы удалить пользовательские свойства по номеру Aspose.Cells, позвоните по телефону[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)и передайте имя свойства документа, которое нужно удалить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **Предварительные темы**
- [Добавление пользовательских свойств, видимых на панели информации о документе](/cells/ru/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа](/cells/ru/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Укажите версию документа файла Excel, используя встроенные свойства документа.](/cells/ru/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Укажите язык файла Excel с помощью встроенных свойств документа.](/cells/ru/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
