---
title: C++ ile Hücreye HTML Zengin Metin Ekleme
linktitle: Html Dize Değeri
type: docs
weight: 50
url: /tr/cpp/adding-html-rich-text-inside-the-cell/
description: Aspose.Cells for C++ API kullanarak Hücreye HTML Zengin Metin eklemeyi öğrenin.
keywords: Hücre İçine HTML Zengin Metin Ekleme, Hücre İçine HTML Zengin Metin Ayarlama, Hücre İçine HTML Zengin Metin Ekleme, Hücre İçine HTML Zengin Metin Ekleme
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel odaklı HTML'yi XLS/XLSX formatına dönüştürmeyi destekler. Bu, Microsoft Excel tarafından oluşturulan HTML'nin Aspose.Cells kullanılarak tekrar XLS/XLSX formatına dönüştürülebileceği anlamına gelir.

Benzer şekilde, eğer basit bir HTML varsa, Aspose.Cells onu HTML Zengin Metne dönüştürebilir. [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) yöntemi, böyle basit bir HTML alabilir ve biçimlendirilmiş hücre metnine dönüştürebilir.

{{% /alert %}}

Aşağıdaki kod örneği, hücre içine HTML zengin metin eklemenin nasıl yapıldığını gösterir. Lütfen çıktı Excel dosyasının ekran görüntüsüne bakın.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## İlgili Makaleler

- [HTML kullanarak Hücre Değeri Ayarıyla Madde İmleri Göster](/cells/tr/cpp/display-bullets-by-setting-cell-value-using/)
- [Hücreden HTML5 dizesi al](/cells/tr/cpp/get-html5-string-from-cell/)
