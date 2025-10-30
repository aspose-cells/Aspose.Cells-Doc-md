---
title: Çoklu kodlama ile CSV Dosyasını Okuma (C++)
linktitle: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/cpp/reading-csv-file-with-multiple-encodings/
description: Çoklu kodlama kullanarak Aspose.Cells for C++ ile CSV dosyalarını okuma yöntemini öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, çoklu kodlama ile CSV'yi düzgün yüklemek için {0} özelliğini **true** yapmanızı sağlar.

{{% /alert %}}

Aspose.Cells, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) özelliği sağlar, bu özelliği doğru şekilde yüklemek için **true** olarak ayarlamanız gerekir.

Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını gösterir. Birinci satır **ANSI** kodlamasında ve ikinci satır **Unicode** kodlamasındadır.

|**Giriş dosyası**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülmüş XLSX dosyasını gösterir, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) özelliği **true** olarak ayarlanmamıştır. Görüldüğü gibi, Unicode metni düzgün çevrilmemiştir.

|**Çıktı dosyası 1: çoklu kodlamalar için herhangi bir düzenleme yapılmamıştır**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülmüş XLSX dosyasını gösterir, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) özelliği **true** olarak ayarlandıktan sonra. Görüldüğü gibi, Unicode metni düzgün şekilde çevrilmiştir.

|**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## İlgili Makaleler

- [CSV Dosyalarını Açma](/cells/tr/cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="cpp" >}}
