---
title: Papierbreite und höhe des Seitenlayouts des Arbeitsblatts abrufen
type: docs
weight: 50
url: /de/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Sie erfahren in diesem Artikel, wie man die Papierbreite und höhe der Excel Arbeitsblattseite programmgesteuert mit Python Code unter Verwendung von Aspose.Cells für Python via .NET API oder Bibliothek erhält.
keywords: Python Excel Bibliothek, Python Excel Seiten Setup Papierbreite, Excel Seiten Setup Papierhöhe in Python.
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie die Breite und Höhe der Papiergröße kennen, wie sie im Seitenlayout des Arbeitsblatts festgelegt wurde. Verwenden Sie hierfür die [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width)- und [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height)-Eigenschaften.

## **Papierbreite und -höhe des Seitenlayouts des Arbeitsblatts abrufen**

Der folgende Beispielcode erklärt die Verwendung der Eigenschaften [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) und [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Es ändert zuerst die Papiergröße auf *A2* und findet dann die Breite und Höhe des Papiers, danach ändert es auf *A3*, *A4*, *Brief* und findet die Breite und Höhe des Papiers jeweils.

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
{{< app/cells/assistant language="python-net" >}}
