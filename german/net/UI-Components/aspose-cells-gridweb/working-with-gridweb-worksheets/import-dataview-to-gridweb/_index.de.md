---
title: Importieren Sie DataView in GridWeb
type: docs
weight: 60
url: /de/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Mit der Veröffentlichung des Microsoft .NET Frameworks wurde eine neue Art der Datenspeicherung eingeführt. Jetzt DataSet-, DataTable- und DataView-Objekte, die Daten im Offline-Modus speichern. Diese Objekte sind sehr praktisch als Datenspeicher. Mit Aspose.Cells.GridWeb ist es möglich, Daten aus DataTable- oder DataView-Objekten in Arbeitsblätter zu importieren. Aspose.Cells. GridWeb unterstützt nur das Importieren von Daten aus einer DataView. -Objekt, aber ein DataTable-Objekt kann auch indirekt verwendet werden. Lassen Sie uns diese Funktion im Detail besprechen.

{{% /alert %}} 
## **Importieren von Daten aus DataView**
Importieren Sie Daten aus einem DataView-Objekt mithilfe der ImportDataView-Methode von GridWorsheetCollection im GridWeb-Steuerelement. Übergeben Sie das DataView-Objekt, aus dem Sie Daten importieren möchten, an die ImportDataView-Methode. Es ist möglich, Spaltenüberschrift und Datenstile während des Imports anzugeben.

{{% alert color="primary" %}} 

Wenn Daten aus einem DataView-Objekt importiert werden, wird ein neues Arbeitsblatt erstellt, um die importierten Daten aufzunehmen. Das Arbeitsblatt wird genauso benannt wie die DataTable.

{{% /alert %}} 

**Ausgabe: Daten, die aus einer DataView in ein neues Arbeitsblatt importiert wurden** 

![todo: Bild_alt_Text](import-dataview-to-gridweb_1.png)

 Die Breite der Spalten wird angepasst, um alle darin enthaltenen Daten anzuzeigen. Wenn die Daten aus DataView importiert werden, werden die Spaltenbreiten nicht automatisch angepasst. Benutzer müssen sie selbst anpassen. Informationen zum programmgesteuerten Anpassen der Spaltenbreite finden Sie unter[Ändern Sie die Größe von Zeilen und Spalten](/cells/de/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Eine überladene Version der ImportDataView-Methode ermöglicht es Entwicklern, den Namen des Blatts anzugeben, das die importierten Daten und eine bestimmte Anzahl von Zeilen und Spalten enthält, die aus dem DataView-Objekt importiert werden sollen.

{{% /alert %}}
