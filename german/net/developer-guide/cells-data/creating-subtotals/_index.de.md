---
title: Erstellen von Zwischensummen
type: docs
weight: 800
url: /de/net/creating-subtotals/
---
{{% alert color="primary" %}}

Sie können automatisch Zwischensummen für sich wiederholende Werte in einer Tabelle erstellen. Aspose.Cells bietet API-Funktionen, mit denen Sie programmgesteuert Zwischensummen zu Tabellenkalkulationen hinzufügen können.

{{% /alert %}}

## **Mit Microsoft Excel**

So fügen Sie Zwischensummen in Microsoft Excel hinzu:

1. Erstellen Sie eine einfache Datenliste im ersten Arbeitsblatt der Arbeitsmappe (wie in der Abbildung unten gezeigt) und speichern Sie die Datei als Book1.xls.
1. Wählen Sie eine beliebige Zelle in Ihrer Liste aus.
1.  Von dem**Daten** Menü, auswählen**Zwischensummen**. Der Dialog Zwischensummen wird angezeigt. Definieren Sie, welche Funktion verwendet werden soll und wo die Zwischensummen platziert werden sollen.

## **Mit der Aspose.Cells API**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Die Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern und anderen Objekten. Jedes Arbeitsblatt besteht aus a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Um Zwischensummen zu einem Arbeitsblatt hinzuzufügen, verwenden Sie die[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse'[**Zwischensumme**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)Methode. Geben Sie Parameterwerte für die Methode an, um anzugeben, wie die Zwischensumme berechnet und platziert werden soll.

In den folgenden Beispielen haben wir dem ersten Arbeitsblatt der Vorlagendatei (Book1.xls) mithilfe von Aspose.Cells API Zwischensummen hinzugefügt. Wenn der Code ausgeführt wird, wird ein Arbeitsblatt mit Zwischensummen erstellt.

Die folgenden Codeschnipsel zeigen, wie man Zwischensummen zu einem Arbeitsblatt mit Aspose.Cells for .NET hinzufügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Themen vorantreiben**
- [Anwenden der Zwischensumme und Ändern der Richtung der Gliederungszusammenfassungszeilen unter den Details](/cells/de/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
