---
title: Pubblico API Modifiche Aspose.Cells 8.0.1
type: docs
weight: 30
url: /it/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Queste pagine elencano le modifiche API pubbliche introdotte in Aspose.Cells 8.0.1. Include non solo metodi pubblici nuovi e obsoleti, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells che potrebbero influire sul codice esistente. Qualsiasi comportamento introdotto che potrebbe essere visto come una regressione e modifica il comportamento esistente è particolarmente importante ed è documentato qui.

{{% /alert %}} 
## **Proprietà MemorySetting Aggiunta alla classe Cells**
Cells ha esposto i metodi setMemorySetting e getMemorySetting che possono essere utilizzati per ottimizzare l'utilizzo della memoria per i dati delle celle e quindi ridurre il costo complessivo della memoria. L'esempio seguente mostra come scrivere dati di grandi dimensioni in un foglio di lavoro in modalità ottimizzata.

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

 Le impostazioni della memoria non funzioneranno per il foglio predefinito creato automaticamente dalla cartella di lavoro. Per modificare le impostazioni di memoria dei fogli esistenti, applicare manualmente le impostazioni di memoria prima di eseguire qualsiasi manipolazione dei dati.

{{% /alert %}} {{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Ottimizzazione della memoria mentre si lavora con set di dati di grandi dimensioni](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
