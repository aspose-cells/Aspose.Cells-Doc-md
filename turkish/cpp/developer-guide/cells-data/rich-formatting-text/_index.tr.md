---
title: C++ ile Hücrelerin Zengin Metin Bölümlerine Erişim ve Güncelleme
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aspose.Cells for C++ API kullanarak Hücrenin Zengin Metin bölümlerine Erişim ve Güncelleme nasıl yapılır öğrenin.
keywords: Hücrenin zengin metin bölümlerine erişme ve güncelleme, Hücrenin zengin metnini alma, Hücrenin zengin metnini düzenleme, Hücrenin zengin metnine erişme, Hücrenin zengin metnini güncelleme, Hücrenin zengin metnini değiştirme
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin zengin metin bölümlerine erişmenize ve güncellemenize izin verir. Bu amaçla, [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) ve [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) yöntemlerini kullanabilirsiniz. Bu yöntemler, font adı, font rengi, kalın olma gibi çeşitli özelliklere erişmek ve bunları güncellemek için kullanabileceğiniz [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) nesnesi dizisini döndürecek ve kabul edecektir.

{{% /alert %}}

## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**

Aşağıdaki kod, [kaynak excel dosyası](5112369.xlsx) kullanılarak [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) ve [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) metodlarının kullanımını gösterir. Kaynak excel dosyasında, hücre A1’de 3 bölümden oluşan ve her biri farklı bir fonta sahip zengin metin vardır. Kod bu bölümlere erişir ve ilk bölümün fontunu **"Arial"** olarak günceller. Değiştirilen çalışma kitabı [çıkış excel dosyasına](5112366.xlsx) kaydedilir.

### C++ ile zengin metin bölümlerine erişim ve güncelleme kodu

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Örnek kod tarafından oluşturulan konsol çıktısı

İşte [kaynak excel dosyası](5112369.xlsx) kullanıldığında konsol çıktısı:

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
