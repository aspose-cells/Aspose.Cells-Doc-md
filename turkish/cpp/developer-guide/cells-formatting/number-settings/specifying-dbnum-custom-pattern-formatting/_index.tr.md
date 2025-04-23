---
title: C++ ile DBNum Özel Desen Biçimlendirmesi Belirtme
linktitle: DBNum Özel Desen Biçimlendirmesi Belirt
description: Aspose.Cells, özel biçimlendirme desenleri kullanarak elektronik çalışma sayfalarıyla çalışmaya imkan tanıyan bir C++ kütüphanesidir. Bu makale, sayıların nasıl görüntüleneceğine daha fazla kontrol sağlamak için dbnum özel biçimlendirme desenini nasıl kullanacağınızı gösterecektir.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik çalışma sayfası, özel biçimlendirme deseni, biçimlendirme, dbnum , ekran görüntüsünü kontrol et
type: docs
weight: 110
url: /tr/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, *DBNum* özel desen biçimlendirmesini destekler. Örneğin, hücre değeri 123 ise ve özel biçimini [DBNum2][$-804]Genel olarak ayarlarsanız, 壹佰贰拾叁 şeklinde görüntülenir. Hücrenin özel biçimini [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) yöntemi ve [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) özelliği kullanarak belirleyebilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod, *DBNum* özel desen biçimlendirmeyi nasıl belirleyeceğinizi gösterir. Daha fazla yardım için [çıktı PDF](43352081.pdf) dosyasına bakınız.

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
