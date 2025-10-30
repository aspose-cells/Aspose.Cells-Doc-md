---
title: Gelişmiş Güvenlik Ayarları Excel XP den itibaren C++ ile
linktitle: Excel XP den beri Gelişmiş Koruma Ayarları
type: docs
weight: 30
url: /tr/cpp/advanced-protection-settings-since-excel-xp/
description: Aspose.Cells kullanarak Excel dosyalarında gelişmiş koruma ayarlarını nasıl uygulayacağınızı öğrenin.
---

{{% alert color="primary" %}}

2002 veya XP sürümüyle birlikte, Microsoft birçok gelişmiş koruma ayarı eklemiştir.

{{% /alert %}}

## **Giriş**

Bu koruma ayarları, kullanıcıların aşağıdakileri kısıtlamasına veya izin vermesini sağlar:

- Satırları veya sütunları sil.
- İçeriği, nesneleri veya senaryoları düzenle.
- Hücreleri, satırları veya sütunları biçimlendir.
- Satırları, sütunları veya köprüleri ekle.
- Kilitli veya kilitsiz hücreleri seç.
- Özet tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP veya sonraki sürümlerinin sunduğu tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

1. **Araçlar** menüsünden **Koruma** ve ardından **Çalışma Sayfası Koru** seçin. Bir iletişim kutusu görüntülenecektir.

Excel 2016'daki koruma ayarlarını görüntülemek için:

1. **Dosya** menüsünden **Çalışma Kitabını Koru** ve ardından **Mevcut Sayfayı Koru** seçin.
1. **İncele** menüsünde **Çalışma Sayfası Koru** seçin.

Yukarıdaki adımları takip etmek, çalışma sayfasında özellikleri izin verme veya kısıtlama ya da parola uygulama diyaloğunu gösterecektir.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim izni veren bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) özelliğini sağlar. Aslında, [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) özelliği, engelleme veya kısıtlamaları etkinleştirmek veya devre dışı bırakmak için birkaç Boolean özelliği kapsayan [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) sınıfından bir nesnedir.

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Lütfen [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) özelliğini kullanırken [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) metodunu çağırmayın. Ayrıca, dosyayı Excel97'den 2003'e veya Xlsx formatında kaydedin çünkü gelişmiş koruma ayarları yalnızca Excel XP ve daha yeni sürümler tarafından desteklenir.

{{% /alert %}}

### **Hücre Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini engellemek istiyorsanız, hücreler herhangi bir koruma ayarı uygulanmadan önce kilitlenmiş olmalıdır. Aksi takdirde, çalışma sayfası korunsa bile hücreler düzenlenebilir. Microsoft Excel XP'de hücreler aşağıdaki iletişim kutusu aracılığıyla kilitlenebilir:

|**Excel XP'de Hücreleri Kilitlme İletişim Kutusu**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells API kullanarak da hücreler kilitlenebilir. Her hücre, [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) biçimlendirmeyi alan ve bir Boolean özellik [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) içeren [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) özelliğine sahip olabilir. Hücreyi kilitlemek veya kilidini açmak için [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) özelliğini **doğru** veya **yanlış** olarak ayarlayın.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
