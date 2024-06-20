---
title: Untersummen erstellen
type: docs
weight: 50
url: /de/java/creating-subtotals/
---

{{% alert color="primary" %}}

Sie können automatisch Zwischensummen für alle wiederkehrenden Werte in einer Tabelle erstellen. Aspose.Cells bietet API-Funktionen, die Ihnen helfen, Zwischensummen programmgesteuert hinzuzufügen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um Zwischensummen in Microsoft Excel zu erstellen:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle innerhalb Ihrer Liste aus.
1. Wählen Sie im **Daten**-Menü **Zwischensummen** aus.
   Das Dialogfeld Zwischensummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Zwischensummen platziert werden sollen.

   **Auswählen eines Datenbereichs, um Zwischensummen hinzuzufügen**

![todo:image_alt_text](creating-subtotals_1.png)

**Das Zwischensummen-Dialogfeld** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Verwendung der Aspose.Cells-API**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält ein [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), das den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht.

Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert. Die Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Arbeitsmappe und anderer Objekte. Jede Arbeitsmappe besteht aus einer [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung. Verwenden Sie die [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Methode der Klasse, um Zwischensummen in einer Arbeitsmappe zu erstellen. Geben Sie geeignete Werte für die Parameter der Methode an, um das gewünschte Ergebnis zu erzielen.

Im folgenden Beispiel wird gezeigt, wie Sie mithilfe der Aspose.Cells-API Zwischensummen in der ersten Arbeitsmappe der Vorlagendatei (Book1.xls) erstellen.

Wenn der Code ausgeführt wird, wird eine Arbeitsmappe mit Zwischensummen erstellt.

**Anwendung von Zwischensummen** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
