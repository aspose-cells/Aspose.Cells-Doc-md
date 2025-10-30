---
title: Node.js ve C++ kullanarak Lokalize Edilmiş Resim ile Grafik Dönüştürme
description: Aspose.Cells for Node.js via C++ kullanarak grafikler için küreselleşme yapılandırmalarını nasıl ayarlayacağınızı öğrenin. Kılavuzumuz, çeşitli diller ve bölgesel biçimler desteklemek için grafik yapılandırmasının nasıl yapıldığını gösterir; böylece metinleri, tarihleri ve sayıları farklı dillerde doğru şekilde görüntüleyebilirsiniz.
keywords: Aspose.Cells for Node.js via C++, Grafikler, Küreselleşme Ayarları, Çoklu Diller, Bölgesel Formatlar, Görüntüleme, Metinler, Tarihler, Sayılar.
linktitle: Yerelleştirilmiş Bölgeyi Ayarlama
type: docs
weight: 50
url: /tr/nodejs-cpp/convert-chart-to-localized-image/
alias: [/nodejs-cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

Bu konuda, bir grafiği yerelleştirilmiş bir görüntüye nasıl dönüştüreceğinizi göstereceğiz. Bir grafik için yerelleştirilmiş bölgeyi nasıl ayarlayacağınızı öğreneceksiniz.

{{% /alert %}}

## **Senaryo**

Bir grafik için yerelleştirilmiş bölgeyi ne zaman ayarlamalıyız? 

Excel'de bir grafik içeren bir xlsx dosyasını açarken, bu durumda diyelim ki Excel'de İspanyol Bölgesel Ayar ile açıyorsunuz, grafik alanındaki öğeleri görebilirsiniz, Örneğin Grafik Başlığı, Efsane, İspanyolcaya çevrilmiştir. Ancak, bu grafiği Aspose.Cells ile resim olarak kaydettiğinizde, aşağıdaki sorunla karşılaşabilirsiniz: 

**![Global Sorunu](GlobalIssue.png)**

Bu senaryoda, çıktı resmindeki Grafik Efsanesi, Excel'deki ile aynı değildir; varsayılan olarak İngilizce görüntülenmeye devam eder. Bu sorunu, grafiğe yerelleştirilmiş bölge ayarlayarak çözebilirsiniz. Doğru ayarlarla, aşağıdaki elemanlar yerelleştirme ayarlarınıza göre görüntülenecektir.

## **Desteklenen öğeler**

Grafikte aşağıdaki elemanlar, yerelleştirme ayarlarınız doğrultusunda görüntülenebilir.

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

Aşağıdaki örnek, istediğiniz efekti elde etmek için yerelleştirilmiş bölgeyi nasıl ayarlayacağınızı detaylı olarak gösterecektir.

- [Grafik için Çince Bölge Nasıl Ayarlanır](/cells/tr/nodejs-cpp/convert-chart-to-image-for-chinese-region/)
- [Grafik için Japon Bölgesi Nasıl Ayarlanır](/cells/tr/nodejs-cpp/convert-chart-to-image-for-japanese-region/)


{{< app/cells/assistant language="nodejs-cpp" >}}
