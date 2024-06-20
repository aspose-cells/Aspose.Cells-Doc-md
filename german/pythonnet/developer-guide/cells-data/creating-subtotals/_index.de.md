---
title: Untersummen erstellen
type: docs
weight: 800
url: /de/python-net/creating-subtotals/
description: Erfahren Sie, wie Sie in einer Tabelle mit Hilfe der Aspose.Cells for Python via .NET API Teilsummen für alle sich wiederholenden Werte generieren.
keywords: Python Excel Bibliothek, Teilsummen anwenden, Teilsummen setzen, Teilsummen hinzufügen, Teilsummen erstellen, Wie man Teilsummen zu einem Arbeitsblatt hinzufügt 
---

{{% alert color="primary" %}}

Sie können automatisch Teilsummen für wiederkehrende Werte in einer Tabelle erstellen. Aspose.Cells for Python via .NET bietet API-Funktionen, welche Ihnen helfen, Teilsummen programmgesteuert zu Arbeitsblättern hinzuzufügen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um Teilsummen in Microsoft Excel hinzuzufügen:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle innerhalb Ihrer Liste aus.
1. Wählen Sie im **Daten**-Menü **Teilsummen** aus. Der Dialog für Teilsummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Teilsummen platziert werden sollen.

## **Verwendung der Aspose.Cells for Python via .NET API**

Aspose.Cells for Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern und anderen Objekten. Jedes Arbeitsblatt besteht aus einer [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung. Um Teilsummen zu einem Arbeitsblatt hinzuzufügen, verwenden Sie die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Klasse und die Methode [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) der Klasse. Geben Sie Parameterwerte an die Methode, um zu spezifizieren, wie die Teilsumme berechnet und platziert werden soll.

In den folgenden Beispielen haben wir Teilsummen zum ersten Arbeitsblatt der Vorlagendatei (Book1.xls) mit Hilfe der Aspose.Cells for Python via .NET API hinzugefügt. Wenn der Code ausgeführt wird, wird ein Arbeitsblatt mit Teilsummen erstellt.

Die nachfolgenden Codeausschnitte zeigen, wie Teilsummen zu einem Arbeitsblatt mit Aspose.Cells for Python via .NET hinzugefügt werden können.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **Erweiterte Themen**
- [Teilsumme anwenden und Richtung der Zusammenfassungszeilen unterhalb der Detaildaten ändern](/cells/de/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
