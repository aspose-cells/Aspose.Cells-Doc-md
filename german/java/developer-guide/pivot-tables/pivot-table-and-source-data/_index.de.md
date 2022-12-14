---
title: Pivot-Tabelle und Quelldaten
type: docs
weight: 110
url: /de/java/pivot-table-and-source-data/
---
## **Quelldaten der Pivot-Tabelle**
Es gibt Zeiten, in denen Sie Microsoft Excel-Berichte mit Pivot-Tabellen erstellen möchten, die Daten aus verschiedenen Datenquellen (z. B. einer Datenbank) verwenden, die zur Entwurfszeit nicht bekannt sind. Dieser Artikel bietet einen Ansatz zum dynamischen Ändern der Datenquelle einer Pivot-Tabelle.
## **Ändern der Quelldaten einer Pivot-Tabelle**
1. Erstellen einer neuen Designervorlage.
1. Erstellen Sie eine neue Designer-Vorlagendatei wie im Screenshot unten.
 1. Definieren Sie dann einen benannten Bereich,**Datenquelle** , was sich auf diesen Zellbereich bezieht.

      **Erstellen einer Designervorlage und Definieren eines benannten Bereichs, DataSource** 

![todo: Bild_alt_Text](pivot-table-and-source-data_1.png)

1. Erstellen einer Pivot-Tabelle basierend auf diesem benannten Bereich.
 1. Wählen Sie in Microsoft Excel**Daten** , dann**PivotTable** und**PivotChart-Bericht**.
 1. Erstellen Sie eine Pivot-Tabelle basierend auf dem benannten Bereich, der im ersten Schritt erstellt wurde.

      **Erstellen einer Pivot-Tabelle basierend auf dem benannten Bereich DataSource** 

![todo: Bild_alt_Text](pivot-table-and-source-data_2.png)

1.  Ziehen Sie das entsprechende Feld in die Zeile und Spalte der Pivot-Tabelle und erstellen Sie dann die resultierende Pivot-Tabelle wie im folgenden Screenshot.

   **Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld** 

![todo: Bild_alt_Text](pivot-table-and-source-data_3.png)

1.  Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie sie aus**Tabellenoptionen**.
 1. Prüfen**Beim Öffnen aktualisieren** in**Datenoptionen** die Einstellungen.

      **Festlegen der Pivot-Tabellenoptionen** 

![todo: Bild_alt_Text](pivot-table-and-source-data_4.png)



Jetzt können Sie diese Datei als Ihre Designer-Vorlagendatei speichern.

1. Neue Daten füllen und Quelldaten einer Pivot-Tabelle ändern.
1. Sobald die Designer-Vorlage erstellt ist, verwenden Sie den folgenden Code, um die Quelldaten der Pivot-Tabelle zu ändern.

Durch Ausführen des folgenden Beispielcodes werden die Quelldaten der Pivot-Tabelle geändert und die Pivot-Tabelle sieht wie folgt aus.

**Dynamisch geänderte Pivot-Tabelle** 

![todo: Bild_alt_Text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
