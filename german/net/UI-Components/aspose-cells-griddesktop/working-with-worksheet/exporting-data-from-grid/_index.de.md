---
title: Exportieren von Daten aus dem Raster
type: docs
weight: 60
url: /de/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

In unserem vorherigen Thema haben wir über das Importieren des Inhalts einer DataTable in das Aspose.Cells.GridDesktop-Steuerelement gesprochen, aber wir haben absichtlich nicht erwähnt, dass Aspose.Cells.GridDesktop auch den umgekehrten Prozess unterstützt. In diesem Thema besprechen wir also das Exportieren der Daten innerhalb des Aspose.Cells.GridDesktop-Steuerelements in eine DataTable.

{{% /alert %}} 
## **Grid-Inhalte exportieren**
### **Exportieren in eine bestimmte DataTable**
 Führen Sie die folgenden Schritte aus, um den Grid-Inhalt in ein bestimmtes DataTable-Objekt zu exportieren:Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrem hinzu**Bilden**.

- Erstellen Sie ein spezifisches DataTable-Objekt gemäß Ihren Anforderungen.
-  Exportieren Sie die Daten eines ausgewählten**Arbeitsblatt** zu Ihrem angegebenen DataTable-Objekt.

In dem unten angegebenen Beispiel haben wir ein bestimmtes DataTable-Objekt mit vier Spalten darin erstellt. Schließlich haben wir Arbeitsblattdaten (beginnend mit der ersten Zelle mit 69 Zeilen und 4 Spalten) in ein bereits von uns erstelltes DataTable-Objekt exportiert.

**Beispiel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportieren in eine neue Datentabelle**
Manchmal sind Entwickler möglicherweise nicht daran interessiert, ein eigenes DataTable-Objekt zu erstellen, und müssen möglicherweise einfach die Arbeitsblattdaten in ein neues DataTable-Objekt exportieren. Es wäre der schnellste Weg für die Entwickler, einfach die Arbeitsblattdaten zu exportieren.

In dem unten angegebenen Beispiel haben wir versucht, die Verwendung der ExportDataTable-Methode auf andere Weise zu erklären. Wir haben die Referenz des derzeit aktiven Arbeitsblatts genommen und dann die vollständigen Daten dieses aktiven Arbeitsblatts in ein neues DataTable-Objekt exportiert. Jetzt kann dieses DataTable-Objekt auf beliebige Weise verwendet werden, die ein Entwickler wünscht. Nur für eine Instanz kann ein Entwickler dieses DataTable-Objekt an ein DataGrid binden, um die Daten anzuzeigen.

**Beispiel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

Im obigen Fall verwenden wir eine überladene Version der ExportDataTable-Methode, die einfach ein neues DataTable-Objekt zurückgibt, das aus dem Arbeitsblatt exportierte Daten enthält.

{{% /alert %}}
