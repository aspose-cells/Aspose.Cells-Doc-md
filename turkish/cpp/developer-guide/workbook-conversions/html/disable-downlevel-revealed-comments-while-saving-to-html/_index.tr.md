---
title: C++ ile Downlevel Revealed Comments devre dışı bırakma
linktitle: Düşük Seviyeli Gösterilen Yorumları Devre Dışı Bırak
type: docs
weight: 20
url: /tr/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Aspose.Cells kullanarak HTML ye kaydederken AltSeviye Açıklandığı Yorumları ortadan kaldırın ve Excel dosyalarını C++ ile kaydederken Eliminate Downlevel Revealed Yorumlar.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, Aspose.Cells AltSeviye Koşullu Yorumları ortaya çıkarır. Bu koşullu yorumlar çoğunlukla eski Internet Explorer sürümleriyle ilgilidir ve modern Web Tarayıcılarında ilgisizdir. Bu konuda detaylı bilgiyi aşağıdaki bağlantıda bulabilirsiniz.

- [Koşullu yorum - Downlevel-açıklanan koşullu yorum](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells, [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) özelliğini **true** olarak ayarlayarak bu AltSeviye Açık Yorumları ortadan kaldırmanıza olanak tanır.

## **HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak**

Aşağıdaki örnek kod, [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/) özelliğinin kullanımını gösterir. Ekran görüntüsü bu özellik ayarlanmadığında etkisini gösterir. Bu kodda kullanılan örnek Excel dosyasını [indirin](50528257.xlsx) ve onun tarafından oluşturulan [çıktı HTML'sini](50528258.zip) referans olarak kullanın.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
