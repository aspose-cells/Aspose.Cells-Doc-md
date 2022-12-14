---
title: Erstellen von Zwischensummen
type: docs
weight: 50
url: /de/java/creating-subtotals/
---
{{% alert color="primary" %}}

Sie können automatisch Zwischensummen für sich wiederholende Werte in einer Tabelle erstellen. Aspose.Cells bietet API-Funktionen, mit denen Sie Zwischensummen programmgesteuert zu Tabellenkalkulationen hinzufügen können.

{{% /alert %}}

## **Mit Microsoft Excel**

So erstellen Sie Zwischensummen in Microsoft Excel:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie in der Abbildung unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle in Ihrer Liste aus.
1.  Von dem**Daten** Menü, auswählen**Zwischensummen**.
 Der Dialog Zwischensummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Zwischensummen platziert werden sollen.

   **Auswählen eines Datenbereichs zum Hinzufügen von Zwischensummen**

![todo: Bild_alt_Text](creating-subtotals_1.png)

**Der Zwischensummendialog** 

![todo: Bild_alt_Text](creating-subtotals_2.png)

## **Mit Aspose.Cells API**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse. Die Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts und anderer Objekte. Jedes Arbeitsblatt besteht aus a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Um Zwischensummen in einem Arbeitsblatt zu erstellen, verwenden Sie die[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Zwischensummenmethode der Klasse. Geben Sie geeignete Werte für die Parameter der Methode an, um das gewünschte Ergebnis zu erhalten.

Das folgende Beispiel zeigt, wie Zwischensummen im ersten Arbeitsblatt der Vorlagendatei (Book1.xls) mit Aspose.Cells API erstellt werden.

Wenn der Code ausgeführt wird, wird ein Arbeitsblatt mit Zwischensummen erstellt.

**Anwenden von Zwischensummen** 

![todo: Bild_alt_Text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
