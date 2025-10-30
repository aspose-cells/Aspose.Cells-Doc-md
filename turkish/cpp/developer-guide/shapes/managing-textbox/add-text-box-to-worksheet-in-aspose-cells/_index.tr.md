---
title: C++ kullanarak Çalışma Sayfasına Metin Kutusu ekleme/yerleştirme
linktitle: Çalışma Sayfasına Metin Kutusu Ekle
type: docs
weight: 10
url: /tr/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Aspose.Cells kullanarak C++ ile çalışma sayfasına Metin Kutusu ekleme/yerleştirme
keywords: Aspose te Excel de metin Kutusu TextBox Çalışma Sayfasına Ekle/Ekle
---

## Excel'de Çalışma Sayfasına Metin Kutusu Ekle

Excel programında (sürüm 07 ve üzeri), metin kutusu ekebileceğiniz iki yer vardır. Biri 'insert-shapes' içinde, diğeri ise 'Insert' seçeneğinin sağ üst menüsündedir.

### Birinci Yöntem:

![1](1.png)

### Yöntem İki:

![2](2.png)

## Nasıl Oluşturulur

Metin Kutusu, yatay veya dikey metinle oluşturulabilir.

- Karşılık gelen seçeneği seçin (yatay veya dikey)
- Sayfada sol tuşa basın.
- Sol tuşa basılı tutun ve sayfada bir mesafe sürükleyin.
- Sol tuşu bırakın.

Şimdi bir metin kutusuna sahipsiniz.

## Aspose.Cells'te Çalışma Sayfasına Metin Kutusu Ekle

İş sayfasına toplu olarak TextBox eklemeniz gerektiğinde, manuel ekleme yöntemi açıkça bir felakettir. Eğer bu sizi rahatsız ediyorsa, bu belgenin size yardımcı olacağını düşünüyorum. [Aspose.Cells](https://products.aspose.com/cells/) size kodunuzda toplu eklemeleri kolayca yapmanızı sağlayan bir API sunar.

Aşağıdaki örnek kod bir metin kutusu oluşturur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Benzer bir dosya alacaksınız [sonuç dosyası](result.xlsx). Dosyada aşağıdakileri göreceksiniz:

![](52449.png)
{{< app/cells/assistant language="cpp" >}}
