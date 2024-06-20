---
title: Bildiri
type: docs
weight: 30
url: /tr/net/declaration/
---

{{% alert color="primary" %}} 

Genellikle, tüm Aspose .NET bileşenleri Tam Güven izinlerinin ayarlanmasını gerektirir. Sebep, Aspose for .NET bileşenlerinin kayıt defteri ayarlarına, parsing fontlar vb. gibi belirli işlemler için sanal dizin dışında sistem dosyalarına erişim gerektirmesidir. Ayrıca, Aspose for .NET bileşenleri (Aspose.Cells for .NET dahil olmak üzere) çoğu durumda Tam Güven izinlerinin ayarlanmasına ihtiyaç duyan çekirdek .NET sistem sınıflarına dayanmaktadır.

{{% /alert %}} 
## **Kısmi Güven / Orta Güven Zorluğu**
Çoğunlukla farklı şirketlerden gelen birden fazla uygulamayı barındıran İnternet Servis Sağlayıcıları genellikle Orta Güvenlik düzeyini zorunlu kılar. Ayrıca, bazen paylaşılan bir sunucuda birden fazla uygulamayı barındırmak zorunda kalabilirsiniz, bu durumda ISP sunucularında barındırılan birden fazla uygulamayı izole etmek için Orta güvenlik düzeyini kullanmanız gerekebilir. ASP.NET Orta güvenlik seviyesi, ISP sunucularında barındırılan birden fazla uygulamayı izole etmek için uygun bir kısıtlı çalışma ortamı sağlar. .NET 2.0'da bir güvenlik seviyesi, Aspose.Cells for .NET’nin doğru bir şekilde çalışmasını etkileyebilecek aşağıdaki kısıtlamaları sağlayabilir:

- **RegistryPermission kullanılamıyor**. Bu, fontları sıralamak için kayıt defterine erişemeyeceğiniz anlamına gelir.
- **FileIOPermission kısıtlıdır**. Bu, yalnızca uygulamanın sanal dizin hiyerarşisindeki dosyalara erişebileceğiniz anlamına gelir. Bu potansiyel olarak dışa aktarma sırasında fontların okunmasını engelleyebilir.
## **Aspose.Cells for .NET'yi Orta Güvenlik İzin Setinde Kullanın**
Aspose.Cells for .NET'yi Orta Güvenlik seviyesinde veya paylaşılan sunucu ortamında çalıştırmak için bazı önerilere uyabilirsiniz:

- Lisans dosyasını kodunuzda ayarlamak için, lisans dosyasını akışlara alıp ardından License.SetLicense(Stream) yöntemini çağırmanız daha iyidir.
- İzinle erişilebilecek fontlar dizini belirtilmelidir. Sunucuda dosyaya erişmenin bir yolu yoksa, gereken font dosyalarını uygulamanıza ekleyin.
- Kısmi güvenlik modunda, Şekil-EMF dönüşümü desteklenmez, bu nedenle (şekiller için) dışa aktarılan görüntü tipini başka bir görüntü formatına ayarlayın.

Aspose.Cells for .NET'yi Orta Güvenlik Modunda Nasıl Kullanacağınızı Gösteren Aşağıdaki Örneğe Bakın

{{< highlight csharp >}}

 // Instantiate the License object

Aspose.Cells.License lic = new Aspose.Cells.License();

// Get the license file into stream

System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

// Set the License stream

lic.SetLicense(stream);

// Close the stream

stream.Close();

// Set the fonts directory

CellsHelper.FontDir = MapPath("~") + @"\Fonts";

//Open the template file

Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

// Set the image type to other format instead of using the default image type, that is, EMF

pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

// Save the PDF file

workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

// Save the XLSX file

workbook.Save(MapPath("~") + @"\dest.xlsx");



{{< /highlight >}}





