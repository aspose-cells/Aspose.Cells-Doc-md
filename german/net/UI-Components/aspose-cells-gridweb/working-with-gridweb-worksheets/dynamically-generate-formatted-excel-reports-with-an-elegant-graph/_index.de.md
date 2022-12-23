---
title: Erstellen Sie dynamisch formatierte Excel-Berichte mit einem eleganten Diagramm
type: docs
weight: 130
url: /de/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Dieses Dokument soll die notwendigen Informationen liefern, wie wir Daten aus einer Datenquelle in ein hervorragendes rasterähnliches Steuerelement extrahieren, ein Diagramm darin einfügen und den Bericht mit Diagramm nach MS Excel exportieren können, um Analysen, Vergleiche und den Druck durchzuführen.

{{% /alert %}} 
## **Überblick**
Es gibt bestimmte Webszenarien, die sowohl Berichterstellung als auch Präsentationen erfordern, eine Kombination aus Teilen oder Objekten, die gut zusammenarbeiten können. Der Artikel erklärt, wie einfach es ist, stilvolle Excel-Berichte dynamisch im WYSIWYG-Stil zu entwerfen und zu generieren. Es exportiert Daten aus einer XML-Datei (Sie können auch andere Datenquellen verwenden) in das Aspose.Cells.GridWeb-Steuerelement, das Ihnen die reale Umgebung bietet, die es Ihnen ermöglicht, reichhaltige und ansprechende Formate auf Daten anzuwenden und Formelergebnisse wie MS Excel zu berechnen. Es generiert auch ein ausgeklügeltes Diagramm basierend auf den Quelldaten des Arbeitsblatts[Aspose.Cells](https://products.aspose.com/cells/) Komponente und fügt das Diagrammbild in den Verkaufsbericht ein. Schließlich wird der Excel-Bericht mit angehängtem Diagramm mit der Komponente Aspose.Cells auf der Festplatte gespeichert.

Dieser Artikel enthält den Quellcode und das voll funktionsfähige Demoprojekt für diese Funktionalität.

Es ermöglicht den Benutzern mit einer detaillierten Vorstellung davon, wie man einen Geschäftsbericht erstellt, Daten in ein Arbeitsblatt des Rasters einzugeben und einige Formatierungen auf die Zellen in den Zeilen und Spalten anzuwenden, ein Diagramm basierend auf dem Quelldatenbereich einzubetten, bevor der gespeichert wird Excel-Bericht auf die Festplatte.
## **Die Aspose Komponenten**
 Ich benutze drei davon[Aspose](http://www.aspose.com/) 's-Komponenten, um die Aufgabe mit Leichtigkeit auszuführen.[Aspose](http://www.aspose.com/) , Der .NET und Java Component Publisher, bietet eine Vielzahl von funktionsreichen Komponenten.[Aspose](http://www.aspose.com/) bietet eine große Auswahl an .NET- und Java-Komponenten. Die Produkte, auf die Tausende von Kunden weltweit vertrauen, umfassen Dateiformatkomponenten, Berichterstellungsprodukte, visuelle Komponenten und Hilfskomponenten, die das programmgesteuerte Öffnen, Ändern, Generieren, Speichern, Zusammenführen, Konvertieren usw. von Dokumenten in verschiedenen Formaten, einschließlich DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, Tabulatorgetrennt, CSV, PPT, SWF, EMF, WMF, MPX, MPD und andere Formate.

Ich möchte diese Gelegenheit nutzen, um Ihnen drei dieser Komponenten vorzustellen, die in dieser Suche verwendet wurden.
## **Aspose.Cells Grid-Steuerelemente**
 Aspose.Cells Grid Controls sind eine vollständige Grid-Lösung. Aspose.Cells Grid Controls werden mit zwei verschiedenen .NET GUI-Komponenten (Aspose.Cells.GridDesktop und Aspose.Cells.GridWeb) geliefert: eine zur Unterstützung von Desktopanwendungen und eine zur Unterstützung von Webanwendungen. Beide Versionen sind gleichermaßen aufeinander abgestimmt, um die Implementierung auf beiden Plattformen zum Kinderspiel zu machen. Aspose.Cells.GridWeb bietet die Möglichkeit zum Importieren und Exportieren in Excel-Tabellen. Jeder, der mit Excel vertraut ist (sogar Endbenutzer), kann das Erscheinungsbild eines Rasters entwerfen. Aspose.Cells.GridWeb bietet auch ein benutzerfreundliches, funktionsreiches API, das Entwicklern die vollständige Kontrolle über das Aussehen, die Bedienung und das Verhalten ihres Grids gibt. Um mehr über das Produkt, seine Funktionen und einen Programmierleitfaden zu erfahren, lesen Sie bitte die Zusammenfassung der Funktionsliste, Aspose.Cells.GridWeb-Dokumentation und Online-Features[Demos](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**ist eine Berichterstellungskomponente für Excel-Tabellen, mit der Sie Excel-Tabellen lesen und schreiben können, ohne dass Microsoft Excel auf der Client- oder Serverseite installiert werden muss.**Aspose.Cells** ist eine funktionsreiche Komponente, die viel mehr bietet als nur das einfache Exportieren von Daten. Mit**Aspose.Cells** Entwickler können Daten exportieren, Tabellen bis ins kleinste Detail und auf jeder Ebene formatieren, Bilder importieren, Diagramme importieren, Diagramme erstellen, Diagramme manipulieren, Excel-Daten streamen, in verschiedenen Formaten speichern, einschließlich XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) integriert) und viele mehr.**Aspose.Cells** bietet eine einfach zu bedienende, funktionsreiche**API** für die Programmierer. Es hat eine riesige Liste von Funktionen. Um mehr über das Produkt, seine Funktionen und eine Programmieranleitung zu erfahren, lesen Sie bitte die Zusammenfassung von**Funktionsliste**, **Aspose.Cells Dokumentation** und online vorgestellte Demos. Sie können[Download](https://downloads.aspose.com/cells) seine Evaluierungsversion kostenlos.
## **Entwerfen der Schnittstelle**
Wir beginnen mit der Erstellung einer neuen Asp.Net-Webanwendung in Visual Studio.Net.

 ich**Referenz hinzufügen**zu den drei Komponenten dh Aspose.Cells.GridWeb.dll, Aspose.Chart.dll und Aspose.Cells.dll zum Projekt zuerst. Ich platziere einige Steuerelemente auf der Seite und lege ihre Eigenschaften fest, dh eine Dropdown-Liste, eine Befehlsschaltfläche und ein Label. Ich stelle dann**Aspose.Cells.GridWeb****Kontrolle**(**GridWeb**) aus der Toolbox hinzufügen, da nach dem Hinzufügen von Verweisen auf die drei Komponenten die**GridWeb**Steuerelement wird in der Toolbox angezeigt. Die anderen beiden Komponenten (**Aspose.Chart**und**Aspose.Cells**) sind nur Bibliotheken, die nur auf das Projekt verweisen.

Ich erstelle auch zwei Ordner "file" und "images", füge diesen Ordnern jeweils "Products.xml" und "chart.gif" hinzu. Die XML-Datei ist eine Datenquelldatei, aus der die Daten extrahiert werden, um die zu füllen**GridWeb**Arbeitsblatt. Die Bilddatei stellt ein Bild für eine benutzerdefinierte Schaltfläche bereit, die auf der platziert wird**GridWeb**Kontrolle.

Ich erstelle jetzt eine benutzerdefinierte Befehlsschaltfläche. Ich klicke einfach mit der rechten Maustaste auf die**GridWeb**Steuerelement und klicken Sie auf die Option „Benutzerdefinierte Befehlsschaltflächen…“.

Dadurch wird der Editor für benutzerdefinierte Befehlsschaltflächen aktiviert. Der Editor ermöglicht es Ihnen, benutzerdefinierte Bildschaltflächen mit angehängtem Tooltip zu erstellen. Ich gebe die Werte für einige Eigenschaften der Schaltfläche an, zB Command (Name) -> "btnChart", ImageUrl -> gebe den Pfad zur Bilddatei an ("chart.gif") und ToolTip -> gebe den Tooltip an.

Die benutzerdefinierte Befehlsschaltfläche wird also hinzugefügt, wie Sie sie im folgenden Screenshot sehen können (mit roter Farbe eingekreist).

|![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Schließlich setze ich einige Schriftattribute (fett) für die Beschriftung und die Befehlsschaltfläche. Ich passe auch die Größe der Steuerelemente an, um das endgültige Aussehen zu erhalten.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Abrufen von Daten aus einer XML-Datei**
Es folgt die XML-Dateistruktur, die im Projekt verwendet wird.
### **XML-Dateistruktur**
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
## **Füllen des Arbeitsblatts des Steuerelements Aspose.Cells.GridWeb mit Daten**
Ich verwende einige der API**GridWeb**-Steuerelement, um ein Arbeitsblatt mit Daten aus der XML-Quelldatei zu füllen. Ich schreibe Code in den Click-Event-Handler der Befehlsschaltfläche (mit der Bezeichnung „Show Report“). Der Datenbericht wird basierend auf dem ausgewählten Element aus der Dropdown-Liste gefiltert.



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
## **Formatieren von Daten in Cells**
Um zwischen verschiedenen Arten von Informationen auf einem Arbeitsblatt zu unterscheiden, die Daten auf Ihrem Arbeitsblatt optimal anzuzeigen und ein Arbeitsblatt einfacher scannen zu können, formatieren Sie das Arbeitsblatt. EIN**Format**stellt einen Stil dar und ist definiert als eine Reihe von Merkmalen, wie z. B. Schriftarten und Schriftgrößen, Zahlenformate, Zellenumrandungen, Zellenschattierung mit einfarbiger Hintergrundfarbe oder einem bestimmten Farbmuster, Einzug, Ausrichtung und Textausrichtung in den Zellen.

Ich füge einige weitere Codezeilen zu oben zusammen. Ich platziere den Titel/Untertitel des Berichts, formatiere Titel, Untertitel und Detailzellen. Ich wende auch die Zahlenformatierung auf die beiden Felder an (stellen Sie das Währungszahlenformat auf die Felder UnitPrice und Sale ein) und passen Sie die Höhe/Breite von Zeilen und Spalten an**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 // Titelzelle (A1) im Blatt erstellen und Formatierungen anwenden.

//Die folgenden Zeilen geben einen Zeichenfolgenwert in die Zelle ein, angeben

//Schriftgröße, horizontale und vertikale Ausrichtungseinstellungen festlegen, festlegen

//Vordergrund- und Hintergrundfarben und Zellen verbinden (A1:E2).

WebWorksheet-Blatt = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Produktverkäufe nach Kategorie");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

Blatt.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

Blatt.Cells["A1"].Style.BackColor = Color.SkyBlue;

Blatt.Cells["A1"].Style.ForeColor = Farbe.Blau;

sheet.Cells.Merge(0, 0, 2, 5);

//Untertitelzelle (A3) im Blatt erstellen und Formatierungen anwenden.

//Die folgenden Zeilen geben einen Zeichenfolgenwert in die Zelle ein, angeben

//Schriftgröße mit Attributen, horizontale und vertikale Ausrichtung angeben

//Einstellungen, Vordergrund- und Hintergrundfarben festlegen und Zellen verbinden

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

Blatt.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

Blatt.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

Blatt.Cells["A3"].Style.BackColor = Color.SeaGreen;

Blatt.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Letzte Zeilen- und Spaltenindizes (die Daten enthalten) abrufen.

int Gesamtzeile = Blatt.Cells.MaxRow +1;

int totalcol = Blatt.Cells.MaxColumn;

// Holen Sie sich die Blatt Cells Sammlungen

WebCells-Zellen = Blatt.Cells;

//Objekt Cell definieren.

WebCell-Zelle;

//Durchlaufen Sie die Daten im Blatt und formatieren Sie zwei Felder mit

//Währungszahlenstil.

für (int i = 4;i<=totalrow;i++)

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
## **Erstellen des formatierten Berichts (.XLS-Datei) mit Graph unter Verwendung der Aspose.Cells-Komponente**
Jetzt werde ich etwas Code schreiben, um den formatierten Bericht mit Diagramm auf der Festplatte zu speichern. Ich nutze**GridWeb** 's**Speichern**Knopf, der**GridWeb** 's**SaveCommand**Das Ereignis wird ausgelöst, wenn Sie auf die Schaltfläche Speichern klicken, also werde ich es handhaben. Hier benutze ich**Aspose.Cells**Komponente, um den formatierten Bericht nach MS Excel zu exportieren, ein Diagramm zu erstellen und es in die Excel-Ausgabedatei einzubetten. Ich habe das Diagrammbild nicht eingefügt (erstellt von**Aspose.Chart**Komponente) erstellen Sie stattdessen das ähnliche Diagramm mit der API von**Aspose.Cells**damit Sie das Diagramm in MS Excel nach Bedarf bearbeiten können.





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
## **Ausführen der Anwendung**
Jetzt führe ich die Anwendung aus. Die Dropdown-Liste wird mit den unterschiedlichen Kategorien gefüllt.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Ich wähle eine Kategorie aus, nach der ich den Verkaufsbericht anzeigen möchte, und klicke auf die Schaltfläche "Bericht anzeigen".

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Der Bericht wird also in angezeigt**GridWeb**basierend auf der ausgewählten Kategorie. Der Bericht wird standardmäßig basierend auf dem (zuvor geschriebenen) Code formatiert.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Wenn Sie Daten in einigen der Zellen in WYSIWYG-Manier formatieren möchten, können Sie dies ganz einfach tun.**Aspose.Cells.GridWeb**bietet**Cells formatieren**Editor, wählen Sie die gewünschte(n) Zelle(n) aus und klicken Sie mit der rechten Maustaste darauf, klicken Sie auf die Option „Format Cell…“.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Der Dialog Format Cell wird angezeigt.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Ich gebe einige Schriftattribute an und klicke auf OK.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Und erhalten Sie das Ergebnis.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Neben der Zellenformatierung können Sie auch Ihre Zellenwerte bearbeiten. Doppelklicken Sie auf die gewünschte(n) Zelle(n) und bearbeiten Sie den Wert.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Um das Bearbeitungsergebnis zu übermitteln und die gesamte Formel neu zu berechnen, klicke ich auf die entsprechende Schaltfläche (rot eingekreist), um den Bericht zu aktualisieren.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Jetzt erstelle ich das Diagramm und füge es in das Steuerelement ein. Ich klicke auf die benutzerdefinierte Befehlsschaltfläche (rot eingekreist), um das Kreisdiagramm basierend auf dem Datenbereich zu erstellen.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Schließlich werde ich diesen Datenbericht mit Diagramm nach MS Excel exportieren. Ich klicke auf die**Speichern**Schaltfläche (mit roter Farbe eingekreist). Ein Klick auf die**Speichern**Schaltfläche wird angezeigt**Datei download**Dialog, Sie können entweder**Offen**den resultierenden Bericht (Ausgabe-Excel-Datei mit Diagramm) in MS Excel oder auf der Festplatte speichern.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Wenn ich auf die Schaltfläche „Öffnen“ (Dialogfeld „Dateidownload“) klicke, wird der Excel-Bericht mit Diagramm nach MS Excel exportiert. Der obere Teil des Berichts wird angezeigt.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Der untere Teil des Excel-Berichts wird angezeigt.

![todo: Bild_alt_Text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
