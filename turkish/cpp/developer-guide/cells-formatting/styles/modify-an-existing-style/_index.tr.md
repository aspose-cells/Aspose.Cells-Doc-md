---
title: C++ ile Mevcut Stili Değiştiriniz
description: Aspose.Cells, kullanıcıların mevcut hücre stillerini değiştirmelerine olanak tanıyan, elektronik tablo dosyalarıyla çalışmak için C++ kütüphanesidir. Bu makale, kullanıcıların hücrelerin görünümünü ihtiyaçlarına göre değiştirebilmeleri için Aspose.Cells kütüphanesi ile mevcut hücre stilini nasıl değiştireceklerini tanıtacaktır.
keywords: Mevcut stilleri değiştirin, uygulamanın görünümünü özelleştirin, kılavuzlar, öğreticiler, yardım belgeleri, geliştirme belgeleri, API referansları, örnek kodlar, indirmeler, destek.
type: docs
weight: 90
url: /tr/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Aynı biçimlendirme seçeneklerini hücrelere uygulamak için yeni bir biçimlendirme stili nesnesi oluşturun. Bir biçimlendirme stili nesnesi, yazı tipi, yazı tipi boyutu, girinti, sayı, kenar, desen vb. gibi biçimlendirme özelliklerinin bir kombinasyonudur, adlandırılır ve bir küme olarak saklanır. Uygulandığında, bu stildeki tüm biçimlendirme uygulanır.

Ayrıca, mevcut bir stili kullanabilir, onu çalışma kitabıyla kaydedebilir ve aynı özelliklere sahip bilgiyi biçimlendirmek için kullanabilirsiniz.

Hücreler açıkça biçimlendirilmediğinde, **Normal** stili (çalışma kitabının varsayılan stili) uygulanır. Microsoft Excel, Comma, Currency ve Percent dahil olmak üzere birkaç önceden tanımlanmış stile ek olarak Normal stili de tanımlar.

Aspose.Cells, bu stillerin herhangi birini veya kendi istediğiniz özelliklere sahip herhangi bir stilini değiştirmenize olanak tanır.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel 97-2003'te bir stil güncellemek için:

1. **Format** menüsünde **Stil**'e tıklayın.
1. Değiştirmek istediğiniz stili **Stil adı** listesinden seçin.
1. **Değiştir**'e tıklayın.
1. Biçim Hücreleri iletişim kutusundaki sekmeleri kullanarak istediğiniz stil seçeneklerini seçin.
1. **Tamam**'a tıklayın.
1. **Stil içerir** altında istediğiniz stil özelliklerini belirtin.
1. Kaydetmek ve seçili aralığa uygulamak için **Tamam**'a tıklayın.

## **Aspose.Cells Kullanımı**

Aşağıdaki örnekler [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/) metodunun nasıl kullanılacağını gösterir.

### **Stil Oluşturma ve Değiştirme**

Bu örnek, bir [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesi oluşturur, onu bir hücre aralığına uygular ve [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) nesnesini değiştirir. Yapılan değişiklikler, otomatik olarak hücreye ve stilin uygulandığı aralığa yansıtılır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Mevcut Bir Stili Değiştirmek**

Bu örnek, zaten bir diziye uygulanmış olan bir stil olan Yüzde'nin bulunduğu basit bir şablon Excel dosyasını kullanır. Örnek:

1. İlgili stili alır,
1. Stil nesnesi oluşturur ve
1. Stil biçimlendirmesini değiştirir.

Değişiklikler otomatik olarak uygulanan aralığa uygulanır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
