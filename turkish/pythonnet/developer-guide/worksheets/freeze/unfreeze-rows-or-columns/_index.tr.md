---
title: Satırları veya Sütunları Dondurma
linktitle: Pencereleri dondur
type: docs
weight: 190
url: /tr/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, Aspose.Cells for Python via .NET API lerini kullanarak Excel İşsayfalarının satır, sütun veya panolarını programatik olarak nasıl serbest bırakacağınızı öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python Panoları Serbest Bırakma, Python Satırların Serbest Bırakılması, Python Sütunların Serbest Bırakılması, Python Pencereyi Nasıl Serbest Bırakılır.
---

## **Giriş**

Bu makalede, Satırları, Sütunları ve Bölmeleri Dondurmayı ve Dondurulmuş Durumu Kaldırmayı nasıl yapacağımızı öğreneceğiz. Excel dosyalarındaki çalışma sayfaları donmuşsa, bazen çalışma sayfasını dondurmak veya donmuş satırları, sütunları veya bölümleri ayarlamak isteyebiliriz.


## **Excel'de Satır veya Sütunların Serbest Bırakılması Nasıl Yapılır**

1. Görünüm sekmesine tıklayın > Bölmeleri Dondur > Bölmeleri Çöz

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**




## **Python Excel Kütüphanesi ile Satırları, Sütunları veya Panoları Nasıl Serbest Bırakılır**
Aspose.Cells for Python via .NET ile panoları serbest bırakmak oldukça basittir. Lütfen panoları serbest bırakmak için [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) metodunu kullanın.

1. Donmuş dosyayı açmak için Workbook oluşturun.
2. Worksheet.UnFreezePanes() yöntemi ile bölmeleri çözün.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Ekli [örnek kaynak Excel dosyası](Frozen.xlsx).
{{< app/cells/assistant language="python-net" >}}
