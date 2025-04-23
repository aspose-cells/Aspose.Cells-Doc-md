---
title: Hücre Yazısını C++ ile Döndürme Yöntemi
linktitle: Hücrenin metnini Nasıl Döndürülür
type: docs
weight: 80
url: /tr/cpp/how-to-rotate-text-of-cell/
description: C++ kodu ile Aspose.Cells for C++ API kullanarak Hücre yazısını döndürme
keywords: c++ ile Hücre yazısını döndürme, C++ ile çalışma kitabında hücreyi programlı olarak döndürme, çalışma kitabında hücre döndürme açısını programlı ayarlama, excel de Hücre yazısını C++ ile nasıl döndürülür
---

## **Aspose.Cells'te Hücrenin Metnini Döndür**

Aspose.Cells, programcıların Excel elektronik tabloları ile programlı olarak çalışmasına olanak sağlayan güçlü bir C++ bileşenidir. Aspose.Cells'in sunduğu özelliklerden biri, hücreleri döndürme yeteneğidir; bu, yazı yönünü özelleştirmenize ve verilerinizin görsel sunumunu geliştirmeye yardımcı olur. Bu belgede, Aspose.Cells kullanarak hücreleri nasıl döndüreceğinizi keşfedeceğiz.

## **Excel'de Hücrenin Metnini Döndürme**
Bir hücreyi Excel'de döndürmek için aşağıdaki adımları kullanabilirsiniz:
1. Excel'i açın ve döndürmek istediğiniz hücreyi veya hücre aralığını seçin.
1. Seçilen hücre(ler)e sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir"'i seçin. Alternatif olarak, Excel şeridinde "Ana Sayfa" sekmesine gidip "Hücreler" grubundaki "Biçimlamanın" açılır menüsüne tıklayıp "Hücreleri Biçimlendir"'i seçebilirsiniz.
1. "Hücreleri Biçimlendir" iletişim kutusunda, "Hizalama" sekmesine gidin.
1. "Yönlendirme" bölümünde, metni döndürebileceğiniz seçenekleri göreceksiniz. "Derece" kutusuna istenen dönme açısını doğrudan girebilirsiniz. Pozitif değerler metni saat yönünün tersine döndürür, negatif değerler ise saat yönünde döndürür.
<br>
![todo:image_alt_text](alignment.png)
1. İstenilen yönlendirmeyi seçtikten sonra, değişiklikleri uygulamak için "Tamam"'a tıklayın. Seçilen hücre(ler) artık seçtiğiniz dönme açısına veya yönlendirmeye göre dönecektir.

## **Aspose.Cells API kullanarak Hücrenin Metnini Döndürme**

[**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) özelliği hücreleri döndürmeyi kolaylaştırır. Aspose.Cells'te hücreleri döndürmek için şu adımları izlemeniz gerekir:
1. Excel Çalışma Kitabını Yükle
<br>
İlk olarak, mevcut bir Excel dosyasını açmak veya yeni bir tane oluşturmak için Workbook sınıfını kullanarak Excel çalışma kitabını yüklemeniz gerekir. 

1. Çalışma Sayfasına Eriş
<br>
Çalışma kitabı yüklendikten sonra, hücreleri döndürmek istediğiniz çalışma sayfasına erişmeniz gerekir. Çalışma sayfasına endeksine veya adına göre erişebilirsiniz. 

1. Hücrenin metnini döndür
<br>
Artık çalışma sayfasına erişiminiz olduğuna göre, istenen hücrelerin Stil objesini değiştirerek hücreleri döndürebilirsiniz. Stil objesi, dönme dahil çeşitli biçimlendirme seçeneklerini belirlemenizi sağlar. 

1. Çalışma Kitabını Kaydet
<br>
Hücreleri döndürdükten sonra, değiştirilmiş çalışma kitabını Save metodunu kullanarak bir dosyaya veya akıma geri kaydedebilirsiniz.

## **C++ Örnek Kodu**

Lütfen aşağıdaki kodu inceleyin, bir çalışma kitabı nesnesi oluşturur ve çeşitli hücreler için farklı döndürme açıları belirler. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra elde edilen sonucu gösterir.
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
