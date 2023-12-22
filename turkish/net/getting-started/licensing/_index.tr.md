---
title: Licensing
type: docs
weight: 120
url: /tr/net/licensing/
description: Aspose.Cells for .NET, farklı satın alma planları sunar veya Licensing'i ve C#'deki Abonelik politikalarını kullanarak değerlendirme için Ücretsiz Deneme ve 30 günlük Geçici Lisans sunar.
keywords: Apply License from Disk or Stream. Set License from Disk or Stream. Apply License in Aspose.Cells.
---
{{% alert color="primary" %}}

 Aspose.Cells'in değerlendirme sürümünü buradan kolayca indirebilirsiniz.[indirme sayfası](https://www.nuget.org/packages/Aspose.Cells) @ NuGet depo. Değerlendirme sürümü, bileşenin lisanslı sürümüyle kesinlikle aynı yetenekleri sağlar. Ayrıca, bir lisans satın aldığınızda ve lisansı uygulamak için birkaç satır kod eklediğinizde değerlendirme sürümü kolayca lisanslanır.

{{% /alert %}}

##  **Değerlendirme Sürümü Sınırlamaları**

Aspose.Cells ürününün değerlendirme sürümü (lisans belirtilmeden) tam ürün işlevselliği sağlar, ancak bir programda 100 dosya açmak ve değerlendirme filigranı içeren ekstra bir çalışma sayfasıyla sınırlıdır.

Sınırlamalar aşağıda gösterilmiştir:

- **Açılan Dosya Sayısı** (Aspose.Cells)
 Programınızı çalıştırırken Aspose.Cells kütüphanesini kullanarak sadece 100 adet Excel dosyasını açabilirsiniz. Başvurunuz bu sayıyı aşarsa bir istisna atılacaktır.
- **Yapılandırma dosyası ayarları**(Aspose.Cells.GridWeb)
 Aşağıdaki kod satırlarını yapılandırma bölümüne (örneğin web.config dosyasına) ekleyerek komut dosyasının yolunu yeniden belirleyemezsiniz. Acw_client, dosyaları içeren bir klasördür ve Aspose.Cells.GridWeb, dahili yapılandırmasını yönetmek için bu klasörü kullanır. İçinde GridWeb'in davranışını belirlemek ve diğer işlemleri ayarlamak için komut dosyaları, görüntü dosyaları ve diğer dosyalar bulunur. Yapılandırma dosyası, kontrolün bazı durumlarda/senaryolarda yararlı olan gömülü istemci kaynaklarını (resimler, komut dosyaları vb.) kullanmasını önlemek için kullanılır. Ayrıca web.config dosyasındaki bu yapılandırma ayarları yalnızca kontrolün LİSANSLI sürümünde geçerli olacaktır.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Dosya Sistemi Web Sitelerinde veya MS Ajax uzantılarında vb. Aspose.Cells.GridWeb kontrolünü kullanıyorsanız bazı durumlarda/senaryolarda bu ayarlar zorunlu olabilir.

{{% /alert %}}

Ayrıca, değerlendirme filigranı içeren bir çalışma sayfası, Aspose.Cells kütüphanesi kullanılarak oluşturulan excel dosyasında her zaman aktif çalışma sayfası olarak görünecektir. Yalnızca lisanslı sürümde etkin çalışma sayfasını diğer çalışma sayfalarına ayarlayabilirsiniz. PDF çıktısında veya Aspose.Cells görüntü dosyasında, belgenin/görüntünün üst kısmına bir değerlendirme filigranı yapıştırılır. Değerlendirme Telif Hakkı Uyarısını (ekstra çalışma sayfası) GridWeb kontrolünde de gizleyemezsiniz, her zaman eklenecektir (çalışma sayfası sekmelerinin sonunda) kontrolde.

{{% alert color="primary" %}}

 Aspose.Cells'i değerlendirme sürümü sınırlaması olmadan test etmek istiyorsanız, ayrıca bir talepte bulunabilirsiniz.[30 Günlük Geçici Lisans](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

##  **Aspose.Cells Bileşeninde Lisans Nasıl Başvurulur**

Lisans, ürün adı, lisanslandığı geliştirici sayısı, aboneliğin sona erme tarihi vb. ayrıntıları içeren düz metinli bir XML dosyasıdır. Dosya dijital olarak imzalanmıştır, dolayısıyla dosyayı değiştirmeyin. Dosyaya yanlışlıkla fazladan bir satır sonu eklenmesi bile dosyayı geçersiz kılacaktır. Değerlendirme sınırlamasından kaçınmak istiyorsanız Aspose.Cells'i kullanmadan önce bir lisans ayarlamanız gerekir. Her uygulama (veya işlem) için yalnızca bir kez lisans ayarlamanız gerekir. Lisans bir dosyadan, akıştan veya yerleşik bir kaynaktan yüklenebilir.

Aspose.Cells, lisansı aşağıdaki konumlarda bulmaya çalışır:

- Açık yol
- Aspose.Cells.dll dosyasını içeren klasör
- Aspose.Cells.dll adlı derlemeyi içeren klasör
- Giriş derlemesini içeren klasör (.exe'niz)
- Derlemede Aspose.Cells.dll adlı gömülü bir kaynak

Lisansı uygulamanın dosyadan, akıştan veya gömülü kaynak olarak iki yaygın yöntemi vardır.

###  **Diskten veya Akıştan Lisans Nasıl Uygulanır?**

Lisans ayarlamanın en kolay yolu, lisans dosyasını Aspose.Cells.dll ile aynı klasöre koymak ve yolu olmadan sadece dosya adını belirtmektir.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense yöntemini çağırdığınızda lisans adı, lisans dosya adınızla aynı olmalıdır. Örneğin, lisans dosyası adını *Aspose.Cells.lic.xml** olarak değiştirebilirsiniz. Daha sonra kodunuzda SetLicense yöntemi için değiştirilmiş lisans adını (**Aspose.Cells.lic.xml**) kullanmalısınız.

{{% /alert %}}

Bir akıştan lisans yüklemek de mümkündür.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Ölçülü Lisans Nasıl Başvurulur**

Aspose.Cells, geliştiricilerin ölçülü anahtar uygulamasına olanak tanır. Yeni bir lisanslama mekanizmasıdır. Yeni lisanslama mekanizması mevcut lisanslama yöntemiyle birlikte kullanılacaktır. API özelliğinin kullanımına göre faturalandırılmak isteyen müşterilerimiz, ölçülü lisanslamayı kullanabilirler. Daha fazla ayrıntı için lütfen bkz.[Ölçülü Licensing SSS](https://purchase.aspose.com/faqs/licensing/metered)bölüm.

Yeni bir sınıf[Ölçülü](https://reference.aspose.com/cells/net/aspose.cells/metered)ölçülü anahtarı uygulamak için tanıtıldı. Ölçülü genel ve özel anahtarın nasıl ayarlanacağını gösteren örnek kod aşağıda verilmiştir.

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

###  **Gömülü Kaynak Nasıl Kullanılır**

Lisansı uygulamanızla birlikte paketlemenin ve kaybolmamasını sağlamanın bir başka düzgün yolu da, onu Aspose.Cells'i çağıran derlemelerden birine gömülü kaynak olarak eklemektir. Lisans dosyasını gömülü kaynak olarak eklemek için aşağıdaki adımları uygulayın. :

1.  Visual Studio .NET'de lisans (.lic) dosyasını seçim yaparak projeye ekleyin**Mevcut Öğeyi Ekle** itibaren**Dosya** Menü.
1.  Çözüm Gezgini'nde dosyayı seçin ve ayarlayın.**Eylem Oluştur** ile**Gömülü Kaynak** Özellikler penceresinde

Derlemeye katıştırılmış lisansa (gömülü kaynak olarak) erişmek için, Microsoft .NET Framework'ün System.Reflection.Assembly sınıfının GetExecutingAssembly ve GetManifestResourceStream yöntemlerini çağırmak gerekli değildir. Yapmanız gereken tek şey, lisans dosyasını projenize gömülü kaynak olarak eklemek ve lisans dosyasının adını SetLicense yöntemine iletmektir.**Aspose.Cells.License** class, lisans dosyasını gömülü kaynaklarda otomatik olarak bulacaktır. Uygulamalarınızda lisans (gömülü) ayarlama yöntemini anlamak için lütfen aşağıda verilen örneği inceleyin.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Aspose.Cells Izgara Kontrollerinde Lisans Nasıl Ayarlanır**

Aspose.Cells Grid Suite'te lisans bir dosyadan, akıştan veya gömülü bir kaynaktan yüklenebilir. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb, lisansı aşağıdaki konumlarda bulmaya çalışır:

1. Açık yol
1. Bileşenin dll'sini içeren klasör (Aspose.Cells.GridDesktop veya Aspose.Cells.GridWeb'de bulunur)
1. Bileşenin dll'sini çağıran derlemeyi içeren klasör (Aspose.Cells.GridDesktop veya Aspose.Cells.GridWeb'de bulunur)
1. Giriş derlemesini içeren klasör (.exe'niz)
1. Bileşenin dll'sini çağıran derlemede yerleşik bir kaynak (Aspose.Cells.GridDesktop veya Aspose.Cells.GridWeb'de bulunur)

{{% alert color="primary" %}}

Aspose.Cells.GridDesktop kontrolünü kullanıyorsanız lisans sınıfı Aspose.Cells.GridDesktop.License olarak kullanılacaktır, ancak Aspose.Cells.GridWeb kontrolünü kullanıyorsanız lisansı ayarlamak için Aspose.Cells.GridWeb.License sınıfı kullanılacaktır.

{{% /alert %}}

###  **Diskten veya Akıştan Lisans Nasıl Uygulanır?**

Bir lisans ayarlamanın en kolay yolu, lisans dosyasını bileşenin dll dosyasıyla (Aspose.Cells.GridWeb'de bulunur) aynı klasöre koymak ve yolu olmadan yalnızca dosya adını belirtmektir.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense yöntemini çağırdığınızda lisans adı, lisans dosya adınızla aynı olmalıdır. Örneğin lisans dosyasının adını "MyLicense.lic.xml" olarak değiştirebilirsiniz. Daha sonra kodunuzda SetLicense yöntemi için değiştirilmiş lisans adını (yani MyLicense.lic.xml) kullanmalısınız.

{{% /alert %}}

Bir akıştan lisans yüklemek de mümkündür.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Gömülü Kaynak Olarak Lisans Nasıl Başvurulur**

Lisansı uygulamanızla birlikte paketlemenin ve kaybolmayacağından emin olmanın başka bir düzgün yolu, onu bileşenin dll'sini (Aspose.Cells.GridDesktop'a dahil) çağıran derlemelerden birine gömülü bir kaynak olarak eklemektir. Lisans dosyasını katıştırılmış kaynak olarak eklemek için aşağıdaki adımları gerçekleştirin:

1.  Visual Studio .NET'de, lisans (.lic) dosyasını kullanarak projeye ekleyin.**Mevcut Öğeyi Ekle** seçeneği**Dosya** Menü.
1. Çözüm Gezgini'nde dosyayı seçin ve Özellikler penceresinde Eylem Oluştur'u Katıştırılmış Kaynak olarak ayarlayın.
1. Derlemeye katıştırılmış lisansa (gömülü kaynak olarak) erişmek için, Microsoft .NET Framework'ün System.Reflection.Assembly sınıfının GetExecutingAssembly ve GetManifestResourceStream yöntemlerini çağırmanıza gerek yoktur. Bunun yerine, lisans dosyasını sisteminize katıştırılmış bir kaynak olarak ekleyin. projeyi oluşturun ve lisans dosyasının adını SetLicense yöntemine iletin. License sınıfı, lisans dosyasını gömülü kaynaklarda otomatik olarak bulur.

Bir lisansı uygulamalarınıza gömülü bir kaynak olarak uygulamanın bu yöntemini anlamak için lütfen aşağıda verilen örneği inceleyin.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **WinForm Uygulaması için Aspose.Cells.GridDesktop'ta Lisans Nasıl Başvurulur**

Lisans kodunuzu başvurunuz başlamadan önce girmeniz ve yalnızca bir kez uygulamanız önerilir. Örneğin, bir Windows C# uygulaması için lisans kodunu Main yöntemine koyun.

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

##  **Aspose.Cells.GridWeb'de Lisans Başvurusuna İlişkin Notlar**

Lisans kodunu web uygulamanızın Global.asax.cs dosyasına yerleştirmeniz önerilir (bu lisans dosyasının " d:\ " sürücüsüne konulduğu varsayılır):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Akıştan Lisans Yükleme

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
