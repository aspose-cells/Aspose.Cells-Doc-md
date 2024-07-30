---
title: Satırları veya Sütunları Dondurma
linktitle: Pencereleri dondur
type: docs
weight: 190
url: /tr/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, Aspose.Cells için Python via .NET API lerini kullanarak programlı olarak Excel Çalışma Sayfalarındaki satırları, sütunları veya panoları nasıl iptal edeceğinizi öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python Panoları Geri Alma, Python Satırları Nasıl Geri Alır, Python Nasıl Sütunları Geri Alır, Python Nasıl Pencereyi serbest bırakır.
---

## **Giriş**

Bu makalede, Satırları, Sütunları ve Bölmeleri Dondurmayı ve Dondurulmuş Durumu Kaldırmayı nasıl yapacağımızı öğreneceğiz. Excel dosyalarındaki çalışma sayfaları donmuşsa, bazen çalışma sayfasını dondurmak veya donmuş satırları, sütunları veya bölümleri ayarlamak isteyebiliriz.


## **Excel'de Satırları veya Sütunları Geri Alma**

1. Görünüm sekmesine tıklayın > Bölmeleri Dondur > Bölmeleri Çöz

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**




## **Aspose.Cells ile Python Excel Kütüphanesiyle Satırları, Sütunları veya Panoları Geri Alma**
Aspose.Cells için Python via .NET ile panoları serbest bırakmak basittir. Lütfen panoları serbest bırakmak için [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) yöntemini kullanın.

1. Donmuş dosyayı açmak için Workbook oluşturun.
2. Worksheet.UnFreezePanes() yöntemi ile bölmeleri çözün.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Ekli [örnek kaynak Excel dosyası](Frozen.xlsx).
