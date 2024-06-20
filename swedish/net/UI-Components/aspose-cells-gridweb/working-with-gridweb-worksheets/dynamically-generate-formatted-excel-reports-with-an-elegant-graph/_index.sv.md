---
title: Dynamiskt generera formaterade Excel rapporter med en elegant graf
type: docs
weight: 130
url: /sv/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, generera rapport, rapport
description: Den här artikeln introducerar hur man genererar rapport i GridWeb.
---

{{% alert color="primary" %}} 

Detta dokument är utformat för att tillhandahålla nödvändig information om hur vi kan extrahera data från någon datakälla till en praktfull gridliknande kontroll, klistra in en graf i den och exportera rapporten med grafen till MS Excel för analys, jämförelser och utskrifter.

{{% /alert %}} 
## **Översikt**
Det finns vissa webbscenarier som kräver både rapportering och presentationer, en kombination av delar eller objekt som kan fungera bra tillsammans. Artikeln förklarar hur enkelt det är att designa och generera snygga Excel-rapporter dynamiskt på ett WYSIWYG-sätt. Den exporterar data från en XML-fil (du kan också använda andra datakällor) till Aspose.Cells.GridWeb-kontrollen som ger dig den verkliga miljö som tillåter dig att tillämpa rik och attraktiv formatering på data och beräkna formelresultat som MS Excel. Den genererar också en sofistikerad graf baserad på källdataarket med hjälp av [Aspose.Cells](https://products.aspose.com/cells/) komponent och klistrar in grafikbilden i Försäljningsrapporten. Slutligen sparas Excel-rapporten med bifogad graf på disken med hjälp av Aspose.Cells-komponenten.

Den här artikeln inkluderar källkod och en fullt utrustad demoapplikation för en sådan funktionalitet.

Den ger användarna en detaljerad uppfattning om hur man skapar en affärsrapport för att mata in data i ett kalkylblad i rutan och tillämpa viss formatering på cellerna i raderna och kolumnerna, bädda in en graf baserad på källdataräckvidden före att spara Excel-rapporten på disken.
## **Aspose-komponenterna**
Jag använder tre av [Aspose](http://www.aspose.com/) komponenter för att utföra uppgiften med lätthet. [Aspose](http://www.aspose.com/), The .NET and Java Component Publisher, tillhandahåller olika komponenter med rika funktioner. [Aspose](http://www.aspose.com/) tillhandahåller en stor samling av .NET- och Java-komponenter. Produkterna inkluderar filformatkomponenter, rapporteringsprodukter, visuella komponenter och hjälpprogram som möjliggör att programmatiskt öppna, ändra, generera, spara, sammanfoga, konvertera etc. dokument i olika format inklusive DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, tabulatorbaserad, CSV, PPT, SWF, EMF,WMF, MPX, MPD och andra format.

Jag vill härmed ta tillfället i akt att introducera tre av dessa komponenter som har använts i denna quest.
## **Aspose.Cells Grid Controls**
Aspose.Cells Grid Controls är en total gridlösning. Aspose.Cells Grid Controls levereras med två olika GUI .NET-komponenter (Aspose.Cells.GridDesktop och Aspose.Cells.GridWeb): en för att stödja skrivbordsapplikationer och den andra för att stödja webbapplikationer. Båda versionerna matchar varandra för att göra implementeringen på någon plattform enkel. Aspose.Cells.GridWeb ger möjlighet att importera från och exportera till Excalkalkylblad, så att vem som helst som är bekant med Excel (även slutanvändare) kan designa gridens utseende. Aspose.Cells.GridWeb erbjuder också ett lättanvänt, funktionsrikt API som ger utvecklare fullständig kontroll över utseendet, känslan och beteendet hos deras rutnät. För att veta mer om produkten, dess funktioner och för en programvaruhandbok, kolla igenom sammanfattningen av funktionerna, Aspose.Cells.GridWeb-dokumentationen och de onlinebaserade [Demona](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells** är en Excel-kalkylrapporteringskomponent som gör att du kan läsa och skriva Excel- kalkylblad utan att använda Microsoft Excel som är installerat vare sig på klient- eller serversidan. **Aspose.Cells** är en funktionsspäckad komponent som erbjuder mycket mer än bara grundläggande export av data. Med **Aspose.Cells** kan utvecklare exportera data, formatera kalkylblad i varje detalj och på varje nivå, importera bilder, importera diagram, skapa diagram, manipulera diagram, strömma Excel-data, spara i olika format inklusive XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) integrerad) och många fler.**Aspose.Cells** erbjuder en lättanvänd, funktionsrik **API** för programmerare. Den har en enorm lista över funktioner. För att veta mer om produkten, dess funktioner och för en programmerarhandbok, kolla sammanfattnngen av **Funktionslistan**, **Aspose.Cells-dokumentationen** och de onlinebaserade Demona. Du kan [ladda ner](https://downloads.aspose.com/cells) dess utvärderingsversion gratis.
## **Designa gränssnittet**
Vi börjar skapa en ny Asp.Net-webbapplikation i Visual Studio.Net.

Jag **Lägger till referens** till de tre komponenterna dvs. Aspose.Cells.GridWeb.dll, Aspose.Chart.dll och Aspose.Cells.dll till projektet först. Jag placerar några kontroller på sidan och ställer in deras egenskaper, dvs. en rullgardinsmeny, en kommandoknapp och en etikett. Jag placerar sedan **Aspose.Cells.GridWeb**-kontrollen (**GridWeb**) i den från verktygsfältet, eftersom efter att ha lagt till referenser till de tre komponenterna, visas **GridWeb**-kontrollen på verktygsfältet. De andra två komponenterna (**Aspose.Chart** och **Aspose.Cells**) är bara bibliotek, blir bara refererade till projektet.

Jag skapar också två mappar "fil" och "bilder", lägger till "Products.xml" och "chart.gif" i dessa mappar respektive. Xml-filen är en datakällfil från vilken data kommer att hämtas för att fylla**GridWeb**-kalkylarket. Bildfilen kommer att tillhandahålla en bild för en anpassad knapp som placeras på**GridWeb**-kontrollen.

Nu skapar jag en anpassad kommandoknapp. Jag högerklickar helt enkelt på**GridWeb**-kontrollen och väljer alternativet "Anpassade kommandoknappar...".

Det kommer att aktivera anpassaren för anpassade kommandoknappar. Anpassaren låter dig skapa anpassade kommando bildknappar med verktygstips bifogat. Jag specificerar värden för några egenskaper för knappen t.ex. Kommando (namn) -> "btnChart", Bild-URL -> ange sökvägen till bildfilen ("chart.gif") och Verktygstips -> ange verktygstipset.

Så, den anpassade kommandoknappen läggs till, som du kan se den (omringad med rött) på följande skärmbild.

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Slutligen ställer jag in några teckensnittsegenskaper (fetstil) för etiketten och kommandoknappen. Jag justerar också storleken på kontrollerna för att få det slutgiltiga utseendet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Hämta Data från en XML-fil**
Det följande är XML-filstrukturen som används i projektet.
### **XML-filstruktur**
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
## **Fylla i kalkylarket för Aspose.Cells.GridWeb-kontrollen med data**
Jag använder några API av**GridWeb**-kontrollen för att fylla ett kalkylblad med data från den käll-XML-filen. Jag skriver kod i kommandoknappen (märkt"Visa rapport") 's klickhändelsehanterare. Datarapporten filtreras baserat på det valda objektet från listrutan.



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
## **Formatering av data i cellerna**
För att särskilja mellan olika typer av information på ett kalkylblad, för optimal visning av datan på ditt kalkylblad och för att göra ett kalkylblad lättare att skanna, formaterar du kalkylbladet. En**Format**representerar en stil och är definierad som en uppsättning egenskaper, såsom teckensnitt och teckenstorlekar, nummerformat, cellgränser, cellfyllning med solid bakgrundsfärg eller ett specifikt färgbeteende, indrag, justering och textorientering i cellerna.

Jag lägger till några fler rader kod till ovanstående. Jag placerar titeln /undertiteln för rapporten, gör lite formatering av titel, undertitel och detaljceller. Jag tillämpar också nummerformatering på de två fälten (anger valutanummerformat för EnhetPris och Försäljningsfält) och justerar höjden/ bredden på rader och kolumner med**Aspose.Cells.GridWeb**-API.



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
## **Producera den formaterade rapporten (.XLS-fil) med grafik med hjälp av Aspose.Cells-komponenten**
Nu ska jag skriva några koder för att spara den formaterade rapporten med grafik på hårddisken. Jag använder**GridWeb** 's**Spara**-knapp, **GridWeb** 's**SparaKommando**-händelse aktiveras när du klickar på Spara-knappen, så jag kommer att hantera den. Här använder jag**Aspose.Cells**-komponenten för att exportera den formaterade rapporten till MS Excel, generera diagram och bädda in det i den resulterande Excel-filen. Jag har inte satt in diagrambilden (skapad av**Aspose.Chart**-komponenten) utan skapat ett liknande diagram med hjälp av**Aspose.Cells**-API, så att du kan redigera diagrammet i MS Excel enligt ditt behov.





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
## **Kör applikationen**
Nu kör jag applikationen. Listrutan fylls med de olika kategorierna.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Jag väljer en kategori genom vilken jag vill visa försäljningsrapporten och klickar på"Visa rapport"-knappen.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Så visas rapporten i**GridWeb**baserat på den valda kategorin. Rapporten formateras som standard baserat på den tidigare skrivna koden.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Om du vill formatera data i några av cellerna på visuellt sätt kan du göra det ganska enkelt.**Aspose.Cells.GridWeb**ger**Format Cell**-redigeraren, välj önskad cell(er) och högerklicka på den, klicka på"Format Cell..."-alternativet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Dialogrutan för Formatcell visas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Jag specificerar några teckensnittsegenskaper och klickar på OK.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Och får resultatet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Förutom cellformatering kan du också redigera dina cellvärden. Dubbelklicka på önskad(e) cell(er) och redigera värdet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

För att skicka in redigeringsresultatet och beräkna om alla formler klickar jag på den relaterade knappen (omringad med rött) för att uppdatera rapporten.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Nu kommer jag att skapa diagrammet och klistra in det i kontrollen. Jag klickar på den anpassade kommandoknappen (omringad med rött) för att skapa cirkeldiagrammet baserat på datområdet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Slutligen exporterar jag denna data rapport med diagram till MS Excel. Jag klickar på**Spara**-knappen (omringad med rött). När du klickar på**Spara**-knappen visas en**File Download**-dialogruta, där kan du antingen**Öppna**den resulterande rapporten (output excel-fil med diagram) i MS Excel eller Spara den på hårddisken.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

När jag klickar på Öppna-knappen (File Download dialogruta), exporteras excel-rapporten med diagrammet till MS Excel. Övre delen av rapporten visas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Den nedre delen av excel-rapporten visas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
