---
title: Aspose.Cells ile FormülMetni Fonksiyonunu C++ kullanarak
linktitle: FormülText Fonksiyonunu Kullanma
description: Bu makale, Aspose.Cells kitaplığını kullanarak Microsoft Excel deki formülleri işlemek için FormulaText fonksiyonunun nasıl kullanılacağını tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak hücrenin formül metnini alabilir ve ayarlayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, FormulaText fonksiyonları
type: docs
weight: 60
url: /tr/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText, Excel 2013 ve sonrası bir fonksiyondur. Önceki sürümler, Excel 2010 veya 2007 gibi, tarafından desteklenmez. Adından da anlaşılacağı gibi, belirli bir hücrede bulunan formülün metnini yazdırır. Bu makale, Aspose.Cells kullanarak bu fonksiyonun nasıl kullanılacağını gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, Aspose.Cells ile FormulaText kullanımını gösterir. Kod önce hücre A1'e bir formül yazar ve sonra A2 hücresinde FormulaText'i kullanarak formülün metnini yazdırır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
