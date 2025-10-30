---
title: C++ ile Çalışma Sayfalarını Koruma
linktitle: Çalışma Sayfalarını Koruma
type: docs
weight: 10
url: /tr/cpp/protecting-worksheets/
description: Aspose.Cells kullanarak Microsoft Excel dosyalarında çalışma sayfalarını, satırları, sütunları ve belirli hücreleri nasıl koruyacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bir çalışma sayfası korunduğunda, bir kullanıcının yapabileceği işlemler kısıtlanır. Örneğin, veri girişi yapamazlar, satır veya sütun ekleyip silemezler, vb.

{{% /alert %}}

## **Çalışma Sayfalarını Koruma**

### **Giriş**

Microsoft Excel'de genel koruma seçenekleri:

- İçerik
- Nesneler
- Senaryolar

Korunan çalışma sayfaları hassas verileri gizlemez veya korumaz, bu nedenle dosya şifrelemesinden farklıdır. Genellikle, çalışma sayfası koruması sunumsal amaçlar için uygundur. Kullanıcının çalışma sayfasındaki veri, içerik ve biçimlendirmeyi değiştirmesini önler.

### **Bir Çalışma Sayfasını Koruma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfasına koruma uygulamak için kullanılan [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) yöntemini sağlar. [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) yöntemi aşağıdaki parametreleri kabul eder:

- Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü, [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) numaralandırma yardımıyla uygulanır.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Parola, çalışma sayfası zaten parola korumalıysa eski paroladır. Çalışma sayfası zaten korunmamışsa sadece null geçirin.

[**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) numaralandırma, aşağıdaki önceden tanımlanmış koruma türlerini içerir:

|**Koruma Türleri**|**Açıklama**|
| :- | :- |
|All|Kullanıcı bu çalışma sayfasında herhangi bir şeyi değiştiremez|
|Contents|Kullanıcı bu çalışma sayfasında veri giremez|
|Objects|Kullanıcı çizim nesnelerini değiştiremez|
|Scenarios|Kullanıcı, kaydedilmiş senaryoları değiştiremez|
|Structure|Kullanıcı yapıyı değiştiremez|
|Windows|Koruma, pencerelere uygulanır|
|None|Koruma uygulanmaz|

Aşağıdaki örnek, bir çalışma sayfasını bir şifre ile korumanın nasıl yapıldığını göstermektedir.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Yukarıdaki kod çalışma sayfasını korumak için kullanıldıktan sonra, çalışma sayfasının korumasını açarak kontrol edebilirsiniz. Dosyayı açtığınızda çalışma sayfasına bazı veriler eklemeye çalıştığınızda aşağıdaki iletişim kutusunu göreceksiniz:

|**Kullanıcının çalışma sayfasını değiştiremeyeceği konusunda uyarı veren iletişim kutusu**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Çalışma sayfasında çalışmak için **Koruma**, ardından **Sayfayı Korumayı Kaldır** öğesini **Araçlar** menü öğesinden seçerek çalışma sayfasının korumasını kaldırın.

**Sayfayı Korumayı Kaldır** menü öğesini seçtikten sonra, bir iletişim kutusu açılacaktır ve size çalışma sayfasında çalışmanız için şifreyi girmenizi isteyecektir, aşağıda gösterildiği gibi:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excel Kullanarak Çalışma Sayfasındaki Birkaç Hücreyi Koruma**

Çalışma sayfasında sadece birkaç hücreyi kilitlemeniz gereken belirli senaryolar olabilir. Çalışma sayfasında belirli hücreleri kilitlemek istiyorsanız, çalışma sayfasındaki tüm diğer hücreleri kilitlemeniz gerekir. Bir çalışma sayfasındaki tüm hücreler zaten kilitlemek için başlatılmış durumda, bunu MS Excel'e herhangi bir Excel dosyasını açarak kontrol edebilir ve **Biçim | Hücreler...**'e tıklayarak **Hücreleri Biçimlendir** iletişim kutusunu gösterin ve sonra **Koruma** sekmesine tıklayarak "Kilitli" olarak adlandırılan bir onay kutusunun varsayılan olarak işaretlenip işaretlenmediğini kontrol edebilirsiniz.

MS Excel kullanarak birkaç hücreyi kilitlemenin aşağıdaki adımları açıklar. Bu yöntem, Microsoft Office Excel 97, 2000, 2002, 2003 ve daha yüksek sürümlerine uygulanır.

1. Satır numarası için doğrudan üzerindeki gri dikdörtgen (satır 1'in hemen üstündeki ve A sütun harfinin solundaki). **Tümünü Seç** düğmesine tıklayarak tüm çalışma sayfasını seçin.
1. **Biçim** menüsünde **Hücreler**'e tıklayın, **Koruma** sekmesine tıklayın ve sonra **Kilitli** onay kutusunu kaldırın.
   Bu, çalışma sayfasındaki tüm hücreleri kilidini açar.
   **Hücreler** komutu kullanılamıyorsa, çalışma sayfasının bazı bölümleri zaten kilitli olabilir. **Araçlar** menüsünde **Koruma**'ya gelin ve ardından **Sayfayı Korumayı Kaldır**'a tıklayın.
1. Kilitlemek istediğiniz hücreleri seçin ve adım 2'yi tekrarlayın, ancak bu sefer **Kilitli** onay kutusunu işaretleyin.
1. **Araçlar** menüsünde **Koruma**'ya gelin, **Sayfayı Koruma**'yı tıklayın ve ardından **Tamam**'ı tıklayın.
1. **Sayfayı Koruma** iletişim kutusunda, kullanıcıların değiştirebileceği öğeleri belirleme seçeneğine sahip olacaksınız.

### **Aspose Cells Kullanarak Çalışma Sayfasındaki Birkaç Hücreyi Korumak**

Bu yöntemde, yalnızca görevi gerçekleştirmek için Aspose.Cells API kullanıyoruz.

Örnek: Aşağıdaki örnek, çalışma sayfasındaki birkaç hücreyi nasıl koruyacağını göstermektedir. İlk olarak çalışma sayfasındaki tüm hücreleri kilidini açar ve ardından (A1, B1, C1) 3 hücreyi kilitleyerek korur. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi, bir boolean özelliğini, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) adlı bir özellik içerir. *Column/Row.ApplyStyle()* yöntemini kullanarak satır/sütunun kilidini açmak veya kilitlemek için [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) özelliğini true ya da false olarak ayarlayabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Çalışma Sayfasında Bir Satırı Koruma**

Aspose.Cells, çalışma sayfasındaki herhangi bir satırı kolayca kilitlemenize olanak tanır. Burada, çalışma sayfasındaki belirli bir satıra uygulamak için [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) sınıfının [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) yöntemini kullanabiliriz. Bu yöntem, uygulanan biçimlendirme ile ilgili tüm üyelere sahip olan bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi ve bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi olmak üzere iki argüman alır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırı nasıl koruyacağını göstermektedir. İlk olarak, çalışma sayfasındaki tüm hücreleri kilidini açar ve ardından ilk satırı kilitleyerek korur. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi, bir [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) adlı bir özellik içerir. Satır/sütunun kilidini açmak veya kilitlemek için [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) özelliğini true ya da false olarak ayarlayabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Çalışma Sayfasında Bir Sütunu Koruma**

Aspose.Cells, çalışma sayfasındaki herhangi bir sütunu kolayca kilitlemenize olanak tanır. Burada, çalışma sayfasındaki belirli bir sütuna uygulamak için [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) sınıfının [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) yöntemini kullanabiliriz. Bu yöntem, uygulanan biçimlendirme ile ilgili tüm üyelere sahip olan bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi ve bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi olmak üzere iki argüman alır.

Aşağıdaki örnek, çalışma sayfasındaki bir sütunu nasıl koruyacağını göstermektedir. İlk olarak, çalışma sayfasındaki tüm hücreleri kilidini açar ve ardından ilk sütunu kilitleyerek korur. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi, bir [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) adlı bir özelliğe sahiptir. Satır/sütunun kilidini açmak veya kilitlemek için [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) özelliğini true ya da false olarak ayarlayabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Kullanıcılara Düzenleme Aralığı Izin Ver**

Aşağıdaki örnek, korunan bir çalışma sayfasında kullanıcılara bir aralığı düzenleme izni vermenin nasıl yapıldığını göstermektedir.

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
