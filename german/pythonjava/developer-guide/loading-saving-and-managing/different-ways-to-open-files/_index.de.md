---
title: Verschiedene Möglichkeiten zum Öffnen von Dateien
type: docs
weight: 10
url: /de/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Mit Aspose.Cells ist es beispielsweise einfach, Dateien zu öffnen, Daten abzurufen oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Öffnen einer Datei über einen Pfad**

 Entwickler können eine Microsoft-Excel-Datei mit ihrem Dateipfad auf dem lokalen Computer öffnen, indem sie ihn in der Datei angeben**[Arbeitsmappe](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**Klassenkonstrukteur. Übergeben Sie den Pfad einfach im Konstruktor als a*Schnur*. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Öffnen einer Datei über einen Stream**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der die akzeptiert*BufferStream*Objekt, das die Datei enthält.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Öffnen einer Datei nur mit Daten**

 Um eine Datei nur mit Daten zu öffnen, verwenden Sie die**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** und**[LoadFilter](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**Klassen, um die zugehörigen Attribute und Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Eine Ausnahme wird ausgelöst, wenn Sie versuchen, nicht native Excel-Dateien oder andere Dateiformate (z. B. PPT/PPTX, DOC/DOCX usw.) bis Aspose.Cells zu öffnen.

{{% /alert %}} {{% alert color="primary" %}}

 Es gibt gute Chancen, dass die**[Arbeitsmappe](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** Konstruktor kann werfen*System.OutOfMemoryException* beim Laden großer Tabellenkalkulationen. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden, daher muss die Tabelle geladen werden, während die Speichereinstellungen aktiviert sind.

{{% /alert %}}
