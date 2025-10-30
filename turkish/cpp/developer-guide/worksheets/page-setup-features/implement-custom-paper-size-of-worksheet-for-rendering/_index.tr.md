---
title: Çalışma Sayfası için Özel Kağıt Boyutu Uygulama (Render İşlemi İçin) C++ ile
linktitle: Otomatik Olarak Çalışma Sayfası Kağıt Boyutunun Oluşturulması için Özelleştirilmiş Kağıt Boyutunun Uygulanması
type: docs
weight: 70
url: /tr/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Bu makale, Excel dosyasını PDF formatında programlı olarak render ederken istediğiniz çalışma sayfalarının özel kağıt boyutunu ayarlamak için C++ API kullanımını açıklar.
keywords: C++ ile Excel i PDF ye dönüştürürken özel kağıt boyutu ayarla
---

## **Olası Kullanım Senaryoları**

MS Excel'de özel kağıt boyutları oluşturmak için doğrudan seçenek bulunmamaktadır; ancak, Excel dosyalarını PDF'ye dönüştürürken istediğiniz çalışma sayfalarının kağıt boyutunu ayarlayabilirsiniz. Bu belge, Aspose.Cells API'leri kullanarak çalışma sayfasının özel kağıt boyutunun nasıl ayarlanacağını açıklar.

## **Otomatik Olarak Çalışma Sayfası için Özel Kağıt Boyutunun Uygulanması**

Aspose.Cells, çalışma sayfasının istediğiniz kağıt boyutunu uygulamanıza olanak tanır. [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) metodunu kullanarak özel bir sayfa boyutu belirtebilirsiniz. Aşağıdaki örnek kod, çalışma kitabının ilk çalışma sayfası için özel bir kağıt boyutunun nasıl belirtileceğini gösterir. Ayrıca, aşağıdaki kodla oluşturulan [çıktı PDF](45056028.pdf) örneği de referans alınabilir.

## **Ekran Görüntüsü**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
