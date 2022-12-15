---
title: Управление свойствами документа
type: docs
weight: 10
url: /ru/java/managing-document-properties/
---
## **Введение**

Microsoft Excel позволяет добавлять свойства в файлы электронных таблиц. Эти свойства документа предоставляют полезную информацию и разделены на 2 категории, как подробно описано ниже.

- Системные (встроенные) свойства. Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (настраиваемые) свойства: настраиваемые свойства, определенные конечным пользователем в виде пары "имя-значение".

{{% alert color="primary" %}}

Самый важный момент, который нужно знать о встроенных и настраиваемых свойствах, заключается в том, что к встроенным свойствам можно получить доступ и изменить их, но нельзя создать или удалить, однако можно создавать настраиваемые свойства документа и управлять ими.

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

 Aspose.Cells for Java непосредственно записывает информацию о API и номере версии в выходных документах. Например, при преобразовании документа в PDF Aspose.Cells for Java заполняет**Заявление** поле со значением «Aspose.Cells» и**PDF-продюсер** поле со значением, например 'Aspose.Cells for Java v17.9'.

Обратите внимание, что вы не можете поручить Aspose.Cells for Java изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

### **Доступ к свойствам документа**

 Aspose.Cells API поддерживают оба типа свойств документа, встроенные и настраиваемые. Aspose.Cells'[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс представляет файл Excel и, как и файл Excel,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)класс может содержать несколько рабочих листов, каждый из которых представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс, тогда как набор рабочих листов представлен[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)учебный класс.

 Использовать[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)для доступа к свойствам документа файла, как описано ниже.

-  Чтобы получить доступ к встроенным свойствам документа, используйте[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  Чтобы получить доступ к пользовательским свойствам документа, используйте[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 Оба[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) а также[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) вернуть экземпляр[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Эта коллекция содержит[**ДокументСвойства**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)объекты, каждый из которых представляет одно встроенное или пользовательское свойство документа.

 Это зависит от требований приложения, как получить доступ к свойству, то есть; используя индекс или имя свойства из[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)как показано в примере ниже.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

[**ДокументСвойства**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)class позволяет получить имя, значение и тип свойства документа:

-  Чтобы получить имя свойства, используйте[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  Чтобы получить значение свойства, используйте[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)возвращает значение как объект.
-  Чтобы получить тип свойства, используйте[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Это возвращает один из[**Тип свойства**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)значения перечисления.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Добавление или удаление пользовательских свойств документа**

Как мы описали ранее в начале этого раздела, разработчики не могут добавлять или удалять встроенные свойства, поскольку эти свойства определяются системой, но можно добавлять или удалять настраиваемые свойства, поскольку они определяются пользователем.

### **Добавление пользовательских свойств**

 Aspose.Cells API-интерфейсы раскрыли[**добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) метод для[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) класс для добавления настраиваемых свойств в коллекцию.[**добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде[**ДокументСвойства**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)объект.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Настройка пользовательского свойства «Ссылка на контент»**

 Чтобы создать пользовательское свойство, связанное с содержимым заданного диапазона, вызовите метод[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) и передать имя свойства и источник. Вы можете проверить, настроено ли свойство как связанное с содержимым, используя[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) имущество. Кроме того, также возможно получить исходный диапазон с помощью[**Источник**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) собственность[**ДокументСвойства**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)учебный класс.

 В примере мы используем простой шаблон файла Excel Microsoft. Рабочая книга имеет определенный именованный диапазон, помеченный**Мой диапазон** который ссылается на значение ячейки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Удаление пользовательских свойств**

 Чтобы удалить пользовательские свойства с помощью Aspose.Cells, вызовите[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) и передайте имя удаляемого свойства документа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
