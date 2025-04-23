---
title: Определение версии документа файла Excel с помощью встроенных свойств документа с C++
linktitle: Определение версии документа
type: docs
weight: 20
url: /ru/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Узнайте, как задать версию документа файла Excel с помощью встроенных свойств документа с Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете изменить **номер версии** файла Excel, щелкнув правой кнопкой мыши по файлу и выбрав Свойства > Детали, а затем отредактировав поле **номер версии**. Для этого используйте свойство [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/) и API Aspose.Cells для программного изменения.

## **Указание версии документа Excel с использованием встроенных свойств документа**

Следующий пример кода создает рабочую книгу и изменяет ее встроенные свойства документа, включающие Заголовок, Авторов и номер версии. Пожалуйста, ознакомьтесь с [выходным файлом Excel](64716811.xlsx), созданным этим кодом, и скриншотом, показывающим измененную версию с помощью свойства [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
