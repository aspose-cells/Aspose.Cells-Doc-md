---
title: Importieren von Daten aus einem DataTable in ein Raster
type: docs
weight: 50
url: /de/net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop,import,data,datatable
description: Dieser Artikel stellt vor, wie Daten in GridDesktop importiert werden.
---

{{% alert color="primary" %}} 

Seit der Veröffentlichung des .NET Frameworks hat Microsoft eine ausgezeichnete Möglichkeit bereitgestellt, Daten im Offline-Modus in Form eines DataTable-Objekts zu speichern. Aspose.Cells.GridDesktop unterstützt auch das Importieren von Daten aus einer Datenbank. Dieses Thema erörtert, wie dies gemacht wird.

{{% /alert %}} 
## **Beispiel**
Um den Inhalt einer Datenbank unter Verwendung der Aspose.Cells.GridDesktop-Steuerelemente zu importieren:

1. Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu einem Formular hinzu.
1. Erstellen Sie ein DataTable-Objekt, das die zu importierenden Daten enthält.
1. Holen Sie sich die Referenz eines gewünschten Arbeitsblatts.
1. Importieren Sie den Inhalt der Datenbank in das Arbeitsblatt.
1. Setzen Sie die Spaltenköpfe des Arbeitsblatts gemäß den Spaltennamen der Datenbank.
1. Legen Sie die Breite der Spalten fest, wenn gewünscht.
1. Zeigen Sie das Arbeitsblatt an.

In dem unten stehenden Beispiel haben wir ein DataTable-Objekt erstellt und es mit einigen Daten gefüllt, die aus einer Datenbanktabelle mit dem Namen Produkte abgerufen wurden. Schließlich haben wir Daten aus diesem DataTable-Objekt in ein gewünschtes Arbeitsblatt mit Aspose.Cells.GridDesktop importiert.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
