---
title: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, Dateien zu öffnen, um beispielsweise Daten abzurufen oder eine Designtemplate zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Öffnen einer Datei über einen Pfad**

Entwickler können eine Microsoft Excel-Datei auf dem lokalen Computer öffnen, indem sie sie im [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)-Klassenkonstruktor angeben. Geben Sie einfach den Pfad im Konstruktor als *string* an. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Öffnen einer Datei über einen Stream**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, die das *BufferStream*-Objekt enthält, das die Datei enthält.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Öffnen einer Datei nur mit Daten**

Um eine Datei nur mit den Daten zu öffnen, verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)- und [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)-Klassen, um die relevanten Attribute und Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Es wird eine Ausnahme ausgelöst, wenn Sie versuchen, nicht native Excel-Dateien oder andere Dateiformate (z. B. PPT/PPTX, DOC/DOCX usw.) mit Aspose.Cells zu öffnen.

{{% /alert %}} {{% alert color="primary" %}}

Es besteht eine faire Chance, dass der Konstruktor [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) eine *System.OutOfMemoryException* auslösen kann, während große Tabellenkalkulationen geladen werden. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabellenkalkulation vollständig in den Speicher zu laden, und daher muss die Tabellenkalkulation geladen werden, während die Arbeitsspeichereinstellungen aktiviert sind.

{{% /alert %}}
