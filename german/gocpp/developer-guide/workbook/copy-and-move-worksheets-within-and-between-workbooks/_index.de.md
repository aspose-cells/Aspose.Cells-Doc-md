---
title: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben mit Golang via C++
linktitle: Arbeitsblätter kopieren und verschieben
type: docs
weight: 80
url: /de/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Lernen Sie, wie Sie Arbeitsblätter innerhalb und zwischen Excel Arbeitsmappen mit Aspose.Cells for C++ kopieren und verschieben.
---

{{% alert color="primary" %}}

Manchmal benötigen Sie mehrere Arbeitsblätter mit gemeinsamer Formatierung und Dateneingabe. Zum Beispiel, wenn Sie vierteljährliche Budgets verwalten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die die gleichen Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Methode, dies zu tun: indem Sie ein Blatt erstellen und es dann mehrfach kopieren.

Aspose.Cells unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierungen, Tabellen, Matrizen, Diagramme, Bilder und anderen Objekten werden mit höchster Genauigkeit kopiert.

{{% /alert %}}

## **Arbeitsblätter kopieren und verschieben**

### **Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren**

Die ersten Schritte sind für alle Beispiele gleich:

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir in Microsoft Excel zwei neue Arbeitsmappen erstellt und Daten in die Arbeitsblätter eingetragen:
   - FirstWorkbook.xlsx (3 Arbeitsblätter)
   - SecondWorkbook.xlsx (1 Arbeitsblatt)

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Download Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. Installieren Sie es auf Ihrem Entwicklungscomputer

1. Ein Projekt erstellen:
   1. Erstellen Sie ein neues C++-Projekt in Ihrer bevorzugten IDE

1. Fügen Sie Verweise hinzu:
   1. Fügen Sie die Aspose.Cells for C++-Bibliothek zu Ihrem Projekt hinzu

1. Kopieren Sie das Tabellenblatt innerhalb einer Arbeitsmappe.
   Das erste Beispiel kopiert das erste Tabellenblatt (Kopie) innerhalb von FirstWorkbook.xlsx.

Beim Ausführen des Codes wird das Arbeitsblatt namens Kopie innerhalb von FirstWorkbook.xlsx mit dem Namen Last Sheet kopiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **Verschieben eines Arbeitsblatts innerhalb eines Arbeitsmappes**

Der untenstehende Code zeigt, wie man ein Arbeitsblatt von einer Position in einer Arbeitsmappe an eine andere verschiebt. Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben vom Index 1 auf den Index 2 in FirstWorkbook.xlsx.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes kopiert das Arbeitsblatt mit dem Namen Copy nach SecondWorkbook.xlsx mit dem Namen Sheet2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben von FirstWorkbook.xlsx nach SecondWorkbook.xlsx mit dem Namen Blatt3.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}
