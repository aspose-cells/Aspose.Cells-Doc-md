---
title: Dynamische Generierung von formatierten Excel Berichten mit einer eleganten Grafik
type: docs
weight: 130
url: /de/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, Bericht generieren, Bericht
description: Dieser Artikel stellt vor, wie ein Bericht in GridWeb generiert werden kann.
---

{{% alert color="primary" %}} 

Dieses Dokument soll die notwendigen Informationen bereitstellen, wie Daten aus einer Datenquelle extrahiert und in einer hervorragenden Gittersteuerelement ähnlichen Ansicht eingefügt werden können, einen Diagramm darin einfügen und den Bericht mit Graphik zur MS Excel exportieren, um Analysen, Vergleiche und Ausdrucken zu ermöglichen.

{{% /alert %}} 
## **Übersicht**
Es gibt bestimmte Web-Szenarien, die sowohl Berichterstattung als auch Präsentationen erfordern, eine Kombination von Teilen oder Objekten, die gut zusammenarbeiten können. Der Artikel erklärt, wie einfach es ist, stilvolle Excel-Berichte dynamisch und im WYSIWYG-Modus zu entwerfen und zu generieren. Er exportiert Daten aus einer XML-Datei (Sie können auch andere Datenquellen verwenden) zum Aspose.Cells.GridWeb-Steuerelement, das Ihnen die reale Umgebung bietet, um reiche und ansprechende Formate auf Daten anzuwenden und Formelergebnisse wie in MS Excel zu berechnen. Es generiert auch ein anspruchsvolles Diagramm basierend auf den Daten der Arbeitsblattquelle mithilfe der [Aspose.Cells](https://products.aspose.com/cells/) Komponente und fügt das Diagrammbild in den Verkaufsbericht ein. Schließlich wird der Excel-Bericht mit angefügter Graphik mithilfe der Aspose.Cells-Komponente auf der Festplatte gespeichert.

Dieser Artikel enthält den Quellcode und ein vollständig ausgestattetes Demo-Projekt für eine solche Funktionalität.

Es ermöglicht den Benutzern eine detaillierte Einsicht, wie man einen Geschäftsbericht erstellen kann, um Daten in ein Arbeitsblatt des Gitters einzugeben und einige Formatierungen auf die Zellen in den Zeilen und Spalten anzuwenden, ein Diagramm basierend auf dem Quellenbereich der Daten einzubetten, bevor der Excel-Bericht auf der Festplatte gespeichert wird.
## **Die Aspose-Komponenten**
Ich verwende drei der [Aspose](http://www.aspose.com/)-Komponenten, um die Aufgabe leicht zu erledigen. [Aspose](http://www.aspose.com/), der .NET- und Java-Komponentenherausgeber, bietet eine Vielzahl von funktionsreichen Komponenten. [Aspose](http://www.aspose.com/) bietet eine großartige Auswahl an .NET- und Java-Komponenten. Vertrauenswürdig von Tausenden von Kunden weltweit, umfassen die Produkte Dateiformatkomponenten, Berichtsprodukte, visuelle Komponenten und Hilfskomponenten, die das programmgesteuerte Öffnen, Ändern, Generieren, Speichern, Zusammenführen, Konvertieren usw. von Dokumenten in verschiedenen Formaten ermöglichen, einschließlich DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, Tab-delimited, CSV, PPT, SWF, EMF, WMF, MPX, MPD und anderen Formaten.

Ich möchte diese Gelegenheit nutzen, um Ihnen drei dieser Komponenten vorzustellen, die bei dieser Aufgabe verwendet wurden.
## **Aspose.Cells Grid Controls**
Aspose.Cells Grid Controls sind eine vollständige Rasterlösung. Aspose.Cells Grid Controls werden mit zwei verschiedenen GUI .NET-Komponenten (Aspose.Cells.GridDesktop und Aspose.Cells.GridWeb) geliefert: eine zur Unterstützung von Desktopanwendungen und eine zur Unterstützung von Webanwendungen. Beide Versionen sind gleichermaßen geeignet, um die Implementierung in jeder Plattform zum Kinderspiel zu machen. Aspose.Cells.GridWeb bietet die Möglichkeit, Excel-Tabellen zu importieren und zu exportieren. So kann jeder, der mit Excel vertraut ist (sogar Endbenutzer), das Aussehen und das Verhalten eines Rasters entwerfen. Aspose.Cells.GridWeb bietet auch eine benutzerfreundliche, funktionsreiche API, die Entwicklern die vollständige Kontrolle über das Aussehen, das Verhalten und die Funktionalität ihres Rasters bietet. Um mehr über das Produkt, seine Funktionen und einen Programmierleitfaden zu erfahren, prüfen Sie bitte die Zusammenfassung der Funktionsliste, die Aspose.Cells.GridWeb-Dokumentation und die online vorgestellten [Demos](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells** ist eine Excel-Tabellenberichtskomponente, mit der Sie Excel-Tabellen lesen und schreiben können, ohne dass Microsoft Excel auf dem Client- oder Servercomputer installiert werden muss. **Aspose.Cells** ist eine funktionsreiche Komponente, die weit mehr als nur das einfache Exportieren von Daten bietet. Mit **Aspose.Cells** können Entwickler Daten exportieren, Tabellenkalkulationen bis ins kleinste Detail und auf jeder Ebene formatieren, Bilder importieren, Diagramme importieren, Diagramme erstellen, Diagramme manipulieren, Excel-Daten streamen, in verschiedenen Formaten wie XLS, CSV, SpreadsheetML, Tabellarisch, TXT, XML (integriert mit [Aspose.Pdf](https://products.aspose.com/pdf/)) und viele weitere speichern. **Aspose.Cells** bietet eine benutzerfreundliche, funktionsreiche **API** für die Programmierer. Es hat eine lange Liste von Funktionen. Um mehr über das Produkt, seine Funktionen und einen Programmierleitfaden zu erfahren, überprüfen Sie bitte die Zusammenfassung der **Funktionsliste**, die **Aspose.Cells-Dokumentation** und die online vorgestellten Demos. Sie können die Evaluierungsversion [herunterladen](https://downloads.aspose.com/cells) und kostenlos testen.
## **Gestaltung der Benutzeroberfläche**
Wir beginnen mit der Erstellung einer neuen Asp.Net-Webanwendung in Visual Studio.Net.

Ich füge zunächst dem Projekt **Verweise** auf die drei Komponenten hinzu, d.h. Aspose.Cells.GridWeb.dll, Aspose.Chart.dll und Aspose.Cells.dll. Ich platziere einige Steuerelemente auf der Seite und setze ihre Eigenschaften, d.h. eine Dropdown-Liste, eine Befehlsschaltfläche und ein Label. Dann füge ich das **Aspose.Cells.GridWeb-Steuerelement** (**GridWeb**) aus der Werkzeugleiste ein, da nach dem Hinzufügen von Verweisen zu den drei Komponenten das **GridWeb-Steuerelement** in der Werkzeugleiste angezeigt wird. Die anderen beiden Komponenten (**Aspose.Chart** und **Aspose.Cells**) sind nur Bibliotheken, die dem Projekt als Referenzen hinzugefügt werden.

Ich erstelle auch zwei Ordner namens "file" und "images" und füge die Dateien "Products.xml" und "chart.gif" hinzu. Die XML-Datei ist eine Datenquelle, aus der die Daten extrahiert werden, um das **GridWeb-Arbeitsblatt** zu füllen. Die Bilddatei wird ein Bild für eine benutzerdefinierte Schaltfläche auf dem **GridWeb-Steuerelement** bereitstellen.

Ich erstelle nun eine benutzerdefinierte Befehlsschaltfläche. Ich klicke einfach mit der rechten Maustaste auf das **GridWeb-Steuerelement** und wähle die Option "Benutzerdefinierte Befehlsschaltflächen...".

Dadurch wird der Editor für benutzerdefinierte Befehlsschaltflächen aktiviert. Der Editor ermöglicht es Ihnen, benutzerdefinierte Befehlsschaltflächen mit angehängtem Tooltiptext zu erstellen. Ich gebe die Werte für einige Eigenschaften der Schaltfläche an, z.B. Befehl (Name) -> "btnChart", ImageUrl -> geben Sie den Pfad zur Bilddatei ("chart.gif") an und ToolTip -> fügen Sie den Tooltiptext hinzu.

So wird die benutzerdefinierte Befehlsschaltfläche hinzugefügt, wie Sie sie im folgenden Screenshot sehen können (umrandet mit roter Farbe).

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Schließlich setze ich einige Schriftattribute (fett) für das Label und die Befehlsschaltfläche. Ich passe auch die Größe der Steuerelemente an, um den endgültigen Look zu erhalten.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Abrufen von Daten aus einer XML-Datei**
Nachfolgend finden Sie die in dem Projekt verwendete XML-Dateistruktur.
### **XML-Dateistruktur**
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
## **Füllen des Arbeitsblatts des Aspose.Cells.GridWeb-Steuerelements mit Daten**
Ich verwende einige APIs des **GridWeb-Steuerelements**, um ein Arbeitsblatt mit Daten aus der Quell-XML-Datei zu füllen. Ich schreibe den Code im Click-Ereignishandler der Befehlsschaltfläche (beschriftet mit "Bericht anzeigen"). Der Datenbericht wird basierend auf dem aus der Dropdown-Liste ausgewählten Element gefiltert.



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
## **Formatieren von Daten in den Zellen**
Um zwischen verschiedenen Arten von Informationen in einem Arbeitsblatt zu unterscheiden, für die optimale Anzeige der Daten auf Ihrem Arbeitsblatt und um ein Arbeitsblatt leichter zu scannen, formatieren Sie das Arbeitsblatt. Ein**Format**repräsentiert einen Stil und ist definiert als eine Reihe von Merkmalen, wie Schriftarten und Schriftgrößen, Zahlenformate, Zellenrahmen, Zellenschattierung mit einfarbiger Hintergrundfarbe oder einem spezifischen Farbmuster, Einrückung, Ausrichtung und Textausrichtung in den Zellen.

Ich füge einige weitere Zeilen Code zu oben hinzu. Ich platziere den Titel/Untertitel des Berichts, führe einige Formatierungen für Titel, Untertitel und Detailzellen durch. Ich wende auch einen Zahlenformatierung auf die beiden Felder an (setze das Währungsnummernformat auf die Felder UnitPrice und Sale) und passe die Höhe/Breite der Zeilen und Spalten mit**Aspose.Cells.GridWeb**API an.



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
## **Erstellung des formatierten Berichts (.XLS-Datei) mit Diagramm unter Verwendung des Aspose.Cells-Bausteins**
Nun werde ich einige Codes schreiben, um den formatierten Bericht mit Diagramm auf der Festplatte zu speichern. Ich nutze die**Speichern**Schaltfläche von**GridWeb**, das**Speichern**Ereignis von**GridWeb**wird ausgelöst, wenn Sie auf die Speichern-Schaltfläche klicken, daher werde ich es bearbeiten. Hier verwende ich den**Aspose.Cells**-Baustein, um den formatierten Bericht in MS Excel zu exportieren, ein Diagramm zu erstellen und es in die Ausgabedatei von Excel einzubetten. Ich habe das Diagrammbild (erstellt von**Aspose.Chart**-Baustein) nicht eingefügt, sondern das ähnliche Diagramm mithilfe der API von**Aspose.Cells**erstellt, sodass Sie das Diagramm in MS Excel nach Ihren Bedürfnissen bearbeiten können.





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
## **Ausführen der Anwendung**
Jetzt führe ich die Anwendung aus. Die Dropdown-Liste wird mit den unterschiedlichen Kategorien gefüllt.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Ich wähle eine Kategorie aus, für die ich den Verkaufsbericht anzeigen möchte, und klicke auf die Schaltfläche "Bericht anzeigen".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Der Bericht wird dann auf der**GridWeb**basierend auf der ausgewählten Kategorie angezeigt. Der Bericht wird standardmäßig basierend auf dem vorher geschriebenen Code formatiert.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Wenn Sie Daten in einigen Zellen in WYSIWYG-Manier formatieren möchten, können Sie dies recht einfach tun.**Aspose.Cells.GridWeb**bietet einen**Format Cells**-Editor, wählen Sie die gewünschten Zellen aus und klicken Sie mit der rechten Maustaste darauf, wählen Sie die Option "Zelle formatieren…".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Der Dialog zur Zellenformatierung wird angezeigt.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Ich gebe einige Schriftattributen an und klicke auf OK.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Und erhalte das Ergebnis.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Neben der Zellformatierung können Sie auch die Zellwerte bearbeiten. Doppelklicken Sie auf die gewünschten Zellen und bearbeiten Sie den Wert.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Um das Bearbeitungsergebnis zu übermitteln und alle Formeln neu zu berechnen, klicke ich auf die entsprechende Schaltfläche (mit roter Farbe umrandet), um den Bericht zu aktualisieren.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Nun werde ich das Diagramm erstellen und in die Steuerung einfügen. Ich klicke auf die benutzerdefinierte Befehlsschaltfläche (mit roter Farbe umrandet), um das Kuchendiagramm basierend auf dem Datenbereich zu erstellen.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Schließlich werde ich diesen Datenausweis mit Diagramm nach MS Excel exportieren. Ich klicke auf die**Speichern**Schaltfläche (mit roter Farbe umrandet). Beim Klicken auf die**Speichern**Schaltfläche wird der**Dateidownload**-Dialog angezeigt, Sie können entweder den resultierenden Bericht (Ausgabedatei von Excel mit Diagramm) in MS Excel öffnen oder ihn auf der Festplatte speichern.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Wenn ich auf die Schaltfläche "Öffnen" (Dateidownload-Dialog) klicke, wird der Excel-Bericht mit Diagramm nach MS Excel exportiert. Der obere Teil des Berichts wird angezeigt.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Der untere Teil des Excel-Berichts wird angezeigt.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
