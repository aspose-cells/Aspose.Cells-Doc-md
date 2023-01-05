---
title: Zarif Bir Grafikle Dinamik Olarak Biçimlendirilmiş Excel Raporları Oluşturun
type: docs
weight: 130
url: /tr/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Bu belge, bazı veri kaynaklarından verileri kontrol gibi muhteşem bir ızgaraya nasıl çıkarabileceğimiz, içine bir grafik yapıştırabileceğimiz ve analiz, karşılaştırmalar ve yazdırma yapmak için grafikli raporu MS Excel'e nasıl aktarabileceğimiz konusunda gerekli bilgileri sağlamak için tasarlanmıştır.

{{% /alert %}} 
## **genel bakış**
Birlikte iyi çalışabilecek parçaların veya nesnelerin bir kombinasyonu olan Raporlama ve Sunumları gerektiren belirli web senaryoları vardır. Makale, WYSIWYG tarzında dinamik olarak şık excel raporları tasarlamanın ve oluşturmanın ne kadar kolay olduğunu açıklıyor. Verilere zengin ve çekici format uygulamanıza ve MS Excel gibi formül sonuçlarını hesaplamanıza izin veren gerçek ortamı sağlayan Aspose.Cells.GridWeb kontrolüne bir XML dosyasından (diğer veri kaynaklarından da yararlanabilirsiniz) veri aktarır. Ayrıca, Çalışma Sayfası kaynak verilerine dayalı olarak gelişmiş bir grafik oluşturur.[Aspose.Cells](https://products.aspose.com/cells/) bileşenini kullanır ve grafik görüntüsünü Satış Raporuna yapıştırır. Son olarak, grafik ekli excel raporu Aspose.Cells bileşeni kullanılarak diske kaydedilir.

Bu makale, bu tür işlevsellik için kaynak kodunu ve tam özellikli demo projesini içerir.

Kullanıcıların, bir iş raporunun nasıl oluşturulacağına ilişkin ayrıntılı bir kavrayışa sahip olarak, tablonun bir çalışma sayfasına veri girmesine ve satır ve sütunlardaki hücrelere biraz biçimlendirme uygulamasına, verileri kaydetmeden önce verilerin kaynak aralığına dayalı bir grafiği gömmesine olanak tanır. diske excel raporu.
## **Aspose Bileşenleri**
 üç tane kullanıyorum[Aspose](http://www.aspose.com/) Görevi kolaylıkla gerçekleştirmek için bileşenleri.[Aspose](http://www.aspose.com/) , .NET ve Java Component Publisher, zengin özelliklere sahip çeşitli bileşenler sağlar.[Aspose](http://www.aspose.com/) .NET ve Java bileşenlerinden oluşan harika bir seri sunar. Dünya çapında binlerce müşterinin güvendiği ürünler, DOC, RTF, WordML dahil olmak üzere çeşitli biçimlerdeki belgeleri programlı olarak açmaya, değiştirmeye, oluşturmaya, kaydetmeye, birleştirmeye, dönüştürmeye vb. izin veren Dosya Biçimi Bileşenleri, Raporlama Ürünleri, Görsel Bileşenler ve Yardımcı Program Bileşenlerini içerir. HTML, PDF, XLS, SpreadsheetML, Sekmeyle Ayrılmış, CSV, PPT, SWF, EMF,WMF, MPX, MPD ve diğer formatlar.

Bu macerada kullanılmış olan bu bileşenlerden üçünü size tanıtmak için bu fırsatı değerlendireceğim.
## **Aspose.Cells Izgara Kontrolleri**
 Aspose.Cells Şebeke Kontrolleri, toplam şebeke çözümüdür. Aspose.Cells Izgara Kontrolleri, iki farklı GUI .NET bileşeni (Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb) ile paketlenmiş olarak gelir: biri masaüstü uygulamalarını, diğeri web uygulamalarını desteklemek için. Her iki platformda da uygulamayı bir çırpıda yapmak için her iki sürüm de eşit şekilde eşleştirilir. Aspose.Cells.GridWeb, Excel elektronik tablolarından içeri ve dışarı aktarma yeteneği sağlar. Böylece Excel'e aşina olan herkes (hatta son kullanıcılar) bir ızgaranın görünümünü ve hissini tasarlayabilir. Aspose.Cells.GridWeb ayrıca, geliştiricilere ızgaralarının görünümü, hissi ve davranışı üzerinde tam kontrol sağlayan, kullanımı kolay, zengin özelliklere sahip bir API sunar. Ürün ve özellikleri hakkında daha fazla bilgi edinmek ve bir programcı kılavuzu için lütfen Özellikler Listesinin özetini, Aspose.Cells.GridWeb Belgelerini ve çevrimiçi özellikleri kontrol edin.[Demolar](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**istemci veya sunucu tarafında kurulacak Microsoft Excel'i kullanmadan Excel elektronik tablolarını okumanızı ve yazmanızı sağlayan bir Excel elektronik tablo raporlama bileşenidir.**Aspose.Cells** verilerin temel dışa aktarımından çok daha fazlasını sunan, zengin özelliklere sahip bir bileşendir. İle birlikte**Aspose.Cells** geliştiriciler verileri dışa aktarabilir, elektronik tabloları her ayrıntıda ve her düzeyde biçimlendirebilir, görüntüleri içe aktarabilir, çizelgeleri içe aktarabilir, grafikler oluşturabilir, çizelgeleri değiştirebilir, Excel verilerini aktarabilir, XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) entegre) ve çok daha fazlası.**Aspose.Cells** kullanımı kolay, zengin özelliklere sahip bir**API** programcılar için. Çok geniş bir özellik listesine sahiptir. Ürün, özellikleri ve programcı kılavuzu hakkında daha fazla bilgi edinmek için lütfen özetini kontrol edin.**Özellikler Listesi**, **Aspose.Cells Dokümantasyon** ve çevrimiçi özellikli Demolar. Yapabilirsin[indirmek](https://downloads.aspose.com/cells) ücretsiz değerlendirme sürümü.
## **Arayüzü Tasarlamak**
Visual Studio.Net'te yeni bir Asp.Net web uygulaması oluşturmaya başlıyoruz.

 ben**Referans ekle**önce projeye ieAspose.Cells.GridWeb.dll, Aspose.Chart.dll ve Aspose.Cells.dll olmak üzere üç bileşene. Sayfaya biraz kontrol yerleştiriyorum ve özelliklerini, yani bir açılır liste, bir komut düğmesi ve bir etiket ayarlıyorum. sonra yerim**Aspose.Cells.GridWeb****kontrol**(**GridWeb**) araç kutusundan ekleyin, çünkü üç bileşene referanslar eklendikten sonra**GridWeb**kontrol araç kutusunda belirir. Diğer iki bileşen (**Aspose.Chart**ve**Aspose.Cells**) yalnızca kitaplıklardır, yalnızca projeye başvurulur.

Ayrıca "file" ve "images" olmak üzere iki klasör oluşturuyorum, bu klasörlere sırasıyla "Products.xml" ve "chart.gif"i ekliyorum. Xml dosyası, verilerin doldurulması için çıkarılacağı bir veri kaynak dosyasıdır.**GridWeb**çalışma kağıdı. Resim dosyası, üzerine yerleştirilen özel bir düğme için bir resim sağlayacaktır.**GridWeb**kontrol.

Şimdi, özel bir komut düğmesi oluşturuyorum. Ben sadece sağ tıklayın**GridWeb**kontrol edin ve "Özel Komut Düğmeleri..." seçeneğini tıklayın.

Özel Komut Düğmesi düzenleyicisini etkinleştirir, düzenleyici araç ipucu eklenmiş özel komut görüntü düğmeleri oluşturmanıza olanak tanır. Komut (Ad) ->"btnChart", ImageUrl -> resim dosyasının yolunu ("chart.gif") vermek ve ToolTip -> araç ipucu vermek gibi düğmenin bazı özellikleri için değerleri belirtiyorum.

Böylece, aşağıdaki ekran görüntüsünde görebileceğiniz gibi (kırmızı renkle çevrelenmiş) özel komut düğmesi eklenir.

|![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Son olarak, etiket ve komut düğmesi için bazı Font nitelikleri (kalın) ayarladım. Son görünümü elde etmek için kontrollerin boyutunu da ayarlıyorum.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Bir XML Dosyasından Veri Alma**
Projede kullanılan XML dosya yapısı aşağıdadır.
### **XML Dosya Yapısı**
**xml**

{{< highlight "csharp" >}}

 <?xml version="1.0" standalone="yes"?>

<SalesData>

  <Products>

    <ProductName>Data</ProductName>

    <QuantityPerUnit>Data</QuantityPerUnit>

    <CategoryName>Data</CategoryName>

    <UnitPrice>Data</UnitPrice>

    <Sale>Data</Sale>

  </Products>

 .........

</SalesData>



{{< /highlight >}}

{{< highlight "java" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

if (!IsPostBack)

{

	// Uncomment the code below when you have purchased license

	// for Aspose.Cells.GridWeb, Aspose.Chart and Aspose.Cells. You need

	// to deploy the licenses in the same folder as your executable,

      // alternatively you can add the license files as an embedded

      // resource to your project.

	//

	// Set the license for Aspose.Cells.GridWeb

	// Aspose.Cells.GridWeb.License gridwebLicense = new

	// Aspose.Cells.GridWeb.License();

	// gridwebLicense.SetLicense("Aspose.Grid.lic");

	//

	// // Set the license for Aspose.Chart

	// Aspose.Chart.License chartLicense = new

	// Aspose.Chart.License();

	// chartLicense.SetLicense("Aspose.Chart.lic");

	//

	// // Set the license for Aspose.Cells

	// Aspose.Cells.License cellsLicense = new

	// Aspose.Cells.License();

	// cellsLicense.SetLicense("Aspose.Cells.lic");

	//Create a DataSet object.

	DataSet ds = new DataSet();

	//Get the Virtual Folder Path.

	string path = MapPath(".");

	//Reads XML data from xml file into DataSet object.

	ds.ReadXml(path + "\\file\\Products.xml");

	//Call the custom method to obtain distinct values from

	//CategoryName field and store data into an object array.

	object [] drs = GetDistinctValues(ds.Tables[0],"CategoryName");

	//Fill the drop down list with distinct field items.

	for(int i = 0;i<drs.Length;i++)

	{

		DropDownList1.Items.Add(drs[i].ToString());

	}

}

}

//This method is used to filter distinct values from CategoryName field in the datatable.

private object[]GetDistinctValues(DataTable dtable, string colName)

{

	// Create a Hashtable object.

	Hashtable hTable = new Hashtable();

	// Loop through the datatable rows and add distinct values to

	// Hashtable object minimizing the duplicates in the field.

	foreach (DataRow drow in dtable.Rows)

	if(!hTable.ContainsKey(drow[colName]))

	hTable.Add(drow[colName], string.Empty);

	// Create an object array based on the distinct key values of the Hashtable object.

	object[] objArray = new object[hTable.Keys.Count];

	// Copy the disctinct values to fill the array.

	hTable.Keys.CopyTo(objArray, 0);

	// Return the array object.

	return objArray;

}

{{< /highlight >}}
## **Aspose.Cells.GridWeb kontrolünün Çalışma Sayfasını Veri ile doldurma**
Bazı API kullanıyorum**GridWeb**bir çalışma sayfasını kaynak XML dosyasındaki verilerle doldurma denetimi. Komut düğmesinin ("Raporu Göster" etiketli) tıklama olay işleyicisine kod yazıyorum. Veri raporu, açılır listeden seçilen öğeye göre filtrelenir.



{{< highlight "java" >}}

 //Clears datasheets of the GridWeb control.

GridWeb1.WebWorksheets.Clear();

//Create a DataSet object.

DataSet ds = new DataSet();

//Get the Virtual Folder path.

string path = MapPath(".");

//Reads XML data from xml file into DataSet object.

ds.ReadXml(path + "\\file\\Products.xml");

//Create a DataView based on the datatable.

DataView dv = new DataView(ds.Tables[0]);

//Filter data in the DataView object based on the selected drop down list item.

dv.RowFilter = "CategoryName ='" + DropDownList1.SelectedItem.Text + "'";

//Importing data from the filtered DataView object to create and

//fill "Products" Worksheet start from A4 cell.

GridWeb1.WebWorksheets.ImportDataView(dv, null, null,"Products",3,0);

{{< /highlight >}}
## **Cells'de Verileri Biçimlendirme**
Bir çalışma sayfasındaki farklı bilgi türleri arasında ayrım yapmak, çalışma sayfanızdaki verilerin en iyi şekilde görüntülenmesi ve bir çalışma sayfasının taranmasını kolaylaştırmak için çalışma sayfasını biçimlendirirsiniz. A**Biçim**bir stili temsil eder ve yazı tipleri ve yazı tipi boyutları, sayı biçimleri, hücre sınırları, düz arka plan rengiyle hücre gölgelendirmesi veya belirli bir renk deseni, hücrelerde girinti, hizalama ve metin yönü gibi bir dizi özellik olarak tanımlanır.

Yukarıya birkaç kod satırı daha birleştiriyorum. Raporun başlığını / alt başlığını yerleştiriyorum, başlık, alt başlık ve detay hücrelerine bazı biçimlendirmeler yapıyorum. Ayrıca iki alana da sayı biçimlendirmesi uyguluyorum (para birimi sayı biçimini UnitPrice ve Sale alanlarına ayarla) ve satırların ve sütunların yüksekliğini/genişliğini şunu kullanarak ayarlıyorum:**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 //Sayfada başlık hücresini (A1) oluşturun ve biçimlendirmeleri uygulayın.

//Aşağıdaki satırlar hücreye bir dizi değeri girer, belirtin

//yazı tipi boyutu, yatay ve dikey hizalama ayarlarını belirtin, ayarlayın

//ön plan ve arka plan renkleri ve hücreleri birleştirme (A1:E2).

WebWorksheet sayfası = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Kategoriye Göre Ürün Satışları");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sayfa.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sayfa.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sayfa.Cells["A1"].Style.BackColor = Color.SkyBlue;

sayfa.Cells["A1"].Style.ForeColor = Color.Blue;

sayfa.Cells.Merge(0, 0, 2, 5);

//Sayfada altyazı hücresini (A3) oluşturun ve formatları uygulayın.

//Aşağıdaki satırlar hücreye bir dizi değeri girer, belirtin

//yazı tipi boyutunu niteliklerle birlikte belirtin, yatay ve dikey hizalamayı belirtin

// ayarlar, ön plan ve arka plan renklerini ayarlayın ve hücreleri birleştirin

//(A3:E3).

sayfa.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sayfa.Cells["A3"].Style.Font.Bold = true;

sayfa.Cells["A3"].Style.Font.Italic = true;

sayfa.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sayfa.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sayfa.Cells["A3"].Style.BackColor = Color.SeaGreen;

sayfa.Cells["A3"].Style.ForeColor = Color.Yellow;

sayfa.Cells.Merge(2, 0, 1, 5);

//Son satır ve sütun (veri içeren) indekslerini alın.

int toplam satır = sayfa.Cells.MaxRow +1;

int totalcol = sayfa.Cells.MaxColumn;

//Cells koleksiyon sayfasını alın

WebCells hücreleri = sayfa.Cells;

//Cell nesnesini tanımlayın.

WebCell hücresi;

//Sayfadaki veriler arasında dolaşın ve iki alanı şununla biçimlendirin:

//Para birimi numarası stili.

için (int ben = 4;i<=totalrow;i++)

{

	//Format the Sale Column.

	cell = cells[i,totalcol];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

	//Format the UnitPrice Column.

	cell = cells[i,totalcol-1];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

}

//Insert the Total row with data, formula and formatting style.

//It will calculate the total Sales of a Category.

cells[totalrow,0].PutValue( DropDownList1.SelectedItem.Text + " Total" );

cells[totalrow,0].Style.Font.Bold = true;

cells[totalrow,totalcol].Formula = "=SUM(E5:E" + totalrow.ToString() + ")";

cells[totalrow,totalcol].Style.Font.Bold = true;

//Specify some Row and Column formattings. It will set row height

//and column width accordingly.

cells.SetRowHeight(2, new Unit("17pt"));

cells.SetColumnWidth(0, new Unit("157pt"));

cells.SetColumnWidth(1, new Unit("106pt"));

cells.SetColumnWidth(2, new Unit("87pt"));

cells.SetColumnWidth(3, new Unit("56pt"));

cells.SetColumnWidth(4, new Unit("50pt"));



{{< /highlight >}}
## **Formatlanmış Raporun (.XLS Dosyası) Grafik ile Aspose.Cells bileşeni kullanılarak üretilmesi**
Şimdi, biçimlendirilmiş raporu grafikle diske kaydetmek için bazı kodlar yazacağım. kullanıyorum**GridWeb** 's**Kayıt etmek**düğme,**GridWeb** 's**Komutu Kaydet**Kaydet düğmesine tıkladığınızda olay tetiklenir, bu yüzden ben hallederim. Burada, kullanıyorum**Aspose.Cells**biçimlendirilmiş raporu MS Excel'e dışa aktarmak, grafik oluşturmak ve bunu çıktı excel dosyasına gömmek için bileşen. Grafik görüntüsünü eklemedim (tarafından oluşturulan**Aspose.Chart**bileşeni) bunun yerine API'i kullanarak benzer grafiği oluşturun.**Aspose.Cells**böylece ihtiyacınıza göre grafiği MS Excel'de düzenleyebilirsiniz.





{{< highlight "java" >}}

 //This GridWeb control event is fired when you click on the "Save" button

//of the control. After Clicking this button "File Download" dialog is

//displayed and you may open into MS Excel / save the output excel file //with graph to disk.

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

	//Create MemoryStream object.

	System.IO.MemoryStream ms = new System.IO.MemoryStream();

	//Save the GridWeb's Report to the stream.

	this.GridWeb1.WebWorksheets.SaveToExcelFile(ms);

	//Create a new Workbook.

	Workbook workbook = new Workbook();

	//Open the stream into the Workbook.

	workbook.Open(ms);

	//Call the custom method which creates Chart.

	Workbook book = CellsChart(workbook);

	//Save the excel file displaying "File Download" dialog box.

	book.Save(ms, FileFormatType.Default);

	this.Response.ContentType = "application/vnd.ms-excel";

	this.Response.AddHeader("content-disposition", "attachment; filename=Export.xls");

	this.Response.BinaryWrite(ms.ToArray());

}

//This custom method is used to create the Chart based on the data source

//range in the GridWeb control. In this method we will use Aspose.Cells

//APIs to create the graph which will be saved later into the output //excel file.

private Workbook CellsChart(Workbook workbook)

{

	//Get the first Worksheet.

	Aspose.Cells.Worksheet sheet = workbook.Worksheets[0];

	//Get the Cells collection in the sheet.

	Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

	//Get the last row index.

	int maxrow = sheet.Cells.MaxDataRow;

	//Unmerge the cells.

	sheet.Cells.UnMerge(maxrow,0,15,10);

	int chartIndex = 0;

	//Add a new Chart into the sheet's Chart Collection.

chartIndex = sheet.Charts.Add(Aspose.Cells.ChartType.Pie,maxrow,0,maxrow+28,5);

	//Get the Chart object.

	Aspose.Cells.Chart chart = sheet.Charts[chartIndex];

	//Set the Chart Area.

	Aspose.Cells.ChartArea chartarea = chart.ChartArea;

	chartarea.Area.Formatting = FormattingType.Custom;

	chartarea.Border.IsVisible = false;

		chartarea.Area.FillFormat.SetTwoColorGradient(Color.PowderBlue, Color.LightSkyBlue, GradientStyleType.FromCenter,1);

	//Set some properties of Chart Plot Area.

	chart.PlotArea.Area.Formatting = FormattingType.None;

	chart.PlotArea.Border.IsVisible = false;

	//Set properties of Chart Title.

	chart.Title.Text = DropDownList1.SelectedItem.Text + " Sales";

	chart.Title.TextFont.Size = 20;

	//Set properties of NSeries

	int lastdatarow = maxrow-1;

	chart.NSeries.Add("E5:E" + lastdatarow.ToString(), true);

	chart.NSeries.CategoryData = "A5:A" + lastdatarow.ToString();

	//Set the Data Labels in the chart

	Aspose.Cells.DataLabels datalabels;

	for ( int i = 0; i < chart.NSeries.Count ;i ++ )

	{

		datalabels = chart.NSeries[i].DataLabels;

		datalabels.Postion = Aspose.Cells.LabelPositionType.Center;

		datalabels.IsPercentageShown = true;

	}

	//Set the Legend settings.

	Aspose.Cells.Legend legend = chart.Legend;

	legend.Position = Aspose.Cells.LegendPositionType.Bottom;

	legend.Height = 85;

	legend.Width = 330;

	legend.AutoScaleFont = true;

	legend.Border.Color = Color.Blue;

	legend.Area.Formatting = FormattingType.Custom;

	FillFormat fillformat = legend.Area.FillFormat;

	legend.Area.Formatting = FormattingType.None;

	legend.Border.IsVisible = false;

	//Autofit the first column.

	sheet.AutoFitColumn(0);

	//Return the Workbook.

	return workbook;

}



{{< /highlight >}}
## **Uygulamayı Çalıştırma**
Şimdi uygulamayı çalıştırıyorum. Açılır liste, farklı kategorilerle doldurulur.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Satış raporunu göstermek istediğim kategoriyi seçip "Raporu Göster" butonuna tıklıyorum.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Böylece, rapor**GridWeb**Seçilen kategoriye göre. Rapor, koda (daha önce yazılmış) göre varsayılan olarak biçimlendirilir.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Verileri bazı hücrelere WYSIWYG biçiminde biçimlendirmek istiyorsanız, bunu oldukça kolay bir şekilde yapabilirsiniz.**Aspose.Cells.GridWeb**sağlar**Biçim Cells**editör, istediğiniz hücreleri seçin ve sağ tıklayın, "Biçim Cell..." seçeneğini tıklayın.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Biçim Cell iletişim kutusu gösterilir.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Bazı Font niteliklerini belirtiyorum ve Tamam'ı tıklıyorum.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Ve sonucu alın.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Hücre biçimlendirmesinin yanı sıra hücre değerlerinizi de düzenleyebilirsiniz. İstediğiniz hücreye/hücrelere çift tıklayın ve değeri düzenleyin.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Düzenleme sonucunu göndermek ve tüm formülü yeniden hesaplamak için, raporu güncellemek için ilgili düğmeyi (kırmızı renkle çevrili) tıklıyorum.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Şimdi grafiği oluşturup kontrole yapıştıracağım. Veri aralığına dayalı pasta grafiği oluşturmak için özel komut düğmesini (kırmızı renkle çevrelenmiş) tıklıyorum.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Son olarak, bu veri raporunu grafikle birlikte MS Excel'e aktaracağım. tıklıyorum**Kayıt etmek**düğmesi (kırmızı renkle çevrelenmiş). tıklayarak**Kayıt etmek**düğme görüntülenecek**Dosya indirme**iletişim kutusu**Açık**ortaya çıkan raporu (grafikli excel dosyası çıktısı) MS Excel'e veya diske kaydedin.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Aç düğmesine tıkladığımda (Dosya İndirme iletişim kutusu), grafikli excel raporu MS Excel'e aktarılıyor. Raporun üst kısmı gösterilir.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Excel raporunun alt kısmı gösterilir.

![yapılacaklar:resim_alternatif_metin](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
