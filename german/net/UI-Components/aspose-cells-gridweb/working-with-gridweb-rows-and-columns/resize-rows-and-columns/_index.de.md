---
title: Ändern Sie die Größe von Zeilen und Spalten
type: docs
weight: 30
url: /de/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

Manchmal sind Zellenwerte breiter als die Zelle, in der sie sich befinden, oder befinden sich in mehreren Zeilen. Solche Werte sind für Benutzer nicht vollständig sichtbar, es sei denn, sie ändern die Höhe und Breite von Zeilen und Spalten. Aspose.Cells. GridWeb unterstützt die Einstellung von Zeilenhöhen und Spaltenbreiten vollständig. In diesem Thema werden diese Features ausführlich anhand von Beispielen erläutert.

{{% /alert %}} 
## **Arbeiten mit Zeilenhöhen und Spaltenbreiten**
### **Zeilenhöhe einstellen**
So legen Sie die Höhe einer Zeile fest:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf die Sammlung Cells des Arbeitsblatts zu.
1. Legen Sie die Höhe aller Zellen in einer beliebigen angegebenen Zeile fest.

{{% alert color="primary" %}} 

Die SetRowHeight- und SetColumnWidth-Methode der Cells-Sammlung verfügt auch über Varianten zum Festlegen von Zeilenhöhen- und Spaltenbreitenmessungen in Zoll und Pixeln.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Spaltenbreite einstellen**
So legen Sie die Breite einer Spalte fest:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf die Sammlung Cells des Arbeitsblatts zu.
1. Legen Sie die Breite aller Zellen in einer beliebigen angegebenen Spalte fest.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
