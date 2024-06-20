---
title: Öffentliche API Änderungen in Aspose.Cells 8.0.1
type: docs
weight: 30
url: /de/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Diese Seite listet öffentliche API-Änderungen auf, die in Aspose.Cells 8.0.1 eingeführt wurden. Es umfasst nicht nur neue und veraltete öffentliche Methoden, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells, die bestehenden Code beeinflussen können. Jedes Verhalten, das als Regression betrachtet werden könnte und bestehendes Verhalten modifiziert, ist besonders wichtig und wird hier dokumentiert.

{{% /alert %}} 
## **MemorySetting-Eigenschaft zur Cells-Klasse hinzugefügt**
Die Cells-Klasse hat die Methoden setMemorySetting & getMemorySetting freigelegt, die zur Optimierung des Speicherverbrauchs für Zelldaten verwendet werden können und somit die Gesamtspeicherkosten senken. Im folgenden Beispiel wird gezeigt, wie große Daten im optimierten Modus in ein Arbeitsblatt geschrieben werden.

**Java**

{{< highlight csharp >}}

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

Die Speichereinstellungen funktionieren nicht automatisch für das standardmäßig von der Arbeitsmappe erstellte Blatt. Um die Speichereinstellungen von vorhandenen Blättern zu ändern, wenden Sie die Speichereinstellungen bitte manuell an, bevor Sie eine Datenumleitung durchführen. 

{{% /alert %}} {{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Speicherplatzoptimierung beim Arbeiten mit großen Datensätzen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
