---
title: Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei
type: docs
weight: 50
url: /de/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung von Tabellenkalkulationsdateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for Java kann unabhängig arbeiten, um eine Tabelle in ein PDF-Dokument zu konvertieren, und Sie müssen Aspose.PDF for Java nicht mehr für die Konvertierung verwenden. Für die Konvertierung müssen keine temporären Dateien erstellt / verwendet werden, da der gesamte Vorgang im Speicher durchgeführt werden kann.

{{% /alert %}}

Wenn Sie jedes Arbeitsblatt in Ihrer Excel-Vorlagendatei speichern müssen, um verschiedene PDF-Dateien zu generieren. Dies kann leicht erreicht werden. Sie können versuchen, Blätter in der Datei auszublenden und jeweils ein Blatt sichtbar zu machen, basierend darauf, wie Sie PDFs rendern würden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten die auf[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())-Methode direkt vor dem Rendern der Tabelle in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die richtigen Werte in PDF gerendert werden.

{{% /alert %}}
