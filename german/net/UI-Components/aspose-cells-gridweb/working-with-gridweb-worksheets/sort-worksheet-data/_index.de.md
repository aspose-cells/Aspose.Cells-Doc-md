---
title: Arbeitsblattdaten sortieren
type: docs
weight: 80
url: /de/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

Das Sortieren ist ein sehr wertvolles Feature, wenn es um die Datenverarbeitung geht. Unsortierte Daten sind für Benutzer bei der Suche nach bestimmten Informationen mühsam. Aspose.Cells.GridWeb unterstützt leistungsstarke Sortierfunktionen. In diesem Thema wird das Sortieren von Daten mit Aspose.Cells.GridWeb API erläutert.

{{% /alert %}} 
## **Daten sortieren**
Aspose.Cells.GridWeb ermöglicht es Entwicklern, Daten horizontal und vertikal zu sortieren, sodass Entwickler Daten von oben nach unten oder von links nach rechts sortieren können.
### **Von oben nach unten**
So sortieren Sie Daten von oben nach unten:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Achten Sie darauf, die Ausrichtung von oben nach unten auszuwählen.

Das folgende Beispiel sortiert Daten in vier Spalten eines Arbeitsblatts in absteigender Reihenfolge. Nur zwanzig Zeilen der vier Spalten sind von oben nach unten sortiert.

Vor dem Anwenden des Codes enthält das Arbeitsblatt ungeordnete Daten.

![todo: Bild_alt_Text](sort-worksheet-data_1.png)

Nach Ausführung des Codes werden die Daten aufsteigend sortiert.

![todo: Bild_alt_Text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Von links nach rechts**
So sortieren Sie Daten von links nach rechts:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Achten Sie darauf, von links nach rechts auszuwählen.

Das folgende Beispiel sortiert Daten in vier Zeilen in aufsteigender Reihenfolge. Nur vier Zeilen mit sieben Spalten werden von links nach rechts sortiert.

Vor dem Anwenden des Codes enthält das Arbeitsblatt ungeordnete Daten.

![todo: Bild_alt_Text](sort-worksheet-data_3.png)

Nach Ausführung des Codes werden die Daten in aufsteigender Reihenfolge sortiert.

![todo: Bild_alt_Text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Die obigen Beispiele demonstrieren das Sortieren von Daten anhand einer Spalte (von oben nach unten) oder einer Zeile (von links nach rechts). Aspose.Cells. GridWeb kann Daten auch nach mehr als einer Spalte oder Zeile sortieren. Übergeben Sie dazu ein Array von Spalten- oder Zeilenindizes an die Sort-Methode. Hybrid-Datentyp-Sortierung wird ebenfalls unterstützt.

{{% /alert %}}
