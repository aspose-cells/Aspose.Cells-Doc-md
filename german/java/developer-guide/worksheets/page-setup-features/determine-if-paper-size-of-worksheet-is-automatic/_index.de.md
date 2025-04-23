---
title: Feststellen, ob das Papierformat des Arbeitsblatts automatisch ist
type: docs
weight: 20
url: /de/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Mögliche Verwendungsszenarien**

Die Papiergröße des Arbeitsblatts ist in der Regel automatisch. Wenn sie automatisch ist, wird sie oft als *Letter* festgelegt. Manchmal setzt der Benutzer die Papiergröße des Arbeitsblatts nach seinen Anforderungen. In diesem Fall ist die Papiergröße nicht automatisch. Sie können mit der Methode [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize) feststellen, ob die Arbeitsblattpapiergröße automatisch ist oder nicht.

## **Feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist**

Der folgende Beispielscode lädt die folgenden beiden Excel-Dateien

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

und überprüft, ob die Papiergröße ihres ersten Arbeitsblatts automatisch ist oder nicht. In Microsoft Excel können Sie über das Dialogfeld Seitenlayout wie in diesem Screenshot gezeigt feststellen, ob die Papiergröße automatisch ist oder nicht.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit den angegebenen Beispieldateien ausgeführt wird.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
