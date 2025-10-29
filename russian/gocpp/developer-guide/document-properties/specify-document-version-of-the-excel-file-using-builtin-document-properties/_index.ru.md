---
title: Задание версии документа Excel с помощью встроенных свойств документа с помощью Golang через C++
linktitle: Определение версии документа
type: docs
weight: 20
url: /ru/go-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Узнайте, как задать версию документа файла Excel с помощью встроенных свойств документа с Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете изменить **номер версии** файла Excel, щелкнув правой кнопкой мыши по файлу и выбрав Свойства > Детали, а затем отредактировав поле **номер версии**. Для этого используйте свойство [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/) и API Aspose.Cells для программного изменения.

## **Указание версии документа Excel с использованием встроенных свойств документа**

Следующий пример кода создает рабочую книгу и изменяет ее встроенные свойства документа, включающие Заголовок, Авторов и номер версии. Пожалуйста, ознакомьтесь с [выходным файлом Excel](64716811.xlsx), созданным этим кодом, и скриншотом, показывающим измененную версию с помощью свойства [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyDocumentVersionOfTheExcelFileUsingBuiltinDocumentProperties.go" >}}
