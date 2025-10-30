---
title: Excel dosyasını HTML ye dışa aktarırken sağdan sola metin genişletme
linktitle: Excel den HTML ye Dönüştürürken Metni Sağdan Sola Doğru Genişletme
type: docs
weight: 60
url: /tr/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye dışa aktarırken sağdan sola metin genişletmeyi nasıl yapacağınızı öğrenin.
---

{{% alert color="primary" %}} 

Aspose.Cells for C++, şu anda HTML'ye dışa aktarırken sağdan sola metin genişletmeyi destekler. Bu özellik v8.9.0.0 sürümünden beri uygulanmaktadır. Kaynak Excel dosyanızda sağdan sola genişleyen herhangi bir metin varsa, Aspose.Cells bunu doğru şekilde HTML'ye aktarır.

{{% /alert %}} 

## **Excel dosyasını HTML'e dönüştüren aşağıdaki örnek kod. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü göstermektedir.**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](5115502.xlsx) HTML'ye dönüştürür. Bu ekran görüntüsü, örnek Excel dosyasının Microsoft Excel 2013'te nasıl göründüğünü gösterir.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Bu ekran görüntüsü, [eski sürümle oluşturulan HTML çıktı](5115509) gösterir.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Bu ekran görüntüsü, [yeni sürümle oluşturulan HTML çıktı](5115508) gösterir.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Görüntülerde görüldüğü gibi, yeni sürüm sağa hizalanmış metni doğru şekilde sola genişletir, tıpkı Microsoft Excel gibi.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
