---
title: Sichere PDF-Dokumente
type: docs
weight: 120
url: /de/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Beispielsweise müssen sie Dokumente mit Benutzer- und Eigentümerkennwörtern sichern, damit nicht jeder sie öffnen kann, oder sie möchten einschränken, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erläutert, wie Sie PDF-Sicherheitsoptionen übergeben, wenn Sie Tabellenkalkulationen als PDF speichern.

{{% /alert %}}

 Aspose.Cells bietet die[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) Namespace für die Arbeit mit Sicherheit. Der folgende Beispielcode beschreibt, wie Sie PDFs mit Aspose.Cells sichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)kurz vor dem Rendern in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die korrekten Werte im PDF wiedergegeben werden.

{{% /alert %}}
