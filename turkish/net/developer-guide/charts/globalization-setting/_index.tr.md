---
title: Grafiği Yerelleştirilmiş Görüntüye Dönüştürme
description: Aspose.Cells for .NET kullanarak grafikler için küreselleştirme yapılandırmalarını nasıl ayarlayacağınızı öğrenin. Rehberimiz, metinleri, tarihleri ve sayıları farklı dillerde doğru bir şekilde görüntülemek için grafikleri yapılandırmayı nasıl destekleyeceğinizi göstermektedir.
keywords: Aspose.Cells for .NET, Grafikler, Küreselleştirme Ayarları, Birden Fazla Dil, Bölgesel Formatlar, Görüntüleme, Metin, Tarihler, Sayılar.
linktitle: Yerelleştirilmiş Bölgeyi Ayarlama
type: docs
weight: 50
url: /tr/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

Bu konuda, bir grafiği yerelleştirilmiş bir görüntüye nasıl dönüştüreceğinizi göstereceğiz. Bir grafik için yerelleştirilmiş bölgeyi nasıl ayarlayacağınızı öğreneceksiniz.

{{% /alert %}}

## **Senaryo**

Hangi senaryoda grafik için yerelleştirilmiş bölgeyi ayarlamamız gerekebilir? 

Bir xlsx dosyasını Excel'de bir grafikle açtığınızda, bu durumda, Excel'de İspanyol Bölgesel Ayarı ile açarsanız, Grafik Başlığı, Lejant vb. gibi grafik alanındaki öğeleri İspanyolca çevrilmiş şekilde görebilirsiniz. Ancak bu grafiği Aspose.Cells ile bir resim olarak kaydettiğinizde, aşağıdaki sorunla karşılaşabilirsiniz: 

**![Global Sorunu](GlobalIssue.png)**

Bu senaryoda, çıktı resimindeki Grafik Lejantı Excel'dekilerle aynı değildir, varsayılan olarak İngilizce olarak görüntülenmeye devam eder. Şimdi grafik için yerelleştirilmiş bölgeyi ayarlayarak bu sorunu çözebilirsiniz. Doğru ayarlarla, aşağıdaki öğeler yerelleştirme ayarlarınıza göre render edilecektir.

## **Desteklenen öğeler**

Grafiğin aşağıdaki öğeleri yerelleştirme ayarlarınıza göre render edilebilir.

|**Desteklenen öğeler**|**İngilizce ortamında varsayılan değer**|
| :- | :- |
|Eksen Başlığı Adı|Eksen Başlığı|
|Eksen Birimi Adı|Yüzler, Binler...|
|Grafik Başlığı Adı|Grafik Başlığı|
|Lejant Artış Adı|Artış|
|Lejant Azalış Adı|Azalış|
|Lejant Toplam Adı|Toplam|
|Diğer Ad|Diğer|
|Seri Adı|Seri|

## **İşlem Adı**

Aşağıdaki örnek, istediğiniz etkiyi elde etmek için yerelleştirilmiş bölgeyi nasıl ayarlayacağınızı detaylı olarak size gösterecektir.

- [Grafik için Çince Bölge Nasıl Ayarlanır](/cells/tr/net/convert-chart-to-image-for-chinese-region/)
- [Grafik için Japon Bölgesi Nasıl Ayarlanır](/cells/tr/net/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="csharp" >}}
