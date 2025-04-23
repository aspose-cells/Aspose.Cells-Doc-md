---
title: Konvertierung zwischen Excel Formaten
type: docs
weight: 20
url: /de/net/convert-between-excel-formats/
---

## **Konvertierung von Excel nach PDF**

**PDF**-Dateien werden weit verbreitet zum Austausch von Dokumenten zwischen Organisationen, Regierungsbehörden und Einzelpersonen eingesetzt. Es ist ein standardisiertes Dokumentenformat, und Softwareentwickler werden häufig gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in **PDF**-Dokumente umzuwandeln.
**Aspose.Cells** unterstützt die Konvertierung von Excel-Dateien in PDF und behält dabei eine hohe visuelle Genauigkeit bei der Konvertierung bei.

Aspose.Cells for .NET unterstützt die Konvertierung von Arbeitsmappen in PDF unabhängig von anderer Software. Speichern Sie eine Excel-Datei im PDF-Format mithilfe der Save-Methode der Workbook-Klasse. Die Save-Methode bietet das enum-Mitglied SaveFormat.Pdf, das die nativen Excel-Dateien in das PDF-Format konvertiert.

Die direkte Konvertierung von Tabellenkalkulationen in PDF anstelle der Verwendung eines Drittanbieter-Tools oder einer externen API hat mehrere Vorteile:

1. Die Direktumwandlung erfordert keine temporären Dateien, da der gesamte Prozess im Speicher durchgeführt werden kann.
1. Es wird keine XML-Datei benötigt, sodass große Dateien einfach konvertiert werden können.
1. Die Konvertierungsgeschwindigkeit ist viel schneller.

**Um Dateien in PDF umzuwandeln:**

1. Instanziieren Sie ein Objekt der **Workbook**-Klasse, indem Sie ihren leeren Konstruktor aufrufen.
1. Sie können eine vorhandene Vorlagendatei **öffnen/laden** oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf neu erstellen.
1. Führen Sie Ihre gewünschten Arbeiten durch (Eingabe von Daten, Anwendung von Formatierungen, Festlegung von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) auf dem Arbeitsblatt unter Verwendung der APIs von Aspose.Cells durch.
1. Wenn der Code des Arbeitsblatts abgeschlossen ist, rufen Sie die **Save-Methode der Klasse Workbook** auf, um das Arbeitsblatt zu speichern. Das Dateiformat sollte PDF sein, wählen Sie also Pdf (einen vordefinierten Wert) aus der SaveFormat-Aufzählung, um das endgültige PDF-Dokument zu erstellen.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Excel in MHTML umwandeln**

**MHTML** kombiniert normales HTML mit externen Ressourcen (d. h. Inhalt, der normalerweise verknüpft ist, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.
Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Excel in XPS umwandeln**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern im Textformat konvertieren oder speichern. Für Textformate (z.B. TXT, TabDelim, CSV etc.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Beispielcode herunterladen**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
