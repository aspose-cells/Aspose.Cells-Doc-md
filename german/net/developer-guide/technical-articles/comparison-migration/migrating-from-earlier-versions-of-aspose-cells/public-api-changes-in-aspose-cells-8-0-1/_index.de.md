---
title: Öffentlich API Änderungen in Aspose.Cells 8.0.1
type: docs
weight: 20
url: /de/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Diese Seiten listen öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.1 eingeführt wurden. Es enthält nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells, die sich auf bestehenden Code auswirken können. Jedes eingeführte Verhalten, das als Rückschritt angesehen werden könnte und bestehendes Verhalten modifiziert, ist besonders wichtig und wird hier dokumentiert.

{{% /alert %}} 
## **MemorySetting-Eigenschaft zur Klasse Cells hinzugefügt**
Cells-Klasse hat die MemorySetting-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die Speichernutzung für Zellendaten zu optimieren und somit die Gesamtspeicherkosten zu senken. Das folgende Beispiel zeigt, wie große Datenmengen im optimierten Modus in ein Arbeitsblatt geschrieben werden.

**C#**

{{< highlight "csharp" >}}

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

Die Speichereinstellungen funktionieren nicht für das vom Workbook-Objekt automatisch erstellte Standardblatt. Um die Speichereinstellungen vorhandener Blätter zu ändern, wenden Sie die Speichereinstellung bitte manuell an, bevor Sie Daten manipulieren.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Optimieren des Arbeitsspeichers beim Arbeiten mit großen Datensätzen](/cells/de/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
