---
title: C++ ile hücre formatını değiştir
linktitle: Bir hücrenin biçimini değiştirme
description: C++ kullanarak Aspose.Cells kütüphanesi ile hücrelerin biçimini değiştirme, font, renk, sınır vb. özellikleri ayarlayarak hücrelerin görünümünü ve nasıl göründüğünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, hücre biçimlendirme, C++, font, renk, sınır
type: docs
weight: 20
url: /tr/cpp/how-to-change-format-of-cell/
---

## **Olası Kullanım Senaryoları**
Belirli verileri vurgulamak istediğinizde, hücrelerin stiline değişiklik yapabilirsiniz.

## **Excel'de bir hücrenin biçimini nasıl değiştirilir**

Excel'de bir tek hücrenin biçimini değiştirmek için şu adımları izleyin:

1. Excel'i açın ve biçimini değiştirmek istediğiniz hücreyi içeren çalışma kitabını açın.

2. Biçimini değiştirmek istediğiniz hücreyi bulun.

3. Hücreye sağ tıklayın ve bağlam menüsünden "Hücre Biçimlendir" seçeneğini seçin. Alternatif olarak, hücreyi seçebilir ve Excel şeridindeki Anahtar sekmesine giderek "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayıp "Hücre Biçimleri"ni seçebilirsiniz.

4. "Hücre Biçimleri" iletişim kutusu görünecektir. Burada, seçilen hücreye uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stilini, yazı tipi boyutunu, yazı tipi rengini, sayı biçimini, sınırları, arka plan rengini vs. değiştirebilirsiniz. Farklı sekmele
rin iletişim kutusunda çeşitli biçimlendirme seçeneklerine erişmek için keşfedin.

5. İstenen biçimlendirme değişiklikleri yapıldıktan sonra, seçilen hücreye biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.

## **C++ kullanarak hücre formatını nasıl değiştirilir**

Aspose.Cells kullanarak hücre biçimlendirmesini değiştirmek için aşağıdaki yöntemleri kullanabilirsiniz:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)

## **Örnek Kod**
Bu örnekte, bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışsayıya erişiyoruz ve iki hücreye("A2" ve "B3") ulaşıyoruz. Daha sonra, hücrenin stili alınıyor, çeşitli biçimlendirme seçenekleri belirleniyor (örneğin, yazı rengi, kalın), ve hücrenin formatı değiştiriliyor. Son olarak, çalışma kitabı yeni bir dosyaya kaydediliyor.
![todo:image_alt_text](change-format.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
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
    Cell a2 = worksheet.GetCells().Get(u"A2");
    Style style = a2.GetStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFontColor(true);
    a2.SetStyle(style, flag);

    Cell b3 = worksheet.GetCells().Get(u"B3");
    Style style2 = b3.GetStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    b3.SetStyle(style2);

    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
}
```
