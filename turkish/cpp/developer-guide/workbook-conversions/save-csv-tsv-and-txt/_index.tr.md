---
title: Excel i CSV, TSV ve Txt e dönüştürmek için C++ kullanın
linktitle: CSV, TSV ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/cpp/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarını kolayca CSV, TSV ve TXT formatlarına dönüştürün.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel, ODS, JSON ve diğer format dosyalarını CSV, TSV ve TXT'ye dönüştürmeyi mümkün kılar.

{{% /alert %}}

## **Workbook'u Metin veya CSV Formatında Kaydet**

Bazen, birden fazla çalışma sayfası olan bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV, vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells sadece etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, bir çalışma kitabını metin formatına kaydetmenin nasıl yapıldığını açıklar. Herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyasını (yani XLS, XLSX, XLSM, XLSB, ODS vb.) yükleyin ve içinde herhangi bir sayıda çalışsayfa olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği kullanarak dosyanızı CSV olarak kaydedebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) virgüldür, bu nedenle CSV formatında kaydederken ayırıcı belirtmeyin.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Özel Ayraçla Metin Dosyaları Kaydetme**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla](/cells/tr/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp](/cells/tr/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="cpp" >}}
