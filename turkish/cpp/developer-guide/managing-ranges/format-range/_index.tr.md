---
title: C++ ile Aralıkları Biçimlendirme
linktitle: Aralıkları Biçimlendir
type: docs
weight: 105
url: /tr/cpp/how-to-format-a-range/
description: Aspose.Cells kullanarak Excel de aralıkları nasıl biçimlendireceğinizi öğrenin. Hücre aralıklarına programlı olarak stil, yazı tipi ve renkleri uygulayın.
---

## **Olası Kullanım Senaryoları**
Bir aralığa stili uygulamanız gerektiğinde, aralık biçimlendirme kullanabilirsiniz.

## **Excel'de bir Aralığı Nasıl Biçimlendirirsiniz**

Excel'de bir aralığı biçimlendirmek için, Excel tarafından sağlanan yerleşik biçimlendirme seçeneklerini kullanabilirsiniz. İşte Excel'de bir aralığı doğrudan nasıl biçimlendireceğiniz:

1. Excel'i açın ve biçimlendirmek istediğiniz aralığı içeren çalışma kitabını açın.

2. Biçimlendirmek istediğiniz hücre aralığını seçin. Aralığı seçmek için tıklayıp sürükleyebilirsiniz veya Shift + Ok tuşları gibi klavye kısayollarını kullanarak seçimi genişletebilirsiniz.

3. Aralık seçildikten sonra, seçilen aralık üzerine sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir" öğesini seçin. Alternatif olarak, Excel şeridindeki Ana sekmesine giderek, "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayın ve "Hücreleri Biçimlendir" seçeneğini belirleyin.

4. "Hücreleri Biçimlendir" iletişim kutusu görünecektir. Burada, seçilen aralığa uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stili, yazı tipi boyutu, yazı tipi rengi, sayı formatı, kenarlıklar, arka plan rengi vb. değiştirebilirsiniz. Farklı sekmeleri keşfetmek için iletişim kutusundaki farklı sekmelere bakın.

5. İstenen biçimlendirme değişikliklerini yaptıktan sonra, seçilen aralığa biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.

## **C++ Kullanarak Aralık Nasıl Biçimlendirilir**

Bir aralığı biçimlendirmek için Aspose.Cells kullanırken aşağıdaki yöntemleri kullanabilirsiniz:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Örnek Kod**
Bu örnekte, bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık tanımlıyoruz ("A1:C3" ve "A4:C5"). Ardından yeni stiller oluşturuyor, çeşitli biçimlendirme seçenekleri ayarlıyor (örneğin, yazı tipi rengi, kalın) ve bunları aralığa uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
