---
title: Bir Çalışma Sayfasındaki Birleştirilmiş Hücreleri Tanımlama C++ ile
linktitle: Birleştirilmiş Hücreleri Tespit Et
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için C++ kütüphanesidir. Bir sayfada birleştirilmiş hücreleri tespit etmeyi destekler, böylece kullanıcıların bu hücreleri tanımlaması ve üzerinde işlem yapması kolaylaşır. Bu makale, Aspose.Cells kütüphanesini kullanarak birleştirilmiş hücreleri nasıl tespit edeceğinizi gösterecek.
keywords: Aspose.Cells, Çalışma Sayfası, Birleştir, Hücreleri Bul, Tanımla, İşlet
type: docs
weight: 80
url: /tr/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Bu makale, çalışma sayfasındaki birleştirilmiş hücre alanlarını nasıl alacağınız hakkında bilgi sağlar.

Aspose.Cells, çalışma sayfasındaki birleştirilmiş hücre alanlarını almanıza izin verir. Onları ayırabilir (bölünebilir)siniz. Bu makale, görevi gerçekleştirmek için Aspose.Cells API'sını kullanarak en basit kodu gösterir.

{{% /alert %}}

Bileşen, tüm birleştirilmiş hücreleri alabilen [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/) yöntemi sağlar. Aşağıdaki kod örneği, bir sayfadaki birleştirilmiş hücreleri nasıl tespit edeceğinizi gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
