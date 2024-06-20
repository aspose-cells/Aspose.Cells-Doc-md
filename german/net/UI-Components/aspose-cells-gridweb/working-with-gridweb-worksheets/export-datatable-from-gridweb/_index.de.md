---
title: Datenbank von GridWeb exportieren
type: docs
weight: 70
url: /de/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb, exportieren
description: Dieser Artikel führt ein, wie man DataTable in GridWeb exportiert.
---

{{% alert color="primary" %}} 

[Import DataView to GridWeb](/cells/de/net/aspose-cells-gridweb/import-dataview-to-gridweb/) beschreibt den Import des Inhalts eines DataView-Objekts in die Aspose.Cells.GridWeb-Steuerung. Dieser Abschnitt behandelt das Exportieren von Daten aus der Aspose.Cells.GridWeb-Steuerung in eine DataTable.

{{% /alert %}} 
## **Exportieren von Arbeitsblattdaten**
### **Zu einer bestimmten DataTable**
Um Arbeitsblattdaten in ein bestimmtes DataTable-Objekt zu exportieren:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Erstellen Sie ein bestimmtes DataTable-Objekt.
1. Exportieren Sie die Daten der ausgewählten Zellen in das angegebene DataTable-Objekt.

Im folgenden Beispiel wird ein spezifisches DataTable-Objekt mit vier Spalten erstellt. Die Arbeitsblattdaten werden ab der ersten Zelle mit allen sichtbaren Zeilen und Spalten im Arbeitsblatt in ein zuvor erstelltes DataTable-Objekt exportiert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Zu einer neuen DataTable**
Manchmal möchten Sie kein DataTable-Objekt erstellen, sondern einfach die Arbeitsblattdaten in ein neues DataTable-Objekt exportieren.

Im folgenden Beispiel wird eine andere Methode gezeigt, wie die Verwendung der Exportmethode erfolgen kann. Es übernimmt den Verweis auf das aktive Arbeitsblatt und exportiert die kompletten Daten dieses Arbeitsblatts in ein neues DataTable-Objekt. Das DataTable-Objekt kann nun auf jede gewünschte Weise verwendet werden. Zum Beispiel kann es an ein GridView gebunden werden, um die Daten anzuzeigen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
