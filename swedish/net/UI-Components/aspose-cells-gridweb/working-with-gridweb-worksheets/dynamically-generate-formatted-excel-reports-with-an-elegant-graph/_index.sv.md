---
title: Generera formaterade Excel-rapporter dynamiskt med en elegant graf
type: docs
weight: 130
url: /sv/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Detta dokument är utformat för att ge den nödvändiga informationen hur vi kan extrahera data från någon datakälla till ett fantastiskt rutnät som kontroll, klistra in ett diagram i det och exportera rapporten med graf till MS Excel för att göra analys, jämförelser och utskrift.

{{% /alert %}} 
## **Översikt**
Det finns vissa webbscenarier som kräver både rapportering och presentationer, en kombination av delar eller objekt som kan fungera bra tillsammans. Artikeln förklarar hur enkelt det är att designa och generera snygga excel-rapporter dynamiskt på WYSIWYG-sätt. Den exporterar data från en XML-fil (du kan också använda andra datakällor) till Aspose.Cells. GridWeb-kontroll som ger dig den verkliga miljön som låter dig tillämpa ett rikt och tilltalande format på data och beräkna formelresultat som MS Excel. Det genererar också ett sofistikerat diagram baserat på källdata för kalkylbladet med hjälp av[Aspose.Cells](https://products.aspose.com/cells/) komponenten och klistrar in diagrambilden i försäljningsrapporten. Slutligen sparas excel-rapporten med bifogad graf på disk med Aspose.Cells-komponenten.

Den här artikeln innehåller källkoden och demoprojektet med alla funktioner för sådan funktionalitet.

Det ger användarna en detaljerad uppfattning om hur man skapar en affärsrapport för att mata in data i ett kalkylblad i rutnätet och tillämpa viss formatering på cellerna i raderna och kolumnerna, bädda in en graf baserad på källdataintervallet innan de sparas excel-rapport till disken.
## **Aspose-komponenterna**
 Jag använder tre av[Aspose](http://www.aspose.com/) s komponenter för att utföra uppgiften med lätthet.[Aspose](http://www.aspose.com/) , .NET och Java Component Publisher, tillhandahåller en mängd funktionsrika komponenter.[Aspose](http://www.aspose.com/) ger en stor rad med .NET och Java komponenter. Tillförlitliga av tusentals kunder över hela världen, produkterna inkluderar filformatskomponenter, rapporteringsprodukter, visuella komponenter och verktygskomponenter som gör det möjligt att programmatiskt öppna, modifiera, generera, spara, slå samman, konvertera etc. dokument i olika format inklusive DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, Tab Delimited, CSV, PPT, SWF, EMF, WMF, MPX, MPD och andra format.

Jag skulle ta tillfället i akt att presentera tre av dessa komponenter för dig som har använts i detta uppdrag.
## **Aspose.Cells Grid Controls**
 Aspose.Cells Grid Controls är en komplett rutnätslösning. Aspose.Cells Grid Controls levereras med två olika GUI .NET-komponenter (Aspose.Cells.GridDesktop och Aspose.Cells.GridWeb): en för att stödja skrivbordsapplikationer och en annan för att stödja webbapplikationer. Båda versionerna är lika matchade för att göra implementering i båda plattformarna på ett kick. Aspose.Cells.GridWeb ger möjlighet att importera från och exportera till Excel-kalkylblad. Så alla som är bekanta med Excel (även slutanvändare) kan designa utseendet och känslan av ett rutnät. Aspose.Cells.GridWeb erbjuder också en lättanvänd, funktionsrik API som ger utvecklare fullständig kontroll över utseendet, känslan och beteendet i deras rutnät. För att veta mer om produkten, dess funktioner och för en programmerares guide, vänligen se sammanfattningen av Features List, Aspose.Cells.GridWeb Documentation and online featured[Demos](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**är en Excel-kalkylbladsrapporteringskomponent som gör att du kan läsa och skriva Excel-kalkylblad utan att använda Microsoft Excel för att installeras antingen på klient- eller serversidan.**Aspose.Cells** är en funktionsrik komponent som erbjuder mycket mer än bara grundläggande export av data. Med**Aspose.Cells** utvecklare kan exportera data, formatera kalkylblad i varje detalj och på varje nivå, importera bilder, importera diagram, skapa diagram, manipulera diagram, strömma Excel-data, spara i olika format inklusive XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) integrerad) och många fler.**Aspose.Cells** erbjuder en lättanvänd, funktionsrik**API** för programmerarna. Den har en enorm lista med funktioner. För att veta mer om produkten, dess funktioner och för en programmerares guide, se sammanfattningen av**Funktionslista**, **Aspose.Cells Dokumentation** och demos online. Du får[ladda ner](https://downloads.aspose.com/cells) dess utvärderingsversion gratis.
## **Designa gränssnittet**
Vi börjar skapa en ny Asp.Net webbapplikation i Visual Studio.Net.

 jag**Lägg till referens**till de tre komponenterna ieAspose.Cells.GridWeb.dll, Aspose.Chart.dll och Aspose.Cells.dll till projektet först. Jag placerar lite kontroll på sidan och ställer in deras egenskaper, dvs en rullgardinslista, en kommandoknapp och en etikett. Jag placerar då**Aspose.Cells.GridWeb****kontrollera**(**GridWeb**) till den från verktygslådan, eftersom efter att ha lagt till referenser till de tre komponenterna,**GridWeb**kontroll visas på verktygslådan. De andra två komponenterna (**Aspose.Chart**och**Aspose.Cells**) är bara bibliotek, bara hänvisas till projektet.

Jag skapar också två mappar "fil" och "bilder", lägger till "Products.xml" och "chart.gif" till dessa respektive mappar. XML-filen är en datakällfil från vilken data kommer att extraheras för att fylla**GridWeb**arbetsblad. Bildfilen kommer att tillhandahålla en bild för en anpassad knapp placerad på**GridWeb**kontrollera.

Jag skapar nu en anpassad kommandoknapp. Jag högerklickar helt enkelt på**GridWeb**kontrollera och klicka på alternativet "Anpassade kommandoknappar...".

Det kommer att aktivera Custom Command Button editor, editorn låter dig skapa anpassade kommandobildsknappar med verktygstips bifogat. Jag anger värdena för vissa egenskaper för knappen, t.ex. Kommando (Namn) ->"btnChart", ImageUrl -> ge sökvägen till bildfilen ("chart.gif") och ToolTip -> ge verktygstipset.

Så den anpassade kommandoknappen läggs till som du kan se den (omringad med röd färg) i följande skärmdump.

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Slutligen ställer jag in några teckensnittsattribut (fet) för etiketten och kommandoknappen. Jag justerar också storleken på kontrollerna för att få det slutgiltiga utseendet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Hämta data från en XML-fil**
Följande är XML-filstruktur som används i projektet.
### **XML-filstruktur**
**XML**

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
## **Fylla i arbetsbladet för Aspose.Cells.GridWeb-kontrollen med data**
Jag använder några API av**GridWeb**kontroll för att fylla ett kalkylblad med data från XML-källfilen. Jag skriver kod i kommandoknappen (märkt "Visa rapport")s klickhändelsehanterare. Datarapporten filtreras baserat på det valda objektet från rullgardinsmenyn.



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
## **Formatera data i Cells**
För att skilja mellan olika typer av information på ett kalkylblad, för optimal visning av data på ditt kalkylblad och för att göra ett kalkylblad lättare att skanna, formaterar du kalkylbladet. A**Formatera**representerar en stil och definieras som en uppsättning egenskaper, såsom teckensnitt och teckenstorlekar, talformat, cellkanter, cellskuggning med enfärgad bakgrundsfärg eller ett specifikt färgmönster, indrag, justering och textorientering i cellerna.

Jag slår ihop några fler rader kod till ovan. Jag placerar rubriken/underrubriken på rapporten, formaterar lite till rubrik, underrubrik och detaljceller. Jag tillämpar även nummerformatering på de två fälten (ställ in valutanummerformat till fälten Enhetspris och Försäljning) och justerar höjden/bredden på rader och kolumner med**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 //Skapa titelcellen (A1) i arket och använd formatering.

//Följande rader matar in ett strängvärde till cellen, specificera

//fontstorlek, ange horisontella och vertikala inställningar, ställ in

//förgrunds- och bakgrundsfärger och slå samman celler (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Produktförsäljning per kategori");

ark.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

ark.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

ark.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

ark.Cells["A1"].Style.BackColor = Färg.Himmelblå;

ark.Cells["A1"].Style.ForeColor = Färg.Blå;

ark.Cells.Sammanfoga(0, 0, 2, 5);

//Skapa undertextcellen (A3) i arket och använd formatering.

//Följande rader matar in ett strängvärde till cellen, specificera

//fontstorlek med attribut, ange horisontell och vertikal justering

//inställningar, ställ in förgrunds- och bakgrundsfärger och slå samman celler

//(A3:E3).

ark.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

ark.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

ark.Cells["A3"].Style.Font.Fet = sant;

ark.Cells["A3"].Style.Font.Italic = sant;

ark.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

ark.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

ark.Cells["A3"].Style.BackColor = Color.SeaGreen;

ark.Cells["A3"].Style.ForeColor = Färg.Gul;

ark.Cells.Sammanfoga(2, 0, 1, 5);

//Hämta de sista rad- och kolumnindexen (som innehåller data).

int totalrad = ark.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Hämta arket Cells samlingar

WebCells celler = ark.Cells;

//Definiera objektet Cell.

WebCell cell;

//Bläddra igenom data i arket och formatera två fält med

//Stil för valutanummer.

för (int i = 4;i<=totalrow;i++)

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
## **Producera den formaterade rapporten (.XLS-fil) med Graph med komponenten Aspose.Cells**
Nu ska jag skriva lite kod för att spara den formaterade rapporten med grafen på disken. jag använder**GridWeb** s**Spara**knappen, The**GridWeb** s**SaveCommand**händelsen aktiveras när du klickar på knappen Spara, så jag kommer att hantera det. Här använder jag**Aspose.Cells**komponent för att exportera den formaterade rapporten till MS Excel, generera diagram och bädda in den i utdata Excel-filen. Jag har inte infogat diagrambilden (skapad av**Aspose.Chart**komponent) skapa snarare ett liknande diagram med hjälp av API av**Aspose.Cells**så att du kan redigera diagram i MS Excel för dina behov.





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
## **Kör applikationen**
Nu kör jag applikationen. Rullgardinslistan är fylld med de distinkta kategorierna.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Jag väljer en kategori för vilken jag vill visa försäljningsrapporten och klickar på knappen "Visa rapport".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Så rapporten visas i**GridWeb**baserat på den valda kategorin. Rapporten formateras som standard baserat på koden (skriven tidigare).

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Om du vill formatera data till några av cellerna på WYSIWYG-sätt kan du göra det ganska enkelt.**Aspose.Cells.GridWeb**tillhandahåller**Format Cells**editor, välj önskad cell(er) och högerklicka på den, klicka på alternativet "Format Cell...".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Dialogrutan Format Cell visas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Jag anger några teckensnittsattribut och klickar på OK.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Och få resultatet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Förutom cellformatering kan du också redigera dina cellvärden. Dubbelklicka på önskad cell(er) och redigera värdet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

För att skicka in redigeringsresultatet och räkna om alla formler klickar jag på den relaterade knappen (omringad med röd färg) för att uppdatera rapporten.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Nu ska jag skapa diagrammet och klistra in det i kontrollen. Jag klickar på den anpassade kommandoknappen (omringad med röd färg) för att skapa ett cirkeldiagram baserat på dataintervallet.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Slutligen kommer jag att exportera denna datarapport med graf till MS Excel. Jag klickar på**Spara**knapp (omringad med röd färg). Genom att klicka på**Spara**knappen visas**Filhämtning**dialog kan du antingen**Öppna**den resulterande rapporten (utdata excel-fil med graf) till MS Excel eller spara den på disken.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

När jag klickar på Öppna-knappen (Hämta fil), exporteras excel-rapporten med graf till MS Excel. Den övre delen av rapporten visas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Den nedre delen av excel-rapporten visas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
