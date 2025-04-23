---
title: Excel Çalışsayfasının panolarını dondurun
linktitle: Pano Dondur
type: docs
weight: 190
url: /tr/python-net/how-to-freeze-panes-of-excel-worksheet
description: Bu makalede, Aspose.Cells for Python via .NET API lerini kullanarak Excel Çalışma Sayfalarının bölmelerini programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python da Bölme Dondurma, Python da pencereyi dondurma.
---

## **Giriş**

Bu makalede, Pencereleri Nasıl Sabitleyeceğimizi öğreneceğiz. Ortak bir başlık altında büyük miktarda veri olduğunda, çalışma sayfasını aşağı kaydırdığınızda başlığı göremezsiniz. Her kayıtta çok veri bulunmaktadır. Panoları dondurarak, geri kalan veriler kaydırıldığında bile donmuş kısmı görebilirsiniz. Başlık satırlarını veya ilk sütunları kolayca görebilirsiniz. Panoları dondurup serbest bırakmak, verinin görünümünü değiştirirken veriyi değiştirmemektedir.

## ***Excel'de Bölmeleri Nasıl Dondurulur**

**![Excel'de Panoları Dondur](Freeze-panes.png)**


1. Eğer panoları, satırları ve sütunları dondurmak istiyorsanız, önce bir hücre seçin (örneğin B2)
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Panoları Dondur'a tıklayın.
4. Aşağı veya sağa kaydırırsanız, ilk satır ve sütun donar.

**![Panoları Dondurma](Frozen-Panes.png)**

Görüldüğü gibi 1. Satır ve A sütunu donmuş durumda, ikinci satır 32 ve ikinci görünür sütun D.'dir. 

Panoları dondurarak büyük verilerinizi kolayca görüntülemenize olanak tanır, Satır veya Sütun etiketlerinin izlenmesi gereksiz hale gelir.




## **Aspose.Cells for Python Excel Kütüphanesi ile Bölmeleri Nasıl Dondurulur**
Aspose.Cells for Python via .NET ile bölmeleri dondurmak oldukça basittir. Seçilen hücrede bölme yapmak için [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) metodunu kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemi ile panoları dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
