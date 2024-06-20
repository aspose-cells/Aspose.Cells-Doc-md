---
title: Speichern einer Excel Datei
type: docs
weight: 20
url: /de/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop, speichern, Datei
description: Dieser Artikel zeigt, wie eine Datei in GridDesktop gespeichert wird.
---

{{% alert color="primary" %}} 

Mithilfe des Aspose.Cells.GridDesktop-Steuerelements können Benutzer nicht nur neue Excel-Dateien erstellen, sondern auch vorhandene verwalten. In beiden Fällen ist es jedoch erforderlich, den Inhalt des Aspose.Cells.GridDesktop zu speichern. Dies ist nun das Thema unserer Diskussion, um unseren Benutzern mitzuteilen, wie sie ihren Grid-Inhalt als Excel-Datei speichern können.

{{% /alert %}} 
## **Einführung**
Um den Inhalt des Aspose.Cells.GridDesktop-Steuerelements als Excel-Datei zu speichern, bietet Aspose.Cells.GridDesktop folgende Methoden.

1. **Als Datei speichern**
1. **Als Stream speichern**
## **Datei speichern**
Erstellen Sie eine Desktopanwendung und fügen Sie der Form zwei Schaltflächen mit einem GridControl-Steuerelement hinzu. Legen Sie die Texteigenschaften der Schaltflächen als **Als Datei speichern** und **Als Stream speichern** fest.
### **Als Datei speichern**
Erstellen Sie das Click-Ereignis der Schaltfläche **Als Datei speichern** und fügen Sie den folgenden Code ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Ein wichtiger Punkt, der zu diskutieren ist, ist, dass Aspose.Cells.GridDesktop-Steuerelement auch eine Methode namens SaveToExcel enthält, die ebenfalls zum Laden des Inhalts einer Excel-Datei in das Grid verwendet wird. Diese Methode ist nun jedoch veraltet. Daher wird allen Entwicklern empfohlen, die Methode ExportExcelFile zu verwenden, die robuster und effizienter als die veraltete ist.

{{% /alert %}} 
### **Als Stream speichern**
Manchmal müssen Entwickler ihren Grid-Inhalt in einen Stream (z.B. MemoryStream) speichern. Um diese Aufgabe zu erleichtern, unterstützt das Aspose.Cells.GridDesktop-Steuerelement auch das Speichern von Grid-Daten in einen Stream. Erstellen Sie das Click-Ereignis der Schaltfläche **Als Stream speichern** und fügen Sie den folgenden Code ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Microsoft Excel unterstützt, dass Excel-Tabellen bis zu 65.536 Zeilen und 256 Spalten enthalten können. Aspose.Cells.GridDesktop folgt auch denselben Standards. Mit dem Aspose.Cells.GridDesktop-Steuerelement können Entwickler jedoch mehr Zeilen und Spalten als das Standardlimit erstellen. Beim Speichern der Rasterdaten in eine Excel-Datei wird jedoch eine Ausnahme ausgelöst. Das bedeutet, dass nur Daten, die in den 65.536 Zeilen und 256 Spalten enthalten sind, mithilfe des Aspose.Cells.GridDesktop in eine Excel-Datei gespeichert werden können.

{{% /alert %}}
