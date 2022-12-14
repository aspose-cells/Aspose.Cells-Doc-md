---
title: beyanname
type: docs
weight: 30
url: /tr/net/declaration/
---
{{% alert color="primary" %}} 

Genel olarak, tüm Aspose .NET bileşenleri, Tam Güven izinlerinin ayarlanmasını gerektirir. Bunun nedeni, Aspose for .NET bileşenlerinin, yazı tiplerini ayrıştırma vb. belirli işlemler için sanal dizin dışındaki sistem dosyalarına ve kayıt defteri ayarlarına erişmesi gerekmesidir. Ayrıca, Aspose for .NET bileşenleri (Aspose.Cells for .NET dahil), Tam Güven izinleri de gerektiren çekirdek .NET sistem sınıflarını temel alır. birçok durumda ayarlayın.

{{% /alert %}} 
## **Kısmi Güven / Orta Güven Zorluğu**
Farklı şirketlerden birden çok uygulamayı barındıran İnternet Servis Sağlayıcıları, çoğunlukla bir Orta Güven güvenlik düzeyi uygular. Ayrıca, bazen bir ISP veya diğer senaryolarda olduğu gibi paylaşılan bir sunucuda birden çok uygulamayı barındırmanız gerekir, uygulamaları sınırlamak için Orta güven düzeyini kullanmanız gerekir. ASP.NET Orta güven düzeyi, ISP sunucularında barındırılan birden çok uygulamayı izole etmeye uygun, kısıtlı bir yürütme ortamı sağlar. .NET 2.0 durumunda, böyle bir güvenlik seviyesi, Aspose.Cells for .NET'in düzgün çalışmasını etkileyebilecek aşağıdaki kısıtlamaları belirleyebilir, örneğin:

- **RegistryPermission kullanılamıyor**. Bu, elektronik tabloları veya diğer belgeleri işlerken yüklü yazı tiplerini numaralandırmak için gerekli olan kayıt defterine erişemeyeceğiniz anlamına gelir.
- **FileIOPermission kısıtlandı**Bu, yalnızca uygulamanızın sanal dizin hiyerarşisindeki dosyalara erişebileceğiniz anlamına gelir. Bu potansiyel olarak yazı tiplerinin dışa aktarma sırasında okunamayacağı anlamına gelir.
## **Orta Güven İzin Setinde Aspose.Cells for .NET kullanın**
Aspose.Cells for .NET'i Medium Trust düzeyinde veya paylaşılan sunucu ortamında çalıştırmak için bazı önerileri uygulayabilirsiniz:

- Lisans dosyasını kodunuzda ayarlamak için, lisans dosyasını akışlara aldıktan sonra bunun yerine License.SetLicense(Stream) yöntemini çağırmanız daha iyi olur.
- Yazı tiplerinin dizini (izinle erişilebilen) ayarlanmalıdır. Sunucudaki dosyaya erişmenin bir yolu yoksa, lütfen uygulamanıza gerekli yazı tipi dosyalarını ekleyin.
- Kısmi güven modunda, Şekilden EMF'ye dönüştürme desteklenmez, bu nedenle dışa aktarılan görüntü türünü (şekiller için) başka bir görüntü formatına ayarlayın.

Orta Güven modunda Aspose.Cells for .NET'in nasıl kullanılacağını/çalıştırılacağını gösteren aşağıdaki örneğe bakın.

{{< highlight "csharp" >}}

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





