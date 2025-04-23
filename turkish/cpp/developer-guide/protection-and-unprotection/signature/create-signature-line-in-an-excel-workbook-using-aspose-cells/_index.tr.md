---
title: Aspose.Cells kullanarak C++ ile Excel Çalışma Kitabında İmza Satırı Oluşturma
linktitle: Excel Çalışma Kitabında İmza Satırı Oluşturma
type: docs
weight: 150
url: /tr/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Bu makale, Aspose.Cells for C++ kullanılarak C++ kodlarıyla Excel Çalışma Kitabında İmza Satırı oluşturmayı anlatır.
keywords: Excel Çalışma Kitabında İmza Çizgisi Oluşturmayı, Excel Çalışma Kitabında İmza Çizgisi Oluşturmayı, İmza Çizgisi Ekleme ve İmza Çizgisinin Excel dosyasına eklenmesini açıklar.
---

## **Giriş**

Microsoft Excel, Excel çalışma kitaplarına **İmza Satırı** eklemek için bir özellik sağlar. Aspose.Cells de bu özelliği sağlar ve bunun için {0} özelliğini sunmuştur. Bu makale, bu özelliği kullanmanın nasıl olduğunu açıklar.

## **Excel için İmza Çizgisi Oluşturmayı**

Aspose.Cells aynı özelliği sağlar ve bu amaçla [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) özelliğini kullanmıştır. Bu makale, bu özelliği kullanmanın nasıl olduğunu açıklayacaktır.

Aşağıdaki örnek kod, [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) özelliğini kullanarak Bir İmza Satırı ekler ve çalışma kitabını kaydeder.

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
