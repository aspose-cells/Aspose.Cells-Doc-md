---
title: Çin Bölgeleri için Grafiği Görüntüye Dönüştürme Golang ile C++ aracılığıyla
linktitle: Çin Bölgesi Ayarla
description: Aspose.Cells for C++ kullanarak tablolar için Çince yapılandırma ayarlamayı öğrenin. Rehberimiz, yazı tipleri, boyutlar, metin yönleri ve daha fazlası dahil olmak üzere Çince karakterleri ve biçimleri desteklemek üzere tabloları nasıl yapılandıracağınızı gösterecektir.
keywords: Aspose.Cells for C++, Tablolar, Çince Yapılandırma, Yazı Tipleri, Yazı Tipi Boyutu, Metin Yönü, Destek.
type: docs
weight: 9
url: /tr/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Bu konuda, bir grafiğe Çin Bölgesi nasıl ayarlanacağını göstereceğiz.

{{% /alert %}}

## **Bir miras sınıfı tanımlar**

İlk adım, `[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/)` sınıfından miras alan "ChartChineseSetttings" adlı bir sınıf tanımlamaktır. 
Daha sonra, ilgili fonksiyonları ezerek, grafik öğelerinin metnini kendi dilinizde ayarlayabilirsiniz.

Kod örneği:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
Ardından çıktı görüntüsünde etkiyi görebilirsiniz, grafikteki unsurlar ayarlarınıza göre yeniden oluşturulur.

## **Sonuç**

Bu örnekte, bir grafiğe Çin Bölgesi ayarlamazsanız, aşağıdaki grafik öğelerinin varsayılan dilde, örneğin İngilizce olarak render edilebileceğini göreceksiniz.
Yukarıdaki işlemden sonra, Çin Bölgesi ayarlamazsak, bir çıktı grafik resmi elde edebiliriz.

|**Desteklenen unsurlar**|**Bu örnekteki değer**|**İngilizce ortamındaki varsayılan değer**|
| :- | :- | :- |
|Eksen Başlık Adı|坐标轴标题|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüz, Bin...|
|Grafik Başlık Adı|图表标题|Grafik Başlığı|
|Açıklama Artışı Adı|增加|Artış|
|Açıklama Azalışı Adı|减少|Azalma|
|Legend Total Name|汇总|Toplam|
|Other Name|其他|Diğer|
|Series Name|系列|Seri|
