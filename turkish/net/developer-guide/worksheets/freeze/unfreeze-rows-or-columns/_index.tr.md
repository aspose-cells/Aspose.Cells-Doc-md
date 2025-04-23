---
title: Satırları veya Sütunları Dondurma
linktitle: Pencereleri dondur
type: docs
weight: 190
url: /tr/net/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, Excel Elektronik Tablolarının satırlarını, sütunlarını veya panolarını programlı olarak nasıl donduracağınızı öğreneceksiniz, C# Kütüphanesi ve .NET API kullanarak.
keywords: Pencereleri dondur, Satırları dondur, Sütunları dondur, Pencereyi dondurma.
---

## **Giriş**

Bu makalede, Satırları, Sütunları ve Bölmeleri Dondurmayı ve Dondurulmuş Durumu Kaldırmayı nasıl yapacağımızı öğreneceğiz. Excel dosyalarındaki çalışma sayfaları donmuşsa, bazen çalışma sayfasını dondurmak veya donmuş satırları, sütunları veya bölümleri ayarlamak isteyebiliriz.


## **Excel'de**

1. Görünüm sekmesine tıklayın > Bölmeleri Dondur > Bölmeleri Çöz

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**




## **.Net için Aspose.Cells ile Satırları, Sütunları veya Bölmeleri Çözmek**
Aspose.Cells for .Net ile bölmeleri çözmek kolaydır. Lütfen [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes) yöntemini kullanarak bölmeleri çözün.

1. Donmuş dosyayı açmak için Workbook oluşturun.
2. Worksheet.UnFreezePanes() yöntemi ile bölmeleri çözün.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Ekli [örnek kaynak Excel dosyası](Frozen.xlsx).
{{< app/cells/assistant language="csharp" >}}
