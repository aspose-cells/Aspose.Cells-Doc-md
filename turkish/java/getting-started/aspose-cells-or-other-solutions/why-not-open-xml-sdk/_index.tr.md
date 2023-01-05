---
title: XML SDK Neden Açılmıyor?
type: docs
weight: 20
url: /tr/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

Bazen şu soruyu duyarız:

**Ücretsiz Open XML SDK yerine neden Aspose ürünlerini kullanmalıyız?**

 Bu soruyu cevaplamak kolaydır:**özellikler ve işlevsellik**.

{{% /alert %}} 
## ** Açık XML SDK'sı nedir?**
MSDN Kitaplığına göre Açık XML SDK şu şekilde tanımlanır: Açık XML SDK 2.0, Açık XML paketlerini ve bir paket içindeki temel Açık XML şema öğelerini değiştirme görevini basitleştirir. Open XML SDK 2.0, geliştiricilerin Open XML paketlerinde gerçekleştirdiği birçok genel görevi kapsar, böylece karmaşık işlemleri yalnızca birkaç satır kodla gerçekleştirebilirsiniz.OOXML belgeleri temelde sıkıştırılmış XML dosyalarıdır ve Open XML SDK, izin veren bir sınıflar koleksiyonudur. OOXML belgelerinin içeriğiyle kesinlikle yazılmış bir şekilde çalışabilirsiniz. Bu, XML'i ayıklamak için bir dosyayı açmak, bu XML'i bir DOM ağacına yüklemek ve doğrudan XML öğeleri ve nitelikleriyle çalışmak yerine, Open XML SDK bunu yapmak için sınıflar sağlar.
## ** Aspose.Cells nedir?**
Aspose.Cells, uygulamanızın aşağıdaki elektronik tablo işleme görevlerini gerçekleştirmesine olanak tanıyan bir sınıf kitaplığıdır: PDF, HTML, TIFF'e dönüştürme ve yazdırma dahil tüm popüler Excel biçimleri arasında Yüksek Kaliteli dönüştürmeler. Çalışma kitabı nesne modeliyle programlama. Verileri biçemsel biçimlendirme, çizelgeler ve grafiklerle otomatik olarak birleştirirken, parçalardan, bir veya daha fazla belgeden belgeler oluşturma yeteneği. Array, ArrayList, DataTable / ResultSet dahil olmak üzere farklı veri kaynaklarından veri içe aktarma gibi üst düzey işlevler. Neredeyse tüm standart ve gelişmiş Microsoft Excel İşlevlerini destekleyen Sağlam Formül Hesaplama Motoru.

{{% alert color="primary" %}}
## ** Open XML SDK ile Aspose.Cells'i karşılaştırın**
 Aşağıdaki tabloda Açık XML SDK ve Aspose.Cells özellikleri karşılaştırılmaktadır.{{% /alert %}}

|**Özellik veya Özellik Kategorisi**|**XML SDK'yı aç**|**Aspose.Cells**|
|:- |:- |:- |
|Desteklenen Excel veya diğer biçimler|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Sekmeyle Ayrılmış, ODS, Düz Metin (TXT), PDF, XPS|
|Excel biçimleri arasında dönüştürme|Numara|Evet|
|<p>Çalışma kitabı nesne modeliyle üst düzey programlama:</p><p>- Bul ve Değiştir.</p><p>- Elektronik tabloları birleştirin.</p><p>- Çalışma kitapları arasında parçaları ve çalışma sayfalarını kopyalayın.</p>|Numara|Evet|
|Belge nesne modeliyle ayrıntılı programlama, tek tek öğelere erişim ve tüm elektronik tablo öğelerinin biçimlendirme özellikleri.|Evet|Evet|
|Bir OOXML belgesinin ilişki tanımlayıcıları, liste tanımlayıcıları gibi temeldeki XML öğelerine ve özniteliklerine düşük düzeyli doğrudan ve tam erişim.|Evet|Numara|
|<p>Raporlar oluşturun, belgeleri verilerle doldurun:</p><p>- Verileri içe/dışa aktarın*Veri tablosu /*Sonuç kümesi.</p><p>- Akıllı İşaretçiler özelliği.</p><p>- Satırları/Sütunları/Aralıkları Ekle/Sil.</p><p>- Özel veri kaynakları.</p>|Numara|Evet|
|<p>Oluşturma ve Yazdırma:* Çalışma sayfası sayfalarını raster görüntülere dönüştürün (TIFF, çok sayfalı TIFF, PNG, JPEG, BMP).*Elektronik tablo sayfalarını vektör görüntülere dönüştürün (EMF).* Grafikleri görüntülere dönüştürün (TIFF, çok sayfalı TIFF, PNG, JPEG, BMP, EMF vb.)</p><p>- Görüntü çözünürlüğünü, kalitesini, sıkıştırmayı ve diğer seçenekleri belirtin. </p><p>- .NET yazdırma altyapısını kullanarak e-tabloları yazdırın. Bileşen, çalışma sayfalarını MS Excel'in Baskı Önizleme'sinde gösterildiği gibi yazdırmak için yerleşik bir yazdırma yöntemine sahiptir.</p>|Numara|Evet|
|Formülleri dinamik olarak hesaplayın/yeniden hesaplayın| Numara| Evet|
|desteklenen platformlar|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Çözüm**
  {{% alert color="primary" %}}Açık XML SDK ve Aspose.Cells, oldukça farklı ihtiyaçlara ve kitlelere hitap ettikleri için kafa kafaya rekabet etmez. Open XML SDK, OOXML belgeleriyle çalışmak için kesin tipte bir yol sağlayan bir sınıf kitaplığıdır. Aspose.Cells, tüm Microsoft Excel ve diğer dosya biçimleri için mükemmel destek sağlayan çok kullanışlı bir elektronik tablo işleme kitaplığıdır. Tek yapmanız gereken bir XLSX belgesinde oldukça basit bir programlama işlemi yapmaksa, Open XML SDK uygun bir seçim olabilir. Open XML SDK ile basit bir XLSX belgesi oluşturmak veya yorumları, üstbilgileri/altbilgileri kaldırmak, görüntüleri ayıklamak veya diğerlerini kaldırmak gibi basit görevleri yaparken oldukça rahat olacaksınız. Bazı görevler Open XML SDK ile gerçekleştirilebilir, ancak Aspose.Cells ile gerçekleştirilemez. Örneğin, bir OOXML belgesinin XML öğelerine ve özniteliklerine doğrudan erişmeniz gerekiyorsa, Open XML SDK kullanmalısınız. belgeler üzerinde aşağıdaki görevlerden bazıları gibi karmaşık işlemler gerçekleştirin, ardından Aspose.Cells'i kullanmak en iyi seçeneğinizdir: XLSX'e ek olarak diğer dosya biçimlerini destekleyin. Çalışma kitapları arasında parçaları ve çalışma sayfalarını kopyalayın veya nesneleri, stilleri ve diğerlerini birleştirecek şekilde çalışma kitaplarını birleştirin. uygun bir şekilde biçimlendirmek. Biçimlendirilmiş veya biçimlendirilmemiş metni değiştirin. Array, ArrayList, DataTable / ResultSet dahil olmak üzere farklı veri kaynaklarından veri içe aktarma gibi üst düzey işlevler. Bir veri kaynağından sipariş ayrıntıları içeren bir sipariş gibi bir iş belgesi oluşturun. Bir belgeyi PDF veya XPS'e dönüştürün, böylece tam olarak Microsoft Excel'in dönüştürdüğü gibi görünür. Bir .NET veya Java uygulaması geliştirin.{{% /alert %}}
