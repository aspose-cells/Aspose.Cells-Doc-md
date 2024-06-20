---
title: Konvertierung von XLS Datei mit Bildern oder Diagrammen in PDF
type: docs
weight: 50
url: /de/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien, die Bilder und Diagramme enthalten, in PDF-Dokumente. Aspose.Cells for .NET kann unabhängig voneinander arbeiten, um eine Tabelle in PDF umzuwandeln: Aspose.PDF für .NET ist für die Konvertierung nicht erforderlich. Der Vorgang kann im Speicher durchgeführt werden, da er nicht von temporären oder zwischengeschalteten XML-Dateien abhängt. Dies bedeutet, dass große Excel-Dateien, die beispielsweise Bilder, Diagramme und andere Zeichenobjekte enthalten, schnell und effizient konvertiert werden können.

{{% /alert %}} 
## **Beispielcode**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor der Konvertierung in PDF aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
