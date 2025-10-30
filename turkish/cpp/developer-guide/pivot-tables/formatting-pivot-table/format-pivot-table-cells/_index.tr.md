---
title: Pivot Tablo Hücrelerini Biçimlendirme ile C++
linktitle: Döşeme Özeti Hücreleri Biçimlendir
type: docs
weight: 30
url: /tr/cpp/format-pivot-table-cells/
description: Aspose.Cells ile C++ kullanarak özet tablo hücrelerini biçimlendirmeyi öğrenin.
---

{{% alert color="primary" %}}

Bazı durumlarda, döşeme tablosu hücrelerini biçimlendirmek isteyebilirsiniz. Örneğin, döşeme tablosu hücrelerine arka plan rengi uygulamak isteyebilirsiniz. Aspose.Cells, bu amaçla kullanabileceğiniz iki yöntem [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) ve [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) sağlar.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) stilini tüm özet tabloya uygular, [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) ise özet tablodaki tek bir hücreye uygular.

{{% /alert %}}

Aşağıdaki örnek kod, iki özet tablo içeren [örnek Excel dosyasını](pivot_format.xlsx) yükler ve tüm özet tablonun biçimlendirilmesi ile bireysel hücrelerin biçimlendirilmesi işlemini gerçekleştirir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"pivot_format.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(u"Sheet1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(1);

    Style style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::LightBlue());
    pivotTable.FormatAll(style);

    style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::Yellow());

    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(0);
    pivotTable2.Format(16, 5, style);

    workbook.Save(u"out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## İlgili Makaleler

- [Pivot Tablosu Biçimlendirme](/cells/tr/cpp/formatting-pivot-table/)
- [Pivot Tablosundaki DataField'ın veri görüntüleme formatları ile çalışma](/cells/tr/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
