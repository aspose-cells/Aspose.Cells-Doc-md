---
title: Job oder Dokumentnamen beim Drucken mit Aspose.Cells angeben
type: docs
weight: 270
url: /de/python-net/specify-job-or-document-name-while-printing-with-aspose-cells/
---

{{% alert color="primary" %}}

Sie können den Jobnamen oder das Dokumentenname beim Drucken Ihres Workbooks oder Worksheets mithilfe der Objekte WorkbookRender oder SheetRender angeben. Aspose.Cells für Python via .NET bietet die Methoden WorkbookRender.ToPrinter(printerName, jobName) und SheetRender.ToPrinter(printerName, jobName), um den Jobnamen beim Drucken festzulegen.

{{% /alert %}}

## **Angabe von Job- oder Dokumentnamen beim Drucken mit Aspose.Cells für Python via .NET**

Der Beispielcode lädt die Ausgangs-Excel-Datei und sendet sie dann an den Drucker, wobei der Job- oder Dokumentname mithilfe der Methoden WorkbookRender.ToPrinter(printerName, jobName) und SheetRender.ToPrinter(printerName, jobName) angegeben wird.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SpecifyJobNameWhilePrinting.py" >}}
