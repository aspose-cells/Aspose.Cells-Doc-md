---
title: C++ ile Microsoft Excel Formül İzleme Penceresine Hücre Ekleme
linktitle: Formül İzleme Penceresine Hücreler Ekleyin
description: Excel de formül izleme penceresine hücre eklemek için Aspose.Cells for C++ kullanmayı öğrenin. Bir Excel dosyası yükleyin veya oluşturun, hücreleri manipüle edin, formüller ayarlayın ve düzenlenmiş dosyayı kaydedin.
keywords: Aspose.Cells, Excel, Formül İzleme Penceresi, Hücreler, Ekleme, C++
type: docs
weight: 60
url: /tr/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel İzleme Penceresi, hücre değerlerini ve formüllerini uygun şekilde izlemek için kullanışlı bir araçtır. Microsoft Excel'de *İzleme Penceresi*ni açmak için *Formüller > İzleme Penceresi* seçeneğine tıklayabilirsiniz. Bu pencerede *İzleme Ekle* düğmesi bulunur ve burada hücreler denetim için eklenebilir. Benzer şekilde, Aspose.Cells API kullanarak [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) metodunu kullanarak hücreleri İzleme Penceresine ekleyebilirsiniz.

## **Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme**

Aşağıdaki örnek kod, hücrelerin C1 ve E1 formüllerini ayarlar ve ikisini de İzleme Penceresine ekler. Daha sonra çalışma kitabını [çıktı Excel dosyası](67338481.xlsx) olarak kaydeder. Çıkış Excel dosyasını açıp *İzleme Penceresi*ni görüntülediğinizde, her iki hücreyi de ekran görüntüsünde gösterildiği gibi göreceksiniz.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
