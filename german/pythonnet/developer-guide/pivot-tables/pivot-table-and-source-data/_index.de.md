---
title: Pivot Tabelle und Quelldaten
type: docs
weight: 30
url: /de/python-net/pivot-table-and-source-data/
description: Dieser Artikel zeigt, wie man die Quelldaten der Pivot Tabelle mit Aspose.Cells für Python via .NET ändert.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Wie man die Quelldaten der Pivot Tabelle mit Hilfe der Aspose.Cells für Python Excel Bibliothek ändert.
---

## **Quelldaten der Pivot-Tabelle**

Es gibt Zeiten, in denen Sie Microsoft Excel-Berichte mit Pivot-Tabellen erstellen möchten, die Daten aus verschiedenen Datenquellen (wie einer Datenbank) enthalten, die zur Entwurfszeit nicht bekannt sind. Dieser Artikel stellt einen Ansatz zur Verfügung, um die Datenquelle einer Pivot-Tabelle dynamisch zu ändern.

### **Ändern der Datenquelle einer Pivot-Tabelle**

1. Erstellen einer neuen Designer-Vorlage.
   1. Erstellen Sie eine neue Designer-Vorlagendatei wie im folgenden Screenshot gezeigt.
   1. Definieren Sie dann einen benannten Bereich, **Datenquelle**, der sich auf diesen Zellenbereich bezieht.

      **Erstellen einer Designer-Vorlage & Definieren eines benannten Bereichs, Datenquelle** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Erstellen einer Pivot-Tabelle auf Basis dieses benannten Bereichs.
   1. Wählen Sie in Microsoft Excel **Daten**, dann **PivotTable** und **PivotChart-Bericht** aus.
   1. Erstellen Sie eine Pivot-Tabelle basierend auf dem im ersten Schritt erstellten benannten Bereich.

      **Erstellen einer Pivot-Tabelle basierend auf dem benannten Bereich, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Ziehen Sie das entsprechende Feld in Zeile und Spalte der Pivot-Tabelle und erstellen Sie dann die resultierende Pivot-Tabelle wie im Screenshot unten.

   **Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie **Tabellenoptionen**.
   1. Aktivieren Sie **Beim Öffnen aktualisieren** in den **Dateneinstellungen**.

      **Festlegen der Pivot-Tabellenoptionen** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Nun können Sie diese Datei als Ihre Designer-Vorlagendatei speichern.

1. Neue Daten einfügen und die Quelldaten einer Pivot-Tabelle ändern.
   1. Sobald die Designer-Vorlage erstellt ist, verwenden Sie den folgenden Code, um die Quelldaten der Pivot-Tabelle zu ändern.

Die Ausführung des untenstehenden Beispielcodes ändert die Quelldaten der Pivot-Tabelle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
