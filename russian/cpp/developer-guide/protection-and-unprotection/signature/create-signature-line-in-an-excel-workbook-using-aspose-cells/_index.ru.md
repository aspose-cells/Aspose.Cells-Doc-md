---
title: Создать линию подписи в рабочей книге Excel с помощью C++ и Aspose.Cells
linktitle: Создать линию подписи в рабочей книге Excel
type: docs
weight: 150
url: /ru/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Эта статья описывает, как создать линию подписи в рабочей книге Excel с помощью кода C++ и Aspose.Cells for C++.
keywords: Создать строку подписи в книге Excel, Как создать строку подписи в книге Excel, Как добавить строку подписи, Как добавить строку подписи в файл Excel.
---

## **Введение**

Microsoft Excel предоставляет возможность добавлять **Строку подписи** в рабочие книги Excel. Вы можете добавить строку подписи, нажав на вкладку **Вставка** и затем выбрав **Строка подписи** из группы **Текст**.

## **Как создать строку подписи для Excel**

Aspose.Cells также предоставляет эту функцию и предоставляет свойство [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) для этой цели. В этой статье будет объяснено, как использовать это свойство для добавления строки подписи с помощью Aspose.Cells.

Приведенный ниже образец кода добавляет строку подписи с использованием свойства [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) и сохраняет книгу.

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
