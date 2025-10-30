---
title: Boş satırlar için ayırıcıları tutarak elektronik tabloları CSV formatına dışa aktarırken C++ ile
linktitle: CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla
type: docs
weight: 160
url: /tr/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Boş satırlar için ayırıcıları nasıl tutacağınızı Aspose.Cells kullanarak CSV ye dışa aktarırken öğrenin.
---

## **CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla**

Aspose.Cells, elektronik tabloları CSV'ye dönüştürürken satır ayırıcılarını tutma yeteneği sağlar. Bunun için, [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/) sınıfının [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) özelliğini kullanabilirsiniz. [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) boolean bir özelliktir. Excel dosyasını CSV'ye dönüştürürken boş satırlar için ayırıcıları tutmak için [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) özelliğini **true** olarak ayarlayın.

Aşağıdaki örnek kod, [kaynak Excel dosyasını](84378743.xlsx) yükler. [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) özelliğini **true** yapar ve [çıktı.csv](84378744.csv) olarak kaydeder. Ekran görüntüsü, kaynak Excel dosyası, varsayılan CSV'ye dönüştürme ve [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) ayarlamasıyla üretilen çıktı arasındaki karşılaştırmayı gösterir.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Örnek Kod**

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
