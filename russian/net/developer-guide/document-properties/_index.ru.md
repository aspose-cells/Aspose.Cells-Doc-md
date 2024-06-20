---
title: Управление свойствами документа
linktitle: Свойства документа
type: docs
weight: 80
url: /ru/net/managing-document-properties/
description: Узнайте, как управлять свойствами документа через API Aspose.Cells for NET.
keywords: Как управлять свойствами документа в C#, получение или установка свойств документа с использованием C#, добавление или удаление свойств документа через C#, вставка или удаление свойств документа с помощью C#, как получить доступ к свойствам документа, используя API Aspose.Cells for NET.
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

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells. Эта функция помогает разработчикам сохранять полезную информацию вместе с файлом, такую как время получения файла, обработки, отметки времени и т. д.

{{% alert color="primary" %}}

Aspose.Cells for .NET напрямую записывает информацию об API и номере версии в выходных документах. Например, при рендеринге документа в PDF Aspose.Cells for .NET заполняет поле **Application** значением 'Aspose.Cells' и поле **PDF Producer** значением, например 'Aspose.Cells v17.9'.

Обратите внимание, что вы не можете указать Aspose.Cells for .NET изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

### **Как получить доступ к свойствам документа**

API Aspose.Cells поддерживает оба типа свойств документа, встроенные и настраиваемые. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Aspose.Cells представляет собой файл Excel, и, как файл Excel, класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) может содержать несколько рабочих листов, каждый из которых представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet), в то время как коллекция рабочих листов представлена классом [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

Используйте [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) для доступа к свойствам документа файла, описанным ниже.

- Чтобы получить доступ к встроенным свойствам документа, используйте [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- Чтобы получить доступ к настраиваемым свойствам документа, используйте [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

И [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties), и [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) возвращают экземпляр [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Эта коллекция содержит [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) объектов, каждый из которых представляет одно встроенное или настраиваемое свойство документа.

Это зависит от требований приложения, как получить доступ к свойству, то есть, используя индекс или имя свойства из [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection), как показано в примере ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

Класс [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) позволяет получить имя, значение и тип свойства документа:

- Чтобы получить имя свойства, используйте [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- Чтобы получить значение свойства, используйте [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) возвращает значение как объект.
- Чтобы получить тип свойства, используйте [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). Это возвращает одно из значений перечисления [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype). После того как вы получите тип свойства, используйте один из методов **DocumentProperty.ToXXX** для получения значения соответствующего типа вместо использования [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). Методы **DocumentProperty.ToXXX** описаны в таблице ниже.

{{% alert color="primary" %}}

Класс [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) также предоставляет набор методов, возвращающих значения других типов данных.

{{% /alert %}}

|**Имя участника**|**Описание**|**Метод ToXXX**|
| :- | :- | :- |
|Boolean|Тип данных свойства - Логический|ToBool|
|Date|Тип данных свойства - Дата и время. Обратите внимание, что Microsoft Excel сохраняет только <br>часть даты, не сохраняется время в настраиваемом свойстве этого типа|ToDateTime|
|Float|Тип данных свойства - Число двойной точности|ToDouble|
|Number|Тип данных свойства - Int32|ToInt|
|String|Тип данных свойства - Строка|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Как добавить или удалить пользовательские свойства документа**

Как мы уже описывали ранее в начале этой темы, разработчики не могут добавлять или удалять встроенные свойства, потому что эти свойства определены системой, но возможно добавить или удалить пользовательские свойства, потому что они определены пользователем.

### **Как добавить пользовательские свойства**

API Aspose.Cells предоставил метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) для класса [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) чтобы добавить пользовательские свойства в коллекцию. Метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) добавляет свойство к файлу Excel и возвращает ссылку на новое свойство документа как объект [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Как настроить пользовательское свойство 'Ссылка на содержимое'**

Чтобы создать пользовательское свойство, связанное с содержимым заданного диапазона, вызовите метод [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) и передайте имя свойства и источник. Вы можете проверить, настроено ли свойство как связанное с содержимым, используя свойство [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent). Более того, также возможно получить исходный диапазон, используя свойство [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) класса [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty).

Мы используем простой шаблон файла Microsoft Excel в примере. Рабочая книга содержит определенный именованный диапазон с меткой '**MyRange**', который ссылается на значение ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Как удалить пользовательские свойства**

Чтобы удалить пользовательские свойства с помощью Aspose.Cells, вызовите метод [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) и передайте имя удаляемого свойства документа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Продвинутые темы**
- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа](/cells/ru/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Указание версии документа Excel с использованием встроенных свойств документа](/cells/ru/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Указание языка файла Excel с использованием встроенных свойств документа](/cells/ru/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
