---
title: Come correggere java.lang.OutOfMemoryError durante il caricamento di fogli di calcolo di grandi dimensioni
type: docs
weight: 20
url: /it/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Ci sono buone possibilità che il costruttore della cartella di lavoro possa generare java.lang.OutOfMemoryError durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando il[Preferenze di memoria](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Come correggere java.lang.OutOfMemoryError durante il caricamento di un foglio di calcolo di grandi dimensioni**
Aspose.Cells Le API forniscono le preferenze di memoria per ottimizzare il consumo di memoria durante il caricamento e l'elaborazione dei fogli di calcolo. Queste opzioni sono utili anche per caricare in modo efficiente i fogli di calcolo di grandi dimensioni contenenti enormi set di dati nell'oggetto cartella di lavoro, come illustrato di seguito.

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
