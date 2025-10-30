---
title: Grafiği Yerelleştirilmiş Resme Çevir Python via .NET ile
linktitle: Yerelleştirilmiş Bölgeyi Ayarlama
type: docs
weight: 50
url: /tr/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Aspose.Cells for Python via .NET kullanarak grafikler için globalizasyon ayarlarını nasıl yapacağınızı öğrenin. Çoklu dil ve bölgesel biçimleri destekleyen grafikler yapılandırın; böylece metinler, tarihler ve sayılar doğru şekilde gösterilir.
keywords: Aspose.Cells for Python via .NET, Grafikler, Küreselleşme Ayarları, Çoklu Diller, Bölgesel Formatlar, Gösterim, Metin, Tarihler, Sayılar.
---

{{% alert color="primary" %}}

Bu konuda, bir grafiği yerelleştirilmiş bir resme dönüştürme ve bir grafik için yerel bölge ayarlarını nasıl yapacağınızı göstereceğiz.

{{% /alert %}}

## **Senaryo**

Bir grafik için yerelleştirilmiş bölge ayarlarını ne zaman yapmanız gerekebilir?

Excel'de İspanyol bölgesel ayarlarla bir XLSX dosyası açarsanız, grafikteki başlıklar ve efsane gibi öğeler İspanyolca görünür. Ancak, Aspose.Cells kullanarak bu grafiği resmi olarak kaydettiğinizde, bu öğelerin varsayılan olarak İngilizce kalması olasıdır:

**![Global Sorunu](GlobalIssue.png)**

Bu durum, çıktı resmindeki grafiğin efsanesinin Excel'in bölgeselleştirmesiyle uyuşmaması nedeniyle oluşur. Bunu, grafiğin yerelleştirilmiş bölge ayarlarını yapılandırarak çözebilirsiniz.

## **Desteklenen Öğeler**

Aşağıdaki grafik öğeleri, bölgeselleştirme ayarlarınıza göre görüntülenecektir:

| **Desteklenen Öğeler**      | **Varsayılan Değer (İngilizce)**       |
|-----------------------------|-----------------------------------|
| Eksen Başlık Adı             | Eksen Başlığı                        |
| Eksen Birimi Adı              | Yüzler, Binler...                |
| Grafik Başlığı Adı            | Grafik Başlığı                   |
| Sembol Artış Adı             | Artış                            |
| Sembol Azalış Adı             | Azalış                           |
| Toplam Sembol Adı             | Toplam                           |
| Diğer Adı                     | Diğer                            |
| Seri Adı                     | Seri                             |

{{< app/cells/assistant language="python-net" >}}
