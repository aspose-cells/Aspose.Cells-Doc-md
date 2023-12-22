---
title: Pivot-Tabelle und Quelldaten
type: docs
weight: 30
url: /de/python-net/pivot-table-and-source-data/
description: In diesem Artikel wird gezeigt, wie Sie die Quelldaten der Pivot-Tabelle mit Aspose.Cells for Python via .NET ändern.
keywords: Change Pivot Table's Source Data
---
##  **Quelldaten der Pivot-Tabelle**

Es gibt Zeiten, in denen Sie Microsoft Excel-Berichte mit Pivot-Tabellen erstellen möchten, die Daten aus verschiedenen Datenquellen (z. B. einer Datenbank) übernehmen, die zur Entwurfszeit noch nicht bekannt sind. Dieser Artikel bietet einen Ansatz zum dynamischen Ändern der Datenquelle einer Pivot-Tabelle.

###  **Ändern der Quelldaten einer Pivot-Tabelle**

1. Erstellen einer neuen Designervorlage.
 1. Erstellen Sie eine neue Designer-Vorlagendatei wie im Screenshot unten.
 1. Definieren Sie dann einen benannten Bereich, *DataSource**, der sich auf diesen Zellbereich bezieht.

      **Erstellen einer Designervorlage und Definieren eines benannten Bereichs, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)
   
1. Erstellen einer Pivot-Tabelle basierend auf diesem benannten Bereich.
1. Wählen Sie in Microsoft Excel**Daten**, dann **PivotTable** und *PivotChart-Bericht**.
 1. Erstellen Sie eine Pivot-Tabelle basierend auf dem benannten Bereich, der im ersten Schritt erstellt wurde.

      **Erstellen einer Pivot-Tabelle basierend auf dem benannten Bereich, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

   
 1. Ziehen Sie das entsprechende Feld in die Zeile und Spalte der Pivot-Tabelle und erstellen Sie dann die resultierende Pivot-Tabelle wie im Screenshot unten.

   **Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

   
1. Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie *Tabellenoptionen**.
 1. Überprüfen**Beim Öffnen aktualisieren** In**Datenoptionen** Einstellungen.

      **Festlegen der Pivot-Tabellenoptionen** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Jetzt können Sie diese Datei als Ihre Designer-Vorlagendatei speichern.

1. Neue Daten auffüllen und Quelldaten einer Pivot-Tabelle ändern.
 1. Sobald die Designervorlage erstellt ist, verwenden Sie den folgenden Code, um die Quelldaten der Pivot-Tabelle zu ändern.

Durch Ausführen des folgenden Beispielcodes werden die Quelldaten der Pivot-Tabelle geändert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

