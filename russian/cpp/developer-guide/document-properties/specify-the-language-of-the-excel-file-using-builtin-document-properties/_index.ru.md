---
title: Задайте язык файла Excel с помощью встроенных свойств документа с C++
linktitle: Задайте язык файла Excel
type: docs
weight: 30
url: /ru/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Узнайте, как программно изменить язык файла Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете изменить язык файла Excel, щелкнув по файлу правой кнопкой мыши и выбрав Свойства > Детали, а затем отредактировав поле Язык. Для этого используйте свойство [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/) и API Aspose.Cells.

## **Указание языка файла Excel с использованием встроенных свойств документа**

Следующий пример кода создает рабочую книгу и изменяет ее встроенное свойство документа, называемое Язык. Пожалуйста, ознакомьтесь с [выходным файлом Excel](64716891.xlsx), созданным этим кодом, и скриншотом, показывающим измененное поле Язык с помощью свойства [**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Образец кода**

```c++
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

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
