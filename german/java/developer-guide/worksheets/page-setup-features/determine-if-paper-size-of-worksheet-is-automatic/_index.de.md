---
title: Stellen Sie fest, ob die Papiergröße des Arbeitsblatts automatisch ist
type: docs
weight: 20
url: /de/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Mögliche Nutzungsszenarien**

 Meistens ist die Papiergröße des Arbeitsblatts automatisch. Wenn es automatisch ist, wird es oft als eingestellt*Brief* . Manchmal legt der Benutzer die Papiergröße des Arbeitsblatts gemäß seinen Anforderungen fest. In diesem Fall wird das Papierformat nicht automatisch eingestellt. Sie können feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist oder nicht, indem Sie die verwenden[**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)Methode.

## **Stellen Sie fest, ob die Papiergröße des Arbeitsblatts automatisch ist**

Der unten angegebene Beispielcode lädt die folgenden zwei Excel-Dateien

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

und finden Sie heraus, ob die Papiergröße ihres ersten Arbeitsblatts automatisch ist oder nicht. In Microsoft Excel können Sie über das Fenster Seite einrichten prüfen, ob das Papierformat automatisch ist oder nicht, wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit den angegebenen Beispiel-Excel-Dateien ausgeführt wird.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
