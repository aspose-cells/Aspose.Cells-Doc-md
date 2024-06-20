---
title: Schützen Sie Zellen
type: docs
weight: 50
url: /de/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb,schützen,schreibgeschützt,bearbeitbar
description: Dieser Artikel zeigt, wie man Zellen in GridWeb schützt.
---

{{% alert color="primary" %}} 

In diesem Thema werden einige Techniken zum Schutz von Zellen beschrieben. Durch die Verwendung dieser Techniken können Entwickler Benutzer daran hindern, alle oder einen ausgewählten Bereich von Zellen in einem Arbeitsblatt zu bearbeiten.

{{% /alert %}} 
## **Zellen schützen**
Aspose.Cells.GridWeb bietet verschiedene Techniken zur Kontrolle des Schutzlevels von Zellen, wenn die Steuerung im [Bearbeitungsmodus](/cells/de/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (der Standardmodus) ist. Dies schützt Zellen davor, von Endbenutzern geändert zu werden.
### **Alle Zellen schreibgeschützt machen**
Um alle Zellen in einem Arbeitsblatt schreibgeschützt zu machen, rufen Sie die Methode SetAllCellsReadonly des Arbeitsblatts auf.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Alle Zellen bearbeitbar machen**
Um den Schutz von allen Zellen zu entfernen, rufen Sie die Methode SetAllCellsEditable des Arbeitsblatts auf. Diese Methode hat den gegenteiligen Effekt der Methode SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Ausgewählte Zellen schreibgeschützt machen**
Um nur einen Bereich von Zellen zu schützen:

1. Machen Sie zuerst alle Zellen bearbeitbar, indem Sie die Methode SetAllCellsEditable aufrufen.
1. Geben Sie den Bereich von Zellen an, der geschützt werden soll, indem Sie die Methode SetReadonlyRange des Arbeitsblatts aufrufen. Diese Methode nimmt die Anzahl von Zeilen und Spalten an, um den Bereich von Zellen festzulegen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Ausgewählte Zellen bearbeitbar machen**
Um einen Bereich von Zellen zu entsperren:

1. Machen Sie alle Zellen schreibgeschützt, indem Sie die Methode SetAllCellsReadonly des Arbeitsblatts aufrufen.
1. Geben Sie den Bereich von Zellen an, der bearbeitbar sein soll, indem Sie die Methode SetEditableRange des Arbeitsblatts aufrufen. Diese Methode nimmt die Anzahl von Zeilen und Spalten an, um den Bereich von Zellen festzulegen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
