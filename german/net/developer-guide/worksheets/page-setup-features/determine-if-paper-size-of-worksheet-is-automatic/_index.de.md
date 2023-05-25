---
title: Stellen Sie fest, ob die Papiergröße des Arbeitsblatts auf „Automatisch“ eingestellt ist
type: docs
weight: 90
url: /de/net/determine-if-paper-size-of-worksheet-is-automatic/
description: In diesem Artikel wird erläutert, wie Sie den Beispielcode der Bibliothek C#, API oder .NET verwenden, um programmgesteuert zu bestimmen, ob die Papiergröße des Arbeitsblatts automatisch ist.
keywords: determine if paper size of worksheet automatic c#
---
##  **Mögliche Nutzungsszenarien**

 Meistens wird die Papiergröße des Arbeitsblatts automatisch eingestellt. Wenn es automatisch ist, wird es oft als *Buchstabe* eingestellt. Manchmal legt der Benutzer das Papierformat des Arbeitsblatts entsprechend seinen Anforderungen fest. In diesem Fall erfolgt die Papiergröße nicht automatisch. Mithilfe von können Sie herausfinden, ob das Arbeitsblattpapierformat automatisch eingestellt wird oder nicht[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)Eigentum.

##  **Stellen Sie fest, ob die Papiergröße des Arbeitsblatts auf „Automatisch“ eingestellt ist**

Der unten angegebene Beispielcode lädt die folgenden zwei Excel-Dateien

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

und finden Sie heraus, ob das Papierformat ihres ersten Arbeitsblatts automatisch ist oder nicht. In Microsoft Excel können Sie über das Fenster „Seite einrichten“ überprüfen, ob das Papierformat automatisch eingestellt wird oder nicht, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

##  **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit den angegebenen Beispiel-Excel-Dateien ausgeführt wird.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
