---
title: C++ kullanarak Formüllü CSV dosyasını yükleme veya içe aktarma
linktitle: Formülleri içeren CSV dosyasını yükle veya içe aktar
type: docs
weight: 350
url: /tr/cpp/load-or-import-csv-file-with-formulas/
description: Aspose.Cells kullanarak formüller içeren CSV dosyasını yükle veya içe aktar.
---

{{% alert color="primary" %}} 

CSV dosyaları çoğunlukla metinsel veri içerir ve genellikle formülleri içermez. Ancak, bazı durumlarda CSV dosyaları formüller de içerebilir. Böyle CSV'ler, [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) değeri **true** olarak ayarlanarak yüklenmelidir. Bu özellik **true** olarak ayarlandığında, Aspose.Cells formülleri basit metin olarak değil, formüller gibi işler ve Aspose.Cells formül hesaplama motoru bunları normal şekilde işler.

{{% /alert %}} 

Aşağıdaki kod, formüllü CSV dosyasını nasıl yükleyip içe aktaracağınızı gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnek olarak, bu veriyi içeren [basit csv dosyasını](5115034.csv) kullanıyoruz. Görünen, formül içeriyor.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    //Create TxtLoadOptions with specified settings
    TxtLoadOptions opts;
    opts.SetSeparator(u','); // Set the separator to a comma
    opts.SetHasFormula(true); // Indicate that the CSV may have formulas

    // Load the CSV file into a Workbook object
    Workbook workbook(srcDir + u"sample.csv", opts);

    // You can also import the CSV file starting from cell D4 (indices 3,3)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().ImportCSV(srcDir + u"sample.csv", opts, 3, 3);

    // Save the workbook in Xlsx format
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "CSV file loaded and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Kod ilk olarak CSV dosyasını yükler, ardından tekrar D4 hücresine içe aktarır. Son olarak, çalışma kitabı nesnesini XLSX biçiminde kaydeder. [Çıktı XLSX dosyası](5115052.xlsx) böyle görünür. Görüldüğü gibi, C3 ve F4 hücreleri formüller içerir ve sonucu 800'dür.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
