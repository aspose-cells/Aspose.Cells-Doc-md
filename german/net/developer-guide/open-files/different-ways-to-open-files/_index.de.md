---
title: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/net/different-ways-to-open-files/
description: Dieser Artikel erklärt, wie Sie eine Excel Datei mithilfe der Aspose.Cells for .NET API öffnen.
keywords: C# Öffnen Sie eine Excel Datei ohne Excel. Wie öffne ich eine Excel Datei?
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, Dateien zu öffnen, um beispielsweise Daten abzurufen oder eine Designtemplate zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Wie man eine Excel-Datei über einen Pfad öffnet**

Entwickler können eine Microsoft Excel-Datei auf dem lokalen Computer öffnen, indem sie sie im [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klassenkonstruktor angeben. Geben Sie einfach den Pfad im Konstruktor als *string* an. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Wie man eine Excel-Datei über einen Stream öffnet**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, die das *Stream*-Objekt enthält, das die Datei enthält.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Wie man eine Datei nur mit Daten öffnet**

Um eine Datei nur mit den Daten zu öffnen, verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)- und [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)-Klassen, um die relevanten Attribute und Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Wie man nur sichtbare Blätter lädt**

Beim Laden einer [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) möchten Sie möglicherweise nur Daten in sichtbaren Arbeitsblättern in einer Arbeitsmappe verwenden. Aspose.Cells ermöglicht es Ihnen, Daten in unsichtbaren Arbeitsblättern zu überspringen, während Sie eine Arbeitsmappe laden. Erstellen Sie dazu eine benutzerdefinierte Funktion, die die Klasse [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) erbt, und übergeben Sie eine Instanz davon an die [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)-Eigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Hier ist die Implementierung der Klasse *CustomnLoad*, auf die im obigen Auszug verwiesen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Es wird eine Ausnahme ausgelöst, wenn Sie versuchen, nicht native Excel-Dateien oder andere Dateiformate (z. B. PPT/PPTX, DOC/DOCX usw.) mit Aspose.Cells zu öffnen.

{{% /alert %}} {{% alert color="primary" %}}

Es besteht eine faire Chance, dass der Konstruktor [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) eine *System.OutOfMemoryException* auslösen kann, während große Tabellenkalkulationen geladen werden. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabellenkalkulation vollständig in den Speicher zu laden, und daher muss die Tabellenkalkulation geladen werden, während die Arbeitsspeichereinstellungen aktiviert sind.

{{% /alert %}}
