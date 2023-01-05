---
title: Speichern einer Excel-Datei
type: docs
weight: 20
url: /de/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Mit dem Control Aspose.Cells.GridDesktop können Anwender nicht nur neue Excel-Dateien erstellen, sondern auch bestehende verwalten. Aber in beiden Fällen wäre es notwendig, den Inhalt von Aspose.Cells.GridDesktop zu speichern. Dies ist also das Thema unserer Diskussion, um unsere Benutzer darüber zu informieren, wie sie ihre Grid-Inhalte als Excel-Datei speichern können.

{{% /alert %}} 
## **Einführung**
Um den Inhalt des Aspose.Cells.GridDesktop-Steuerelements als Excel-Datei zu speichern, bietet Aspose.Cells.GridDesktop folgende Methoden.

1. **Als Datei speichern**
1. **Als Stream speichern**
## **Datei speichern**
 Erstellen Sie eine Desktopanwendung, und fügen Sie dem Formular zwei Schaltflächen mit einem GridControl-Steuerelement hinzu. Legen Sie die Texteigenschaften von Schaltflächen fest als**Als Datei speichern** und**Als Stream speichern** beziehungsweise.
### **Als Datei speichern**
 Erstellen Sie das Click-Ereignis der**Als Datei speichern** Schaltfläche und fügen Sie den folgenden Code darin ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Ein wichtiger zu diskutierender Punkt ist, dass das Steuerelement Aspose.Cells.GridDesktop auch eine Methode namens SaveToExcel enthält, die auch zum Laden des Inhalts einer Excel-Datei in das Grid verwendet wird. Aber diese Methode ist jetzt veraltet. Daher wird allen Entwicklern empfohlen, die ExportExcelFile-Methode zu verwenden, die robuster und effizienter ist als die veraltete.

{{% /alert %}} 
### **Als Stream speichern**
 Manchmal kann es von Entwicklern verlangt werden, ihre Grid-Inhalte in einem Stream zu speichern (z. B. MemoryStream). Um diese Aufgabe zu erleichtern, unterstützt das Aspose.Cells.GridDesktop-Steuerelement auch das Speichern von Grid-Daten in einem Stream. Erstellen Sie das Click-Ereignis der**Als Stream speichern** Schaltfläche und fügen Sie den folgenden Code darin ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Microsoft Excel unterstützt Excel-Tabellen können maximal 65.536 Zeilen und 256 Spalten enthalten. Aspose.Cells.GridDesktop folgt ebenfalls denselben Standards. Im Aspose.Cells.GridDesktop-Steuerelement können Entwickler mehr Zeilen und Spalten als das Standardlimit erstellen, aber beim Speichern der Rasterdaten in einer Excel-Datei wird eine Ausnahme ausgelöst. Das bedeutet, dass nur Daten, die in den 65.536 Zeilen und 256 Spalten enthalten sind, mit Aspose.Cells.GridDesktop in einer Excel-Datei gespeichert werden können.

{{% /alert %}}
