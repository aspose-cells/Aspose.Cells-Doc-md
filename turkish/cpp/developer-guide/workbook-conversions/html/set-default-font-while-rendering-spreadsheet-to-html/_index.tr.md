---
title: C++ ile Elektronik Tabloyu HTML’ye Dönüştürürken Varsayılan Yazı Tipini Ayarlayın
linktitle: Elektronik tabloyu HTML e dönüştürürken varsayılan yazı tipini ayarlayın
type: docs
weight: 370
url: /tr/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Aspose.Cells for C++ kullanarak elektronik tabloyu HTML’ye dönüştürürken varsayılan yazı tipini nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, elektronik tabloyu HTML’ye dönüştürürken varsayılan yazı tipini ayarlamanıza olanak tanır. Lütfen bu amaçla [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/)'ı kullanın. Bu özellik, bir elektronik tabloda geçersiz veya mevcut olmayan yazı tiplerine sahip hücreler varsa faydalıdır. Bu hücreler, [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) özelliği ile belirtilen yazı tipinde görüntülenir.

{{% /alert %}}

## Elektronik tabloyu HTML'e dönüştürürken varsayılan yazı tipini ayarlayın

Aşağıdaki örnek kod bir çalışma kitabı oluşturur, ilk çalışma sayfasının B4 hücresine bir metin ekler ve yazı tipini bilinmeyen/bulunmayan bir yazı tipine ayarlar. Daha sonra, çalışma kitabını farklı varsayılan yazı tipi adları olarak Courier New, Arial, Times New Roman vb. ayarlayarak HTML olarak kaydeder.

Ekran görüntüsü, farklı varsayılan yazı tipi adlarını [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) özelliği aracılığıyla ayarlamanın etkisini gösterir.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Kod, [Courier New ile](5115516), [Arial ile](5115518) ve [Times New Roman ile](5115517) çıktı HTML dosyasını oluşturur.

## Örnek Kod

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

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
