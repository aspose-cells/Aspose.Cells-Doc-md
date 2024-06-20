---
title: Управление свойствами документа
type: docs
weight: 10
url: /ru/java/managing-document-properties/
---

## **Введение**

Microsoft Excel предоставляет возможность добавлять свойства к файлам электронных таблиц. Эти свойства документов предоставляют полезную информацию и делятся на 2 категории, как описано ниже.

- Системные (встроенные) свойства: Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (пользовательские) свойства: Пользовательские свойства, определенные конечным пользователем в виде пары имя-значение.

{{% alert color="primary" %}}

Самое важное, что нужно знать о встроенных и пользовательских свойствах, заключается в том, что встроенные свойства могут быть доступны и изменены, но не могут быть созданы или удалены, однако пользовательские свойства документа могут быть созданы и управляться.

{{% /alert %}}

## **Управление свойствами документа в Microsoft Excel**

Microsoft Excel позволяет управлять свойствами документа файлов Excel в режиме WYSIWYG. Пожалуйста, следуйте нижеуказанным шагам, чтобы открыть диалоговое окно **Свойства** в Excel 2016.

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

## **Работа с свойствами документа с помощью Aspose.Cells**

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells. Эта функция помогает разработчикам сохранять полезную информацию вместе с файлом, такую как время получения файла, обработки, отметки времени и т. д.

{{% alert color="primary" %}}

Aspose.Cells for Java напрямую записывает информацию о API и номере версии в выходные документы. Например, при преобразовании документа в PDF, Aspose.Cells for Java заполняет поле **Приложение** значением 'Aspose.Cells' и поле **PDF Producer** значением, например 'Aspose.Cells for Java v17.9'.

Обратите внимание, что нельзя указать Aspose.Cells for Java изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

### **Доступ к свойствам документа**

API Aspose.Cells поддерживает оба типа свойств документа, встроенные и настраиваемые. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Aspose.Cells представляет собой файл Excel, и, как файл Excel, класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) может содержать несколько рабочих листов, каждый из которых представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet), в то время как коллекция рабочих листов представлена классом [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection).

Используйте [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) для доступа к свойствам документа файла, описанным ниже.

- Чтобы получить доступ к встроенным свойствам документа, используйте [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- Чтобы получить доступ к пользовательским свойствам документа, используйте [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Оба [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) и [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) возвращают экземпляр [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). Эта коллекция содержит [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) объекты, каждый из которых представляет одно встроенное или пользовательское свойство документа.

Это зависит от требований приложения, как получить доступ к свойству, то есть, используя индекс или имя свойства из [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection), как показано в примере ниже.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

Класс [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) позволяет получить имя, значение и тип свойства документа:

- Чтобы получить имя свойства, используйте [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- Чтобы получить значение свойства, используйте [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) возвращает значение как объект.
- Чтобы получить тип свойства, используйте [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). Это возвращает одно из значений перечисления [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Добавление или удаление пользовательских свойств документа**

Как мы уже описывали ранее в начале этой темы, разработчики не могут добавлять или удалять встроенные свойства, потому что эти свойства определены системой, но возможно добавить или удалить пользовательские свойства, потому что они определены пользователем.

### **Добавление пользовательских свойств**

API Aspose.Cells предоставляют метод [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) для класса [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) с целью добавления пользовательских свойств в коллекцию. Метод [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде объекта [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Настройка пользовательского свойства «Ссылка на содержимое»**

Чтобы создать пользовательское свойство, связанное с содержимым заданного диапазона, вызовите метод [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String)) и передайте имя свойства и источник. Вы можете проверить, настроено ли свойство как связанное с содержимым, используя свойство [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent). Более того, также возможно получить исходный диапазон, используя свойство [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) класса [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty).

Мы используем простой шаблон файла Microsoft Excel в примере. Рабочая книга содержит определенный именованный диапазон с меткой '**MyRange**', который ссылается на значение ячейки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Удаление пользовательских свойств**

Чтобы удалить пользовательские свойства с помощью Aspose.Cells, вызовите метод [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) и передайте имя удаляемого свойства документа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
