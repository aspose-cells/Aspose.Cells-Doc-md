---
title: DataTable aus GridWeb exportieren
type: docs
weight: 70
url: /de/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[Importieren Sie DataView in GridWeb](/cells/de/net/import-dataview-to-gridweb/)sprachen über das Importieren des Inhalts einer DataView in das Aspose.Cells.GridWeb-Steuerelement. In diesem Thema wird das Exportieren der Daten aus dem Aspose.Cells.GridWeb-Steuerelement in eine DataTable erläutert.

{{% /alert %}} 
## **Arbeitsblattdaten exportieren**
### **Zu einer bestimmten DataTable**
So exportieren Sie Arbeitsblattdaten in ein bestimmtes DataTable-Objekt:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Erstellen Sie ein bestimmtes DataTable-Objekt.
1. Exportiert die Daten der ausgewählten Zellen in das angegebene DataTable-Objekt.

Das folgende Beispiel erstellt ein bestimmtes DataTable-Objekt mit vier Spalten. Die Arbeitsblattdaten werden ab der ersten Zelle mit allen im Arbeitsblatt sichtbaren Zeilen und Spalten in ein bereits erstelltes DataTable-Objekt exportiert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Zu einer neuen Datentabelle**
Manchmal möchten Sie kein DataTable-Objekt erstellen, sondern einfach die Arbeitsblattdaten in ein neues DataTable-Objekt exportieren.

Das folgende Beispiel versucht auf andere Weise, die Verwendung der Export-Methode zu zeigen. Es nimmt die Referenz des aktiven Arbeitsblatts und exportiert die vollständigen Daten dieses Arbeitsblatts in ein neues DataTable-Objekt. Das DataTable-Objekt kann nun beliebig verwendet werden. Beispielsweise ist es möglich, das DataTable-Objekt an eine GridView zu binden, um die Daten anzuzeigen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
