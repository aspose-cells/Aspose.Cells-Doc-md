---
title: Öffentliche API Änderungen in Aspose.Cells 8.0.1
type: docs
weight: 20
url: /de/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Diese Seite listet öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.1 eingeführt wurden. Es umfasst nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells, die bestehenden Code beeinflussen können. Jedes Verhalten, das als Regression betrachtet werden könnte und bestehendes Verhalten modifiziert, ist besonders wichtig und wird hier dokumentiert.

{{% /alert %}} 
## **MemorySetting-Eigenschaft der Cells-Klasse hinzugefügt**
Die Cells-Klasse hat die MemorySetting-Eigenschaft freigelegt, die zur Optimierung des Speicherverbrauchs für Zellendaten verwendet werden kann und somit die Gesamtspeicherkosten verringert. Das folgende Beispiel zeigt, wie große Daten im optimierten Modus in ein Arbeitsblatt geschrieben werden können.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

Die Speichereinstellungen funktionieren standardmäßig nicht für das automatisch vom Workbook-Objekt erstellte Blatt. Um die Speichereinstellungen bestehender Blätter zu ändern, wenden Sie die Speichereinstellung manuell an, bevor Sie eine Datenmanipulation durchführen.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Optimieren des Speichers bei der Arbeit mit großen Datensätzen](/cells/de/net/speichern-von-arbeitsspeicher-verwenden-mit-großen-dateien-die-große-datenbestände-haben/)

{{% /alert %}}
