---
title: Pubblico API Modifiche Aspose.Cells 8.0.1
type: docs
weight: 20
url: /it/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Queste pagine elencano le modifiche API pubbliche introdotte in Aspose.Cells 8.0.1. Include non solo metodi pubblici nuovi e obsoleti, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells che potrebbero influire sul codice esistente. Qualsiasi comportamento introdotto che potrebbe essere visto come una regressione e modifica il comportamento esistente è particolarmente importante ed è documentato qui.

{{% /alert %}} 
## **Proprietà MemorySetting Aggiunta alla classe Cells**
La classe Cells ha esposto la proprietà MemorySetting che può essere utilizzata per ottimizzare l'utilizzo della memoria per i dati delle celle e quindi ridurre il costo complessivo della memoria. L'esempio seguente mostra come scrivere dati di grandi dimensioni in un foglio di lavoro in modalità ottimizzata.

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

Le impostazioni di memoria non funzioneranno per il foglio predefinito creato automaticamente dall'oggetto cartella di lavoro. Per modificare le impostazioni di memoria dei fogli esistenti, applicare manualmente l'impostazione di memoria prima di eseguire qualsiasi manipolazione dei dati.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottimizzazione della memoria mentre si lavora con set di dati di grandi dimensioni](/cells/it/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
