---
title: Veri Filtreleme C++ ile
linktitle: Veri Filtreleme
type: docs
weight: 85
url: /tr/cpp/data-filtering/
description: Aspose.Cells for C++ API kullanarak veri filtresi eklemeyi öğrenin.
keywords: Renkle Filtre Ekleme, Tarih Filtreleri Ekleme, Sayı Filtreleri Ekleme, Dinamik Filtre Ekleme, Metin Filtreleri Ekleme, İçeren Özel Filtre Ekleme, İçermeyen Özel Filtre Ekleme, Başlayan Özel Filtre Ekleme, Biten Özel Filtre Ekleme
---

{{% alert color="primary" %}}

Microsoft Excel, elektronik tablo verilerini otomatik filtreleme özellikleri sağlar. Aspose.Cells, Microsoft Excel'in otomatik filtreleme özelliklerini tamamen destekler. Bu makale, Microsoft Excel'deki özellikleri nasıl kullanabileceğinizi ve onları Aspose.Cells kullanarak nasıl kodlayabileceğinizi açıklar.

{{% /alert %}}

## **Veriye Otomatik Filtreleme Uygulama**

Otomatik filtreleme, listede görüntülemek istediğiniz yalnızca öğeleri seçmenin en hızlı yoludur. Otomatik filtreleme özelliği, kullanıcılara belirli bir kriterlere göre listedeki öğeleri filtreleme olanağı sağlar. Metne, sayılara veya tarih bilgilerine göre filtreleme yapın.

### **Microsoft Excel'de Otomatik Filtreleme**

Microsoft Excel'de otomatik filtreleme özelliğini etkinleştirmek için:

1. Bir çalışma sayfasında başlık satırına tıklayın.
1. **Veri** menüsünden **Filtre** seçin ve ardından **Otomatik Filtre**'yi seçin.

Bir çalışma sayfasına otomatik filtre uyguladığınızda, filtre anahtarları (siyah oklar) sütun başlıklarının sağında görünür.

1. Bir filtre okuna tıklayarak filtre seçeneklerinin listesini görüntüleyin.

Otomatik filtre seçeneklerinden bazıları:

|**Seçenekler**|**Açıklama**|
| :- | :- |
|All|Listedeki tüm öğeleri bir kez gösterir.
|Custom|İçerir/içermez gibi özel filtre kriterleri
|Filter by Color|Dolgu rengine göre filtreleme
|Date Filters|Tarihe göre farklı kriterlere dayalı filtreleme
|Number Filters|Karşılaştırma, ortalama ve En Üst 10 vb. gibi sayılar üzerinde farklı filtre türleri.
|Text Filters|Başlangıç, son, içerir vb. gibi farklı filtreler
|Blanks/Non Blanks|Bu filtreler Metin Filtre Boş üzerinden uygulanabilir

Kullanıcılar, Microsoft Excel'de bu seçenekleri kullanarak çalışma sayfalarındaki verileri manuel olarak filtreler.

### **Aspose.Cells ile Autofilter**

Aspose.Cells, Excel dosyasını temsil eden `Workbook` adlı bir sınıf sağlar. `Workbook` sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan `Worksheets` koleksiyonunu içerir.

Bir çalışma sayfası, `Worksheet` sınıfı ile temsil edilir. `Worksheet` sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Otomatik filtre oluşturmak için `Worksheet` sınıfının `AutoFilter` özelliği kullanılır. `AutoFilter` özelliği, başlık satırını oluşturan hücrelerin aralığını belirlemek için `Range` özelliği sağlayan `AutoFilter` sınıfının bir nesnesidir. Bir otomatik filtre, başlık satırını içeren hücre aralığına uygulanır.

Her çalışma sayfasında, sadece bir filtre aralığı belirtebilirsiniz. Bu, Microsoft Excel tarafından sınırlandırılmıştır. Özelleştirilmiş veri filtreleme için `AutoFilter.Custom` yöntemi kullanılır.

Aşağıdaki örnekte, Yukarıdaki bölümde Microsoft Excel kullanarak oluşturulan AutoFilter'ı Aspose.Cells kullanarak oluşturduk.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Farklı Türlerde Filtre**

Aspose.Cells, Renk Filtresi, Tarih Filtresi, Sayı Filtresi, Metin Filtresi, Boş Filtreler ve Dolu Filtreler gibi farklı filtre türleri uygulamak için birden fazla seçenek sağlar.

##### **Dolgu Rengi**

Aspose.Cells, hücrelerin dolgu rengi özelliğine göre veri filtrelemek için `AddFillColorFilter` fonksiyonunu sağlar. Aşağıda verilen örnekte, sayfa ilk sütununda farklı dolgu renkleri olan bir şablon dosya kullanılarak renk filtresi testi yapılmıştır. Örnek dosyalar aşağıdaki bağlantılardan indirilebilir.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Tarih**

Farklı tarih filtreleri uygulanabilir, örneğin, Ocak 2018 tarihlerini içeren tüm satırları filtrelemek gibi. Aşağıdaki örnek kod bu filtreyi `AddDateFilter` fonksiyonunu kullanarak gösterir. Örnek dosyalar aşağıda verilmiştir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Dinamik Tarih**

Bazen, tarihe göre dinamik filtreler gereklidir, örneğin, yıl farketmeksizin Ocak ayındaki tüm hücreleri filtrelemek. Bu durumda `DynamicFilter` fonksiyonu kullanılır; aşağıdaki örnekte gösterilmiştir. Örnek dosyalar aşağıda verilmiştir.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Sayı**

Aspose.Cells kullanarak özelleştirilmiş filtreler uygulanabilir, örneğin, belirli bir aralıktaki sayıları içeren hücreleri seçmek. Aşağıdaki örnek, sayıları filtrelemek için `Custom()` fonksiyonunun kullanımını gösterir. Örnek dosyalar aşağıda ayrıntılıdır.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Metin**

Bir sütun metin içeriyorsa ve belirli bir metni içeren hücreler seçilmek isteniyorsa, `Filter()` fonksiyonu kullanılabilir. Aşağıdaki örnekte, şablon dosyasında ülkelerin listesi vardır ve belirli ülke adını içeren satır seçilir. Metin filtreleme gösterilmektedir. Örnek dosyalar aşağıda verilmiştir.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Boşluklar**

Bir sütun metin içeriyorsa ve birkaç hücre boşsa ve sadece boş hücreler içeren satırların seçilmesi gerekiyorsa, `MatchBlanks()` fonksiyonu kullanılabilir, aşağıda gösterildiği gibi. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBos.xlsx](72417325.xlsx)

```c++
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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Boş Olmayanlar**

Metin içeren hücreleri filtrelemek istiyorsanız, `MatchNonBlanks` filtresi kullanılabilir, aşağıda gösterilmiştir. Örnek dosyalar aşağıda verilmiştir.

1. [Boş.xlsx](72417324.xlsx)
1. [FiltreliBosOlmayan.xlsx](72417326.xlsx)

```c++
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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Contains ile Özel filtre**

Excel, bazı belirli dizeleri içeren satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir. Örnek dosyalar aşağıda verilmiştir

1. [sourseOrnekUlkeIsimleri.xlsx](sourseOrnekUlkeIsimleri.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Contains Kullanmadan Özel filtre**

Excel, belirli bir dizeyi içermeyen satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Belirli bir dizeyle Başlayan Özel Filtre**

Excel, belirli bir dizeyle başlayan satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Belirli Bir Dize ile Biten Özel Filtre**

Excel, belirli bir dizeyle biten satırları filtrelemek gibi özel filtreler sunar. Bu özellik Aspose.Cells'te mevcuttur ve aşağıda örnek dosyadaki isimleri filtreleyerek gösterilmiştir.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın](/cells/tr/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın](/cells/tr/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
