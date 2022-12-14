---
title: Aspose.Cells 7.0.0 veya Üstüne Nasıl Geçilir?
type: docs
weight: 10
url: /tr/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

Bu yazıda, Aspose.Cells for Java 7.0.0 ve sonraki sürümlerde Aspose.Cells for Java'in önceki sürümlerine göre taşınan API'deki önemli değişiklikleri paylaştık. Bu makale, kullanıcıların Eski API'den yeni sürüme hızlı bir şekilde geçiş yapmasına yardımcı olacaktır. API yapılan değişiklikleri anlayarak ve uygulamalarında gerçekleştirerek.

{{% /alert %}}

## **Mevcut Kullanıcılar İçin Önemli Değişiklikler**

Aspose.Cells for Java v7.0.0 sürümünden bu yana, API'de bazı büyük değişiklikler yaptık ve bugüne kadar Aspose.Cells for .NET'de bulunan tüm özellikleri ekledik. Böylece hem Aspose.Cells for Java hem de .NET artık özellikler açısından ve hatta yöntem ve özellik adları açısından karşılaştırılabilir olacaktır.

Eski yaklaşıma benzer şekilde, tüm sınıfları, arayüzleri vb. getirmek için uygulamanıza yalnızca bir import deyimi aktarabilirsiniz.

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Belirli API'lerin setini API yapısını Aspose.Cells for .NET ile eşleştirmek için temizleyecek şekilde yeniden adlandırdık. Şimdi bazı koleksiyon sınıfları ekledik ve bunları mevcut koleksiyon sınıflarıyla değiştirdik. Like Worksheets sınıfı ile değiştirildi**Çalışma Sayfası Koleksiyonu** . Benzer şekilde, Shapes sınıfı ile değiştirildi**Şekil Koleksiyonu**. Ancak, sınıfların işlevselliği etkilenmemiş, aksine geliştirilmiştir.

Yeni API'e geçmek istiyorsanız, işlerin sizin tarafınızdan çalışmasını sağlamak için başvurunuzda aşağıdaki değişiklikleri yapmanız gerekebilir. Aşağıdaki liste, sınıflarda yapılan değişiklikleri ve bunların ilgili yöntemlerini de içerir.

## **API'deki Değişikliklerin Özeti**

1) Adları 's' ile biten v2.5.4 veya önceki sürümlerdeki koleksiyonlar yeniden adlandırıldı. v7.0.0 veya üzeri sürümlerde, Koleksiyonlar şu şekilde adlandırılır:
örneğin, Şekiller (Eski) -> ShapeCollection (Yeni), Çalışma Sayfaları (Eski) -> WorksheetCollection (Yeni), ...,vb.

2) Koleksiyondan öğe alma değişti. Örneğin, v2.5.4 veya öncesinde bunu getXXX(int) olarak yapıyorduk, v7.0.0 veya üzerinde ise şimdi get(int) olarak yapıyoruz:
örneğin, Worksheets.getSheet(int) (Eski) -> WorksheetCollection.get(int) (Yeni), ...vb.

3) Bir Koleksiyonun alma boyutu (element sayısı) değiştirildi. v2.5.4 veya önceki sürümlerde bunu size() ile yapıyorduk, v7.0.0 veya üzeri sürümlerde ise şimdi getCount() ile yapıyoruz:
Worksheets.size() (Eski) -> WorksheetCollection.getCount() (Yeni), ...,vb.

4) v2.5.4 veya önceki sürümlerde 'is' ile başlayan adları değiştirilen Boolean özelliklerinin alıcı yöntemleri. v7.0.0'da bunlar "get" ile başlatılır:
örneğin, PageSetup.isBlackAndWhite() (Eski) -> PageSetup.getBlackAndWhite() (Yeni), ...,vb.
