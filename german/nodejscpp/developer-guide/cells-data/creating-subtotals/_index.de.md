---
title: Untersummen erstellen
type: docs
weight: 800
url: /de/nodejs-cpp/creating-subtotals/
description: Lernen Sie, wie Sie Zwischensummen für wiederkehrende Werte in einer Tabelle mithilfe der Aspose.Cells for Node.js via C++ API erstellen.
keywords: Untertotale anwenden, Untertotale festlegen, Untertotale hinzufügen, Untertotale erstellen, Wie Sie Untertotale zu einem Arbeitsblatt hinzufügen 
---

{{% alert color="primary" %}}

Sie können automatisch Zwischensummen für wiederkehrende Werte in einer Tabelle erstellen. Aspose.Cells for Node.js via C++ stellt API-Funktionen bereit, die Ihnen helfen, Zwischensummen programmatisch zu einer Tabelle hinzuzufügen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um Teilsummen in Microsoft Excel hinzuzufügen:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle innerhalb Ihrer Liste aus.
1. Wählen Sie im **Daten**-Menü **Teilsummen** aus. Der Dialog für Teilsummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Teilsummen platziert werden sollen.

## **Mit der Aspose.Cells for Node.js via C++ API**

Aspose.Cells for Node.js via C++ stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern und anderen Objekten. Jedes Arbeitsblatt besteht aus einer [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung. Um Teilsummen zu einem Arbeitsblatt hinzuzufügen, verwenden Sie die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Klasse und die Methode [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) der Klasse. Geben Sie Parameterwerte an die Methode, um zu spezifizieren, wie die Teilsumme berechnet und platziert werden soll.

In den folgenden Beispielen haben wir mit der Aspose.Cells for Node.js via C++ API Zwischensummen zum ersten Arbeitsblatt der [Vorlage](book1.xlsx) hinzugefügt. Beim Ausführen des Codes wird ein Arbeitsblatt mit Zwischensummen erstellt.

Die folgenden Codebeispiele zeigen, wie man mit Aspose.Cells for Node.js via C++ Zwischensummen zu einem Arbeitsblatt hinzufügt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

