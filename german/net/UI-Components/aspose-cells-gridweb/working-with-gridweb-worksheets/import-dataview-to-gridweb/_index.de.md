---
title: DataView in GridWeb importieren
type: docs
weight: 60
url: /de/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb importieren
description: Dieser Artikel führt ein, wie man Daten in GridWeb importiert.
---

{{% alert color="primary" %}} 

Mit der Veröffentlichung des Microsoft .NET Frameworks wurde eine neue Methode zur Speicherung von Daten eingeführt. Jetzt gibt es DataSet-, DataTable- und DataView-Objekte, die Daten im Offline-Modus speichern. Diese Objekte sind als Datenbanken sehr praktisch. Mit Aspose.Cells.GridWeb ist es möglich, Daten entweder aus DataTable- oder DataView-Objekten in Arbeitsblätter zu importieren. Aspose.Cells.GridWeb unterstützt nur den Import von Daten aus einem DataView-Objekt, aber ein DataTable-Objekt kann auch indirekt verwendet werden. Lassen Sie uns diese Funktion im Detail besprechen.

{{% /alert %}} 
## **Daten von DataView importieren**
Importieren Sie Daten aus einem DataView-Objekt unter Verwendung der Methode ImportDataView der GridWorsheetCollection im GridWeb-Control. Übergeben Sie das DataView-Objekt, von dem Sie Daten importieren möchten, an die Methode ImportDataView. Es ist möglich, während des Imports Spaltenüberschriften und Datenstile zu spezifizieren.

{{% alert color="primary" %}} 

Beim Importieren von Daten aus einem DataView-Objekt wird ein neues Arbeitsblatt erstellt, um die importierten Daten zu halten. Das Arbeitsblatt wird genauso benannt wie das DataTable.

{{% /alert %}} 

**Ergebnis: Daten aus einem DataView in ein neues Arbeitsblatt importiert** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Die Breiten der Spalten werden so angepasst, dass alle enthaltenen Daten angezeigt werden. Wenn die Daten aus dem DataView importiert werden, werden die Spaltenbreiten nicht automatisch angepasst. Benutzer müssen sie selbst anpassen. Um die Spaltenbreiten programmgesteuert anzupassen, verweisen Sie auf [Größenanpassung von Zeilen und Spalten](/cells/de/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

Eine überladene Version der Methode ImportDataView ermöglicht Entwicklern, den Namen des Blatts anzugeben, das die importierten Daten enthält, und eine spezifische Anzahl von Zeilen und Spalten aus dem DataView-Objekt zu importieren.

{{% /alert %}}
