---
title: Excel Çalışma Sayfasının Üst Satır(larını) Sabitle
linktitle: Satırları Sabitle
type: docs
weight: 190
url: /tr/python-net/how-to-freeze-rows-of-excel-worksheet
description: Bu makalede, Aspose.Cells for Python via .NET API lerini kullanarak Excel Çalışma Sayfalarının üst satırlarını programlı olarak nasıl donduracağınızı öğrenin.
keywords: Python Excel Kütüphanesi, Python Üst Satırları Dondur, Python Üst Satırları Dondur.
---

## **Giriş**

Bu makalede, üst satır(ları) dondurmayı nasıl yapacağımızı öğreneceğiz. Ortak bir başlık altında büyük miktarda veri olduğunda sayfayı çalışma sayfasında yukarı kaydırdığınızda başlığı göremeyebilirsiniz. Üst satır(ları) dondurarak, geri kalan veriler kaydırılsa bile donmuş kısmı görebilirsiniz. Üst satırlardaki başlıkları kolayca görebilirsiniz.

## **Excel'de Satırları Nasıl Dondurulur**

![Excel'de üst satır(ları) dondur](Freeze-Rows.png)


1. Eğer üst satır(ları) dondurmak istiyorsanız, ilk önce dondurulması gereken satırın altındaki satırı seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Üst Satırı Dondur'a tıklayın.
4. Aşağı doğru kaydırdığınızda, ilk satır her zaman üst görünüme sahip olacaktır.

![Satırı Dondur](Frozen-Row.png)

Görüldüğü gibi 1. Satır donmuş durumda, aşağı kaydırsanız bile ilk satır her zaman üst görünümde kalır.

Satırları Dondurarak büyük verilerinizi satır etiketleriyle uğraşmadan görüntülemenize olanak tanır.




## **Aspose.Cells for Python Excel Kütüphanesi ile Satırları Nasıl Dondurulur**
Aspose.Cells for Python via .NET kullanarak satırları dondurmak çok basittir. Seçilen satırda satırı dondurmak için [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) yöntemini kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemi ile ilk satırı dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Row.py" >}}

Ekli [örnek kaynak Excel dosyası](../Freeze.xlsx).
{{< app/cells/assistant language="python-net" >}}
