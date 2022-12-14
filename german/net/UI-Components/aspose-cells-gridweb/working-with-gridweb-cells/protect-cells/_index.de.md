---
title: Cells schützen
type: docs
weight: 50
url: /de/net/protect-cells/
---
{{% alert color="primary" %}} 

In diesem Thema werden einige Techniken zum Schutz von Zellen beschrieben. Mithilfe dieser Techniken können Entwickler verhindern, dass Benutzer alle oder einen ausgewählten Bereich von Zellen in einem Arbeitsblatt bearbeiten.

{{% /alert %}} 
## **Schützen Cells**
 Aspose.Cells. GridWeb bietet einige unterschiedliche Techniken zum Steuern der Schutzebene für Zellen, wenn die Kontrolle aktiviert ist[Bearbeitungsmodus](/cells/de/net/enable-different-gridweb-modes/#edit-mode) (der Standardmodus). Dies schützt Zellen davor, von Endbenutzern geändert zu werden.
### **Alle Cells schreibgeschützt machen**
Um alle Zellen in einem Arbeitsblatt schreibgeschützt festzulegen, rufen Sie die SetAllCellsReadonly-Methode des Arbeitsblatts auf.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Alle Cells bearbeitbar machen**
Um den Schutz von allen Zellen aufzuheben, rufen Sie die SetAllCellsEditable-Methode des Arbeitsblatts auf. Diese Methode hat den gegenteiligen Effekt zur SetAllCellsReadonly-Methode.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Ausgewählte Cells schreibgeschützt machen**
So schützen Sie nur eine Reihe von Zellen:

1. Machen Sie zunächst alle Zellen bearbeitbar, indem Sie die SetAllCellsEditable-Methode aufrufen.
1. Geben Sie den zu schützenden Zellbereich an, indem Sie die SetReadonlyRange-Methode des Arbeitsblatts aufrufen. Diese Methode verwendet die Anzahl der Zeilen und Spalten, um den Zellbereich anzugeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Ausgewählte Cells bearbeitbar machen**
So heben Sie den Schutz einer Reihe von Zellen auf:

1. Machen Sie alle Zellen schreibgeschützt, indem Sie die SetAllCellsReadonly-Methode aufrufen.
1. Geben Sie den bearbeitbaren Zellbereich an, indem Sie die SetEditableRange-Methode des Arbeitsblatts aufrufen. Diese Methode verwendet die Anzahl der Zeilen und Spalten, um den Zellbereich anzugeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
