---
title: Feststellen, ob das Papierformat des Arbeitsblatts automatisch ist
type: docs
weight: 90
url: /de/python-net/determine-if-paper-size-of-worksheet-is-automatic/
description: Dieses Artikel erklärt, wie man den Papierzium eines Arbeitsblattes programmatisch mithilfe der Aspose.Cells für Python via .NET APIs auf Automatic überprüft.
keywords: Python Excel Bibliothek, Python automatisch das Papierformat des Arbeitsblatts bestimmen.
---

## **Mögliche Verwendungsszenarien**

Die meiste Zeit ist die Papiergröße des Arbeitsblatts automatisch. Wenn sie automatisch ist, wird sie oft als *Brief* eingestellt. Manchmal legt der Benutzer die Papiergröße des Arbeitsblatts entsprechend seinen Anforderungen fest. In diesem Fall ist die Papiergröße nicht automatisch. Sie können über die [**Worksheet.page_setup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_automatic_paper_size/)-Eigenschaft feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist oder nicht.

## **Feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist**

Der folgende Beispielscode lädt die folgenden beiden Excel-Dateien

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

und überprüft, ob die Papiergröße ihres ersten Arbeitsblatts automatisch ist oder nicht. In Microsoft Excel können Sie über das Dialogfeld Seitenlayout wie in diesem Screenshot gezeigt feststellen, ob die Papiergröße automatisch ist oder nicht.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.py" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit den angegebenen Beispieldateien ausgeführt wird.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
