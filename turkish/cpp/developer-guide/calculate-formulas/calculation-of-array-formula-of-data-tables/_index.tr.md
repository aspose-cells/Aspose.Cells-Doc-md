---
title: C++ ile Veri Tabloları için Dizi Formülü Hesaplama
linktitle: Veri Tablolarının Dizilerini Hesaplama
description: Aspose.Cells kütüphanesini kullanarak Microsoft Excel deki veri tablosu için dizi formüllerinin nasıl hesaplanacağını C++ ile anlatır. Var olan bir Excel dosyasını yükleyerek veya yeni bir dosya oluşturarak, Aspose.Cells tarafından sağlanan metodları kullanarak veri tablosunun dizi formülünü hesaplayabilir ve sonucu alabilirsiniz. Son olarak, değiştirilen Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, veri tabloları, dizi formülleri, hesaplamalar, C++
type: docs
weight: 70
url: /tr/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft Excel'de Veri Tablosu oluşturabilirsiniz. Aspose.Cells şimdi bir veri tablosunun dizi formülünü hesaplamanıza izin verir. Her türlü formülü hesaplamak için lütfen [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) kullanınız.

{{% /alert %}}

Aşağıdaki örnek kodda, [kaynak excel dosyası](5115535.xlsx)'ı kullandık. Eğer B1 hücresinin değerini 100 olarak değiştirirseniz, Sarı renkle doldurulan Veri Tablosu değerleri 120 olarak değişir ve [çıktı PDF'sini](5115538.pdf) oluşturur. Daha fazla bilgi için yorumları okuyunuz.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

[çıktı PDF'sini](5115538.pdf) oluşturmak için [kaynak excel dosyası](5115535.xlsx)'ı kullanılan örnek kod aşağıdaki gibidir. Daha fazla bilgi için yorumları okuyunuz.

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
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
