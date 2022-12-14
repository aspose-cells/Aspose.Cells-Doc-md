---
title: Izgara Verilerini Göndermek için Ortak Bir Düğme Kullanma
type: docs
weight: 20
url: /tr/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb, aşağıdaki gibi bazı yerleşik komut düğmeleri sağlar**Göndermek** ve**Kaydetmek**. İlgili görevleri gerçekleştirmek için bu düğmeleri kullanın.

Bu makale, verilerin yalnızca GridWeb'in yerleşik**Kaydetmek** komut düğmesi, ancak ortak bir ASP.NET Düğmesine (Web Kontrolü) tıklayarak. Bu makalenin amacı Aspose.Cells.GridWeb'in esnekliğini göstermektir. Ayrıca bu makale, istemci tarafı komut dosyasında kullanılmak üzere Aspose.Cells.GridWeb tarafından sunulan özel işlevleri de kullanır.

{{% /alert %}} 
## **ASP.NET Düğmesini Kullanarak Kılavuz Verilerini Gönderme**
Aspose.Cells.GridWeb üç yerleşik düğme sağlar (**Göndermek**, **Kaydetmek** ve**Geri alma** ). GridWeb'de düzenleme yaptıktan sonra, bir kullanıcı**Göndermek** veya**Kaydetmek** GridWeb'in verileri sunucuya göndermesine izin vermek için Sekme Çubuğundaki düğme. Kullanıcı bir Sayfa Sekmesine tıklarsa, GridWeb denetimi yerleşik komut düğmeleriyle aynı görevi gerçekleştirir. Aspose.Cells.GridWeb, bu işlevi ortak bir ASP.NET Düğme denetimine eklemeyi de destekler, ancak uygulamaya bazı ekstra kodlar eklemeniz gerekir.
### **1. Test Uygulaması Oluşturma**
Visual Studio.NET IDE'nizi açın ve yeni bir ASP.NET Web Uygulaması projesi oluşturun. Uygulama oluşturulduktan sonra, projenize varsayılan bir WebForm1.aspx sayfası eklenecektir. GridWeb kontrolünü Araç Kutunuzdan Web Formuna sürükleyip bırakın. Araç Kutunuzda GridWeb kontrolünü bulamıyorsanız, bu sayfaya bakın:[Aspose.Cells Izgara Denetimlerini Visual Studio.NET ile entegre edin](/cells/tr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) Web Formunuza GridWeb denetimi eklendikten sonra, Toolbox'tan Web Formunuza bir Button web denetimi de ekleyin.
### **2. Page_Load Olayına Kod Ekleme**
Şimdi, Sayfaya biraz kod ekleme zamanı_Web Formunun yükleme olayı. Tasarım görünümünde Web Formuna çift tıklayabilirsiniz ve VS.NET IDE sizi otomatik olarak Sayfaya götürür_OnClick olayını geçersiz kılmak için Button'ın Nitelikler koleksiyonunu kullanmanız gereken yerde olay işleyicisini yükleyin.

{{% alert color="primary" %}} 

ASP.NET Düğme denetimi, bir sunucu tarafı denetimidir. Her tıklandığında, bir sunucu tarafı olayı tetiklenir, ancak bu Düğme kontrolünü istemci tarafında (normalde javascript kullanarak) bazı kodları yürütmek için kullanmak istiyorsanız, Page_Load olayı altındaki onclick özniteliğini değiştirmeniz gerekir. Aspose.Cells.GridWeb, istemci tarafından GridWeb denetimiyle ilgilenmek için javascript'te çağrılabilen bazı işlevler sağlar. Aşağıdaki örnekte, Grid verilerini güncellemek ve doğrulamak için GridWeb'in updateData & validall işlevlerini (istemci tarafı işlevleridir) kullandık.

{{% /alert %}} 
#### **Kod Örneği**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Uygulamayı Çalıştırma**
Artık Ctrl+F5 tuşlarına basarak uygulamanızı derleyebilir ve çalıştırabilirsiniz; sayfa yeni bir tarayıcı penceresinde açılacaktır. GridWeb'e bazı değerler ekleyelim ve Grid Verilerini Sunucuya Gönder düğmesine basalım ve GridWeb verilerini güncellemek ve doğrulamak için bir geri gönderme yapıldığını göreceksiniz.
## **Çözüm**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, sunucu veya istemci tarafında GridWeb kontrolleriyle çalışmak için büyük esneklik sunar. Geliştiriciler, müşterilerine daha iyi çözümler sağlamak için GridWeb kontrolünü farklı türde senaryolarda kullanmak için çok sayıda seçeneğe sahiptir.

{{% /alert %}}
