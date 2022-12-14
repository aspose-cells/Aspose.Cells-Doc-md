---
title: Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei
type: docs
weight: 130
url: /de/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for .NET kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren, und Sie müssen Aspose.PDF for .NET nicht für die Konvertierung verwenden. Für die Konvertierung muss die Software keine temporären Dateien erstellen oder verwenden, da der gesamte Vorgang im Speicher durchgeführt werden kann.

{{% /alert %}} 
## **Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei**
Wenn Sie jedes Arbeitsblatt in Ihrer Excel-Vorlagendatei speichern müssen, um verschiedene PDF-Dateien zu generieren, können Sie dies ganz einfach erreichen. Sie können versuchen, Blätter in der Datei auszublenden und jeweils ein Blatt sichtbar zu machen, um es als PDF zu rendern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) unmittelbar vor dem Rendern der Tabelle in das PDF-Format. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte im PDF wiedergegeben werden.

{{% /alert %}}
