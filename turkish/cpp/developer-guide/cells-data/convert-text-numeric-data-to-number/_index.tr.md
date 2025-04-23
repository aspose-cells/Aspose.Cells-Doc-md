---
title: Metin Sayısal Veriyi Sayıya Dönüştürme C++ ile
linktitle: Metin Sayısal Verileri Sayıya Dönüştür
type: docs
weight: 900
url: /tr/cpp/convert-text-numeric-data-to-number/
description: Excel de metin olarak depolanan sayıları Aspose.Cells for C++ API kullanarak nasıl sayıya dönüştüreceğinizi öğrenin.
keywords: excel metni sayıya dönüştür, excel metni sayıya dönüştür c++, excel metin sayısal veriyi sayıya dönüştür, excel metin sayısal veriyi sayıya dönüştür c++, excel sayısal metni sayıya dönüştür, excel sayısal metni sayıya dönüştür c++, excel sayısal metni sayıya dönüştür, excel sayısal metni sayıya dönüştür c++, metin sayısal veriyi sayıya dönüştür, excel metni sayıya dönüştür c++, sayısal dizgiyi sayıya dönüştür excel ile c++
---

## **Olası Kullanım Senaryoları**
Ara sıra, metin olarak girilmiş sayısal verileri sayılara dönüştürmek isteyebilirsiniz. Microsoft Excel'de sayıları metin olarak girebilirsiniz, örneğin **'12345**. Excel, ardından sayıyı bir dize olarak işler. Aspose.Cells, dizeleri sayılara dönüştürmenize olanak sağlar.

## Excel'de metin olarak depolanan sayıları sayılara dönüştürme
Birkaç basit adımı izleyerek metin olarak depolanan sayıları sayılara dönüştürebilirsiniz.
1. Sol üst köşede bir hata göstergesi bulunan herhangi bir tek hücre veya hücre aralığını seçin.
1. Seçili hücre veya hücre aralığının yanına, ortaya çıkan hata düğmesine tıklayın. Menüde, Sayıya Dönüştür üzerine tıklayın. 
<br>
<img src="4.png" width=70% />
1. Uyarı düğmesi kullanılabilir değilse, Bu sorunu yaşayan bir sütun seçin. Tüm sütunu dönüştürmek istemiyorsanız, bunun yerine bir veya daha fazla hücre seçebilirsiniz. Seçtiğiniz hücrelerin aynı sütunda olduğundan emin olun, aksi halde bu işlem çalışmaz. Bir sütunu bölme için genellikle Metin Bölme düğmesi kullanılır, ancak aynı zamanda bir sütun metnini sayılara dönüştürmek için de kullanılabilir. Veri sekmesinde, Metin Bölme'ye tıklayın.
<br>
<img src="1.png" width=70% />
1. Açılır pencerede Tamam düğmesine tıklayın.
<br>
<img src="2.png" width=70% />
1. Metin olarak depolanan sayılar sayılara dönüştürülür.
<br>
<img src="3.png" width=70% />

## Metin olarak depolanan sayıları nasıl sayıya dönüştürebiliriz Aspose.Cells for C++ kullanarak
Aspose.Cells, tüm dize veya metin sayısal verilerini sayılara dönüştürmek için kullanılabilecek [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) yöntemini sağlar.

Aşağıdaki ekran görüntüsü, hücrelerdeki string sayıları **A1:A17** göstermektedir. Dize sayıları sola hizalanmıştır.
<br>
<img src="5.png" width=70% />

Bu string sayılar aşağıdaki ekran görüntüsünde [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) kullanılarak sayılara dönüştürülmüştür. Görebileceğiniz gibi, şimdi sağa hizalanmış durumdadırlar.
<br>
<img src="6.png" width=70% />

## Dizgi sayısal veriyi gerçek sayıya dönüştüren C++ kodu

Aşağıdaki örnek kod, tüm çalışma sayfalarındaki dize sayısal verileri gerçek sayılara dönüştürmenin nasıl yapıldığını göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
