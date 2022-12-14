---
title: Importieren von Daten aus einer DataTable in Grid
type: docs
weight: 50
url: /de/net/importing-data-from-a-datatable-to-grid/
---
{{% alert color="primary" %}} 

Seit der Veröffentlichung des Frameworks .NET bietet Microsoft eine hervorragende Möglichkeit, Daten im Offlinemodus in Form eines DataTable-Objekts zu speichern. Aspose.Cells.GridDesktop versteht die Anforderungen von Entwicklern und unterstützt auch das Importieren von Daten aus einer Datentabelle. In diesem Thema wird erläutert, wie Sie dies tun.

{{% /alert %}} 
## **Beispiel**
So importieren Sie den Inhalt einer Datentabelle mit dem Aspose.Cells.GridDesktop-Steuerelement:

1. Fügen Sie einem Formular das Aspose.Cells.GridDesktop-Steuerelement hinzu.
1. Erstellen Sie ein DataTable-Objekt, das die zu importierenden Daten enthält.
1. Rufen Sie die Referenz eines gewünschten Arbeitsblatts ab.
1. Importieren Sie den Inhalt der Datentabelle in das Arbeitsblatt.
1. Legen Sie die Spaltenüberschriften des Arbeitsblatts entsprechend den Spaltennamen der Datentabelle fest.
1. Stellen Sie die Breite der Spalten ein, falls gewünscht/
1. Zeigen Sie das Arbeitsblatt an.

In dem unten angegebenen Beispiel haben wir ein DataTable-Objekt erstellt und es mit einigen Daten gefüllt, die aus einer Datenbanktabelle namens Products abgerufen wurden. Schließlich haben wir Daten aus diesem DataTable-Objekt mit Aspose.Cells.GridDesktop in ein gewünschtes Arbeitsblatt importiert.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
