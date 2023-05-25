---
title: Ermitteln Sie die Papierbreite und -höhe der Seiteneinrichtung des Arbeitsblatts
type: docs
weight: 50
url: /de/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: In diesem Artikel erfahren Sie, wie Sie die Seitenbreite und -höhe des Excel-Arbeitsblatts mithilfe des Codes C# programmgesteuert mit .NET API oder der Bibliothek abrufen können.
keywords: excel page setup paper width c#, excel page setup paper height c#
---
##  **Mögliche Nutzungsszenarien**

Manchmal müssen Sie die Breite und Höhe des Papierformats kennen, wie es bei der Seiteneinrichtung des Arbeitsblatts festgelegt wurde. Bitte nutzen Sie die[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)Und[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)Eigenschaften für diesen Zweck.

##  **Ermitteln Sie die Papierbreite und -höhe der Seiteneinrichtung des Arbeitsblatts**

 Der folgende Beispielcode erläutert die Verwendung von[**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) Und[**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) Eigenschaften. Zunächst wird das Papierformat auf geändert*A2*und ermittelt dann die Breite und Höhe des Papiers und ändert sie dann in*A3*, *A4*, *Letter*und ermittelt die Breite bzw. Höhe des Papiers.

###  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

###  **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
