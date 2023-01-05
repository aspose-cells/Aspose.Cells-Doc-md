---
title: Öffentlich API Änderungen in Aspose.Cells 8.0.1
type: docs
weight: 30
url: /de/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Diese Seiten listen öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.1 eingeführt wurden. Es enthält nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells, die sich auf bestehenden Code auswirken können. Jedes eingeführte Verhalten, das als Rückschritt angesehen werden könnte und bestehendes Verhalten modifiziert, ist besonders wichtig und wird hier dokumentiert.

{{% /alert %}} 
## **MemorySetting-Eigenschaft Der Klasse Cells hinzugefügt**
Cells-Klasse hat setMemorySetting- und getMemorySetting-Methoden verfügbar gemacht, die verwendet werden können, um die Speichernutzung für Zellendaten zu optimieren und somit die Gesamtspeicherkosten zu senken. Das folgende Beispiel zeigt, wie große Datenmengen im optimierten Modus in ein Arbeitsblatt geschrieben werden.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

 Die Speichereinstellungen funktionieren nicht für das automatisch von der Arbeitsmappe erstellte Standardblatt. Um die Speichereinstellungen vorhandener Blätter zu ändern, wenden Sie die Speichereinstellungen bitte manuell an, bevor Sie Daten manipulieren.

{{% /alert %}} {{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Optimieren des Arbeitsspeichers beim Arbeiten mit großen Datensätzen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
