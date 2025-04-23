---
title: Yazdırma Alanı Nasıl Ayarlanır
type: docs
weight: 200
url: /tr/java/how-to-set-print-area/
description: Bu makale, Aspose.Cells kütüphanesi kullanarak yazdırma alanını nasıl ayarlayacağınızı açıklayan kod örnekleri sunmaktadır.
keywords: Yazdırma alanını sınırlandırma, Yazdırma Alanını Belirleme, Yazdırma Alanını Temizleme, Java kullanarak Yazdırma Alanını Ayarla ve Temizle, Java da Yazdırma Alanını Nasıl Belirlenir, Yazdırma Alanını ve Temizleme, Excel de Yazdırma Alanını Temizleme, Java kullanarak yazdırma alanını ekleme ve kaldırma, Yazdırma alanını ayarlama ve temizleme.
---

## **Olası Kullanım Senaryoları**

Bir belge, örneğin bir Excel sayfası, içinde yer alan içeriği kontrol etmek için yazdırma alanı ayarlamak faydalıdır. İşte yazdırma alanı ayarlamanın bazı nedenleri:

1. Belirli Verilere Odaklanma: Sadece en önemli bölümleri yazdırabilir, gereksiz içeriği engelleyebilirsiniz.
1. Gelişmiş Düzen: İçeriğin düzenlenmesine ve düzgün şekilde sığdırılmasına yardımcı olur, bölünmeleri veya istenmeyen sayfa sonlarını önler.
1. Kaynak Tasarrufu: Yazdırma alanını sınırlandırarak kağıt ve mürekkep kullanımını azaltabilirsiniz.
1. Profesyonel Sunum: Yalnızca verilerin düzgün ve son halini yazdırdığınızdan emin olur, bu özellikle raporlar veya sunumlar için önemlidir.
1. Tutarlılık: Aynı belgeyi birden fazla kez yazdırırken, belirli bir yazdırma alanı kullanmak, çıktıdaki tutarlılığı sağlar.

<br>
Yazdırma alanı ayarlamak, özellikle büyük belgelerde, yalnızca bir kısmının paylaşılması veya yazdırılmak üzere gözden geçirilmesi gerektiğinde çok kullanışlıdır.

## **Excel'de Yazdırma Alanı Nasıl Ayarlanır**

Excel'de yazdırma alanı belirlemek için şu adımları izleyin:

1. Hücreleri Seçin: Yazdırma alanı olarak ayarlamak istediğiniz hücre aralığını tıklayıp sürükleyerek seçin.
1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki şeritteki "Sayfa Düzeni" sekmesine gidin.
1. Yazdırma Alanını Ayarla: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Ayarla"yı seçin.
<br>
<img src="3.png" width=60% />

1. Yazdırma Alanına Ekleyin: Mevcut yazdırma alanına başka hücreler ekmek istiyorsanız, ek hücreleri seçin, "Sayfa Düzeni" sekmesinde "Yazdırma Alanı"na gidin ve "Yazdırma Alanına Ekle"yi seçin.

<br>
Bu işlem, seçilen hücreleri yazdırma alanı olarak tanımlar. Çalışma sayfasını yazdırdığınızda, yalnızca bu tanımlı alan yazdırılır.

## **Excel'de Yazdırma Alanını Temizle Nasıl Yapılır**

Excel'de yazdırma alanını temizlemek için şu adımları izleyin:

1. Sayfa Düzeni Sekmesini Açın: Excel penceresinin üstündeki "Sayfa Düzeni" sekmesine tıklayın.
1. Yazdırma Alanını Temizle: "Sayfa Kurulum" grubunda, "Yazdırma Alanı"na tıklayın. Açılan menüden "Yazdırma Alanını Temizle"yi seçin.
<br>
<img src="4.png" width=60% />

<br>
Bu işlem, önceden ayarlanmış yazdırma alanını kaldırır ve tüm çalışma sayfasının yazdırılmasına izin verir.

## **Yazdırma Alanını Temizledikten Sonra Neler Olur**

Excel gibi elektronik tablo uygulamasında Aspose.Cells kullanarak yazdırma alanını temizlemek, belgenin tamamını yazdırmak anlamına gelir. Yazdırma alanı ayarlandıysa, yalnızca belirli hücre aralığı yazdırılır. Yazdırma alanı temizlendiğinde, herhangi bir belirli aralık tanımlanmaz ve varsayılan yazdırma davranışı devreye girer, bu da tüm sayfayı içerir.

1. Varsayılan Yazdırma Davranışı: Tüm çalışma sayfası yazdırılmak üzere değerlendirilir. Bu, tüm hücrelerin verileri veya biçimlendirmeleri kabul eder.
1. Yazdırma Alanı Sınırları Kalmadı: Önceden belirlenmiş yazdırma alanı sınırları kaldırılır. Önceden belirlenen satır ve sütunlar artık bu sınırlar içinde kalmaz.
1. Tüm İçeriğin Yazdırılması: Başlıklar, altbilgiler ve çalışma sayfasındaki diğer tüm veriler yazdırma işlemine dahil edilir.


## **Aspose.Cells kullanarak Yazdırma Alanını Nasıl Belirlerim**

Belirtilmiş bir çalışma sayfasında yazdırma alanını ayarlamak için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) nesnesinin [**Worksheet.getPageSetup().setPrintArea()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setPrintArea-java.lang.String-) özelliğini değiştirmeniz gerekir. Bu özelliği bir aralık dizisi olarak ayarlamak yazdırma alanını belirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-set-print-area.java" >}}

Çıktı sonucu:
<br>
<img src="1.png" width=60% />

## **Aspose.Cells kullanarak Yazdırma Alanını Nasıl Temizlerim**

Belirtilmiş bir çalışma sayfasında yazdırma alanını temizlemek için: Önce [örnek dosyayı](input.xlsx) yükleyin, ardından istenen çalışma sayfası için [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) nesnesinin [**Worksheet.getPageSetup().setPrintArea()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setPrintArea-java.lang.String-) özelliğini değiştirmeniz gerekir. Bu özelliği boş bir dize olarak ayarlamak yazdırma alanını temizler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-clear-print-area.java" >}}

Çıktı sonucu:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="java" >}}
