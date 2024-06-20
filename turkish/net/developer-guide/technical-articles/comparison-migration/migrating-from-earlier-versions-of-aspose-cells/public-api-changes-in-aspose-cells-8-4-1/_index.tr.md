---
title: Aspose.Cells 8.4.1 de Genel API Değişiklikleri
type: docs
weight: 140
url: /tr/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Bu belge, sürüm 8.4.0'dan 8.4.1'e Aspose.Cells API'deki değişiklikleri açıklar ve modül/uygulama geliştiricilerin ilgisini çekebilecek yeni ve güncellenmiş genel yöntemler, [eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-1/) ve [kaldırılan sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-4-1/) yanı sıra Aspose.Cells'in arka plandaki davranışlarındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Veritabanı Bağlantısını Değiştirme Mekanizması**
Aspose.Cells.ExternalConnections.ExternalConnection sınıfı zaten bir elektronik tablo içinde depolanan veritabanı bağlantı ayrıntılarını incelemek için kullanılabilecek yöntem ve özellikleri içeriyordu. Aspose.Cells.ExternalConnections.ExternalConnection sınıfıyla ilişkilendirilen çoğu özellik, Aspose.Cells for .NET 8.4.1 sürümüne kadar salt okunurdur. Bu sürümle birlikte API, veritabanı bağlantı ayarlarını değiştirmeyi desteklemiştir.

Aşağıdaki kod örneği, veritabanı bağlantı ayarlarını dinamik olarak nasıl değiştireceğinizi gösterir.

**C#**

{{< highlight csharp >}}

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



Aşağıda {Aspose.Cells.ExternalConnections.ExternalConnection}} sınıfı tarafından sunulan birkaç önemli özellik bulunmaktadır.

|**Özellik Adı**|**Açıklama**|
| :- | :- |
|BackgroundRefresh|Bağlantının arka planda (asyenkron olarak) yenilenebileceğini gösterir. <br>Bağlantının tercih edilen kullanımının arka planda asenkron olarak yenilenmesi ise true; <br>bağlantının tercih edilen kullanımının ön planda senkron olarak yenilenmesi ise false.|
|ConnectionDescription|Bu bağlantı için kullanıcı açıklamasını belirtir|
|ConnectionId|Bu bağlantının benzersiz kimliğini belirtir.|
|Credentials|Bağlantıyı kurarken (veya yeniden kurarken) kullanılacak kimlik doğrulama yöntemini belirtir.|
|IsDeleted|İlgili elektronik tablo bağlantısının silinip silinmediğini belirtir. Bağlantı silinmişse true; aksi halde false.|
|IsNew|Bağlantının ilk kez yenilenmediğini belirtir. <br>Bu durum, kullanıcının bir sorgu tamamlanmadan dosyayı kaydettiği durumda gerçekleşebilir.|
|KeepAlive|Elektronik tablo uygulamasının bağlantıyı açık tutma çabası göstermesi durumunda true. false ise, uygulama bilgileri alındıktan sonra bağlantıyı kapatmalıdır.|
|Name|Bağlantının adını belirtir. Her bağlantının benzersiz bir adı olmalıdır.|
|OdcFile|Bu bağlantının oluşturulduğu dış bağlantı dosyasının tam yolunu belirtir. Bir bağlantı bir veriyi yenilemeye çalışırken hata oluşursa ve reconnectionMethod=1 ise, elektronik tablo uygulaması, bağlantı nesnesinin içinde değil, dış bağlantı dosyasından gelen bilgileri kullanarak tekrar deneyecektir.|
|OnlyUseConnectionFile|Elektronik tablo uygulamasının bağlantı yenilendiğinde her zaman ve yalnızca odcFile özniteliğinin belirttiği dış bağlantı dosyasındaki bağlantı bilgilerini kullanıp kullanmayacağını belirtir. false ise, elektronik tablo uygulaması, reconnectionMethod özniteliği tarafından belirtilen prosedürü takip etmelidir.|
|Parameters|Bir ODBC veya web sorgusu için ConnectionParameterCollection alır.|
|ReConnectionMethod|Yeniden bağlanma yöntemi türünü belirtir|
|RefreshInternal| Bağlantının otomatik olarak yenilenmesi arasındaki dakika sayısını belirtir.|
|RefreshOnLoad|Dosya açıldığında bu bağlantının yenilenip yenilenmeyeceğini belirtir; aksi takdirde false.|
|SaveData|Bir tabloyu doldurmak için bağlantı üzerinden getirilen dış verilerin elektronik tablo ile birlikte kaydedilip kaydedilmeyeceğini belirtir; aksi takdirde false.|
|SavePassword|Şifrenin bağlantı dizesinin bir parçası olarak kaydedilip kaydedilmeyeceğini belirtir; aksi takdirde false.|
|SourceFile|Dış veri kaynağı dosya tabanlı olduğunda kullanılır. Bir bağlantı başarısız olduğunda, elektronik tablo uygulaması doğrudan bu dosyaya bağlanmaya çalışır. URI veya sistem özgü dosya yolu gösteriminde olabilir.|
|SSOId| Kimlik doğrulama için Ara Sunucu ve dış veri kaynağı arasında kullanılan Tek Oturum Açma (SSO) kimliğini belirtir.|
|Type|Veri kaynağı türünü belirtir.|

### **Veri Etiketleri Metninin Alt Dizgisini Biçimlendirme Yeteneği**
Aspose.Cells for .NET 8.4.1, DataLabels.Characters yöntemini açığa çıkardı ve bu yöntem, bir ChartPoints.DataLabels alt dizisinin karşılık gelen FontSetting sınıfını almak için kullanılır. Sırasıyla, FontSetting sınıfının örneği, DataLabels'in alt dizisini farklı font ayarları ve renkleri ile biçimlendirmek için kullanılabilir.

Aşağıdaki kod örneği, DataLabels.Characters yönteminin nasıl kullanılacağını gösterir.

**C#**

{{< highlight csharp >}}

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


### **Elektronik Tablo ve Grafik Dışa Aktarma İçin İstenen Görüntü Boyutunu Ayarlama Yeteneği**
Aspose.Cells for .NET 8.4.1, ImageOrPrintOptions.SetDesiredSize yöntemini dışa aktarılan elektronik tablolar ve grafikler için sonuç görüntüsünün boyutlarını ayarlamak için kullanılabilir hale getirdi. ImageOrPrintOptions.SetDesiredSize yöntemi, istenen genişlik ve yükseklik olmak üzere iki tamsayı türü parametre kabul eder.

Aşağıdaki kod parçası, çalışma sayfasının PNG olarak dışa aktarılırken istenen boyutların nasıl ayarlanacağını gösterir.

**C#**

{{< highlight csharp >}}

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

Aynı özellik, grafikleri görüntülere dönüştürmek için de kullanılabilir.

{{% /alert %}} 


### **PDF'ye Yorumları Oluşturma**
v8.4.1'in yayınlanmasıyla, Aspose.Cells API, elektronik tabloların PDF biçimine dönüştürülürken yorumların oluşturulmasını kolaylaştırmak için PageSetup.PrintComments özelliğini ve PrintCommentsType numaralandırmasını sağlamıştır. PrintCommentsType numaralandırmasında aşağıdaki sabitler bulunmaktadır.

- PrintCommentsType.PrintNoComments: Yorumlar oluşturulmayacak.
- PrintCommentsType.PrintInPlace: Yorumlar yerleştirildikleri yerde oluşturulacak.
- PrintCommentsType.PrintSheetEnd: Yorumlar çalışma sayfasının sonunda oluşturulacak.

Aşağıdaki örnek kod, PageSetup.PrintComments özelliğinin kullanımını, tüm olası PrintCommentsType numaralandırma değerleri kullanarak yorumları oluşturmayı gösterir.

**C#**

{{< highlight csharp >}}

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


### **Aspose.Cells.GridDesktop'ta Çalışma Sayfalarını Taşıma**
Aspose.Cells.GridDesktop, bir çalışma sayfasını belirtilen dizine taşımak için kullanılabilecek WorksheetCollection.MoveTo yöntemini sağlar. Söz konusu yöntem, kaynak çalışma sayfasının ve hedef çalışma sayfasının (sıfır tabanlı) dizinlerini parametre olarak alır.

Aşağıdaki örnek kod, WorksheetCollection.MoveTo özelliğinin kullanımını gösterir.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Eklendi Workbook.IsLicensed Özelliği**
Aspose.Cells for .NET 8.4.1, Workbook.IsLicensed'ı açığa çıkardı, bu özellik yükün başarıyla yüklenip yüklenmediğini belirlemede büyük bir yardımcı olabilir. Bu özelliğe lisansı ayarlamadan erişirseniz false döndürecektir, tam tersi şekilde, lisansın geçerli olması gerekir.

Aşağıdaki örnek kod, Workbook.IsLicensed özelliğinin kullanımını gösterir.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.4.1, ImageOrPrintOptions sınıfı için SVGFitToViewPort özelliğini açığa çıkardı, bu özellik, elektronik tabloları veya grafikleri SVG biçimine dönüştürürken viewBox özniteliğini etkinleştirmek için kullanılabilir. Bu özelliğin varsayılan değeri false olduğundan dolayı, söz konusu özelliği ayarlamadan oluşturan SVG dosyasının temel XML'i viewBox özniteliğini içermez.

Aşağıdaki örnek kod, ImageOrPrintOptions.SVGFitToViewPort özelliğinin nasıl kullanılacağını gösterir.

**C#**

{{< highlight csharp >}}

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
### **Eskiye Düşmüş Workbook.ValidateFormula Yöntemi**
Formülü doğrulamak için Cell.Formula yöntemini kullanın.
