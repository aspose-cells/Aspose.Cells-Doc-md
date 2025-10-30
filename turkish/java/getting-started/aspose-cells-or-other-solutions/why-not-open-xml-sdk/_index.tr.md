---
title: Neden Open XML SDK sını Kullanmamalıyız
type: docs
weight: 20
url: /tr/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

Bazı zamanlarda şu soruyu duyarız:

**Neden ücretsiz Open XML SDK'sı yerine Aspose ürünlerini kullanmalıyız?**

Bu soruyu cevaplamak kolaydır: **özellikler ve işlevsellik**.

{{% /alert %}} 
## **Open XML SDK nedir?**
MSDN Kütüphanesine göre, Open XML SDK şu şekilde tanımlanmıştır:Open XML SDK 2.0, paketleri ve paket içindeki Open XML şema öğelerini manipüle etme görevini basitleştirir. Open XML SDK 2.0, geliştiricilerin Open XML paketlerinde gerçekleştirdiği birçok ortak görevi kapsar, böylece karmaşık işlemleri sadece birkaç satır kodla gerçekleştirebilirsiniz. OOXML belgeleri esasen sıkıştırılmış XML dosyalarıdır ve Open XML SDK, OOXML belgelerinin içeriğiyle güçlü bir şekilde çalışmanızı sağlayan bir sınıf koleksiyonudur. Yani, bir dosyayı açıp XML'i çıkarmak, bu XML'i DOM ağacına yüklemek ve XML öğeleri ve nitelikleriyle doğrudan çalışmak yerine, Open XML SDK, bunu yapmak için sınıflar sağlar.
## **Aspose.Cells nedir?**
Aspose.Cells, uygulamanızın aşağıdaki elektronik tablo işleme görevlerini gerçekleştirmesine olanak tanıyan bir sınıf kitaplığıdır: Tüm popüler Excel formatları arasında yüksek kaliteli dönüşümler, PDF, HTML, TIFF ve yazdırma dahil. Bir çalışma kitabı nesne modeli ile programlama. Bir veya birden çok belgeden belge parçaları oluşturma ve veri, stil analizi, grafikler ve grafiklerle otomatik olarak birleştirme yeteneği. Yüksek seviyeli işlevler, Array, ArrayList, DataTable / ResultSet gibi farklı veri kaynaklarından veri alımı da dahil olmak üzere. Neredeyse tüm standart ve gelişmiş Microsoft Excel İşlevlerini destekleyen güçlü Formül Hesaplama Motoru.


## **Open XML SDK ve Aspose.Cells Karşılaştırması**
Aşağıdaki tablo Open XML SDK ve Aspose.Cells özelliklerini karşılaştırıyor. 

|**Özellik veya Özellik Kategorisi**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Desteklenen Excel veya diğer formatlar|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tab Delimited, ODS, Düz Metin (TXT), PDF, XPS|
|Excel formatları arasında dönüşüm yap|Hayır|Evet|
|<p>Bir çalışma kitabı nesne modeli ile yüksek seviyeli programlama:</p><p>- Bul ve değiştir.</p><p>- Elektronik tabloları birleştirmek.</p><p>- Parça ve çalışma kitapları arasında sayfaları kopyalamak.|Hayır|Evet|
|Ayrıntılı belge nesne modeliyle programlama, tüm elektronik tablo elemanlarının ve biçimlendirme özelliklerinin erişimi.|Evet|Evet|
|Düşük seviyeli doğrudan ve tam erişim, ilişki tanımlayıcılar gibi OOXML belgesi listesi tanımlayıcıları gibi temel XML öğelerine ve özniteliklerine.|Evet|Hayır|
|<p>Raporlar oluşturma, belgelere veri yerleştirme:</p><p>- Veri içe/dışa aktarma *DataTable / *ResultSet'dan.</p><p>- Akıllı İşaretçiler özelliği.</p><p>- Satır/Sütun/Aralık Ekle/Sil.</p><p>- Özel veri kaynakları.</p>|Hayır|Evet|
|<p>Render alma ve Baskı:* Sayfa raster görüntülerine çalışma sayfalarını (TIFF, çok sayfalı TIFF, PNG, JPEG, BMP) renderlayın.* Şekil sayfalarını vektör görüntülere (EMF) dönüştürün.* Grafikleri görüntülere dönüştürün(TIFF, çok sayfalı TIFF, PNG, JPEG, BMP, EMF vb.)</p><p>- Görüntü çözünürlüğü, kalitesi, sıkıştırma ve diğer seçenekleri belirtin.</p><p>- .NET baskı altyapısını kullanarak elektronik tabloları yazdırın. Bileşik, MS Excel'in Baskı Önizleme'sinde gösterildiği gibi çalışma sayfalarını yazdırmak için yerleşik baskı yöntemine sahiptir.|Hayır|Evet|
|Formülleri dinamik olarak hesaplayın/yeniden hesaplayın|Hayır|Evet|
|Desteklenen platformlar|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Sonuç**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
