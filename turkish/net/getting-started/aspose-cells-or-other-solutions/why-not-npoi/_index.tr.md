---
title: Aspose.Cells veya NPOI
linktitle: Neden NPOI Değil
description: C# kullanarak Excel dosyalarıyla çok sayıda görevi NPOI'den daha hızlı ve daha rahat gerçekleştirin
type: docs
weight: 40
url: /tr/net/why-not-npoi
---
Bazen şu soruyu alıyoruz: NPOI yerine neden Aspose ürünlerini kullanmalıyız? Bu sorunun yanıtlanması kolaydır: özellikler ve işlevsellik.

NPOI (POI Java projesinin NET versiyonu), Microsoft Office formatlarındaki dosyaları okumanıza veya yazmanıza yardımcı olabilecek açık kaynaklı bir projedir. Mevcut karşılaştırmanın bir parçası olarak, aşağıdaki NPOI bileşenlerini göz önünde bulundurun - HSSF ve XSSF:

**HSSF** POI Projesi'nin Excel 97(-2007) dosya biçiminin saf Java uygulamasıdır.

**XSSF** POI Projesi'nin Excel 2007 OOXML (.xlsx) dosya biçiminin saf Java uygulamasıdır.

HSSF ve XSSF, elektronik tabloları okumanın, XLS elektronik tablolarını oluşturmanın, değiştirmenin, okumanın ve yazmanın yollarını sağlar. Sağladıkları:

- özel ihtiyaçları olanlar için düşük seviyeli yapılar
- verimli salt okunur erişim için bir eventmodel api
- XLS dosyalarını oluşturmak, okumak ve değiştirmek için eksiksiz bir kullanıcı modeli api'si

Hem HSSF hem de XSSF, Temel Metin Çıkarma, Belirli Metin Çıkarma, Üstbilgi ve Altbilgilere Erişim ve Metin Değiştirme özelliklerini sağlar. HSSF ve XSSF benzer işlevsellik sağlarken, şu anda ortak bir arayüze sahip değiller. .xlsx dosyalarının ana bölümlerine okuma veya yazma erişimi sağlayan oldukça kararlı bir çekirdeğe API sahiptir, ancak tam değildir.

Aspose.Cells, tüm Microsoft Excel ve diğer belge biçimleri için büyük destek sağlayan çok kullanışlı bir belge işleme kitaplığıdır. Aspose.Cells ile belgeleri Microsoft Excel kullanmadan okuyabilir, oluşturabilir, değiştirebilir, dönüştürebilir, işleyebilir ve yazdırabilirsiniz.

Bu yazımızda Aspose.Cells'i tercih etmenin sizin için ne zaman mantıklı olduğuna bakacağız.

## Neden NPOI Değil

Bazı görevlerin Aspose.Cells ile gerçekleştirilebileceğini ancak NPOI ile gerçekleştirilemeyeceğini belirtmekte fayda var. Örneğin, Excel dosyalarını PDF, JSON ve görsellere dönüştürmeniz gerekiyorsa, o zaman sadece NPOI kullanamazsınız, ayrıca Microsoft Excel 365 veya diğer araçlara ihtiyacınız vardır.

NPOI'yi Aspose.Cells ile karşılaştırabilirsiniz Bunu yapmak için, NPOI için Aspose.Cells projesine (HSSF ve XSSF) aşina olmanızı öneririz - bu, Aspose.Cells for .NET API ile NPOI kullanılarak nasıl farklı görevlerin yapılabileceğini gösterir. Proje ayrıca, yalnızca Aspose.Cells'de bulunan ancak NPOI'de bulunmayan metin belgeleriyle çalışmaya yönelik özellikleri de kapsar.

Bu proje aynı zamanda NPOI'den Aspose.Cells'e geçmek isteyen geliştiriciler için de kullanışlıdır.

{{% alert color="primary" %}}

 Keşfetmek[NPOI ile karşılaştırıldığında Aspose.Cells for .NET özelliklerinin kaynak kodu örnekleri ile eklenti](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/NPOI).

Bu eklenti, Aspose.Cells'in değerlendirme sürümünü kullanır. Değerlendirmenizden memnun olduğunuzda, şu adresten bir lisans satın alabilirsiniz:[Aspose web sitesi](https://purchase.aspose.com/buy) . Değerlendirme mesajını ve özellik sınırlamalarını kaldırmak için bir ürün lisansı uygulamanız gerekir. Ürünü satın aldıktan sonra bir lisans dosyası alacaksınız. Lütfen içindeki talimatları takip edin.["Lisanslama ve Abonelik"](/cells/tr/net/licensing/) Bunu yapmak için makale.

{{% /alert %}}

Aşağıdaki bölümlerde ve makalelerde, Aspose.Cells tarafından sağlanan bazı özellik ve yeteneklere daha yakından bakacağız.

### istikrar

Aspose bileşenleri kapsamlı bir şekilde test edilmiştir. Aspose bileşenleri tek bir DLL'de paketlendiğinden, bunların çalışması için herhangi bir ek parça veya parça yüklemeye asla gerek kalmayacaktır. Bu, Aspose.Cells ile istikrarlı bir çalışma sağlamakla kalmaz, aynı zamanda öngörülemeyen durumların riskini neredeyse sıfıra indirir.

### Ölçeklenebilirlik ve Hız

Aspose bileşenleri yüksek düzeyde ölçeklenebilir ve ışık hızındadır. Bunlar gerçek bir .NET çözümüdür ve tek bir uygulamaya güç sağlayan tek bir sunucuda veya kurumsal bir uygulamaya güç veren yük dengeli bir web grubu üzerinde kusursuz bir şekilde çalışır.

### Özellikler

Aspose bileşenleri, Office dosyalarını yönetmek için ihtiyaç duyduğunuz her şeyin yanı sıra çok daha fazlasını sağlar. Geliştiricilerin en az çalışmayla en iyi sonuçları elde etmelerine izin verme felsefesiyle tasarlanmıştır.

 Aspose bileşenleri, birçok güçlü zaman kazandıran işlev sağlar. Örneğin,[Aspose.Cells](https://products.aspose.com/cells/net/) geliştiricilerin JSON'u Excel dosyalarına aktarmasına izin veren bir özellik sunar. Aspose ailesindeki her bileşenin kendi benzersiz ve güçlü özelliklerini sunduğunu belirtmek gerekir.

## Ayrıca bakınız

* [Apache POI hakkında daha fazla bilgi](https://poi.apache.org/)

