---
title: Daten auf dem Arbeitsblatt sortieren
type: docs
weight: 80
url: /de/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb,sortieren
description: Dieser Artikel stellt vor, wie Daten in GridWeb sortiert werden.
---

{{% alert color="primary" %}} 

Das Sortieren ist ein sehr wertvolles Feature, wenn es um die Datenverarbeitung geht. Unsortierte Daten sind für Benutzer eine Qual bei der Suche nach bestimmten Informationen. Aspose.Cells.GridWeb unterstützt leistungsstarke Sortierfunktionen. Dieses Thema behandelt das Sortieren von Daten mithilfe der Aspose.Cells.GridWeb-API.

{{% /alert %}} 
## **Daten sortieren**
Aspose.Cells.GridWeb ermöglicht Entwicklern, Daten horizontal und vertikal zu sortieren, sodass Daten von oben nach unten oder von links nach rechts sortiert werden können.
### **Von oben nach unten**
Um Daten von oben nach unten zu sortieren:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Wählen Sie dabei die Orientierung von oben nach unten aus.

Das folgende Beispiel sortiert Daten in vier Spalten eines Arbeitsblatts in absteigender Reihenfolge. Die vier Spalten enthalten nur zwanzig Zeilen sortierter Daten in der Ausrichtung von oben nach unten.

Vor der Anwendung des Codes enthält das Arbeitsblatt ungeordnete Daten.

![todo:image_alt_text](sort-worksheet-data_1.png)

Nach Ausführung des Codes sind die Daten in aufsteigender Reihenfolge sortiert.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Von links nach rechts**
Um Daten von links nach rechts zu sortieren:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Stellen Sie sicher, dass Sie von links nach rechts auswählen.

Das folgende Beispiel sortiert Daten in vier Zeilen in aufsteigender Reihenfolge. Es werden nur vier Zeilen von sieben Spalten von links nach rechts sortiert.

Vor der Anwendung des Codes enthält das Arbeitsblatt ungeordnete Daten.

![todo:image_alt_text](sort-worksheet-data_3.png)

Nach Ausführen des Codes werden die Daten in aufsteigender Reihenfolge sortiert.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Die obigen Beispiele zeigen das Sortieren von Daten basierend auf einer Spalte (von oben nach unten) oder einer Zeile (von links nach rechts). Aspose.Cells.GridWeb kann auch Daten gemäß mehr als einer Spalte oder Zeile sortieren. Geben Sie dazu ein Array von Spalten- oder Zeilenindizes an die Sort-Methode weiter. Die Sortierung von Hybriddatentypen wird ebenfalls unterstützt.

{{% /alert %}}
