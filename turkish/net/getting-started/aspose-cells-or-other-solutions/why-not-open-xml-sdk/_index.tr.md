---
title: XML SDK Neden Açılmıyor?
type: docs
weight: 90
url: /tr/net/why-not-open-xml-sdk/
---
{{% alert color="primary" %}}

Bazen şu soruyu duyarız:

**Ücretsiz Open XML SDK yerine neden Aspose ürünlerini kullanmalıyız?**

Bu sorunun yanıtlanması kolaydır: özellikler ve işlevsellik.

{{% /alert %}}

## **Açık XML SDK'sı nedir?**

 Göre[MSDN Kitaplığı](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN), Açık XML SDK'sı şu şekilde tanımlanır:

"Açık XML SDK 2.5, Açık XML paketlerini ve bir paket içindeki temel Açık XML şema öğelerini değiştirme görevini basitleştirir. Açık XML SDK 2.5, geliştiricilerin Açık XML paketlerinde gerçekleştirdiği birçok genel görevi içerir, sadece birkaç satır kod."

OOXML belgeleri esas olarak sıkıştırılmış XML dosyalarıdır ve Open XML SDK, OOXML belgelerinin içeriğiyle kesin olarak yazılmış bir şekilde çalışmanıza izin veren bir sınıflar koleksiyonudur. Bu, XML'i ayıklamak için bir dosyayı açmak, bu XML'i bir DOM ağacına yüklemek ve doğrudan XML öğeleri ve nitelikleriyle çalışmak yerine, Open XML SDK bunu yapmak için sınıflar sağlar.

## **Aspose.Cells nedir?**

Aspose.Cells, uygulamaların aşağıdaki elektronik tablo işleme görevlerini gerçekleştirmesine izin veren bir sınıf kitaplığıdır:

- PDF, HTML, TIFF'e dönüştürme ve yazdırma dahil olmak üzere tüm popüler Microsoft Excel biçimleri arasında yüksek kaliteli dönüştürmeler.
- Çalışma kitabı nesne modeliyle programlama.
- Verileri biçimsel biçimlendirme, çizelgeler ve grafiklerle otomatik olarak birleştirirken parçalardan, bir veya daha fazla belgeden belgeler oluşturma yeteneği.
- Array, ArrayList, DataTable / ResultSet gibi farklı veri kaynaklarından veri alma gibi üst düzey işlevler.
- Neredeyse tüm standart ve gelişmiş Microsoft Excel İşlevlerini destekleyen Sağlam Formül Hesaplama Motoru.

## **Open XML SDK ile Aspose.Cells'i karşılaştırın**

Aşağıdaki tabloda Açık XML SDK'sı ve Aspose.Cells özellikleri karşılaştırılmaktadır.

|**Özellik veya Özellik Kategorisi**|**XML SDK'yı aç**|**Aspose.Cells**|
|:- |:- |:- |
|Desteklenen Excel veya diğer biçimler|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Sekmeyle Ayrılmış, ODS, Düz Metin (TXT), PDF, XPS|
|Excel biçimleri arasında dönüştürme|Numara|Evet|
|<p>Çalışma kitabı nesne modeliyle üst düzey programlama:</p><p>- Bul ve Değiştir.</p><p>- Elektronik tabloları birleştirin.</p><p>- Çalışma kitapları arasında parçaları ve çalışma sayfalarını kopyalayın.</p>|Numara|Evet|
|Belge nesne modeliyle ayrıntılı programlama, tek tek öğelere erişim ve tüm elektronik tablo öğelerinin biçimlendirme özellikleri.|Evet|Evet|
|Bir OOXML belgesinin ilişki tanımlayıcıları, liste tanımlayıcıları gibi temeldeki XML öğelerine ve özniteliklerine düşük düzeyli doğrudan ve tam erişim.|Evet|Numara|
|<p>Raporlar oluşturun, belgeleri verilerle doldurun:</p><p>- DataTable / _ResultSet'ten/verileri içe/dışa aktarın.</p><p>- Akıllı İşaretçiler özelliği.</p><p>- Satır/Sütun/Aralık Ekle/Sil.</p><p>- Özel veri kaynakları.</p>|Numara|Evet|
|<p>Oluşturma ve Yazdırma:* Çalışma sayfası sayfalarını raster görüntülere dönüştürün (TIFF, çok sayfalı TIFF, PNG, JPEG, BMP).* Elektronik tablo sayfalarını vektör görüntülere (EMF) dönüştürün.</p><p>- Grafikleri resimlere dönüştürün (TIFF, çok sayfalı TIFF, PNG, JPEG, BMP, EMF, vb.)</p><p>- Görüntü çözünürlüğünü, kalitesini, sıkıştırmayı ve diğer seçenekleri belirleyin.</p><p>- .NET yazdırma altyapısını kullanarak elektronik tabloları yazdırın. Bileşen, çalışma sayfalarını Microsoft Excel'in Baskı Önizleme'de gösterildiği gibi yazdırmak için yerleşik bir yazdırma yöntemine sahiptir.</p>|Numara|Evet|
|Formülleri dinamik olarak hesaplayın/yeniden hesaplayın|Numara|Evet|
|desteklenen platformlar|Windows, .NET|Windows, Linux, Java, .NET, Mono|

OpenXML'yi Aspose.Cells ile karşılaştırabilirsiniz Bunları yapmak için, OpenXML için Aspose.Cells projesine aşina olmanızı öneririz - bu, Aspose.Cells for .NET API ile OpenXML kullanılarak nasıl farklı görevlerin yapılabileceğini gösterir. Proje ayrıca, yalnızca Aspose.Cells'de bulunan ancak OpenXML'de bulunmayan metin belgeleriyle çalışmaya yönelik özellikleri de kapsar.

Bu proje aynı zamanda OpenXML'den Aspose.Cells'e geçiş yapmak isteyen geliştiriciler için de yararlıdır.

{{% alert color="primary" %}}

 Keşfetmek[OpenXML ile karşılaştırıldığında Aspose.Cells for .NET özelliklerinin kaynak kodu örnekleri ile eklenti](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Bu eklenti, Aspose.Cells'in değerlendirme sürümünü kullanır. Değerlendirmenizden memnun olduğunuzda, şu adresten bir lisans satın alabilirsiniz:[Aspose web sitesi](https://purchase.aspose.com/buy) . Değerlendirme mesajını ve özellik sınırlamalarını kaldırmak için bir ürün lisansı uygulamanız gerekir. Ürünü satın aldıktan sonra bir lisans dosyası alacaksınız. Lütfen içindeki talimatları takip edin.["Lisanslama ve Abonelik"](/cells/tr/net/licensing/) Bunu yapmak için makale.

{{% /alert %}}

**Çözüm**: Open XML SDK ve Aspose.Cells, oldukça farklı ihtiyaçlara ve kitlelere hitap ettikleri için kafa kafaya rekabet etmezler.

## **XML SDK Neden Açılmıyor?**
Open XML SDK, OOXML belgeleriyle çalışmak için kesin tipte bir yol sağlayan bir sınıf kitaplığıdır. Aspose.Cells, tüm Microsoft Excel ve diğer dosya biçimleri için mükemmel destek sağlayan çok kullanışlı bir elektronik tablo işleme kitaplığıdır.

Tek yapmanız gereken bir XLSX belgesinde oldukça basit bir programlama işlemi yapmaksa, Open XML SDK uygun bir seçim olabilir. Açık XML SDK ile, basit bir XLSX belgesi oluşturmak veya yorumları, üstbilgileri/altbilgileri kaldırmak, görüntüleri ayıklamak veya diğerlerini kaldırmak gibi basit görevleri yaparken oldukça rahat olacaksınız.
Bazı görevler Open XML SDK ile gerçekleştirilebilir, ancak Aspose.Cells ile gerçekleştirilemez. Örneğin, bir OOXML belgesinin XML öğelerine ve özniteliklerine doğrudan erişmeniz gerekiyorsa, Open XML SDK kullanmalısınız.

Ancak, aşağıdaki görevlerden bazıları gibi belgeler üzerinde karmaşık işlemler gerçekleştirmeniz gerekiyorsa, Aspose.Cells'i kullanmak en iyi seçeneğinizdir:

- XLSX'e ek olarak diğer dosya formatlarını destekleyin.
- Parçaları ve çalışma sayfalarını çalışma kitapları arasında kopyalayın veya çalışma kitaplarını nesneleri, stilleri ve diğer biçimlendirmeyi uygun bir şekilde birleştirecek şekilde birleştirin.
- Biçimlendirilmiş veya biçimlendirilmemiş metni değiştirin.
- Array, ArrayList, DataTable / ResultSet gibi farklı veri kaynaklarından veri alma gibi üst düzey işlevler.
- Bir veri kaynağından sipariş ayrıntıları içeren bir sipariş gibi bir iş belgesi oluşturun.
- Bir belgeyi tam olarak Microsoft Excel'in dönüştürdüğü gibi görünmesi için PDF veya XPS'ye dönüştürün.
- Bir .NET veya Java uygulaması geliştirin.

