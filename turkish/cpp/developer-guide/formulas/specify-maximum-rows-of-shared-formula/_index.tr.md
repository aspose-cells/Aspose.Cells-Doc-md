---
title: C++ ile Paylaşılan Formül Maksimum Satırını Belirle
linktitle: Paylaşılan Formülün Maksimum Satırlarını Belirtme
type: docs
weight: 40
url: /tr/cpp/specify-maximum-rows-of-shared-formula/
description: Aspose.Cells for C++ kullanarak Excel dosyalarında paylaşılan formülün maksimum satırını nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Paylaşılan formülün varsayılan maksimum satır sayısı 64'tür. Bu herhangi bir sayı olabilir, örneğin 1000. Paylaşılan formülün performansı farklı satır sayılarıyla değişir. Bu nedenle, Aspose.Cells, paylaşılan formülün maksimum satırını belirlemek için kullanılabilecek [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) özelliği sağlar. Paylaşılan formül toplam satır sayısı bu değerden büyükse, birkaç paylaşılan formüle bölünecektir, aşağıdaki ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Paylaşılan Formülün Maksimum Satırlarını Belirtme**

Aşağıdaki örnek kod, [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) özelliğinin kullanımını açıklar. Paylaşılan formülün maksimum satırını 5 olarak ayarlar ve hücre D1'de 100 satırda paylaşılan formülü ekler ve [çıkış Excel dosyasına](61767856.xlsx) kaydeder. Çıkış Excel dosyasının içeriğini çıkartıp *sheet1.xml*'ye bakarsanız, paylaşılan formülün her 5 satırda bir bölündüğünü göreceksiniz, yukarıdaki ekran görüntüsünde vurgulandığı gibi.

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
