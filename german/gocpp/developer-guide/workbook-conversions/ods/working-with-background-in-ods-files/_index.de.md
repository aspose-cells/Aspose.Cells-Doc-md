---
title: Arbeiten mit Hintergründen in ODS Dateien mit Golang über C++
linktitle: Arbeiten mit Hintergrund in ODS Dateien
type: docs
weight: 150
url: /de/go-cpp/working-with-background-in-ods-files/
description: Lernen Sie, wie man farbige und grafische Hintergründe in ODS Dateien mit Aspose.Cells in Golang über C++ verwaltet.
---

## **Hintergrund in ODS-Dateien**

Hintergrund kann zu Blättern in ODS-Dateien hinzugefügt werden. Der Hintergrund kann entweder ein farbiger Hintergrund oder ein grafischer Hintergrund sein. Der Hintergrund ist nicht sichtbar, wenn die Datei geöffnet ist, aber wenn die Datei als PDF gedruckt wird, ist der Hintergrund im generierten PDF sichtbar. Der Hintergrund ist auch in der Druckvorschau sichtbar.

Aspose.Cells bietet die Möglichkeit, die Hintergrundinformationen zu lesen und den Hintergrund in ODS-Dateien hinzuzufügen.

## **Hintergrundinformationen aus ODS-Datei lesen**

Aspose.Cells stellt die [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)-Klasse bereit, um Hintergründe in ODS-Dateien zu verwalten. Das folgende Codebeispiel zeigt die Verwendung der [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)-Klasse durch Laden der [Quelle ODS](90112030.ods) und Lesen der Hintergrundinformationen. Bitte sehen Sie sich die vom Code generierte Konsolenausgabe zur Referenz an.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Konsolenausgabe**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Farbigen Hintergrund zu ODS-Datei hinzufügen**

Aspose.Cells stellt die [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)-Klasse bereit, um Hintergründe in ODS-Dateien zu verwalten. Das folgende Codebeispiel zeigt die Verwendung der Eigenschaft [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/), um einem ODS-Datei einen Farb-Hintergrund hinzuzufügen. Bitte sehen Sie sich die [Ausgabedatei ODS](90112031.ods) an, die vom Code generiert wurde, zur Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **Grafischen Hintergrund zu ODS-Datei hinzufügen**

Aspose.Cells stellt die [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/)-Klasse zur Verwaltung des Hintergrunds in ODS-Dateien bereit. Das folgende Codebeispiel demonstriert die Verwendung der [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/)-Eigenschaft, um einen grafischen Hintergrund zur ODS-Datei hinzuzufügen. Bitte sehen Sie sich die [Ausgabe-ODS](90112030.ods)-Datei an, die vom Code generiert wurde, zur Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
