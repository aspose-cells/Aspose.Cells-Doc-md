---
title: Neden Open XML SDK sını Kullanmamalıyız
type: docs
weight: 90
url: /tr/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

Bazı zamanlarda şu soruyu duyarız:

**Neden ücretsiz Open XML SDK'sı yerine Aspose ürünlerini kullanmalıyız?**

Bu soruya cevap vermek kolaydır: özellikler ve işlevsellik.

{{% /alert %}}

## **Open XML SDK nedir?**

[MSDN Kütüphanesi](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN)'ne göre, Open XML SDK şöyle tanımlanmaktadır:

"Open XML SDK 2.5, Open XML paketlerini ve bir paket içindeki temel Open XML şema öğelerini manipüle etme görevini basitleştirir. Open XML SDK 2.5, geliştiricilerin Open XML paketleri üzerinde gerçekleştirdikleri birçok yaygın görevi kapsar, bu sayede karmaşık işlemleri birkaç satır kodla gerçekleştirebilirsiniz."

OOXML belgeleri esasen sıkıştırılmış XML dosyalarıdır ve Open XML SDK, OOXML belgelerinin içeriğiyle çalışmanıza izin veren bir sınıf koleksiyonudur. Yani, bir dosyayı açmak, XML'i çıkarmak, bu XML'i bir DOM ağacına yüklemek ve XML öğeleriyle ve öznitelikleriyle doğrudan çalışmak yerine, Open XML SDK bunu yapmak için sınıflar sağlar.

## **Aspose.Cells nedir?**

Aspose.Cells, uygulamaların aşağıdaki elektronik tablo işleme görevlerini gerçekleştirmesine izin veren bir sınıf kütüphanesidir:

- PDF, HTML, TIFF'e dönüşüm de dahil olmak üzere tüm popüler Microsoft Excel formatları arasında yüksek kaliteli dönüşümler.
- Elektronik tablo nesne modeliyle programlama.
- Belge parçalarından, tek veya çoklu belgelerden belge oluşturma yeteneği, veri birleştirme otomatik olarak biçimsel biçimlendirme, grafikler ve grafiklerle.
- Dizi, ArrayList, DataTable / ResultSet vb. farklı veri kaynaklarından veri alma gibi yüksek düzeyli işlevler.
- Neredeyse tüm standart ve gelişmiş Microsoft Excel İşlevlerini destekleyen sağlam Formül Hesaplama Motoru.

## **Open XML SDK ve Aspose.Cells'in Karşılaştırılması**

Aşağıdaki tablo, Open XML SDK ve Aspose.Cells özelliklerini karşılaştırır.

|**Özellik veya Özellik Kategorisi**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Desteklenen Excel veya diğer formatlar|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tab Delimited, ODS, Düz Metin (TXT), PDF, XPS|
|Excel formatları arasında dönüşüm yap|Hayır|Evet|
|<p>Bir çalışma kitabı nesne modeli ile yüksek seviyeli programlama:</p><p>- Bul ve değiştir.</p><p>- Elektronik tabloları birleştirmek.</p><p>- Parça ve çalışma kitapları arasında sayfaları kopyalamak.|Hayır|Evet|
|Ayrıntılı belge nesne modeliyle programlama, tüm elektronik tablo elemanlarının ve biçimlendirme özelliklerinin erişimi.|Evet|Evet|
|Düşük seviyeli doğrudan ve tam erişim, ilişki tanımlayıcılar gibi OOXML belgesi listesi tanımlayıcıları gibi temel XML öğelerine ve özniteliklerine.|Evet|Hayır|
|Raporlar oluşturma, belgeleri veriyle doldurma:<br>- DataTable / _ResultSet'e veri aktarımı/aktarımı.<br>- Akıllı İşaretçiler özelliği.<br>- Satır/Sütun/Aralıklar Ekle/Sil.<br>- Özel veri kaynakları.|Hayır|Evet|
|<p>Raster resme (TIFF, çoklu sayfalı TIFF, PNG, JPEG, BMP) çalışsayfa sayfalarını dönüştürme.<br>- Vektör resme (EMF) elektronik tablo sayfalarını dönüştürme.</p><p> - Grafikleri resimlere dönüştürme (TIFF, çoklu sayfalı TIFF, PNG, JPEG, BMP, EMF vb.).</p><p>- Resim çözünürlüğü, kalitesi, sıkıştırma ve diğer seçenekleri belirtme.<br>- .NET baskı altyapısını kullanarak elektronik tabloları yazdırma. Bileşenin, Microsoft Excel'in Yazdır Önizlemesi'nde gösterildiği gibi çalışsayfalarını yazdırmak için yerleşik bir yazdırma yöntemi bulunur.|Hayır|Evet|
|Formülleri dinamik olarak hesaplama/yeniden hesaplama|Hayır|Evet|
|Desteklenen platformlar|Windows, .NET|Windows, Linux, Java, .NET, Mono|

OpenXML'i Aspose.Cells ile karşılaştırabilirsiniz. Bunun için, farklı görevlerin Aspose.Cells for .NET API'si ile OpenXML kullanarak nasıl yapılabileceğini gösteren Aspose.Cells for OpenXML projesiyle tanışmanızı öneririz. Proje ayrıca yalnızca Aspose.Cells'te mevcut olan ancak OpenXML'de bulunmayan metin belgeleri ile çalışma özelliklerini de kapsar.

Bu proje aynı zamanda OpenXML'den Aspose.Cells'e geçmeyi düşünen geliştiriciler için de faydalıdır.

{{% alert color="primary" %}}

AçıkMXL (OpenXML) ile karşılaştırmalı Aspose.Cells for .NET özellikleri örnekleri ile eklentiye göz atın [örnek kaynak kodlarıyla](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Bu eklenti, Aspose.Cells'in değerlendirme sürümünü kullanır. Değerlendirmenizden memnun kalırsanız, lisansı [Aspose web sitesinden](https://purchase.aspose.com/buy) satın alabilirsiniz. Değerlendirme ile ilgili mesajı ve özellik kısıtlamalarını kaldırmak için bir ürün lisansı uygulamanız gerekir. Ürün satın aldıktan sonra bir lisans dosyası alacaksınız. Bunun için lütfen ["Lisanslama ve Abonelik"](/cells/tr/net/licensing/) makalesindeki talimatları uygulayın.

{{% /alert %}}

**Sonuç**: Open XML SDK ve Aspose.Cells doğrudan rekabet etmez çünkü oldukça farklı ihtiyaçları ve kitleleri ele alırlar.

## **Neden Open XML SDK Kullanılmasın**
Open XML SDK, OOXML belgeleriyle çalışmak için tip güvenli bir yol sağlamak için bir sınıf kitaplığıdır. Aspose.Cells, tüm Microsoft Excel ve diğer dosya biçimleri için mükemmel destek sağlayan çok kullanışlı bir elektronik tablo işleme kitaplığıdır.

Eğer yapmanız gereken sadece bir XLSX belgesinde temel bir programlama işlemiyse, o zaman Open XML SDK uygun bir seçenek olabilir. Open XML SDK ile basit görevleri yapmak, örneğin basit bir XLSX belgesi oluşturmak veya yorumları kaldırmak, üstbilgiler/altbilgiler, resimleri çıkarmak veya diğer işleri yaparken oldukça rahat hissedeceksiniz. 
Bazı görevler Open XML SDK ile gerçekleştirilebilir ancak Aspose.Cells ile gerçekleştirilemez. Örneğin, OOXML belgesinin XML öğelerine ve özniteliklerine doğrudan erişmeniz gerekiyorsa, o zaman Open XML SDK'yi kullanmalısınız.

Ancak, eğer belgeler üzerinde karmaşık işlemler yapmanız gerekiyorsa, aşağıdaki görevlerden bazılarını yapmanız gerekiyorsa, o zaman Aspose.Cells kullanmak en iyi seçeneğinizdir:

- XLSX'ye ek olarak diğer dosya biçimlerini destekleme.
- Fragmanları ve çalışma kitapları arasında kopyaları yapmak veya çalışma kitaplarını birleştirmek ve nesneleri, stilleri ve diğer biçimlendirmeyi uygun bir şekilde birleştirmek.
- Biçimlendirilmiş veya biçimsiz metni değiştirme.
- Dizi, ArrayList, DataTable / ResultSet vb. farklı veri kaynaklarından veri alma gibi yüksek düzeyli işlevler.
- Bir veri kaynağından sipariş detayları ile bir sipariş gibi iş belgeleri oluşturma.
- Bir belgeyi Microsoft Excel tarafından dönüştürülmüş gibi PDF veya XPS'e dönüştürme.
- .NET veya Java uygulaması geliştirme.

{{< app/cells/assistant language="csharp" >}}
