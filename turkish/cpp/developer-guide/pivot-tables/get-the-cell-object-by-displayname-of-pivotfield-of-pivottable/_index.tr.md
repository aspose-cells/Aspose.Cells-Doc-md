---
title: C++ kullanarak PivotTable ın PivotField DisplayName ile Hücre Nesnesi Alımı
linktitle: PivotTable ın PivotField DisplayName ile Hücre Nesnesi Alımı
type: docs
weight: 70
url: /tr/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Aspose.Cells for C++ kullanarak pivot alanın görüntü adına göre hücre nesnesini nasıl alınacağını ve biçimlendirme uygulayacağınızı öğrenin.
---

{{% alert color="primary" %}}

 Aspose.Cells, pivot alanının görüntü adına göre hücre nesnesine erişmek için kullanabileceğiniz [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/) metodunu sağlar. Bu metod, pivot alan başlığınızı vurgulamak veya biçimlendirmek istediğinizde faydalıdır. Bu makale, veri alanının görünüm adına göre hücre nesnesini nasıl alınacağını ve ardından biçimlendirme uygulanacağını açıklar.

{{% /alert %}}

## ** PivotTable'ın PivotField DisplayName ile Hücre Nesnesi Alımı**

 Aşağıdaki kod, sayfadaki ilk pivot tabloya erişir ve ardından pivot tablonun ikinci veri alanının görünüm adına göre hücreyi alır. Hücrenin dolgu rengi ve yazı tipi rengi sırasıyla açık mavi ve siyah olarak değiştirilir. Aşağıda, kod çalıştırılmadan önce ve sonra pivot tablonun nasıl göründüğünü gösteren ekran görüntüleri bulunmaktadır.

|**Pivot Tablosu - Önce**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**Pivot Tablosu - Sonra**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
