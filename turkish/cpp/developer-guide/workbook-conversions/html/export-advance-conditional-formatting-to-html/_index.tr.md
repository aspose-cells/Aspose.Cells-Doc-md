---
title: DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeyi HTML ye Dışa Aktarırken C++ ile Dışa Aktar
linktitle: Koşullu Biçimlendirmeyi HTML ye Dışa Aktar
type: docs
weight: 30
url: /tr/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye dönüştürürken DataBar, ColorScale ve IconSet koşullu biçimlendirmeyi nasıl dışa aktaracağınızı öğrenin.
---

{{% alert color="primary" %}} 

Excel dosyanızı HTML'ye çevirirken DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeleri dışa aktarabilirsiniz. Bu özellik kısmen Microsoft Excel tarafından desteklenmektedir, ancak Aspose.Cells for C++ tamamen destekler.

{{% /alert %}} 

## **Excel'den HTML'ye Dönüşüm sırasında DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeleri Dışa Aktar**
Aşağıdaki ekran görüntüsü, DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeleri içeren örnek Excel dosyasını göstermektedir. Dosyayı verilen bağlantıdan indirebilirsiniz.

![todo:image_alt_text](conversion_1.png)

Aşağıdaki ekran görüntüsü, DataBar, ColorScale ve IconSet Koşullu Biçimlendirmeleri gösteren Aspose.Cells çıktı HTML dosyasını göstermektedir. Görüntü, tamamen [örnek excel dosyası](5115558.xlsx) ile aynıdır.

![todo:image_alt_text](conversion_2.png)

### **Örnek Kod**
Aşağıdaki örnek kod, örnek excel dosyasını HTML'ye dönüştürür, bu sadece normal bir [Excel'den HTML'ye dönüşüm] (/cells/tr/cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
