---
title: Скопируйте VBA Macro UserForm DesignerStorage из шаблона в целевую книгу
type: docs
weight: 60
url: /ru/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет копировать проект VBA из одного файла Excel в другой файл Excel. Проект VBA состоит из различных типов модулей, т. е. документов, процедурных, конструкторов и т. д. Все модули можно скопировать с помощью простого кода, но для модуля конструктора есть некоторые дополнительные данные, называемые хранилищем конструктора, к которым необходимо получить доступ или скопировать. Следующие два метода относятся к Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Скопируйте VBA Macro UserForm DesignerStorage из шаблона в целевую книгу**

См. следующий пример кода. Он копирует проект VBA из[шаблон файла Excel](50528367.xlsm)в пустую книгу и сохраняет ее как[выходной файл Excel](50528366.xlsm). Если вы откроете проект VBA внутри файла шаблона Excel, вы увидите форму пользователя, как показано ниже. Пользовательская форма состоит из Designer Storage, поэтому она будет скопирована с помощью[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) а также[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) методы.

![дело:изображение_альтернативный_текст](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

На следующем снимке экрана показан выходной файл Excel и его содержимое, скопированное из файла шаблона Excel. Когда вы нажимаете кнопку 1, она открывает форму пользователя VBA, которая сама имеет командную кнопку, которая показывает окно сообщения при нажатии.

![дело:изображение_альтернативный_текст](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
