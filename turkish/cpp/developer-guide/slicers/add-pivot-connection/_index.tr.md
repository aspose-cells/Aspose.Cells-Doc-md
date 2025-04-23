---
title: Pivot Bağlantısı Eklemek (C++)
linktitle: Pivot Bağlantısı Ekleme
type: docs
weight: 30
url: /tr/cpp/add-pivot-connection/
description: Aspose.Cells kütüphanesini kullanarak pivot bağlantısı eklemeyi öğrenin.
keywords: Ofis 2013, Ofis 2016, Ofis 2019 ve Ofis 365 olmadan pivot bağlantısı ekleme.
---

## **Olası Kullanım Senaryoları**

Excel'de dilimleyici ve pivot tabloyu ilişkilendirmek istiyorsanız, dilimleyiciye sağ tıklayarak "Rapor Bağlantıları..." öğesini seçmeniz gerekmektedir. Seçenek listesinde onay kutusunda işlem yapabilirsiniz. Benzer şekilde, Aspose.Cells API'sını kullanarak dilimleyici ve pivot tablo ilişkilendirmek istiyorsanız, [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/) yöntemini kullanmalısınız. Bu, dilimleyici ve pivot tabloyu ilişkilendirecektir.

## **Dilimleyiciyi ve Pivot Tablosunu İlişkilendir**

Aşağıdaki örnek kod önceden var olan bir dilimleyici içeren [örnek Excel dosyasını](add-pivot-connection.xlsx) yükler. Slicer'a erişir ve sonra Slicer'ı ve PivotTabloyu ilişkilendirir. Son olarak, çalışma kitabını [çıkış Excel dosyası](add-pivot-connection-out.xlsx) olarak kaydeder. 

## **Örnek Kod**

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
