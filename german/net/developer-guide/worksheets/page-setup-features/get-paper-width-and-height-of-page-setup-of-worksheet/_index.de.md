---
title: Papierbreite und höhe des Seitenlayouts des Arbeitsblatts abrufen
type: docs
weight: 50
url: /de/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: In diesem Artikel erfahren Sie, wie Sie mit dem C# Code programmgesteuert die Papierbreite und höhe des Excel Arbeitsblattseitenlayouts mit der .NET API oder Bibliothek abrufen.
keywords: Excel Seitenlayout Papierbreite c#, Excel Seitenlayout Papierhöhe c#
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie die Breite und Höhe der Papiergröße kennen, wie sie im Seitenlayout des Arbeitsblatts festgelegt wurde. Verwenden Sie hierfür die [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)- und [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)-Eigenschaften.

## **Papierbreite und -höhe des Seitenlayouts des Arbeitsblatts abrufen**

Der folgende Beispielscode erläutert die Verwendung der [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth)- und [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight)-Eigenschaften. Er ändert zuerst die Papiergröße in *A2* und findet dann die Breite und Höhe des Papiers, ändert sie dann auf *A3*, *A4*, *Brief* und findet jeweils die Breite und Höhe des Papiers.

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
