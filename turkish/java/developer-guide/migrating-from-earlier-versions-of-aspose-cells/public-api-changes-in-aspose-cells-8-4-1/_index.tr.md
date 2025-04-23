---
title: Aspose.Cells 8.4.1 de Genel API Değişiklikleri
type: docs
weight: 150
url: /tr/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sinde 8.4.0'dan 8.4.1'e yapılan değişiklikleri açıklar, modül/uygulama geliştiricileri için ilginç olabilecek yeni ve güncellenmiş genel yöntemlerin yanı sıra [eklenen sınıflar vs.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-1/) ve [kaldırılan sınıflar vs.](/cells/tr/java/public-api-changes-in-aspose-cells-8-4-1/) ve Aspose.Cells'in arka planda olan herhangi bir değişikliklerin bir açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Veritabanı Bağlantısını Değiştirme Mekanizması**
com.aspose.cells.ExternalConnection sınıfı, elektronik tabloda depolanan veritabanı bağlantı ayrıntılarını incelemek için kullanılabilen yöntem ve özellikleri zaten içeriyordu. Aspose.Cells for Java 8.4.1 sürümü ile API, veritabanı bağlantı ayarlarını manipüle etme desteği sağlamıştır.

Aşağıdaki kod örneği, veritabanı bağlantı ayarlarını dinamik olarak nasıl değiştireceğinizi gösterir.

**Java**

{{< highlight csharp >}}

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

{ExternalConnection} sınıfı tarafından sunulan birkaç önemli özellik şunlardır.

|**Özellik Adı** |**Açıklama** |
| :- | :- |
|BackgroundRefresh | Bağlantının arka planda yenilenebilir olup olmayacağını gösterir. <br> Bağlantının tercih edilen kullanımı arka planda asenkron olarak yenilemekse true;<br>Bağlantının tercih edilen kullanımı önde senkron olarak yenilemekse false. |
|ConnectionDescription | Bu bağlantı için kullanıcı açıklamasını belirtir. |
|ConnectionId | Bu bağlantının benzersiz tanımlayıcısını belirtir. |
|Credentials | Bağlantıyı kurarken (veya yeniden kurarken) kullanılacak kimlik doğrulama yöntemini belirtir. |
|IsDeleted | İlişkilendirilen çalışma kitabı bağlantısının silinip silinmediğini gösterir. Eğer<br>bağlantı silinmişse true; aksi takdirde, false |
|IsNew | Bağlantının ilk kez yenilenmediyse True; Aksi takdirde, false. Bu durum, kullanıcının sorgu bitmeden önce dosyayı kaydettiğinde meydana gelebilir. |
|KeepAlive | Elektronik tablo uygulamasının bağlantıyı açık tutmaya çalışması gerekirse True;<br>false ise, bilgi alındıktan sonra bağlantıyı kapatması gerekecektir. |
|Name | Bağlantı adını belirtir. Her bağlantının benzersiz bir adı olmalıdır. |
|OdcFile | Bu bağlantıdan oluşturulan dış bağlantı dosyasının tam yolunu belirtir.<br>Bir bağlantı, verileri yenilemeye çalışırken başarısız olursa ve reconnectionMethod=1 ise,<br> elektronik tablo uygulaması, bağlantı nesnesinin yerine dış bağlantı dosyasındaki bilgileri kullanarak yeniden deneyecektir. |
|OnlyUseConnectionFile | Elektronik tablo uygulamasının bağlantı yenilendiğinde her zaman ve sadece bağlantı bilgilerini odcFile özniteliği tarafından gösterilen dış bağlantı dosyasında kullanıp kullanmamasını belirtir. False, elektronik tablo uygulamasının<br> reconnectionMethod özniteliği tarafından gösterilen prosedürü takip etmesi gerektiğini gösterir. |
|Parameters | Bir ODBC veya web sorgusu için ConnectionParameterCollection'ı alır. |
|ReConnectionMethod | ReconnectionMethod türünü belirtir |
|RefreshInternal| Bağlantının otomatik olarak yenilenmesi arasındaki dakika sayısını belirtir. |
|RefreshOnLoad | Bu bağlantının dosya açıldığında yenilenmesi gerekip gerekmediğini belirtir; Aksi takdirde, false. |
|SaveData | Tabloyu doldurmak için bağlantı üzerinden alınan dış verilerin çalışma kitabıyla birlikte kaydedilip<br>kaydedilmeyeceğini belirtir. Aksi takdirde, false. |
|SavePassword | Şifrenin bağlantı dizesinin bir parçası olarak kaydedilip<br>kaydedilmeyeceğini belirtir. Aksi takdirde, false. |
|SourceFile |Harici veri kaynağı dosya tabanlı olduğunda kullanılır. Böyle bir veri kaynağına bağlantı başarısız olduğunda, elektronik tablo uygulaması doğrudan bu dosyaya bağlanmaya çalışır. URI veya sistem özgü dosya yolu gösterilebilir. |
|SSOId|Tek Oturum Açma (SSO) için kimlik denetimi için kullanılan tanımlayıcıdır. Orta düzeydeki elektronik tabloML sunucusu ile harici veri kaynağı arasındaki kimlik denetimi için kullanılır. |
|Type |Veri kaynağı türünü belirtir. |

### **Veri Etiketleri Metninin Alt Dizgisini Biçimlendirme Yeteneği**
Aspose.Cells for Java 8.4.1, VeriEtiketleri.karakterler methodunun, ChartPoints.DataLabels'ın alt dizgisine karşılık gelen FontSetting sınıfının bir örneğini almak için kullanılmasını sağlamıştır. Sırasıyla, FontSetting sınıfının örneği, VeriEtiketleri'nin alt dizgisini farklı yazı tipi ayarları ve renkle biçimlendirmek için kullanılabilir.

Aşağıdaki kod parçası, VeriEtiketleri.karakterler methodunun nasıl kullanılacağını gösterir.

**Java**

{{< highlight csharp >}}

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

### **Elektronik Tablo ve Grafik Dışa Aktarma İçin İstenen Görüntü Boyutunu Ayarlama Yeteneği**
Aspose.Cells for Java 8.4.1, ImageOrPrintOptions.setDesiredSize methodunu, elektronik tabloların ve grafiklerin görüntüye dışa aktarılırken sonuç görüntünün boyutlarını ayarlamak için kullanılabilir. ImageOrPrintOptions.setDesiredSize methodu, istenen genişlik ve yükseklik olmak üzere iki tamsayı türünden parametreleri kabul eder.

Aşağıdaki kod parçası, çalışma sayfasının PNG olarak dışa aktarılırken istenen boyutların nasıl ayarlanacağını gösterir.

**Java**

{{< highlight csharp >}}

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

Aynı method, grafiklerin görüntülere dönüştürülmesi için de kullanılabilir. 

{{% /alert %}} 

### **PDF'ye Yorumları Oluşturma**
v8.4.1'in yayınlanmasıyla, Aspose.Cells API, elektronik tabloların PDF biçimine dönüştürülürken yorumların oluşturulmasını kolaylaştırmak için PageSetup.PrintComments özelliğini ve PrintCommentsType numaralandırmasını sağlamıştır. PrintCommentsType numaralandırmasında aşağıdaki sabitler bulunmaktadır. 

- PrintCommentsType.PRINT_NO_COMMENTS: Yorumlar oluşturulmayacak.
- PrintCommentsType.PRINT_IN_PLACE: Yorumlar yerleştirildikleri yerde oluşturulacak.
- PrintCommentsType.PRINT_SHEET_END: Yorumlar çalışma sayfasının sonunda oluşturulacak.

Aşağıdaki örnek kod, PageSetup.PrintComments özelliğinin kullanımını, tüm olası PrintCommentsType numaralandırma değerleri kullanarak yorumları oluşturmayı gösterir.

**Java**

{{< highlight csharp >}}

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

### **Lisanslı Workbook.isLicensed Özelliği Eklendi**
Aspose.Cells for Java 8.4.1, Workbook.isLicensed'i kullanıma sunmuştur. Bu özellik, lisansın başarıyla yüklenip yüklenmediğini belirleme konusunda büyük bir yardımcı olabilir. Lisansı ayarlamadan önce bu özelliğe erişirseniz false döndürecektir ve tersi durumda, ancak lisansın geçerli olması gerekir.

Aşağıdaki örnek kod, Workbook.isLicensed özelliğinin nasıl kullanılacağını gösterir.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.4.1, ImageOrPrintOptions sınıfı için SVGFitToViewPort özelliğini kullanıma sunmuştur. Bu özellik, elektronik tabloların veya grafiklerin SVG biçimine dışa aktarılırken viewBox niteliğini açmak için kullanılabilir. Bu özelliğin varsayılan değeri false olduğu için, yukarıdaki özelliği belirlemeden oluşturulan SVG dosyasının temel XML'i viewBox özniteliğini içermeyecektir.

Aşağıdaki örnek kod, ImageOrPrintOptions.SVGFitToViewPort özelliğinin nasıl kullanılacağını gösterir.

**Java**

{{< highlight csharp >}}

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
## **Eskimiş API'lar**
### **Eski Workbook.validateFormula Yöntemi Kaldırıldı**
Formülü doğrulamak için Cell.Formula özelliğini kullanın.
{{< app/cells/assistant language="java" >}}
