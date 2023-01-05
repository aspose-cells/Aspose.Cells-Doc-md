---
title: Genel API Aspose.Cells 8.4.1'deki değişiklikler
type: docs
weight: 150
url: /tr/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.4.0'dan 8.4.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-1/) ve[kaldırılan sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-1/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Veritabanı Bağlantısını Değiştirme Mekanizması**
com.aspose.cells.ExternalConnection sınıfı, bir elektronik tabloda saklanan veritabanı bağlantı ayrıntılarını incelemek için kullanılabilecek yöntemi ve özellikleri zaten içeriyordu. ExternalConnection sınıfıyla ilişkili özelliklerin çoğu, Aspose.Cells for Java 8.4.1 sürümüne kadar salt okunurdu. Bu sürümle birlikte API, veritabanı bağlantı ayarlarını değiştirme desteği de sağlamıştır.

Aşağıdaki kod parçacığı, veritabanı bağlantı ayarlarının dinamik olarak nasıl değiştirileceğini gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

İşte {ExternalConnection}} sınıfı tarafından sunulan en önemli birkaç özellik.

|**Mülkiyet adı** |**Açıklama** |
|:- |:- |
| ArkaplanYenile|Bağlantının arka planda (eşzamansız olarak) yenilenip yenilenemeyeceğini belirtir.<br> true bağlantının tercih edilen kullanımı arka planda eşzamansız olarak yenilemekse;<br> false bağlantının tercih edilen kullanımı ön planda eşzamanlı olarak yenilemekse.|
| BağlantıAçıklaması| Bu bağlantı için kullanıcı açıklamasını belirtir|
| Bağlantı Kimliği| Bu bağlantının benzersiz tanımlayıcısını belirtir.|
| kimlik bilgileri| Bağlantı kurulurken (veya yeniden kurulurken) kullanılacak kimlik doğrulama yöntemini belirtir.|
| Silindi|İlişkili çalışma kitabı bağlantısının silinip silinmediğini gösterir. doğru ise<br> bağlantı silindi; Aksi takdirde, yanlış.|
| Yeni| Bağlantı ilk kez yenilenmediyse doğrudur; Aksi takdirde, yanlış. Bu<br> Durum, bir sorgunun döndürülmesi tamamlanmadan önce kullanıcı dosyayı kaydettiğinde gerçekleşebilir.|
| Hayatta kal|Elektronik tablo uygulamasının bağlantıyı sürdürmek için çaba göstermesi gerektiğinde doğrudur<br> açık. Yanlış olduğunda, uygulama, bağlantıyı aldıktan sonra bağlantıyı kapatmalıdır.<br> bilgi.|
| İsim| Bağlantının adını belirtir. Her bağlantının benzersiz bir adı olmalıdır.|
| OdcDosyası| Bu bağlantının yapıldığı harici bağlantı dosyasının tam yolunu belirtir.<br> oluşturuldu. Verileri yenileme girişimi sırasında bir bağlantı başarısız olursa ve reconnectionMethod=1,<br> ardından elektronik tablo uygulaması, harici bağlantı dosyasındaki bilgileri kullanarak tekrar deneyecektir.<br> çalışma kitabına katıştırılmış bağlantı nesnesi yerine.|
| Yalnızca Bağlantı Dosyasını Kullan| Elektronik tablo uygulamasının her zaman ve yalnızca<br> odcFile özniteliği tarafından belirtilen harici bağlantı dosyasındaki bağlantı bilgileri<br> bağlantı yenilendiğinde. Yanlışsa, elektronik tablo uygulaması<br>reconnectionMethod özniteliği tarafından belirtilen prosedürü izlemelidir|
| parametreler| Bir ODBC veya web sorgusu için ConnectionParameterCollection alır.|
| Yeniden Bağlantı Yöntemi| ReconnectionMethod türünü belirtin|
|Dahili Yenile| Bağlantının otomatik yenilemeleri arasındaki dakika sayısını belirtir.|
| Yüklendiğinde Yenile| Dosya açılırken bu bağlantının yenilenmesi gerekiyorsa doğrudur; Aksi takdirde, yanlış.|
| Veri kaydet|Bir tabloyu doldurmak için bağlantı üzerinden getirilen harici veriler kaydedilecekse doğrudur.<br> çalışma kitabı ile; Aksi takdirde, yanlış.|
| Şifreyi kaydet| Parola bağlantı dizesinin bir parçası olarak kaydedilecekse doğrudur; Aksi takdirde, Yanlış.|
| Kaynak dosyası| Harici veri kaynağı dosya tabanlı olduğunda kullanılır. Böyle bir veriye bağlantı kurulduğunda<br> kaynak başarısız olursa, elektronik tablo uygulaması doğrudan bu dosyaya bağlanmaya çalışır. Belki<br> URI veya sisteme özel dosya yolu notasyonu ile ifade edilir.|
|SSID|Bir aracı arasında kimlik doğrulama için kullanılan Çoklu Oturum Açma (SSO) tanımlayıcısı<br> elektronik tabloML sunucusu ve harici veri kaynağı.|
| Tip| Veri kaynağı türünü belirtir.|

### **DataLabels Metninin Alt Dizisini Formatlama Yeteneği**
Aspose.Cells for Java 8.4.1, ChartPoints.DataLabels alt dizisine karşılık gelen FontSetting sınıfı örneğini almak için DataLabels.characters yöntemini kullanıma sundu. Buna karşılık, FontSetting sınıfının örneği, DataLabels alt dizesini farklı yazı tipi ayarları ve rengiyle biçimlendirmek için kullanılabilir.

Aşağıdaki kod parçacığı, DataLabels.characters yönteminin nasıl kullanılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Elektronik Tablo ve Grafik Dışa Aktarma için İstenilen Görüntü Boyutlarını Ayarlayabilme**
Aspose.Cells for Java 8.4.1, elektronik tabloları ve çizelgeleri görüntülere dışa aktarırken ortaya çıkan görüntünün boyutlarını ayarlamak için ImageOrPrintOptions.setDesiredSize yöntemini kullanıma sundu. ImageOrPrintOptions.setDesiredSize yöntemi, birincisi istenen genişlik ve ikincisi istenen yükseklik olmak üzere iki tamsayı tipi parametreyi kabul eder.

Aşağıdaki kod parçacığı, çalışma sayfasını PNG'e dışa aktarırken istenen boyutların nasıl ayarlanacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Grafikleri görüntülere dönüştürmek için de aynı yöntem kullanılabilir.

{{% /alert %}} 

### **Yorumlar PDF'e işleniyor**
 v8.4.1'in piyasaya sürülmesiyle, Aspose.Cells API, elektronik tabloları PDF biçimine dönüştürürken yorumların işlenmesini kolaylaştırmak için PageSetup.PrintComments özelliğini ve PrintCommentsType numaralandırmasını sağladı. PrintCommentsType numaralandırması aşağıdaki sabitlere sahiptir.

- PrintCommentsType.PRINT_HAYIR_YORUMLAR: Yorumlar yapılmamalıdır.
- PrintCommentsType.PRINT_İÇİNDE_YER: Yorumlar yerleştirildikleri yerde işlenecektir.
- PrintCommentsType.PRINT_ÇARŞAF_END: Yorumlar çalışma sayfasının sonunda işlenecektir.

Aşağıdaki örnek kod, tüm olası PrintCommentsType numaralandırma değerlerini kullanarak yorumları işlemek için PageSetup.PrintComments özelliğinin kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Workbook.isLicensed Özelliği Eklendi**
Aspose.Cells for Java 8.4.1, lisansın başarıyla yüklenip yüklenmediğini belirlemede çok yardımcı olabilecek Workbook.isLicensed'ı kullanıma sundu. Bu özelliğe lisansı ayarlamadan önce erişirseniz, false döndürür ve bunun tersi de geçerlidir, ancak lisansın geçerli olması gerekir.

Aşağıdaki örnek kod, Workbook.isLicensed özelliğinin kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **ImageOrPrintOptions.SVGFitToViewPort Özelliği Eklendi**
Aspose.Cells for Java 8.4.1, elektronik tabloları veya grafikleri SVG formatına dışa aktarırken SVG dosya formatı için viewBox özniteliğini açmak için kullanılabilen ImageOrPrintOptions sınıfı için SVGFitToViewPort özelliğini kullanıma sundu. Bu özelliğin varsayılan değeri yanlıştır, bu nedenle yukarıda belirtilen özellik ayarlanmadan oluşturulan SVG dosyası için temel XML, viewBox özniteliğini içermeyecektir.

Aşağıdaki örnek kod, ImageOrPrintOptions.SVGFitToViewPort özelliğinin kullanımını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **Eski API'ler**
### **Yöntem Workbook.validateFormula Eskimiş**
Formülü doğrulamak için Cell.Formula özelliğini kullanın.
