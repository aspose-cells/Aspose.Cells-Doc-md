---
title: Verschiedene Möglichkeiten zum Öffnen von Dateien
type: docs
weight: 10
url: /de/net/different-ways-to-open-files/
description: In diesem Artikel wird erläutert, wie Sie eine Excel-Datei mit Aspose.Cells for .NET API öffnen.
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, beispielsweise Dateien zu öffnen, Daten abzurufen oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

##  **So öffnen Sie eine Excel-Datei über einen Pfad**

 Entwickler können eine Excel-Datei Microsoft über ihren Dateipfad auf dem lokalen Computer öffnen, indem sie ihn im angeben**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klassenkonstruktor. Übergeben Sie den Pfad einfach im Konstruktor als *String*. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **So öffnen Sie eine Excel-Datei über einen Stream**

 Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der die übernimmt*Strom*Objekt, das die Datei enthält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **So öffnen Sie eine Datei nur mit Daten**

 Um eine Datei nur mit Daten zu öffnen, verwenden Sie die**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** Und**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**Klassen, um die zugehörigen Attribute und Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **So laden Sie nur sichtbare Blätter**

 Beim Laden eines**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Manchmal benötigen Sie möglicherweise nur Daten in sichtbaren Arbeitsblättern einer Arbeitsmappe. Mit Aspose.Cells können Sie beim Laden einer Arbeitsmappe Daten in unsichtbaren Arbeitsblättern überspringen. Erstellen Sie dazu eine benutzerdefinierte Funktion, die die erbt**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**Klasse und übergeben Sie ihre Instanz an**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Hier ist die Umsetzung des*CustomnLoad*Klasse, auf die im obigen Snippet verwiesen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Eine Ausnahme wird ausgelöst, wenn Sie versuchen, nicht-native Excel-Dateien oder andere Dateiformate (z. B. PPT/PPTX, DOC/DOCX usw.) bis Aspose.Cells zu öffnen.

{{% /alert %}} {{% alert color="primary" %}}

 Es bestehen gute Chancen, dass die**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Der Konstruktor kann werfen*System.OutOfMemoryException* beim Laden großer Tabellenkalkulationen. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden. Daher muss die Tabelle geladen werden, während die Speichereinstellungen aktiviert sind.

{{% /alert %}}
