---
title: Управление свойствами документа
linktitle: Свойства документа
type: docs
weight: 80
url: /ru/net/managing-document-properties/
description: Управление свойствами документов файлов электронных таблиц.
---
## **Введение**

Microsoft Excel позволяет добавлять свойства в файлы электронных таблиц. Эти свойства документа предоставляют полезную информацию и разделены на 2 категории, как подробно описано ниже.

- Системные (встроенные) свойства. Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (настраиваемые) свойства: настраиваемые свойства, определенные конечным пользователем в виде пары "имя-значение".

{{% alert color="primary" %}}

Самое важное, что нужно знать о встроенных и настраиваемых свойствах, это то, что к встроенным свойствам можно получить доступ и изменить их, но нельзя создать или удалить. Однако можно создавать настраиваемые свойства и управлять ими.

{{% /alert %}}

## **Управление свойствами документа с помощью Microsoft Excel**

 Microsoft Excel позволяет управлять свойствами документов файлов Excel в режиме WYSIWYG. Пожалуйста, выполните следующие шаги, чтобы открыть**Характеристики** диалоговое окно в Excel 2016.

1.  От**Файл** меню, выберите**Информация**.

|**Выбор информационного меню**|
|:- |
|![дело:изображение_альтернативный_текст](managing-document-properties_1.png)|
1.  Нажмите на**Характеристики** заголовок и выберите «Дополнительные свойства».

|**Щелкнув Выбор дополнительных свойств**|
|:- |
|![дело:изображение_альтернативный_текст](managing-document-properties_2.png)|
1. Управление свойствами документа файла.

|**Диалог свойств**|
|:- |
|![дело:изображение_альтернативный_текст](managing-document-properties_3.png)|
В диалоговом окне «Свойства» есть различные вкладки, такие как «Общие», «Сводка», «Статистика», «Содержание» и «Пользовательские настройки». Каждая вкладка помогает настроить различные виды информации, связанной с файлом. Вкладка Custom используется для управления пользовательскими свойствами.

## **Работа со свойствами документа с помощью Aspose.Cells**

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells. Эта функция помогает разработчикам хранить полезную информацию вместе с файлом, например, когда файл был получен, обработан, с отметкой времени и т. д.

{{% alert color="primary" %}}

 Aspose.Cells for .NET непосредственно записывает информацию о API и номере версии в выходных документах. Например, при преобразовании документа в PDF Aspose.Cells for .NET заполняет**Заявление** поле со значением «Aspose.Cells» и**PDF-продюсер** поле со значением, например 'Aspose.Cells v17.9'.

Обратите внимание, что вы не можете поручить Aspose.Cells for .NET изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

### **Доступ к свойствам документа**

Aspose.Cells API поддерживают оба типа свойств документа, встроенные и настраиваемые. Aspose.Cells'[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс представляет файл Excel и, как и файл Excel,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс может содержать несколько рабочих листов, каждый из которых представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс, тогда как набор рабочих листов представлен[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)учебный класс.

 Использовать[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)для доступа к свойствам документа файла, как описано ниже.

-  Чтобы получить доступ к встроенным свойствам документа, используйте[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Чтобы получить доступ к пользовательским свойствам документа, используйте[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Оба[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) а также[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) вернуть экземпляр[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Эта коллекция содержит[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)объекты, каждый из которых представляет одно встроенное или пользовательское свойство документа.

 Это зависит от требований приложения, как получить доступ к свойству, то есть; используя индекс или имя свойства из[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)как показано в примере ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)class позволяет получить имя, значение и тип свойства документа:

-  Чтобы получить имя свойства, используйте[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Чтобы получить значение свойства, используйте[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)возвращает значение как объект.
-  Чтобы получить тип свойства, используйте[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Это возвращает один из[**Тип свойства**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) значения перечисления. После получения типа свойства используйте один из**DocumentProperty.ToXXX** методы для получения значения соответствующего типа вместо использования[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) .**DocumentProperty.ToXXX**методы описаны в таблице ниже.

{{% alert color="primary" %}}

[**ДокументСвойства**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)класс также предоставляет набор методов, которые возвращают значения других типов данных.

{{% /alert %}}

|**Имя члена**|**Описание**|**Метод ToXXX**|
|:- |:- |:- |
|логический|Тип данных свойства — логический.|ToBool|
|Свидание|Тип данных свойства — DateTime. Обратите внимание, что Microsoft Excel хранит только<br>часть даты, время не может быть сохранено в пользовательском свойстве этого типа|ToDateTime|
|Плавать|Тип данных свойства — Double|Удвоить|
|Число|Тип данных свойства — Int32.|ToInt|
|Нить|Тип данных свойства — String|Нанизывать|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Добавление или удаление пользовательских свойств документа**

Как мы описали ранее в начале этого раздела, разработчики не могут добавлять или удалять встроенные свойства, поскольку эти свойства определяются системой, но можно добавлять или удалять настраиваемые свойства, поскольку они определяются пользователем.

### **Добавление пользовательских свойств**

 Aspose.Cells API-интерфейсы раскрыли[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) метод для[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) класс для добавления настраиваемых свойств в коллекцию.[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) метод добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Настройка пользовательского свойства «Ссылка на контент»**

 Чтобы создать пользовательское свойство, связанное с содержимым заданного диапазона, вызовите метод[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) метод и передать имя свойства и источник. Вы можете проверить, настроено ли свойство как связанное с содержимым, используя[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) имущество. Кроме того, также возможно получить исходный диапазон с помощью[**Источник**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) собственность[**ДокументСвойства**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)учебный класс.

 В примере мы используем простой шаблон файла Excel Microsoft. Рабочая книга имеет определенный именованный диапазон, помеченный**Мой диапазон** который ссылается на значение ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Удаление пользовательских свойств**

 Чтобы удалить пользовательские свойства с помощью Aspose.Cells, вызовите[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)и передайте имя удаляемого свойства документа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Предварительные темы**
- [Добавление настраиваемых свойств, видимых на панели сведений о документе](/cells/ru/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа](/cells/ru/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Укажите версию документа файла Excel с помощью встроенных свойств документа](/cells/ru/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Укажите язык файла Excel с помощью встроенных свойств документа](/cells/ru/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
