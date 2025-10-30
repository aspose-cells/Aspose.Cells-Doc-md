---
title: C++ ile spreadsheet leri görsellere dönüştürürken Varsayılan Yazı Tipini Ayarla
linktitle: Varsayılan Yazı Tipini Ayarla
type: docs
weight: 360
url: /tr/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Aspose.Cells kullanarak spreadsheet leri görsellere dönüştürürken varsayılan yazı tipinin nasıl ayarlanacağını öğrenin.
---

{{% alert color="primary" %}}

Yayımlama sırasında elektronik tabloları görüntü olarak oluşturmak için [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliğini kullanın. Bu özellik, elektronik tablonun varsayılan yazı tipi karakterlerinizi oluşturamadığında yalnızca etkilidir. [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliği ile belirtilen varsayılan yazı tipi, geçersiz veya var olmayan yazı tiplerine sahip tüm hücreler için kullanılır.

{{% /alert %}}

## Yayımlama Sırasında Varsayılan Yazı Tipini Ayarlayın

Aşağıdaki örnek kod, bir worbook oluşturur, ilk çalışma sayfasının A4 hücresine bir metin ekler ve yazı tipini geçersiz veya varolmayan bir yazı tipine ayarlar. Ardından, çalışma sayfasının iki görüntüsünü alır. İlk görüntü, [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliğini *Courier New* olarak ayarlama ile alınır ve ikinci görüntü, [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliğini *Times New Roman* olarak ayarlama ile alınır.

Bu, [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliğini *Courier New* olarak ayarladıktan sonraki çıktı görüntüsüdür.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Bu, [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliğini *Times New Roman* olarak ayarladıktan sonraki çıktı görüntüsüdür.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Örnek Kod

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Set default font of the workbook to none
    Style s = wb.GetDefaultStyle();
    s.GetFont().SetName(u"");
    wb.SetDefaultStyle(s);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"A4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell A4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    st.SetIsTextWrapped(true);
    cell.SetStyle(st);

    // Set first column width and fourth column height
    ws.GetCells().SetColumnWidth(0, 80);
    ws.GetCells().SetRowHeight(3, 60);

    // Create image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    // Render worksheet image with Courier New as default font
    opts.SetDefaultFont(u"Courier New");
    SheetRender sr(ws, opts);
    sr.ToImage(0, outDir + u"out_courier_new_out.png");

    // Render worksheet image again with Times New Roman as default font
    opts.SetDefaultFont(u"Times New Roman");
    SheetRender sr2(ws, opts);
    sr2.ToImage(0, outDir + u"times_new_roman_out.png");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
