---
title: Excel Çalışma Sayfasının İlk Sütunlarını Sabitle
linktitle: Sütunları Sabitle
type: docs
weight: 190
url: /tr/python-net/how-to-freeze-columns-of-excel-worksheet
description: Bu makalede, Aspose.Cells for Python via .NET API lerini kullanarak Excel Çalışma Sayfalarının sol sütunlarını programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python Sol Sütunları Dondur, Python İlk Sütunları Dondur, Python Sütunlarını Kilitle.
---

## **Giriş**

Bu makalede, sol sütun(lar) dondurmayı nasıl yapacağımızı öğreneceğiz. Bir satırda büyük miktarda veri olduğunda, sayfayı yatay olarak kaydırdığınızda sol sütunları göremeyebilirsiniz. İlk sütun(ları) dondurup kilitleyerek, geri kalan veriler kaydırılsa bile donmuş kısmı görebilirsiniz. Sol sütunlardaki başlıkları kolayca görebilirsiniz.


## **Excel'de Sütunları Nasıl Dondurulur**

**![Excel'de sol sütunları sabitle](freeze-columns.png)**


1. Sol sütunları sabitlemek istiyorsanız, öncelikle sabitlenecek sütunun altındaki sütunu seçin
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden İlk Sütunu Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk sütun her zaman sol görünümde olacaktır.

**![Sürekli sütun](frozen-columns.png)**

Görüldüğü gibi 1. sütun donmuş durumda, yatay kaydırdığınızda ilk sütun her zaman görünümün üstünde sabitlenir.

Sütunları Sabitlemek, ilk sütunu izlemek zorunda kalmadan uzun verilerinizi görüntülemenize olanak tanır.




## **Aspose.Cells for Python Excel Kütüphanesi ile Sütunları Nasıl Dondurulur**
Aspose.Cells for Python via .NET kullanarak ilk sütun(ları) dondurmak çok basittir. Seçilen sütunu dondurmak için [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) yöntemini kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemi ile ilk sütunu dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
