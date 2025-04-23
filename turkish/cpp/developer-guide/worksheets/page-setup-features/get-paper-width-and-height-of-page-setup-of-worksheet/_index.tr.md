---
title: C++ ile Çalışma Sayfasının Sayfa Düzeni Kağıt Genişliği ve Yüksekliğini Alın
linktitle: Sayfa Düzeni Kağıt Genişliği ve Yüksekliğini Alın
type: docs
weight: 50
url: /tr/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: C++ kullanarak Aspose.Cells for C++ API ile Excel Çalışma Sayfası Sayfa Ayarı Kağıt Genişliği ve Kağıt Yüksekliği nasıl alınır, programlı olarak öğrenin.
keywords: excel sayfa düzeni kağıt genişliği c++, excel sayfa düzeni kağıt yüksekliği c++
---

## **Olası Kullanım Senaryoları**

Bazen, çalışma sayfasının sayfa düzeninde ayarlanmış olan kağıt boyutunun genişliği ve yüksekliğini bilmeniz gerekebilir. Bu amaçla [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) ve [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) metodlarını kullanabilirsiniz.

## **Çalışma Sayfası Sayfa Ayarları Kağıt Genişliği ve Yüksekliğini Alma**

Aşağıdaki örnek kod, [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) ve [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) metodlarının kullanımını açıklar. İlk olarak kağıt boyutunu *A2* olarak değiştirir, ardından kağıdın genişliği ve yüksekliğini bulur, sonra sırasıyla *A3*, *A4*, *Letter* olarak değiştirir ve kağıdın genişliği ve yüksekliğini bulur.

### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
