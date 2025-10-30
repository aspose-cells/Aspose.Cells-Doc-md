---
title: C++ ile Stil Nesnelerini Tekrar Kullanma
linktitle: Stil Nesnelerini Yeniden Kullanma
description: Aspose.Cells for C++ te, yeniden kullanılabilir stil nesneleri oluşturarak stil yönetimini basitleştirebilir ve kod verimliliğini artırabilirsiniz. Kılavuzumuz, yinelenebilir stil nesnelerinin avantajlarından nasıl yararlanacağınızı ve bunları uygulamanıza nasıl entegre edeceğinizi anlatacaktır.
keywords: Aspose.Cells for C++, Stil Nesnelerini Yeniden Kullanma, Stil Yönetimi, Kod Verimliliği, Yeniden Kullanılabilir Stiller, Uygulama Geliştirme, API Referansı, Örnek Kod, İndirme, Destek.
type: docs
weight: 3000
url: /tr/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Stil nesnelerini yeniden kullanmak, belleği boşaltabilir ve programı daha hızlı hale getirebilir.

{{% /alert %}}

Bir çalışsayfadaki geniş bir hücre aralığına bazı biçimlendirme uygulamak için:

1. Bir stil nesnesi oluşturun.
1. Öznitelikleri belirtin.
1. Stili aralıktaki hücrelere uygulayın.

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

[**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) yaklaşımı çok daha az bellek kullanır ve verimlidir, bu nedenle gereksiz bellek tüketen eski Cell.Style özelliği Aspose.Cells 7.1.0 sürümü ile kaldırılmıştır.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
