---
title: Hücrelerin Hizalamasını Değiştir ve Mevcut Biçimlendirmeyi Koru ile C++
description: Hücre düzenini değiştirmek ve mevcut biçimi korumak için Aspose.Cells kütüphanesini kullanın
keywords: Aspose.Cells, C++, Hücre hizalaması, mevcut biçimlendirmeyi koru
type: docs
weight: 340
url: /tr/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazen, birden çok hücrenin hizalamasını değiştirmek istersiniz ama mevcut biçimlendirmeyi de korumak istersiniz. Aspose.Cells, bu işlemi [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/) özelliği ile yapmanızı sağlar. Eğer **true** olarak ayarlarsanız, hizalamadaki değişiklikler gerçekleşir, aksi takdirde gerçekleşmez. Lütfen unutmayın, [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) nesnesi [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) metoduna parametre olarak geçirilir ve bu metod aslında hücre aralığına biçimlendirme uygular.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338585.xlsx) yükler, aralık oluşturur ve yatay ve dikey olarak ortalayıp mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338586.xlsx) karşılaştırır ve hücrelerin mevcut biçimlendirmesinin aynı olduğunu ancak hücrelerin şimdi yatay ve dikey olarak merkezlenmiş olduğunu gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing cells with formatting.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx");

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create cells range.
    Range rng = ws.GetCells().CreateRange(u"B2:D7");

    // Create style object.
    Style st = wb.CreateStyle();

    // Set the horizontal and vertical alignment to center.
    st.SetHorizontalAlignment(TextAlignmentType::Center);
    st.SetVerticalAlignment(TextAlignmentType::Center);

    // Create style flag object.
    StyleFlag flag;

    // Set style flag alignments true. It is the most crucial statement.
    // Because if it is false, no changes will take place.
    flag.SetAlignments(true);

    // Apply style to range of cells.
    rng.ApplyStyle(st, flag);

    // Save the workbook in XLSX format.
    wb.Save(outputDir + u"outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
