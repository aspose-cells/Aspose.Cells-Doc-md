---
title: Genel API Aspose.Cells 8.4.1'deki değişiklikler
type: docs
weight: 140
url: /tr/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.4.0'dan 8.4.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-1/) ve[kaldırılan sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-1/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Veritabanı Bağlantısını Değiştirme Mekanizması**
Aspose.Cells.ExternalConnections.ExternalConnection sınıfı, bir elektronik tabloda saklanan veritabanı bağlantı ayrıntılarını incelemek için kullanılabilecek yöntem ve özellikleri zaten içeriyordu. Aspose.Cells.ExternalConnections.ExternalConnection sınıfıyla ilişkili özelliklerin çoğu, Aspose.Cells for .NET 8.4.1 sürümüne kadar salt okunurdu. Bu sürümle birlikte API, veritabanı bağlantı ayarlarını değiştirme desteği de sağlamıştır.

Aşağıdaki kod parçacığı, veritabanı bağlantı ayarlarının dinamik olarak nasıl değiştirileceğini gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



{Aspose.Cells.ExternalConnections.ExternalConnection}} sınıfı tarafından sunulan en önemli birkaç özelliği burada bulabilirsiniz.

|**Mülkiyet adı**|**Açıklama**|
|:- |:- |
|ArkaplanYenile|Bağlantının arka planda (eşzamansız olarak) yenilenip yenilenemeyeceğini belirtir.<br> true bağlantının tercih edilen kullanımı arka planda eşzamansız olarak yenilemekse;<br>false bağlantının tercih edilen kullanımı ön planda eşzamanlı olarak yenilemekse.|
|BağlantıAçıklaması|Bu bağlantı için kullanıcı açıklamasını belirtir|
|Bağlantı Kimliği|Bu bağlantının benzersiz tanımlayıcısını belirtir.|
|kimlik bilgileri|Bağlantı kurulurken (veya yeniden kurulurken) kullanılacak kimlik doğrulama yöntemini belirtir.|
|Silindi|İlişkili çalışma kitabı bağlantısının silinip silinmediğini gösterir. doğru ise<br>bağlantı silindi; Aksi takdirde, yanlış.|
|Yeni| Bağlantı ilk kez yenilenmediyse doğrudur; Aksi takdirde, yanlış. Bu<br>Durum, bir sorgunun döndürülmesi tamamlanmadan önce kullanıcı dosyayı kaydettiğinde gerçekleşebilir.|
|Hayatta kal|Elektronik tablo uygulamasının bağlantıyı sürdürmek için çaba göstermesi gerektiğinde doğrudur<br> açık. Yanlış olduğunda, uygulama, bağlantıyı aldıktan sonra bağlantıyı kapatmalıdır.<br>bilgi.|
|İsim|Bağlantının adını belirtir. Her bağlantının benzersiz bir adı olmalıdır.|
|OdcDosyası| Bu bağlantının yapıldığı harici bağlantı dosyasının tam yolunu belirtir.<br> oluşturuldu. Verileri yenileme girişimi sırasında bir bağlantı başarısız olursa ve reconnectionMethod=1,<br> ardından elektronik tablo uygulaması, harici bağlantı dosyasındaki bilgileri kullanarak tekrar deneyecektir.<br>çalışma kitabına katıştırılmış bağlantı nesnesi yerine.|
|Yalnızca Bağlantı Dosyasını Kullan| Elektronik tablo uygulamasının her zaman ve yalnızca<br> odcFile özniteliği tarafından belirtilen harici bağlantı dosyasındaki bağlantı bilgileri<br> bağlantı yenilendiğinde. Yanlışsa, elektronik tablo uygulaması<br>reconnectionMethod özniteliği tarafından belirtilen prosedürü izlemelidir|
|parametreler|Bir ODBC veya web sorgusu için ConnectionParameterCollection alır.|
|Yeniden Bağlantı Yöntemi|ReconnectionMethod türünü belirtin|
|Dahili Yenile|Bağlantının otomatik yenilemeleri arasındaki dakika sayısını belirtir.|
|Yüklendiğinde Yenile|Dosya açılırken bu bağlantının yenilenmesi gerekiyorsa doğrudur; Aksi takdirde, yanlış.|
|Veri kaydet|Bir tabloyu doldurmak için bağlantı üzerinden getirilen harici veriler kaydedilecekse doğrudur.<br>çalışma kitabı ile; Aksi takdirde, yanlış.|
|Şifreyi kaydet|Parola bağlantı dizesinin bir parçası olarak kaydedilecekse doğrudur; Aksi takdirde, Yanlış.|
|Kaynak dosyası| Harici veri kaynağı dosya tabanlı olduğunda kullanılır. Böyle bir veriye bağlantı kurulduğunda<br> kaynak başarısız olursa, elektronik tablo uygulaması doğrudan bu dosyaya bağlanmaya çalışır. Belki<br>URI veya sisteme özel dosya yolu notasyonu ile ifade edilir.|
|SSID|Bir aracı arasında kimlik doğrulama için kullanılan Çoklu Oturum Açma (SSO) tanımlayıcısı<br>elektronik tabloML sunucusu ve harici veri kaynağı.|
|Tip|Veri kaynağı türünü belirtir.|

### **DataLabels Metninin Alt Dizisini Formatlama Yeteneği**
Aspose.Cells for .NET 8.4.1, ChartPoints.DataLabels alt dizisine karşılık gelen FontSetting sınıfı örneğini almak için DataLabels.Characters yöntemini kullanıma sundu. Buna karşılık, FontSetting sınıfının örneği, DataLabels alt dizesini farklı yazı tipi ayarları ve rengiyle biçimlendirmek için kullanılabilir.

Aşağıdaki kod parçacığı, DataLabels.Characters yönteminin nasıl kullanılacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Elektronik Tablo ve Grafik Dışa Aktarma için İstenilen Görüntü Boyutlarını Ayarlayabilme**
Aspose.Cells for .NET 8.4.1, elektronik tabloları ve çizelgeleri görüntülere dışa aktarırken ortaya çıkan görüntünün boyutlarını ayarlamak için ImageOrPrintOptions.SetDesiredSize yöntemini kullanıma sundu. ImageOrPrintOptions.SetDesiredSize yöntemi, birincisi istenen genişlik ve ikincisi istenen yükseklik olmak üzere iki tamsayı tipi parametreyi kabul eder.

Aşağıdaki kod parçacığı, çalışma sayfasını PNG'e dışa aktarırken istenen boyutların nasıl ayarlanacağını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Aynı özellik, çizelgeleri resimlere dönüştürmek için de kullanılabilir.

{{% /alert %}} 


### **Yorumlar PDF'e işleniyor**
v8.4.1'in piyasaya sürülmesiyle, Aspose.Cells API, elektronik tabloları PDF biçimine dönüştürürken yorumların işlenmesini kolaylaştırmak için PageSetup.PrintComments özelliğini ve PrintCommentsType numaralandırmasını sağladı. PrintCommentsType numaralandırması aşağıdaki sabitlere sahiptir.

- PrintCommentsType.PrintNoComments: Yorumlar işlenmez.
- PrintCommentsType.PrintInPlace: Yorumlar yerleştirildikleri yerde işlenecektir.
- PrintCommentsType.PrintSheetEnd: Yorumlar çalışma sayfasının sonunda işlenecek.

Aşağıdaki örnek kod, tüm olası PrintCommentsType numaralandırma değerlerini kullanarak yorumları işlemek için PageSetup.PrintComments özelliğinin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Aspose.Cells.GridDesktop'ta Çalışma Sayfalarını Taşı**
Aspose.Cells.GridDesktop, bir çalışma sayfasını belirtilen dizine taşımak için kullanılabilen WorksheetCollection.MoveTo yöntemini sağlar. Bahsedilen yöntem, kaynak çalışma sayfası ve hedef çalışma sayfasının dizinlerini (sıfır tabanlı) parametre olarak alır.

Aşağıdaki örnek kod, WorksheetCollection.MoveTo özelliğinin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Workbook.IsLicensed Özelliği Eklendi**
Aspose.Cells for .NET 8.4.1, lisansın başarıyla yüklenip yüklenmediğini belirlemede çok yardımcı olabilecek Workbook.IsLicensed'ı kullanıma sundu. Bu özelliğe lisansı ayarlamadan önce erişirseniz, false döndürür ve bunun tersi de geçerlidir, ancak lisansın geçerli olması gerekir.

Aşağıdaki örnek kod, Workbook.IsLicensed özelliğinin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **ImageOrPrintOptions.SVGFitToViewPort Özelliği Eklendi**
Aspose.Cells for .NET 8.4.1, elektronik tabloları veya grafikleri SVG formatına dışa aktarırken SVG dosya formatı için viewBox özniteliğini açmak için kullanılabilen ImageOrPrintOptions sınıfı için SVGFitToViewPort özelliğini kullanıma sundu. Bu özelliğin varsayılan değeri yanlıştır, bu nedenle yukarıda belirtilen özellik ayarlanmadan oluşturulan SVG dosyası için temel XML, viewBox özniteliğini içermeyecektir.

Aşağıdaki örnek kod, ImageOrPrintOptions.SVGFitToViewPort özelliğinin kullanımını gösterir.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **Eski API'ler**
### **Yöntem Workbook.ValidateFormula Eskimiş**
Formülü doğrulamak için Cell.Formula yöntemini kullanın.
