---
title: Öffentliche API Änderungen in Aspose.Cells 8.4.1
type: docs
weight: 140
url: /de/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.4.0 auf 8.4.1, die für Modul-/Anwendungs-Entwickler interessant sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-1/) und [entfernte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-4-1/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Mechanismus zur Änderung der Datenbankverbindung**
Die Klasse Aspose.Cells.ExternalConnections.ExternalConnection enthielt bereits die Methode und Eigenschaften, die zur Überprüfung der in einer Arbeitsmappe gespeicherten Datenbankverbindungsdetails verwendet werden konnten. Die meisten Eigenschaften, die mit der Klasse Aspose.Cells.ExternalConnections.ExternalConnection verbunden sind, waren bis zur Version Aspose.Cells for .NET 8.4.1 schreibgeschützt. Mit dieser Version bietet die API nun auch Unterstützung zur Manipulation der Datenbankverbindungseinstellungen.

Der folgende Codeauszug zeigt, wie die Datenbankeinstellungen dynamisch geändert werden können.

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



Hier sind einige der wichtigsten Eigenschaften, die von der {Aspose.Cells.ExternalConnections.ExternalConnection-Klasse} freigegeben werden.

|**Eigenschaftsname**|**Beschreibung**|
| :- | :- |
|BackgroundRefresh|Gibt an, ob die Verbindung im Hintergrund (asynchron) aktualisiert werden kann.<br>true, wenn die bevorzugte Verwendung der Verbindung darin besteht, asynchron im Hintergrund zu aktualisieren;<br>false, wenn die bevorzugte Verwendung der Verbindung darin besteht, synchron im Vordergrund zu aktualisieren.|
|ConnectionDescription|Gibt die Benutzerbeschreibung für diese Verbindung an|
|ConnectionId|Gibt die eindeutige Kennung für diese Verbindung an.|
|Credentials|Gibt die Authentifizierungsmethode an, die beim Herstellen (oder Wiederherstellen) der Verbindung verwendet werden soll.|
|IsDeleted|Gibt an, ob die zugehörige Arbeitsmappe-Verbindung gelöscht wurde. true, wenn die Verbindung gelöscht wurde; ansonsten false.|
|IsNew|True, wenn die Verbindung noch nicht zum ersten Mal aktualisiert wurde; ansonsten false. Dieser Zustand kann eintreten, wenn der Benutzer die Datei speichert, bevor eine Abfrage mit Ergebnis zurückgegeben wurde.|
|KeepAlive|True, wenn die Tabellenkalkulationsanwendung Anstrengungen unternehmen sollte, um die Verbindung offen zu halten. Wenn false, sollte die Anwendung die Verbindung nach dem Abrufen der Informationen schließen.|
|Name|Gibt den Namen der Verbindung an. Jede Verbindung muss über einen eindeutigen Namen verfügen.|
|OdcFile|Gibt den vollständigen Pfad zur externen Verbindungsdatei an, aus der diese Verbindung erstellt wurde. Wenn eine Verbindung bei einem Versuch der Datenaktualisierung fehlschlägt und reconnectionMethod = 1 ist, wird die Tabellenkalkulationsanwendung erneut versuchen, die Informationen aus der externen Verbindungsdatei anstelle des in der Arbeitsmappe eingebetteten Verbindungsobjekts zu verwenden.|
|OnlyUseConnectionFile|Gibt an, ob die Tabellenkalkulationsanwendung immer und nur die Verbindungsinformationen in der durch das odcFile-Attribut angezeigten externen Verbindungsdatei verwenden sollte, wenn die Verbindung aktualisiert wird. Wenn false ist, sollte die Tabellenkalkulationsanwendung den im reconnectionMethod-Attribut angezeigten Prozess befolgen.|
|Parameter|Erhalten ConnectionParameterCollection für eine ODBC- oder Web-Abfrage.|
|ReConnectionMethod|Geben Sie den Typ der ReconnectionMethod an.|
|RefreshInternal| Gibt die Anzahl der Minuten zwischen automatischen Aktualisierungen der Verbindung an.
|RefreshOnLoad|True, wenn diese Verbindung beim Öffnen der Datei aktualisiert werden soll, andernfalls false.|
|SaveData|True, wenn die externen Daten, die über die Verbindung abgerufen werden, um eine Tabelle zu bevölkern, mit der Arbeitsmappe gespeichert werden sollen; andernfalls false.|
|SavePassword|True, wenn das Kennwort als Teil der Verbindungszeichenfolge gespeichert werden soll; andernfalls False.|
|SourceFile|Wird verwendet, wenn die externe Datenquelle dateibasiert ist. Wenn eine Verbindung zu einer solchen Datenquelle fehlschlägt, versucht die Tabellenkalkulationsanwendung, sich direkt mit dieser Datei zu verbinden. Kann in URI- oder systemspezfische Pfadnotation ausgedrückt werden.|
|SSOId| Kennung für Single Sign On (SSO), die zur Authentifizierung zwischen einem Zwischen-Tabellenkalkulations-Server und der externen Datenquelle verwendet wird.
|Typ|Gibt den Datenquelle-Typ an.|

### **Fähigkeit, einen Teil des Texts der Datenbeschriftungen zu formatieren**
Aspose.Cells for .NET 8.4.1 hat die Methode DataLabels.Characters freigelegt, um eine Instanz der Klasse FontSetting abzurufen, die dem Teilstring eines ChartPoints.DataLabels entspricht. Die Instanz der Klasse FontSetting kann wiederum verwendet werden, um den Teilstring der DataLabels mit unterschiedlichen Schriftart-Einstellungen und Farbe zu formatieren.

Der folgende Code-Ausschnitt zeigt, wie die Methode DataLabels.Characters verwendet wird.

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


### **Fähigkeit, die gewünschten Bildabmessungen für den Export von Arbeitsmappe und Diagramm festzulegen**
Aspose.Cells for .NET 8.4.1 hat die Methode ImageOrPrintOptions.SetDesiredSize freigelegt, um die Dimensionen des resultierenden Bildes beim Export von Tabellenkalkulationen & Charts auf Bilder festzulegen. Die Methode ImageOrPrintOptions.SetDesiredSize akzeptiert zwei Parameter vom Typ Integer, wobei der erste die gewünschte Breite und der zweite die gewünschte Höhe ist.

Der folgende Code-Schnipsel zeigt, wie die gewünschten Abmessungen beim Exportieren des Arbeitsblatts in PNG festgelegt werden.

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

Dasselbe Attribut kann auch für die Konvertierung von Diagrammen in Bilder verwendet werden.

{{% /alert %}} 


### **Kommentare als PDF rendern**
Mit der Version v8.4.1 hat die Aspose.Cells-API die Eigenschaft PageSetup.PrintComments und die Aufzählung PrintCommentsType zur Verfügung gestellt, um das Rendern von Kommentaren beim Konvertieren von Tabellenkalkulationen in das PDF-Format zu erleichtern. Die Aufzählung PrintCommentsType hat die folgenden Konstanten.

- PrintCommentsType.PrintNoComments: Kommentare werden nicht gerendert.
- PrintCommentsType.PrintInPlace: Kommentare werden dort gerendert, wo sie platziert sind.
- PrintCommentsType.PrintSheetEnd: Kommentare sollen am Ende des Arbeitsblatts gerendert werden.

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft PageSetup.PrintComments, um die Kommentare mit allen möglichen Werten der Aufzählung PrintCommentsType zu rendern.

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


### **Arbeitsblätter in Aspose.Cells.GridDesktop verschieben**
Aspose.Cells.GridDesktop bietet die WorksheetCollection.MoveTo-Methode, die verwendet werden kann, um ein Arbeitsblatt zum angegebenen Index zu verschieben. Die genannte Methode nimmt die Indizes (nullbasiert) des Quell-Arbeitsblatts und des Ziel-Arbeitsblatts als Parameter.

Der folgende Beispielcode zeigt die Verwendung der WorksheetCollection.MoveTo-Eigenschaft.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Eigenschaft Workbook.IsLicensed hinzugefügt**
Aspose.Cells for .NET 8.4.1 hat die Workbook.IsLicensed freigelegt, die bei der Bestimmung hilfreich sein könnte, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie auf diese Eigenschaft zugreifen, bevor Sie die Lizenz festlegen, gibt sie false zurück, und umgekehrt. Die Lizenz sollte jedoch gültig sein.

Der folgende Beispielcode zeigt die Verwendung der Workbook.IsLicensed-Eigenschaft.

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


### **Hinzugefügtes ImageOrPrintOptions.SVGFitToViewPort-Attribut**
Aspose.Cells for .NET 8.4.1 hat die SVGFitToViewPort-Eigenschaft für die ImageOrPrintOptions-Klasse freigelegt, die beim Exportieren von Tabellenkalkulationen oder Diagrammen in das SVG-Format verwendet werden kann, um das viewBox-Attribut einzuschalten. Der Standardwert dieser Eigenschaft ist false. Daher wird das Basismodell für die SVG-Datei ohne Einstellung der genannten Eigenschaft das viewBox-Attribut nicht enthalten.

Der folgende Beispielcode zeigt die Verwendung des ImageOrPrintOptions.SVGFitToViewPort-Attributs.

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
## **Veraltete APIs**
### **Methode Workbook.ValidateFormula veraltet**
Verwenden Sie die Cell.Formula-Methode, um die Formel zu validieren.
