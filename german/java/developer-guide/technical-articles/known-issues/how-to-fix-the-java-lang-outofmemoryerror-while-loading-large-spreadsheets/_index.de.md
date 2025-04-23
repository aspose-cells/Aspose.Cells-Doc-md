---
title: Wie behebt man die java.lang.OutOfMemoryError beim Laden großer Tabellenkalkulationen
type: docs
weight: 20
url: /de/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Es besteht eine faire Chance, dass der Workbook-Konstruktor eine java.lang.OutOfMemoryError beim Laden großer Tabellenkalkulationen wirft. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden. Daher muss die Tabelle beim Aktivieren der [Memory Preferences](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) geladen werden.

{{% /alert %}} 
## **Wie behebt man die java.lang.OutOfMemoryError beim Laden großer Tabellenkalkulationen**
Aspose.Cells APIs bieten Speicherpräferenzen zur Optimierung des Speicherverbrauchs beim Laden und Verarbeiten von Tabellenkalkulationen. Diese Optionen sind auch hilfreich beim effizienten Laden großer Tabellenkalkulationen mit riesigen Datensätzen im Workbook-Objekt, wie unten demonstriert. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
