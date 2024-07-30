---
title: Papierbreite und höhe des Seitenlayouts des Arbeitsblatts abrufen
type: docs
weight: 50
url: /de/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: In diesem Artikel erfahren Sie, wie Sie mit dem Python Code programmgesteuert die Papierbreite und Papierhöhe des Excel Arbeitsblatts mit der Aspose.Cells für Python via .NET API oder Bibliothek abrufen können.
keywords: Python Excel Bibliothek, Papierbreite des Excel Seiteneinrichtungs Papiers, Papierhöhe der Excel Seiteneinrichtung in Python.
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie die Breite und Höhe der Papiergröße kennen, wie sie im Seitenlayout des Arbeitsblatts festgelegt wurde. Verwenden Sie hierfür die [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width)- und [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)-Eigenschaften.

## **Papierbreite und -höhe des Seitenlayouts des Arbeitsblatts abrufen**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaften [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) und [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Zuerst wird die Papiergröße auf *A2* geändert und dann die Breite und Höhe des Papiers ermittelt, dann wird sie auf *A3*, *A4*, *Letter* geändert und die Breite und Höhe des Papiers jeweils gefunden.

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
