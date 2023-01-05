---
title: Öffentlich API Änderungen in Aspose.Cells 8.4.1
type: docs
weight: 150
url: /de/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.4.0 zu 8.4.1, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-1/) und[Klassen entfernt usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-4-1/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Mechanismus zum Ändern der Datenbankverbindung**
Die Klasse com.aspose.cells.ExternalConnection enthielt bereits die Methode und die Eigenschaften, die verwendet werden konnten, um die in einer Tabelle gespeicherten Datenbankverbindungsdetails zu überprüfen. Die meisten Eigenschaften, die der Klasse ExternalConnection zugeordnet sind, waren bis zur Veröffentlichung von Aspose.Cells for Java 8.4.1 schreibgeschützt. Mit dieser Version hat die API die Unterstützung bereitgestellt, um auch die Datenbankverbindungseinstellungen zu manipulieren.

Das folgende Code-Snippet zeigt, wie Datenbankverbindungseinstellungen dynamisch geändert werden.

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

Hier sind einige der wichtigsten Eigenschaften, die von der Klasse {ExternalConnection}} bereitgestellt werden.

|**Name des Anwesens** |**Beschreibung** |
|:- |:- |
| HintergrundAktualisieren|Gibt an, ob die Verbindung im Hintergrund (asynchron) aktualisiert werden kann.<br> true, wenn die bevorzugte Verwendung der Verbindung die asynchrone Aktualisierung im Hintergrund ist;<br> false, wenn die bevorzugte Verwendung der Verbindung die synchrone Aktualisierung im Vordergrund ist.|
| Verbindungsbeschreibung| Gibt die Benutzerbeschreibung für diese Verbindung an|
| ConnectionId| Gibt den eindeutigen Bezeichner dieser Verbindung an.|
| Referenzen| Gibt die Authentifizierungsmethode an, die beim Herstellen (oder Wiederherstellen) der Verbindung verwendet werden soll.|
| Ist gelöscht|Gibt an, ob die zugehörige Arbeitsmappenverbindung gelöscht wurde. wahr, wenn die<br> Verbindung wurde gelöscht; andernfalls falsch.|
| Ist neu| True, wenn die Verbindung nicht zum ersten Mal aktualisiert wurde; andernfalls falsch. Diese<br> Zustand kann auftreten, wenn der Benutzer die Datei speichert, bevor eine Abfrage die Rückgabe beendet hat.|
| Bleib am Leben|True, wenn das Tabellenkalkulationsprogramm Anstrengungen unternehmen soll, um die Verbindung aufrechtzuerhalten<br> offen. Bei „false“ sollte die Anwendung die Verbindung nach dem Abrufen von schließen<br> Information.|
| Name| Gibt den Namen der Verbindung an. Jede Verbindung muss einen eindeutigen Namen haben.|
| OdcDatei| Gibt den vollständigen Pfad zur externen Verbindungsdatei an, von der diese Verbindung stammt<br> erstellt. Wenn eine Verbindung beim Versuch, Daten zu aktualisieren, fehlschlägt und reconnectionMethod=1,<br> dann versucht die Tabellenkalkulationsanwendung erneut, Informationen aus der externen Verbindungsdatei zu verwenden<br> anstelle des in die Arbeitsmappe eingebetteten Verbindungsobjekts.|
| OnlyUseConnectionFile| Gibt an, ob die Tabellenkalkulationsanwendung immer und nur die verwenden soll<br> Verbindungsinformationen in der externen Verbindungsdatei, die durch das Attribut odcFile angegeben wird<br> wenn die Verbindung aktualisiert wird. Wenn falsch, dann die Tabellenkalkulationsanwendung<br>sollte dem durch das Attribut reconnectionMethod angegebenen Verfahren folgen|
| Parameter| Ruft ConnectionParameterCollection für eine ODBC- oder Webabfrage ab.|
| ReConnectionMethod| Geben Sie den ReconnectionMethod-Typ an|
|AktualisierenIntern| Gibt die Anzahl der Minuten zwischen automatischen Aktualisierungen der Verbindung an.|
| Beim Laden aktualisieren| True, wenn diese Verbindung beim Öffnen der Datei aktualisiert werden soll; andernfalls falsch.|
| Daten speichern|True, wenn die über die Verbindung abgerufenen externen Daten zum Füllen einer Tabelle gespeichert werden sollen<br> mit dem Arbeitsbuch; andernfalls falsch.|
| Passwort speichern| True, wenn das Kennwort als Teil der Verbindungszeichenfolge gespeichert werden soll; andernfalls falsch.|
| Quelldatei| Wird verwendet, wenn die externe Datenquelle dateibasiert ist. Bei einer Verbindung zu solchen Daten<br> source fehlschlägt, versucht die Tabellenkalkulationsanwendung, eine direkte Verbindung zu dieser Datei herzustellen. Vielleicht<br> ausgedrückt in URI oder systemspezifischer Dateipfadnotation.|
|SSOID|Bezeichner für Single Sign On (SSO), der für die Authentifizierung zwischen einem Intermediate verwendet wird<br> SpreadsheetML-Server und die externe Datenquelle.|
| Typ| Gibt den Datenquellentyp an.|

### **Möglichkeit zum Formatieren einer Teilzeichenfolge des DataLabels-Textes**
Aspose.Cells for Java 8.4.1 hat die DataLabels.characters-Methode verfügbar gemacht, um eine Instanz der FontSetting-Klasse abzurufen, die der Teilzeichenfolge von ChartPoints.DataLabels entspricht. Die Instanz der FontSetting-Klasse kann wiederum verwendet werden, um die Teilzeichenfolge der DataLabels mit unterschiedlichen Schriftarteinstellungen und Farben zu formatieren.

Der folgende Codeausschnitt zeigt, wie die DataLabels.characters-Methode verwendet wird.

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

### **Möglichkeit, die gewünschten Bildabmessungen für den Export von Tabellenkalkulationen und Diagrammen festzulegen**
Aspose.Cells for Java 8.4.1 hat die ImageOrPrintOptions.setDesiredSize-Methode verfügbar gemacht, um die Abmessungen des resultierenden Bildes festzulegen, während Tabellenkalkulationen und Diagramme in Bilder exportiert werden. Die Methode ImageOrPrintOptions.setDesiredSize akzeptiert zwei ganzzahlige Parameter, wobei der erste die gewünschte Breite und der zweite die gewünschte Höhe ist.

Das folgende Code-Snippet zeigt, wie Sie die gewünschten Abmessungen beim Exportieren des Arbeitsblatts auf PNG festlegen.

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

 Dieselbe Methode kann auch zum Konvertieren von Diagrammen in Bilder verwendet werden.

{{% /alert %}} 

### **Rendern von Kommentaren zu PDF**
 Mit der Veröffentlichung von v8.4.1 hat Aspose.Cells API die PageSetup.PrintComments-Eigenschaft und die PrintCommentsType-Enumeration bereitgestellt, um das Rendern von Kommentaren beim Konvertieren von Tabellenkalkulationen in das PDF-Format zu erleichtern. Die PrintCommentsType-Enumeration hat die folgenden Konstanten.

- PrintCommentsType.PRINT_NEIN_KOMMENTARE: Kommentare dürfen nicht wiedergegeben werden.
- PrintCommentsType.PRINT_IN_PLACE: Kommentare sollen dort gerendert werden, wo sie platziert sind.
- PrintCommentsType.PRINT_BLATT_ENDE: Kommentare sollen am Ende des Arbeitsblatts ausgegeben werden.

Der folgende Beispielcode veranschaulicht die Verwendung der PageSetup.PrintComments-Eigenschaft zum Rendern der Kommentare unter Verwendung aller möglichen PrintCommentsType-Enumerationswerte.

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

### **Workbook.isLicensed-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.4.1 hat Workbook.isLicensed verfügbar gemacht, was bei der Bestimmung, ob die Lizenz erfolgreich geladen wurde oder nicht, eine große Hilfe sein könnte. Wenn Sie auf diese Eigenschaft zugreifen, bevor Sie die Lizenz festlegen, wird false zurückgegeben und umgekehrt, die Lizenz sollte jedoch gültig sein.

Der folgende Beispielcode veranschaulicht die Verwendung der Workbook.isLicensed-Eigenschaft.

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

### **ImageOrPrintOptions.SVGFitToViewPort-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.4.1 hat die SVGFitToViewPort-Eigenschaft für die ImageOrPrintOptions-Klasse verfügbar gemacht, die verwendet werden kann, um das viewBox-Attribut für das SVG-Dateiformat zu aktivieren, während Tabellenkalkulationen oder Diagramme in das SVG-Format exportiert werden. Der Standardwert dieser Eigenschaft ist „false“, daher wird das Basis-XML für die SVG-Datei, die ohne Festlegen der oben genannten Eigenschaft generiert wird, das viewBox-Attribut nicht enthalten.

Der folgende Beispielcode veranschaulicht die Verwendung der ImageOrPrintOptions.SVGFitToViewPort-Eigenschaft.

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
## **Veraltete APIs**
### **Methode Workbook.validateFormula Veraltet**
Verwenden Sie die Eigenschaft Cell.Formula, um die Formel zu validieren.
