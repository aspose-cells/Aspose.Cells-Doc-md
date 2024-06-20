---
title: Öffentliche API Änderungen in Aspose.Cells 8.4.1
type: docs
weight: 150
url: /de/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells API von Version 8.4.0 auf 8.4.1, die für Modul-/Anwendungsentwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/de/java/public-api-changes-in-aspose-cells-8-4-1/) und [entfernte Klassen usw.](/de/java/public-api-changes-in-aspose-cells-8-4-1/), sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Mechanismus zur Änderung der Datenbankverbindung**
Die Klasse com.aspose.cells.ExternalConnection enthielt bereits die Methode und Eigenschaften, die zur Inspektion der in einer Tabellenkalkulation gespeicherten Datenbankverbindungsdetails verwendet werden konnten. Die meisten Eigenschaften, die mit der Klasse ExternalConnection verbunden waren, waren bis zur Version Aspose.Cells for Java 8.4.1 schreibgeschützt. Mit dieser Version hat die API die Unterstützung zur Manipulation der Datenbankverbindungseinstellungen bereitgestellt.

Der folgende Codeauszug zeigt, wie die Datenbankeinstellungen dynamisch geändert werden können.

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

Hier sind einige der wichtigsten von der {ExternalConnection}-Klasse freigegebenen Eigenschaften.

|**Eigenschaftsname** |**Beschreibung** |
| :- | :- |
|BackgroundRefresh |Gibt an, ob die Verbindung im Hintergrund aktualisiert werden kann (asynchron). <br>true, wenn die bevorzugte Verwendung der Verbindung darin besteht, sie im Hintergrund asynchron zu aktualisieren; <br>false, wenn die bevorzugte Verwendung der Verbindung darin besteht, sie synchron im Vordergrund zu aktualisieren. |
|ConnectionDescription |Gibt die Benutzerbeschreibung für diese Verbindung an |
|ConnectionId |Gibt die eindeutige Kennung dieser Verbindung an. |
|Credentials |Legt die Authentifizierungsmethode fest, die beim Herstellen (oder Wiederherstellen) der Verbindung verwendet werden soll. |
|IsDeleted |Gibt an, ob die zugehörige Arbeitsmapppenverbindung gelöscht wurde. true, wenn die<br>Verbindung gelöscht wurde; andernfalls false. |
|IsNew |True, wenn die Verbindung noch nicht zum ersten Mal aktualisiert wurde; andernfalls false. Dieser <br>Zustand kann eintreten, wenn der Benutzer die Datei speichert, bevor eine Abfrage zur Rückgabe fertig ist. |
|KeepAlive |True, wenn die Tabellenkalkulationsanwendung versuchen sollte, die Verbindung offenzuhalten. Wenn false, sollte die Anwendung die Verbindung nach dem Abrufen der Informationen schließen.
|Name |Gibt den Namen der Verbindung an. Jede Verbindung muss einen eindeutigen Namen haben.
|OdcFile |Gibt den vollständigen Pfad zur externen Verbindungsdatei an, aus der diese Verbindung erstellt wurde. Wenn eine Verbindung bei einem Versuch, Daten zu aktualisieren, fehlschlägt und reconnectionMethod=1, wird die Tabellenkalkulationsanwendung erneut versuchen, die Informationen aus der externen Verbindungsdatei anstelle des in der Arbeitsmappe eingebetteten Verbindungsobjekts zu verwenden.
|OnlyUseConnectionFile |Gibt an, ob die Tabellenkalkulationsanwendung immer und nur die Verbindungsinformationen in der externen Verbindungsdatei, die durch das odcFile-Attribut angegeben ist, verwenden sollte, wenn die Verbindung aktualisiert wird. Wenn false, sollte die Tabellenkalkulationsanwendung das Verfahren gemäß dem reconnectionMethod-Attribut befolgen.
|Parameters |Ruft ConnectionParameterCollection für eine ODBC- oder Webabfrage ab.
|ReConnectionMethod |Gibt den ReconnectionMethod-Typ an.
|RefreshInternal|Gibt die Anzahl der Minuten zwischen automatischen Aktualisierungen der Verbindung an.
|RefreshOnLoad |True, wenn diese Verbindung beim Öffnen der Datei aktualisiert werden soll; andernfalls False.
|SaveData |True, wenn die externen Daten, die über die Verbindung abgerufen werden, um eine Tabelle zu befüllen, mit der Arbeitsmappe gespeichert werden sollen; andernfalls False.
|SavePassword |True, wenn das Passwort als Teil der Verbindungszeichenfolge gespeichert werden soll; andernfalls False.
|SourceFile |Wird verwendet, wenn die externe Datenquelle dateibasiert ist. Wenn eine Verbindung zu einer solchen Datenquelle fehlschlägt, versucht die Tabellenkalkulationsanwendung, direkt auf diese Datei zuzugreifen. Kann in URI- oder systemspezifischer Dateipfadnotation ausgedrückt werden.
|SSOId|Kennung für Single Sign On (SSO), die zur Authentifizierung zwischen einem Zwischen-SpreadsheetML-Server und der externen Datenquelle verwendet wird.
|Type |Gibt den Datenquellentyp an.

### **Fähigkeit, einen Teil des Texts der Datenbeschriftungen zu formatieren**
Aspose.Cells for Java 8.4.1 hat die DataLabels.characters-Methode freigelegt, um eine Instanz der FontSetting-Klasse abzurufen, die dem Teil-String von ChartPoints.DataLabels entspricht. Die Instanz der FontSetting-Klasse kann wiederum verwendet werden, um den Teil-String der DataLabels mit verschiedenen Schriftarteinstellungen und Farben zu formatieren.

Der folgende Code-Schnipsel zeigt, wie die DataLabels.characters-Methode verwendet wird.

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

### **Fähigkeit, die gewünschten Bildabmessungen für den Export von Arbeitsmappe und Diagramm festzulegen**
Aspose.Cells for Java 8.4.1 hat die ImageOrPrintOptions.setDesiredSize-Methode freigelegt, um die Dimensionen des resultierenden Bilds beim Export von Arbeitsmappen und Diagrammen in Bilder festzulegen. Die ImageOrPrintOptions.setDesiredSize-Methode akzeptiert zwei Parameter vom Typ Integer, wobei der erste die gewünschte Breite und der zweite die gewünschte Höhe ist.

Der folgende Code-Schnipsel zeigt, wie die gewünschten Abmessungen beim Exportieren des Arbeitsblatts in PNG festgelegt werden.

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

Derselbe Methode kann auch verwendet werden, um Diagramme in Bilder zu konvertieren. 

{{% /alert %}} 

### **Kommentare als PDF rendern**
Mit der Version v8.4.1 hat die Aspose.Cells-API die Eigenschaft PageSetup.PrintComments und die Aufzählung PrintCommentsType zur Verfügung gestellt, um das Rendern von Kommentaren beim Konvertieren von Tabellenkalkulationen in das PDF-Format zu erleichtern. Die Aufzählung PrintCommentsType hat die folgenden Konstanten. 

- PrintCommentsType.PRINT_NO_COMMENTS: Kommentare sollen nicht gerendert werden.
- PrintCommentsType.PRINT_IN_PLACE: Kommentare sollen an der Stelle gerendert werden, an der sie platziert sind.
- PrintCommentsType.PRINT_SHEET_END: Kommentare sollen am Ende des Arbeitsblatts gerendert werden.

Der folgende Beispielcode zeigt die Verwendung der Eigenschaft PageSetup.PrintComments, um die Kommentare mit allen möglichen Werten der Aufzählung PrintCommentsType zu rendern.

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

### **Hinzugefügtes Workbook.isLicensed-Attribut**
Aspose.Cells for Java 8.4.1 hat das Workbook.isLicensed-Attribut freigelegt, das bei der Bestimmung hilfreich sein könnte, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie auf dieses Attribut zugreifen, bevor Sie die Lizenz setzen, wird es false zurückgeben und umgekehrt, jedoch sollte die Lizenz gültig sein.

Der folgende Beispielcode zeigt die Verwendung des Workbook.isLicensed-Attributs.

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

### **Hinzugefügtes ImageOrPrintOptions.SVGFitToViewPort-Attribut**
Aspose.Cells for Java 8.4.1 hat das SVGFitToViewPort-Attribut für die Klasse ImageOrPrintOptions freigelegt, das verwendet werden kann, um das viewBox-Attribut für das SVG-Dateiformat beim Exportieren von Tabellenkalkulationen oder Diagrammen in das SVG-Format einzuschalten. Der Standardwert dieses Attributs ist false, daher wird das Basis-XML für die SVG-Datei ohne Festlegung des genannten Attributs das viewBox-Attribut nicht enthalten.

Der folgende Beispielcode zeigt die Verwendung des ImageOrPrintOptions.SVGFitToViewPort-Attributs.

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
## **Veraltete APIs**
### **Veraltete Workbook.validateFormula-Methode**
Verwenden Sie die Cell.Formula-Eigenschaft, um die Formel zu validieren.
