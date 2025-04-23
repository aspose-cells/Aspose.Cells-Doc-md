---
title: Bir Excel çalışma sayfasında Satırları Ekle veya Sil ile C++
linktitle: Satır Ekle veya Sil
type: docs
weight: 20
url: /tr/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Bu makale, bir Excel çalışma sayfasında satır ve sütunları ekleme ve silme işlemleri için C++ kodunu sağlar.
keywords: C++ ile Excel çalışma sayfasına satır ekleme veya silme, C++ ile Excel e satır ekleme veya silme, C++ ile Excel e satır ekleme, C++ ile Excel den satır silme, C++ ile Excel çalışma sayfasına satır ekleme veya silme, C++ ile Excel de satır ekleme veya silme, C++ ile Excel e satır ekleme, C++ ile Excel den satır silme
---

{{% alert color="primary" %}}

Yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, verileri karşılamak için ekstra satırlar veya sütunlar eklemeniz gerekebilir. Diğer zamanlarda, belirli pozisyonlardan satırları veya sütunları silmeniz gerekebilir.

{{% /alert %}}

Aspose.Cells, satırları eklemek ve silmek için iki yöntem sunar: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) ve [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Bu yöntemler, performans için optimize edilmiştir ve işi çok hızlı bir şekilde yapar.

Birkaç satır eklemek veya kaldırmak amacıyla, her zaman döngüde [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) veya [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) yöntemlerini kullanmak yerine [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) ve [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) yöntemlerini kullanmanızı öneririz.

Aspose.Cells, Microsoft Excel'in çalışma şekliyle aynı şekilde çalışır. Satırlar veya sütunlar eklenirse, çalışma sayfası içeriği aşağıya ve sağa kaydırılır. Satırlar veya sütunlar kaldırıldığında, çalışma sayfası içeriği yukarı veya sola kaydırılır. Satırlar eklenip kaldırıldığında diğer çalışma sayfaları ve hücrelerdeki referanslar güncellenir.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
