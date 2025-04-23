---
title: Pivot Bağlantısını C++ ile Kaldırma
linktitle: Pivot Bağlantısını Kaldır
type: docs
weight: 30
url: /tr/cpp/remove-pivot-connection/
description: Aspose.Cells kütüphanesini kullanarak C++ ile pivot bağlantısını nasıl kaldıracağınızı öğrenin.
keywords: Office 2013, office 2016, office 2019 ve office 365 olmadan pivot bağlantısını kaldırın.
---

## **Olası Kullanım Senaryoları**

Excel'de dilimleyiciyi ve pivot tabloyu ayırmak istiyorsanız, dilimleyiciye sağ tıklayın ve "Rapor Bağlantıları..." öğesini seçin. Seçenek listesinde onay kutusunda işlem yapabilirsiniz. Benzer şekilde, Aspose.Cells API'sını kullanarak dilimleyiciyi ve pivot tabloyu ayırmak için lütfen [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/) yöntemini kullanın. Bu, dilimleyiciyi ve pivot tabloyu ayıracaktır.

## **Dilimleyici ve pivot tablosunu ayır**

Aşağıdaki örnek kod önceden var olan bir dilimleyici içeren [örnek Excel dosyasını](remove-pivot-connection.xlsx) yükler. Daha sonra dilimleyicilere erişir ve dilimleyici ile pivot tabloyu ayırır. Son olarak, çalışma kitabını [çıkış Excel dosyası](remove-pivot-connection-out.xlsx) olarak kaydeder. 

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
