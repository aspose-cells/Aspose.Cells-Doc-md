---
title: Bir Zarif Grafikle Dinamik Olarak Biçimlendirilmiş Excel Raporları Oluşturma
type: docs
weight: 130
url: /tr/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, rapor oluştur, rapor
description: Bu makale, GridWeb de rapor oluşturmanın nasıl yapıldığını tanıtır.
---

{{% alert color="primary" %}} 

Bu belge, işletme raporu oluşturmak için gereken bilgileri sağlama amacını taşımaktadır. Muhteşem bir grid benzeri kontrol üzerinden veri çıkartmanın, içine bir grafik yapıştırmanın ve analiz, karşılaştırma ve yazdırma yapmak için MS Excel'e grafik ile raporu dışa aktarmanın nasıl yapıldığını anlatır.

{{% /alert %}} 
## **Genel Bakış**
Hem Raporlama hem de Sunumlar gerektiren belirli web senaryoları bulunmaktadır, iyi bir şekilde birlikte çalışabilen parça veya nesne kombinasyonu. Makale, WYSIWYG şekilde şık excel raporları oluşturmanın ne kadar kolay olduğunu açıklar. Aspose.Cells.GridWeb kontrolüne XML dosyasından (Diğer veri kaynaklarını da kullanabilirsiniz) veri dışa aktarır ve size, verilere zengin ve çekici bir biçim uygulamanıza ve MS Excel gibi formül sonuçlarını hesaplamanıza izin veren gerçek bir ortam sunar. Ayrıca [Aspose.Cells](https://products.aspose.com/cells/) bileşenini kullanarak Çalışma Sayfası kaynağı verilere dayalı sofistike bir grafik oluşturur ve Satış Raporuna grafik görüntüsünü yapıştırır. Son olarak, grafikli excel raporu Aspose.Cells bileşenini kullanarak diske kaydedilir.

Bu makale, bu tür işlevselliğin kaynak kodunu ve tam özellikli demo projesini içermektedir.

Bu, kullanıcılara bir iş raporu oluşturmak için iş sayfasına veri girmenin, satır ve sütunlardaki hücrelere bazı biçimlendirme uygulamanın, kaynak veri aralığına dayalı bir grafik gömmenin ve excel raporunu diske kaydetmeden önce çeşitli adımları ayrıntılı bir şekilde sunar.
## **Aspose Bileşenleri**
Bu görevi kolayca yerine getirmek için üç adet [Aspose](http://www.aspose.com/)'un bileşenini kullanıyorum. [Aspose](http://www.aspose.com/), .NET ve Java Bileşen Yayıncısı, özellik dolu çeşitli bileşenler sunar. [Aspose](http://www.aspose.com/), bir dizi etkileyici özelliklere sahip olan .NET ve Java bileşenleri sunar. Küresel müşteriler tarafından güvenilen ve binlerce müşteri tarafından kullanılan bu ürünler, belge biçim bileşenlerini, raporlama ürünlerini, görsel bileşenleri ve yardımcı öğeleri içerir ve belgeleri açma, değiştirme, oluşturma, kaydetme, birleştirme, dönüştürme vb. işlemleri programlı olarak yapmanızı sağlar.

Bu görevde kullanılan bu bileşenlerden üç tanesini tanıtmak için bu fırsatı kullanmak isterim.
## **Aspose.Cells Grid Kontrolleri**
Aspose.Cells Grid Kontrolleri, toplam bir grid çözümüdür. Aspose.Cells Grid Kontrolleri, masaüstü uygulamaları (Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb) için iki farklı GUI .NET bileşeniyle birlikte gelir: biri masaüstü uygulamaları desteklemek için diğeri web uygulamaları desteklemek içindir. Her iki versiyon da platforma göre uygulamayı kolaylaştırmak amacıyla eşit derecede uyumludur. Aspose.Cells.GridWeb, Excel elektronik tablolarına aktarma ve aktarma işlevselliği sunar. Bu nedenle Excel'e aşina olan herkes (hatta son kullanıcılar) bir gridin görünümünü tasarlayabilir. Aspose.Cells.GridWeb ayrıca gelişmiş özellikli bir API sunar, bu da geliştiricilere gridlerinin görünümü, hissi ve davranışı üzerinde tam kontrole sahip olmalarını sağlar. Ürün hakkında daha fazla bilgi, özellikleri ve bir programcı kılavuzu için lütfen Özellikler Listesi Özeti, Aspose.Cells.GridWeb Belgeleri ve çevrim içi olan özellikli [Demo'ları](https://aspose.github.io/) kontrol edin
## **Aspose.Cells**
**Aspose.Cells**, Microsoft Excel'in kurulu olmasına gerek duyulmadan Excel elektronik tablolarını okuma ve yazma imkanı sunan bir Excel elektronik tablo raporlama bileşenidir. **Aspose.Cells**, verilerin temel dışa aktarımını aşan temel veri dışa aktarımının yanı sıra çok daha fazlasını sunan özellikli bir bileşendir. **Aspose.Cells** ile geliştiriciler, veri dışa aktarımı yaparken, elektronik tabloları her ayrıntıda ve her düzeyde biçimlendirebilirler, görüntüler, grafikleri içe aktarabilir, grafikler oluşturabilir, grafikleri değiştirebilir, Excel verilerini aktarabilir, XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) entegre) ve çok daha fazlası gibi çeşitli formatlarda kaydedebilirler. **Aspose.Cells**, programcılar için kullanması kolay, özellikli bir **API** sunar. Bu, büyük bir özellik listesine sahiptir. Ürün hakkında daha fazla bilgi, özellikleri ve bir programcı kılavuzu için lütfen Özellikler Listesi Özeti, Aspose.Cells Belgeleri ve çevrim içi olan özellikli Demo'ları kontrol edin. Ücretsiz olarak [indirmek](https://downloads.aspose.com/cells)' için değerlendirme sürümünü indirebilirsiniz.
## **Arayüz Tasarımı**
Visual Studio.Net'te yeni bir Asp.Net web uygulaması oluşturmaya başlıyoruz.

İlk olarak, projeye Aspose.Cells.GridWeb.dll, Aspose.Chart.dll ve Aspose.Cells.dll üç bileşenine **Referans Ekle**. Ardından sayfaya bazı kontroller ekleyip özelliklerini ayarlarım, yani bir açılır liste, bir komut düğmesi ve bir etiket. Ardından, **GridWeb**'i (Aspose.Cells.GridWeb kontrolü) araç kutusundan sayfaya yerleştiririm, çünkü üç bileşene referans ekledikten sonra, **GridWeb** kontrolü araç kutusunda görünür hale gelmiştir. Diğer iki bileşen (Aspose.Chart ve Aspose.Cells) sadece kütüphanelerdir, sadece projeye referans alır.

"file" ve "images" adında iki klasör oluşturur, bunlara sırasıyla "Products.xml" ve "chart.gif" eklerim. XML dosyası, verilerin **GridWeb** çalışsayfasını doldurmak için çıkarılacağı veri kaynağı dosyasıdır. Resim dosyası, **GridWeb** kontrolüne yerleştirilen özel bir düğme için bir resim sağlayacak.

Şimdi özel bir komut düğmesi oluşturuyorum. Sadece **GridWeb** kontrolüne sağ tıklayıp "Özel Komut Düğmeleri..." seçeneğini tıklarım.

Bu, Özel Komut Düğme düzenleyicisini etkinleştirecek, düzenleyici size araç ipucu eklenmiş özel komut resim düğmeleri oluşturmanıza olanak tanır. Düğme için bazı özellik değerlerini belirtirim, örn. Komut (Ad) -> "btnChart", ImageUrl -> resim dosyasının yolu ("chart.gif") ve Araç İpucu -> araç ipucu ver.

Bu şekilde özel komut düğmesi eklenir (kırmızı renkle çevrili olarak) aşağıdaki ekran görüntüsünde görüldüğü gibi.

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Son olarak, etiket ve komut düğmesi için bazı yazı tipi özniteliklerini (kalın) ayarlarım. Ayrıca, kontrol boyutlarını ayarlayarak nihai görünümü elde ederim.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Bir XML Dosyasından Veri Alma**
Projede kullanılan XML dosyası yapısı aşağıdaki gibidir.
### **XML Dosyası Yapısı**
**XML**

{{< highlight csharp >}}

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

{{< highlight java >}}

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

private object[] GetDistinctValues(DataTable dtable, string colName)

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
## **Aspose.Cells.GridWeb kontrolünün çalışsayfasını kaynaktan alınan veri ile doldurma**
**GridWeb** kontrolünün API'sinden kaynak XML dosyasından çalışsayfayı veri ile doldurmak için bir dizi API kullanırım. Veri raporu, açılır listeden seçilen öğeye göre filtrelenir.



{{< highlight java >}}

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
## **Hücrelerde Veri Biçimlendirme**
Çalışsayfada farklı bilgi tiplerini ayırt etmek, verinin optimal bir şekilde görüntülenmesi ve çalışsayfanın taranmasının daha kolay olması için çalışsayfayı biçimlendirirsiniz. **Format**, yazı tipi boyutları, sayı biçimleri, hücre sınırları, hücre renklendirmeleri, hiza, içerik ve metin yönlendirmesi gibi özelliklerden oluşan bir stil olarak tanımlanır.

Yukarıda bahsedilen kod parçalarına ek olarak, raporun başlık/alt başlığını yerleştirir, başlık, alt başlık ve detay hücrelerini biçimlendiririm. Ayrıca, iki alana (Birim Fiyat ve Satış alanlarına) sayı biçimlendirme uygular ve **Aspose.Cells.GridWeb**API'sini kullanarak satır ve sütunların yüksekliğini/genişliğini ayarlarım.



{{< highlight java >}}

 //Create the title cell (A1) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size, specify horizontal and vertical align settings, set

//foreground and background colors and merge cells (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Product Sales By Category");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

sheet.Cells.Merge(0, 0, 2, 5);

//Create the subtitle cell (A3) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size with attributes, specify horizontal and vertical align

//settings, set foreground and background colors and merge cells

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Obtain the last row and column (which contain data) indexes.

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Get the sheet Cells collections

WebCells cells = sheet.Cells;

//Define the Cell object.

WebCell cell;

//Loop through the data in the sheet and format two fields with

//Currency number style.

for (int i = 4;i<=totalrow;i++)

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
## **Aspose.Cells bileşenini kullanarak Grafikli Biçimlendirilmiş Rapor (.XLS Dosyası) Oluşturma**
Şimdi, grafikli biçimlendirilmiş raporu diske kaydetmek için bazı kodlar yazarım. **GridWeb** 'in **Kaydet** düğmesini kullanırım, **GridWeb** 'in **KaydetKomutu** olayı, Kaydet düğmesine tıkladığınızda tetiklenir, bu nedenle ben bunu ele alırım. Burada, biçimlendirilmiş raporu MS Excel'e dışa aktarmak, grafik oluşturmak ve grafikleri çıktı excel dosyasına yerleştirmek için **Aspose.Cells** bileşenini kullanırım. **Aspose.Chart** bileşeni tarafından oluşturulan grafik resmini (resim) yerine, MS Excel'de grafikliyi oluşturmak için **Aspose.Cells** API'sini kullanırım.





{{< highlight java >}}

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
## **Uygulamanın Çalıştırılması**
Şimdi uygulamayı çalıştırıyorum. Açılır liste farklı kategorilerle doldurulmuş durumda.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Satış raporunu göstermek istediğim bir kategori seçer ve "Raporu Göster" düğmesine tıklarım.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Bu şekilde, seçilen kategoriye göre **GridWeb** tablosuna rapor eklenir. Rapor, varsayılan olarak yazılan kodlara göre biçimlendirilir.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Eğer hücrelere WYSIWYG (ne görürsen onu alırsın) biçimde veri biçimlendirmek isterseniz, bunu oldukça kolayca yapabilirsiniz. **Aspose.Cells.GridWeb**, **Hücre Biçimlendirme** düzenleyicisini sağlar, istediğiniz hücreleri seçip üzerine sağ tıklayarak "Hücre Biçimlendirme..." seçeneğini tıklarsınız.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Hücre Biçimlendirme iletişim kutusu gösterilir.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Belirli bir yazı tipi özelliği belirtirim ve Tamam'a tıklarım.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Ve sonucu alırım.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Hücre biçimlendirmenin yanı sıra, hücre değerlerinizi de düzenleyebilirsiniz. İstenen hücreye çift tıklar ve değeri düzenlerim.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Düzenleme sonucunu göndermek ve tüm formülü yeniden hesaplamak için ilişkili düğmeye tıklarım (kırmızı renkle çevrili).

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Şimdi grafiği oluşturup kontrolüne yapıştırırım. Veri aralığına dayanarak pasta grafiğini oluşturmak için özel komut düğmesine tıklarım (kırmızı renkle çevrili).

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Son olarak, bu veri raporunu grafikle birlikte MS Excel'e dışa aktarırım. **Kaydet** düğmesine tıklarım (kırmızı renkle çevrili). **Kaydet** düğmesine tıkladığınızda, **Dosya İndirme** iletişim kutusu görüntülenir, çıktı excel dosyası ile MS Excel'de açabilir veya diske kaydedebilirsiniz.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Açtığım düğmeye tıkladığımda (Dosya İndirme iletişim kutusu), excel raporunun üst kısmı gösterilir.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Excel raporunun alt kısmı gösterilir.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
