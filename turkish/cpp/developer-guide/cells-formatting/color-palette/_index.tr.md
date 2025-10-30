---
title: Color Paleti kullanımıyla ilgili nasıl kullanılır
linktitle: Renk Paletini Nasıl Kullanılır
type: docs
weight: 80
url: /tr/cpp/excel-color-palette/
description: Paletteye özel renkler eklemek ve Aspose.Cells for C++ API ile Excel renk paletini kullanmak için C++ kodu.
keywords: c++ ile palete özel renkler ekleme, programlı olarak Excel renk paleti kullanımı, çalışma kitabında renk paletini nasıl kullanırım, c++ ile excel de renk paletini nasıl kullanırım
---

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells ile sadece paletin mevcut renklerini değil aynı zamanda özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, önce paletine ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

## **Paletine Özel Renkler Ekleyin**

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, paleti değiştirmek için özel bir renk eklemek için aşağıdaki parametreleri alan bir [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) yöntemi sağlar:

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid is now in the palette
    std::cout << "Is Orchid in palette now? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
