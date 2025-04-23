---
title: Alternatif Satırlar ve Sütunlar için Koşullu Biçimlendirmeli Gölgelendirme Uygula C++ ile
linktitle: Alternatif Satır ve Sütunlara Gölgelendirme Uygula
description: C++ ile Aspose.Cells kütüphanesini kullanarak alternan satır ve sütunlar için gölgeli koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, C++, Alternatif Satırlar, Alternatif Sütunlar, Gölgeleme
type: docs
weight: 30
url: /tr/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) nesnesine koşullu biçimlendirme kuralları ekleme ve buna müdahale etme imkânı sağlar. Bu kurallar, istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, koşullu biçimlendirme kuralları ve Excel'in yerleşik fonksiyonları ile alternatif satırlar ve sütunlara gölgeleme uygulamak için Aspose.Cells for C++ API'lerinin kullanımını gösterecektir.

{{% /alert %}}

Bu makale, Excel'in yerleşik işlevleri ROW, COLUMN ve MOD'u kullanmaktadır. İleride sunulan kod örneğini daha iyi anlayabilmek için bu işlevlerin bazı ayrıntıları aşağıda verilmiştir.

- **ROW()** işlevi, bir hücre başvurusunun satır numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, ROW işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **COLUMN()** işlevi, bir hücre başvurusunun sütun numarasını döndürür. Eğer başvuru parametresi ihmal edilirse, COLUMN işlevinin girildiği hücre adresinin başvuru olduğunu varsayar.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Hedefe ulaşmak için Aspose.Cells for C++ API'si yardımıyla bazı kodlar yazmaya başlayalım.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin. 
Bu durumda elde edilen elektronik tablo aşağıdaki gibi görünecektir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
