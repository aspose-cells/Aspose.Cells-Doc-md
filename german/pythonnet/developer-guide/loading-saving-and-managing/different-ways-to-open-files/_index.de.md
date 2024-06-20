---
title: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, Dateien zu öffnen, um beispielsweise Daten abzurufen oder eine Designtemplate zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Öffnen einer Datei über einen Pfad**

Entwickler können eine Microsoft Excel-Datei auf dem lokalen Computer öffnen, indem sie sie im **Workbook**-Klassenkonstruktor angeben. Geben Sie einfach den Pfad im Konstruktor als *String* an. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Öffnen einer Datei über einen Stream**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, die das *BufferStream*-Objekt enthält, das die Datei enthält.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Öffnen einer Datei nur mit Daten**

Um eine Datei nur mit Daten zu öffnen, verwenden Sie die Klassen **LoadOptions** und **LoadFilter**, um das entsprechende Attribut und die Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Es wird eine Ausnahme ausgelöst, wenn Sie versuchen, nicht native Excel-Dateien oder andere Dateiformate (z. B. PPT/PPTX, DOC/DOCX usw.) mit Aspose.Cells zu öffnen.

{{% /alert %}} {{% alert color="primary" %}}

Es besteht eine faire Chance, dass der Konstruktor der **Workbook**-Klasse eine *System.OutOfMemoryException* auslöst, wenn große Tabellenkalkulationen geladen werden. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden. Die Tabelle muss daher geladen werden, während die Speicherpräferenzen aktiviert sind.

{{% /alert %}}
