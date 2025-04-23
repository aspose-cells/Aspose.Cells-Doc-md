---
title: Untersummen erstellen
type: docs
weight: 800
url: /de/net/creating-subtotals/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for .NET Untertotale für wiederholte Werte in einem Tabellenblatt erstellen können.
keywords: Untertotale anwenden, Untertotale festlegen, Untertotale hinzufügen, Untertotale erstellen, Wie Sie Untertotale zu einem Arbeitsblatt hinzufügen 
---

{{% alert color="primary" %}}

Sie können automatisch Teilergebnisse für beliebige wiederholende Werte in einem Tabellenblatt erstellen. Aspose.Cells bietet API-Funktionen, die Ihnen helfen, Teilergebnisse programmgesteuert zu Tabellenblättern hinzuzufügen.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Um Teilsummen in Microsoft Excel hinzuzufügen:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle innerhalb Ihrer Liste aus.
1. Wählen Sie im **Daten**-Menü **Teilsummen** aus. Der Dialog für Teilsummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Teilsummen platziert werden sollen.

## **Verwendung der Aspose.Cells-API**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern und anderen Objekten. Jedes Arbeitsblatt besteht aus einer [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung. Um Teilsummen zu einem Arbeitsblatt hinzuzufügen, verwenden Sie die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Klasse und die Methode [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) der Klasse. Geben Sie Parameterwerte an die Methode, um zu spezifizieren, wie die Teilsumme berechnet und platziert werden soll.

In den folgenden Beispielen haben wir Untertotale dem ersten Arbeitsblatt der Vorlagendatei (Book1.xls) mit der Aspose.Cells-API hinzugefügt. Wenn der Code ausgeführt wird, wird ein Arbeitsblatt mit Untertotalen erstellt.

Die folgenden Code-Ausschnitte zeigen, wie Sie Zwischensummen zu einem Arbeitsblatt mit Aspose.Cells for .NET hinzufügen können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Erweiterte Themen**
- [Teilsumme anwenden und Richtung der Zusammenfassungszeilen unterhalb der Detaildaten ändern](/cells/de/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
{{< app/cells/assistant language="csharp" >}}
