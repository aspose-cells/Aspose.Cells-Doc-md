---
title: Lisanslama
type: docs
weight: 120
url: /tr/net/licensing/
description: Aspose.Cells for .NET, C# Lisanslama ve Abonelik politikaları kullanarak satın alma için farklı planlar veya Ücretsiz Deneme ve değerlendirme için 30 günlük Geçici Lisans sunar.
keywords: C# Diskten veya Akıştan Lisans Uygulama. C# Diskten veya Akıştan Lisans Ayarlama. Aspose.Cells for NET te Lisans Uygulama.
---

## **Aspose.Cells Bileşeninde Lisans Nasıl Uygulanır**

Lisans, ürün adı, lisanslanan geliştiricilerin sayısı, abonelik sona erme tarihi vb. gibi ayrıntıları içeren düz metin XML dosyasıdır. Dosya dijital olarak imzalanmıştır, bu nedenle dosyayı değiştirmeyin. Dosyaya yanlışlıkla bir ek satır eklemek bile dosyayı geçersiz kılacaktır. Aspose.Cells'in değerlendirme sınırlamasından kaçınmak istiyorsanız, Aspose.Cells'i kullanmadan önce bir lisans ayarlamanız gerekir. Lisans, uygulama (veya işlem) başına yalnızca bir kez ayarlanması gereklidir. Lisans, bir dosya, akış veya gömülü bir kaynaktan yüklenebilir.

Aspose.Cells, lisansı aşağıdaki konumlarda aramaya çalışır:

- Açık yolu
- Aspose.Cells.dll'yi içeren klasör
- Aspose.Cells.dll'yi çağıran derlemenin bulunduğu klasör
- Giriş derlemesini (kendi .exe dosyanız) içeren klasör
- Aspose.Cells.dll'yi çağıran derlemede gömülü bir kaynak

Dosyadan veya akıştan lisans uygulamanın iki yaygın yöntemi bulunur.

### **Diskten veya bir akıştan lisans uygulamanın en kolay yolu, lisans dosyasını, bileşenin (Aspose.Cells.GridWeb içeren) dll'sinin bulunduğu klasörle aynı klasöre koymak ve yalnızca dosya adını, yol olmadan belirtmektir.**

Lisansı belirlemenin en kolay yolu, Aspose.Cells.dll dosyasının bulunduğu klasörde lisans dosyasını koymak ve yalnızca dosya adını, yol olmadan belirtmektir.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense yöntemini çağırdığınızda, lisans adı lisans dosya adıyla aynı olmalıdır. Örneğin, lisans dosya adını **Aspose.Cells.lic.xml** olarak değiştirebilirsiniz. Daha sonra kodunuzda, SetLicense yöntemi için değiştirilmiş lisans adını (**Aspose.Cells.lic.xml**) kullanmalısınız.

{{% /alert %}}

Bir lisansı bir akıştan yüklemek de mümkündür.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Saatlik Lisansın Uygulanması**

Aspose.Cells, geliştiricilere saatlik anahtar uygulama imkanı tanır. Bu yeni bir lisanslama mekanizmasıdır. Yeni lisanslama mekanizması, mevcut lisanslama yöntemi ile birlikte kullanılacaktır. API özelliklerinin kullanımına göre faturalandırılmak isteyen müşteriler, saatlik lisanslamayı kullanabilir. Daha fazla bilgi için lütfen [Saatlik Lisanslama SSY](https://purchase.aspose.com/faqs/licensing/metered) bölümüne başvurun.  

Saatlik anahtar uygulamak için yeni bir [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) sınıfı tanıtılmıştır. Aşağıda, saatlik genel ve özel anahtarın nasıl ayarlanacağını gösteren örnek bir kod bulunmaktadır.

{{< highlight csharp >}}

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

### **Bir Gömülü Kaynağın Kullanımı**

Lisansı uygulamanın yanına yerleştirme ve kaybolmamasını sağlamanın başka bir güzel yolu, onu Aspose.Cells'i çağıran derlemelerden birine gömülü bir kaynak olarak eklemektir. Lisans dosyasını gömülü bir kaynak olarak eklemek için aşağıdaki adımları gerçekleştirin:

1. Visual Studio .NET'te, **Dosya** menüsünden **Mevcut Öğe Ekle** seçeneğini seçerek (.lic) lisans dosyasını projeye ekleyin.
1. Çözüm Gezgini'nde dosyayı seçin ve Özellikler penceresinde **Yerleşik Kaynak** seçeneğine **Yapılandırma Eylemi**'ni ayarlayın.

Derlemeye gömülü lisansa (yerleşik kaynak olarak) erişmek için Microsoft .NET Framework'ün System.Reflection.Assembly sınıfının GetExecutingAssembly ve GetManifestResourceStream yöntemlerini çağırmak gerekli değildir. Yapmanız gereken tek şey, lisans dosyasını projenize gömülü bir kaynak olarak eklemek ve SetLicense yöntemine lisans dosyasının adını iletmektir. **Aspose.Cells.License** sınıfı, lisans dosyasını yerleşik kaynaklarda otomatik olarak bulur. Bu lisanslama yönteminin uygulanması hakkında daha fazla ayrıntı için aşağıdaki örneği inceleyin.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Aspose.Cells Grid Kontrollerinde Lisansı Ayarlama**

Aspose.Cells Grid Suite'te lisans, dosyadan, akıştan veya bir gömülü kaynaktan yüklenebilir. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb, lisansı aşağıdaki konumlarda bulmaya çalışır:

1. Belirtilen yol
1. Bileşenin dll'sini içeren klasör (Aspose.Cells.GridDesktop veya Aspose.Cells.GridWeb'in bir parçası olarak)
1. Bileşenin dll'sini çağıran derlemeyi içeren klasör (Aspose.Cells.GridDesktop veya Aspose.Cells.GridWeb'in bir parçası olarak)
1. Giriş derlemesini (yani .exe dosyasını) içeren klasör
1. Bileşenin dll'sini çağıran derlemenin gömülü bir kaynağı olarak (Aspose.Cells.GridDesktop veya Aspose.Cells.GridWeb'in bir parçası olarak)

{{% alert color="primary" %}}

Aspose.Cells.GridDesktop denetimini kullanıyorsanız, lisans sınıfı Aspose.Cells.GridDesktop.License olarak kullanılır, ancak Aspose.Cells.GridWeb denetimini kullanıyorsanız, lisans sınıfı Aspose.Cells.GridWeb.License kullanılır.

{{% /alert %}}

### **Diskten veya bir akıştan lisans uygulamanın en kolay yolu, lisans dosyasını, bileşenin (Aspose.Cells.GridWeb içeren) dll'sinin bulunduğu klasörle aynı klasöre koymak ve yalnızca dosya adını, yol olmadan belirtmektir.**

SetLicense yöntemini çağırdığınızda, lisans adı, lisans dosya adıyla aynı olmalıdır. Örneğin, lisans dosya adını "MyLicense.lic.xml" olarak değiştirebilirsiniz. Daha sonra kodunuzda, SetLicense yöntemi için değiştirilmiş lisans adını (yani MyLicense.lic.xml) kullanmalısınız.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

SetLicense yöntemini çağırdığınızda, lisans adının lisans dosya adıyla aynı olması gerekir. Örneğin, lisans dosya adını "MyLicense.lic.xml" olarak değiştirebilirsiniz. Ardından kodunuzda, lisans adını değiştirilmiş lisans adını (yani MyLicense.lic.xml) SetLicense yöntemi için kullanmalısınız.

{{% /alert %}}

Bir lisansı bir akıştan yüklemek de mümkündür.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Bir Gömülü Kaynak Olarak Lisans Uygulama**

Lisansı uygulamanın yanına yerleştirme ve kaybolmamasını sağlamanın başka bir güzel yolu, onu bileşenin (Aspose.Cells.GridDesktop içeren) derlemelerden birine gömülü bir kaynak olarak eklemektir. Lisans dosyasını gömülü bir kaynak olarak eklemek için aşağıdaki adımları gerçekleştirin:

1. Visual Studio .NET'te, **Dosya** menüsünde **Mevcut Öğe Ekle** seçeneğini kullanarak (.lic) lisans dosyasını projeye ekleyin.
1. Çözüm Gezgini'nde dosyayı seçin ve Özellikler penceresinde **Yapılandırma Eylemi**'ni **Yerleşik Kaynak** olarak ayarlayın.
Derlemeye gömülü bulunan lisansa (yerleşik kaynak olarak) erişmek için, Microsoft .NET Framework'ün System.Reflection.Assembly sınıfının GetExecutingAssembly ve GetManifestResourceStream yöntemleri çağrılmasına gerek yoktur. Yapmanız gereken tek şey, lisans dosyasını projenize gömülü bir kaynak olarak eklemek ve SetLicense yöntemine lisans dosyasının adını iletmektir. Lisans sınıfı, lisans dosyasını yerleşik kaynaklarda otomatik olarak bulur. Bu lisanslama yönteminin uygulanması hakkında daha fazla ayrıntı için aşağıdaki örneği inceleyin.

Bu yöntemi uygulayarak lisansı, gömülü kaynak olarak uygulamanıza entegre edebilirsiniz.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **WinForm Uygulaması için Aspose.Cells.GridDesktop'ta Lisans Uygulama**

Tavsiye edilen uygulama başlamadan önce lisanslama kodunun yerleştirilmesi ve sadece bir kez uygulanması önerilir. Örneğin, bir windows C# uygulaması için, lisanslama kodunu Main metodu içine yerleştirin.

{{< highlight csharp >}}

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

## **Aspose.Cells.GridWeb'de Lisans Uygulanması Notları**

Lisanslama kodunu web uygulamanızın Global.asax.cs dosyasına yerleştirmeniz önerilir (bu lisans dosyasının " d:\ " sürücüsüne konulması varsayılmıştır):

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Bir Akıştan Lisans Yükleme

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
