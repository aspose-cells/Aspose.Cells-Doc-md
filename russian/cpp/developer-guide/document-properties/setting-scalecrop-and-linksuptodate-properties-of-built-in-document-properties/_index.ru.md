---
title: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа с C++
linktitle: Настройка свойств ScaleCrop и LinksUpToDate
type: docs
weight: 320
url: /ru/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Узнайте, как установить свойства ScaleCrop и LinksUpToDate встроенных свойств документа с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) и [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) — это два расширенных встроенных свойства документа, определенных внутри формата OpenXml. Назначение этих свойств следующее:

## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **TRUE**, чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в **FALSE**, чтобы обрезать миниатюру документа и показать только секции, которые помещаются на экране.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **TRUE**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **FALSE**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
Следующий пример кода задает расширенные встроенные свойства документа [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) и [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) для рабочей книги. Пожалуйста, проверьте [выходной файл Excel](5115500.xlsx), созданный этим кодом, измените его расширение на .zip, распакуйте его содержимое и просмотрите app.xml, как показано на скриншоте выше.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
