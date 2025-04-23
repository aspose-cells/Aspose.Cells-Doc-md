---
title: Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу
type: docs
weight: 60
url: /ru/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет скопировать проект VBA из одного файла Excel в другой файл Excel. Проект VBA состоит из различных типов модулей, таких как Документ, Процедурный, Дизайнер и т.д. Все модули могут быть скопированы с помощью простого кода, но для модуля Дизайнера есть дополнительные данные, называемые Хранилищем дизайнера. Следующие два метода работают с Хранилищем дизайнера.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу**

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода. Он копирует проект VBA из [шаблонного файла Excel](50528367.xlsm) в пустую книгу и сохраняет его как [выходной файл Excel](50528366.xlsm). Если вы откроете проект VBA внутри шаблонного файла Excel, вы увидите пользовательскую форму, как показано ниже. Пользовательская форма состоит из дизайнерского хранилища, поэтому она будет скопирована с использованием методов [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) и [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-).

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

На следующем скриншоте показан файл Excel вывода и его содержимое, которое было скопировано из файла Excel-шаблона. При нажатии на Кнопку 1, открывается VBA User Form, который сам имеет кнопку команды, открывающую диалоговое окно при нажатии.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
