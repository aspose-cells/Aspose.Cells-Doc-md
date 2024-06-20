---
title: Daten aus Grid exportieren
type: docs
weight: 60
url: /de/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop, Export, Daten, Daten exportieren
description: Dieser Artikel zeigt, wie Daten in GridDesktop exportiert werden können.
---

{{% alert color="primary" %}} 

In unserem vorherigen Thema haben wir darüber gesprochen, wie Sie den Inhalt einer DataTable in die Aspose.Cells.GridDesktop-Steuerung importieren können, aber wir haben absichtlich nicht erwähnt, dass Aspose.Cells.GridDesktop auch den umgekehrten Prozess unterstützt. In diesem Thema werden wir also über das Exportieren der Daten innerhalb der Aspose.Cells.GridDesktop-Steuerung in eine DataTable diskutieren.

{{% /alert %}} 
## **Gridinhalte exportieren**
### **Exportieren in eine bestimmte DataTable**
Um die Gridinhalte in ein bestimmtes DataTable-Objekt zu exportieren, befolgen Sie bitte die folgenden Schritte: Fügen Sie der **Form** die Aspose.Cells.GridDesktop-Steuerung hinzu.

- Erstellen Sie ein bestimmtes DataTable-Objekt nach Ihren Bedürfnissen.
- Exportieren Sie die Daten eines ausgewählten **Arbeitsblatts** in Ihr spezifiziertes DataTable-Objekt.

Im unten gezeigten Beispiel haben wir ein spezifisches DataTable-Objekt erstellt, das vier Spalten enthält. Schließlich haben wir Arbeitsblattdaten (beginnend mit der ersten Zelle mit 69 Zeilen und 4 Spalten) in ein bereits von uns erstelltes DataTable-Objekt exportiert.

**Beispiel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exportieren in eine neue DataTable**
Manchmal sind Entwickler nicht daran interessiert, ein eigenes DataTable-Objekt zu erstellen, und haben möglicherweise nur die einfache Notwendigkeit, die Arbeitsblattdaten in ein neues DataTable-Objekt zu exportieren. Es wäre der schnellste Weg für die Entwickler, die Arbeitsblattdaten einfach zu exportieren.

Im unten gezeigten Beispiel haben wir eine andere Möglichkeit ausprobiert, die Verwendung der Methode ExportDataTable zu erläutern. Wir haben uns auf das Arbeitsblatt bezogen, das derzeit aktiv ist, und dann die vollständigen Daten dieses aktiven Arbeitsblatts in ein neues DataTable-Objekt exportiert. Jetzt kann dieses DataTable-Objekt von einem Entwickler auf jede gewünschte Weise verwendet werden. Nur zum Beispiel kann ein Entwickler dieses DataTable-Objekt an ein DataGrid binden, um die Daten anzuzeigen.

**Beispiel:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

In dem oben genannten Fall werden wir eine überladene Version der ExportDataTable-Methode verwenden, die einfach ein neues DataTable-Objekt zurückgibt, das die aus dem Arbeitsblatt exportierten Daten enthält.

{{% /alert %}}
