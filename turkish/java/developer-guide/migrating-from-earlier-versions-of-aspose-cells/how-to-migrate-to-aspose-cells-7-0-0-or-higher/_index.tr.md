---
title: Aspose.Cells 7.0.0 veya üstüne Nasıl Geçilir
type: docs
weight: 10
url: /tr/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

Bu makalede, API'deki dikkate değer değişiklikleri, Aspose.Cells for Java 7.0.0 ve sonraki sürümlerde öncü sürümlere kıyasla yapılan değişikliklere yönelik paylaştık. Bu makale, kullanıcıların eski API'den yeni API'ye hızla geçiş yapmalarına yardımcı olacak ve yapılan değişiklikleri anlayarak uygulamalarında gerçekleştirebilecekler.

{{% /alert %}}

## **Mevcut Kullanıcılar için Dikkate Değer Değişiklikler**

Aspose.Cells for Java v7.0.0'ın piyasaya sürülmesinden bu yana, API'de bazı büyük değişiklikler yaptık ve şu ana kadar Aspose.Cells for .NET içeren tüm özellikleri ekledik. Dolayısıyla, hem Aspose.Cells for Java hem de .NET şimdi özellikler ve hatta yöntemler ve özellik isimleri açısından karşılaştırılabilir olacak.

Eski yaklaşıma benzer şekilde, uygulamanıza sadece bir import ifadesi ekleyerek tüm sınıfları, arabirimleri vb. getirebilirsiniz.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

API yapısını temizlemek için belirli API'ların adını değiştirdik ve Aspose.Cells for .NET'yle eşleşecek şekilde ayarladık. Bazı koleksiyon sınıflarına şimdi eklemeler yaptık ve mevcut koleksiyon sınıflarını değiştirildi. Örneğin, Worksheets sınıfı **WorksheetCollection** ile değiştirilmiştir. Benzer şekilde, Shapes sınıfı **ShapeCollection** ile değiştirilmiştir. Bununla birlikte, sınıfların işlevselliği, etkilenmemiş, aksine geliştirilmiştir.

Yeni API'ya geçmek istiyorsanız, uygulamanızda aşağıdaki değişiklikleri gerçekleştirmeniz gerekebilir. Aşağıdaki liste, sınıflarda ve ilgili yöntemlerde yapılan değişiklikleri içermektedir.

## **API'deki Değişikliklerin Özeti**

1) v2.5.4 veya önceki sürümlerde 's' ile biten koleksiyonlar yeniden adlandırılmıştır. v7.0.0 veya üstü sürümlerde, Koleksiyonlar şu şekilde adlandırılmaktadır:
örn., Şekiller (Eski) -> ShapeCollection (Yeni), Çalışma Sayfaları (Eski) -> WorksheetCollection (Yeni), ..., vb.

2) Koleksiyondan eleman almak değiştirildi. Örneğin, v2.5.4 veya önceki sürümlerde bunu getXXX(int) olarak yapardık, v7.0.0 veya üstünde artık bunu get(int) olarak yapıyoruz:
örn., Worksheets.getSheet(int) (Eski) -> WorksheetCollection.get(int) (Yeni), ...vb.

3) Bir Koleksiyonun boyutunu (eleman sayısı) almak değiştirildi. v2.5.4 veya önceki sürümlerde bunu size() ile yapardık, v7.0.0 veya üstünde artık getCount() ile yapıyoruz:
Worksheets.size() (Eski) -> WorksheetCollection.getCount() (Yeni), ...,vb.

4) v2.5.4 veya önceki sürümlerde 'is' ile başlayan Boolean özelliklerin getirme yöntemleri değişti. v7.0.0'da bunlar 'get' ile başlıyor:
örn., PageSetup.isBlackAndWhite() (Eski) -> PageSetup.getBlackAndWhite() (Yeni), ...vb.
{{< app/cells/assistant language="java" >}}
