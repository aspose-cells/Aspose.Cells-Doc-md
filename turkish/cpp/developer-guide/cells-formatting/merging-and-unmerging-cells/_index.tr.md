---
title: Hücreleri Birleştirme ve Çözme ile C++
linktitle: Hücreleri Birleştirme ve Ayırma
description: Aspose.Cells, hücreleri birleştirmeyi ve çözmeyi destekleyen C++ için bir kütüphanedir. Bu makale, Aspose.Cells kütüphanesi kullanarak hücreleri nasıl birleştirip çözeceğinizi ve birleştirilen hücre stilini nasıl özelleştireceğinizi anlatacaktır.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, hücreleri birleştir, hücreleri çöz, stil ayarları, özel stiller
type: docs
weight: 190
url: /tr/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells, bu özelliği destekler ve çalışsheet'lerde hücreleri birleştirebilir. Birleştirilmiş hücreleri de ayırabilir veya bölebilirsiniz. Birleştirilmiş bir hücrenin hücre referansı, orijinal seçilen aralıktaki sol üst hücrenin referansıdır.

{{% /alert %}} 

## **Giriş**
Her zaman her satır veya sütunda aynı hücre sayısını istemezsiniz. Örneğin, birkaç sütunu kapsayan bir hücreye başlık koymak isteyebilirsiniz. Veya, bir fatura oluştururken toplam için daha az sütun isteyebilirsiniz. İki veya daha fazla hücreden bir hücre yapmak için hücreleri birleştirin. Microsoft Excel, kullanıcılara dosyaları seçme ve istedikleri şekilde elektronik tabloyu yapılandırmak için birleştirmelerine izin verir.

{{% alert color="primary" %}} 

Hücreler birleştirildiğinde, aralıktaki sol üst hücredeki veriler yalnızca korunur. Aralıktaki diğer hücrelerde veri varsa, bu veri silinir.
Benzer şekilde, biçimlendirme, birleştirme hücresinin referans hücresine dayalı olduğundan, hücreleri birleştirdiğinizde, aralıktaki sol üst hücrenin biçimlendirme ayarları birleştirilmiş hücreye uygulanır. Hücre bölündüğünde, yeni hücreler özgün biçim ayarlarını korur.

{{% /alert %}} 

## **Çalışsheet'te Hücreleri Birleştirme**
### **Microsoft Excel'de Hücreleri Birleştirme**
Aşağıdaki adımlar, MS Excel kullanarak çalışsheet'te hücreleri birleştirmeyi açıklar.

1. İstenen veriyi aralıktaki en sol üst hücreye kopyalayın.
2. Birleştirmek istediğiniz hücreleri seçin.
3. Bir satır veya sütunda hücreleri birleştirmek ve hücre içeriğini ortalamak için, **Biçimlendirme** araç çubuğundaki **Birleştir ve Ortala** simgesine tıklayın.

### **Aspose.Cells ile Hücreleri Birleştirmek**
`Aspose::Cells::Cells` sınıfı, bu görev için kullanışlı bazı yöntemler içerir. Örneğin, `Merge()` yöntemi, hücreleri belirli bir aralık içinde tek bir hücreye birleştirir.

Aşağıdaki örnek, bir çalışsheet'te (C6:E7) hücrelerin nasıl birleştirileceğini göstermektedir.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Hücreleri Ayırma (Birleştirmeyi Bölmek)**
### **Microsoft Excel Kullanımı**
Aşağıdaki adımlar, Microsoft Excel kullanarak birleştirilmiş hücreleri nasıl ayıracağınızı açıklar.

1. Birleştirilmiş hücreyi seçin.
   Hücreler birleştirildiğinde, **Birleştir ve Ortala**, **Biçimlendirme** araç çubuğunda seçilidir.
1. **Biçimlendirme** araç çubuğunda **Birleştir ve Ortala**'ya tıklayın.

### **Aspose.Cells Kullanımı**
`Aspose::Cells::Cells` sınıfında, hücreleri başlangıç durumuna döndürmek için `UnMerge()` adında bir yöntem vardır. Bu, hücreleri, birleştirildiği hücre referansını kullanarak ayırır.

Aşağıdaki örnek, birleştirilmiş hücreleri (C6) nasıl ayıracağınızı göstermektedir. Örnek, önceki örnekte oluşturulan dosyayı kullanır ve birleştirilmiş hücreleri ayırır.

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
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Çalışsheet'teki Birleştirilmiş Hücreleri Bulma](/cells/tr/cpp/detect-merged-cells-in-a-worksheet/)
