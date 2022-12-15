---
title: Konvertieren Sie zwischen Excel-Formaten
type: docs
weight: 20
url: /de/net/convert-between-excel-formats/
---
## **Konvertieren von Excel in PDF**

**Pdf** Dateien werden häufig für den Austausch von Dokumenten zwischen Organisationen, Regierungssektoren und Einzelpersonen verwendet. Es ist ein Standarddokumentformat und Softwareentwickler werden oft gebeten, einen Weg zu finden, Microsoft Excel-Dateien in zu konvertieren**Pdf** Unterlagen.
**Aspose.Cells** unterstützt die Konvertierung von Excel-Dateien in PDF und behält eine hohe visuelle Wiedergabetreue bei der Konvertierung bei.

Aspose.Cells for .NET unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie eine Excel-Datei mit der Save-Methode der Workbook-Klasse im PDF-Format. Die Save-Methode stellt das SaveFormat.Pdf-Enumerationselement bereit, das die nativen Excel-Dateien in das PDF-Format konvertiert.

**Konvertieren** direkt aus der Tabelle in PDF, anstatt ein Drittanbieter-Tool oder externe API zu verwenden, hat mehrere**Vorteile**:

1. Für die direkte Konvertierung sind keine temporären Dateien erforderlich, da der gesamte Vorgang im Speicher durchgeführt werden kann.
1. Es wird keine XML-Datei benötigt, sodass große Dateien einfach konvertiert werden können.
1. Die Konvertierungsgeschwindigkeit ist viel schneller.

**So konvertieren Sie Dateien in PDF:**

1.  Instanziieren Sie ein Objekt der**Arbeitsmappe** Klasse, indem Sie ihren leeren Konstruktor aufrufen.
1.  Du könntest**öffnen/laden** eine vorhandene Vorlagendatei oder überspringen Sie diesen Schritt, wenn Sie die Arbeitsmappe von Grund auf neu erstellen.
1. Führen Sie Ihre gewünschte Arbeit (Daten eingeben, Formatierung anwenden, Formeln festlegen, Bilder oder andere Zeichenobjekte einfügen usw.) in der Tabelle mithilfe von Aspose.Cells-APIs aus.
1.  Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie die auf**Die Save-Methode der Workbook-Klasse** um die Tabelle zu speichern. Das Dateiformat sollte PDF sein, also wählen Sie Pdf (ein vordefinierter Wert) aus der SaveFormat-Enumeration, um das endgültige PDF-Dokument zu generieren.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Konvertieren von Excel in MHTML**

**MHTML** kombiniert normales HTML mit externen Ressourcen (d. h. Inhalte, die üblicherweise eingebunden werden, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.
Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Konvertieren von Excel in XPS**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
