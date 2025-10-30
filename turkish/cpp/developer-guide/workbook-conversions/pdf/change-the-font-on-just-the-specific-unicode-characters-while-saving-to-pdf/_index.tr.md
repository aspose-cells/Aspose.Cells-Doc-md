---
title: Sadece belirli Unicode karakterleri değiştirerek ve PDF ye kaydederken fontu değiştirme
linktitle: Ünicode Karakterlerde Yazı Tipini Değiştir
type: docs
weight: 260
url: /tr/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cells ile C++ kullanarak PDF ye kaydederken belirli Unicode karakterlerin fontunu nasıl değiştireceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazı Unicode karakterleri, kullanıcı tarafından belirtilen font tarafından görüntülenemez. Bu tür bir Unicode karakter **Bilinmeyen Kesme** (U+2011)'dır ve Unicode numarası 8209'dur. Bu karakter **Times New Roman** ile görüntülenemez, ancak **Arial Unicode MS** gibi diğer fontlarla görüntülenebilir.

 Bir karakter, Times New Roman gibi belirli bir fontta olan bir kelime veya cümle içinde oluşursa, Aspose.Cells bu karakteri gösterebilecek bir fonta, örneğin Arial Unicode MS'ye, tüm kelimenin veya cümleğin fontunu değiştirir.

Ancak bu, bazı kullanıcılar için istenmeyen bir davranıştır ve yalnızca o belirli karakterin fontunun değiştirilmesini isterler, tüm kelimenin veya cümlenin fontunun değiştirilmesi yerine.

Bu sorunu çözmek için Aspose.Cells, `PdfSaveOptions.IsFontSubstitutionCharGranularity` özelliği sağlar, bu özellik `true` olarak ayarlanmalıdır ki sadece görüntülenemeyen belirli karakterin fontu, görüntülenebilir bir fonta değiştirilsin ve kelimenin veya cümlenin geri kalanı orijinal fontta kalsın.

{{% /alert %}}

## **Örnek**

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodu ile oluşturulan iki PDF'yi karşılaştırır.

Biri `PdfSaveOptions.IsFontSubstitutionCharGranularity` özelliği ayarlanmadan oluşturulmuş, diğeri ise bu özellik `true` yapıldıktan sonra oluşturulmuştur.

İlk PDF'de tüm cümlenin fontu Times New Roman'dan Arial Unicode MS'ye Non-Breaking Hyphen nedeniyle değişti. İkinci PDF'de ise yalnızca Non-Breaking Hyphen'in fontu değişti.

|**İlk PDF Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**İkinci PDF Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Örnek Kod**

```c++
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
    Style style = cell1.GetStyle();
    style.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(style);
    cell2.SetStyle(style);

    // Put the values inside the cell
    cell1.PutValue(u"Hello without Non-Breaking Hyphen");
    cell2.PutValue(u"Hello\u2011 with Non-Breaking Hyphen");

    // Autofit the columns
    worksheet.AutoFitColumns();

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.pdf");

    // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
    PdfSaveOptions opts;
    opts.SetIsFontSubstitutionCharGranularity(true);
    workbook.Save(outDir + u"SampleOutput2_out.pdf", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
