---
title: Come risolvere java.lang.OutOfMemoryError durante il caricamento di grandi fogli di calcolo
type: docs
weight: 20
url: /it/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Ci sono buone possibilità che il costruttore di Workbook possa generare java.lang.OutOfMemoryError durante il caricamento di grandi fogli di calcolo. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando le [Preferenze di memoria](/cells/it/java/ottimizzazione-dell-utilizzo-della-memoria-nel-lavoro-con-file-di-grandi-dimensioni-contenenti-grandi-insiemi-di-dati/)

{{% /alert %}} 
## **Come risolvere java.lang.OutOfMemoryError durante il caricamento di un grande foglio di calcolo**
Le API Aspose.Cells forniscono Preferenze di Memoria per ottimizzare il consumo di memoria durante il caricamento e l'elaborazione dei fogli di calcolo. Queste opzioni sono utili anche per caricare efficientemente grandi fogli di calcolo contenenti enormi set di dati nell'oggetto Workbook come dimostrato di seguito. 

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
