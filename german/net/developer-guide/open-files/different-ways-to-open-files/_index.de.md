---
title: Verschiedene Möglichkeiten zum Öffnen von Dateien
type: docs
weight: 10
url: /de/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Mit Aspose.Cells ist es beispielsweise einfach, Dateien zu öffnen, Daten abzurufen oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Öffnen einer Datei über einen Pfad**

 Entwickler können eine Microsoft-Excel-Datei mit ihrem Dateipfad auf dem lokalen Computer öffnen, indem sie ihn in der Datei angeben**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klassenkonstrukteur. Übergeben Sie den Pfad einfach im Konstruktor als a*Schnur*. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Öffnen einer Datei über einen Stream**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der die akzeptiert*Strom*Objekt, das die Datei enthält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Öffnen einer Datei nur mit Daten**

 Um eine Datei nur mit Daten zu öffnen, verwenden Sie die**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** und**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**Klassen, um die zugehörigen Attribute und Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Nur sichtbare Blätter laden**

 Beim Laden a**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Manchmal benötigen Sie möglicherweise nur Daten in sichtbaren Arbeitsblättern in einer Arbeitsmappe. Aspose.Cells ermöglicht es Ihnen, Daten in unsichtbaren Arbeitsblättern zu überspringen, während Sie eine Arbeitsmappe laden. Erstellen Sie dazu eine benutzerdefinierte Funktion, die die erbt**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**Klasse und übergeben Sie ihre Instanz an**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Hier ist die Umsetzung der*CustomnLoad*Klasse, auf die im obigen Snippet verwiesen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Eine Ausnahme wird ausgelöst, wenn Sie versuchen, nicht native Excel-Dateien oder andere Dateiformate (z. B. PPT/PPTX, DOC/DOCX usw.) bis Aspose.Cells zu öffnen.

{{% /alert %}} {{% alert color="primary" %}}

 Es gibt gute Chancen, dass die**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Konstruktor kann werfen*System.OutOfMemoryException* beim Laden großer Tabellenkalkulationen. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden, daher muss die Tabelle geladen werden, während die Speichereinstellungen aktiviert sind.

{{% /alert %}}
