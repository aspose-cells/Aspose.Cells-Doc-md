---
title: So beheben Sie den java.lang.OutOfMemoryError beim Laden großer Tabellenkalkulationen
type: docs
weight: 20
url: /de/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Es besteht die Möglichkeit, dass der Workbook-Konstruktor beim Laden großer Tabellenkalkulationen java.lang.OutOfMemoryError auslöst. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden, daher muss die Tabelle geladen werden, während die aktiviert wird[Speichereinstellungen](/cells/de/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **So beheben Sie den java.lang.OutOfMemoryError beim Laden einer großen Tabelle**
Aspose.Cells APIs bieten Speichereinstellungen, um den Speicherverbrauch beim Laden und Verarbeiten von Tabellenkalkulationen zu optimieren. Diese Optionen sind auch hilfreich beim effizienten Laden der großen Tabellenkalkulationen mit riesigen Datensätzen im Workbook-Objekt, wie unten gezeigt.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
