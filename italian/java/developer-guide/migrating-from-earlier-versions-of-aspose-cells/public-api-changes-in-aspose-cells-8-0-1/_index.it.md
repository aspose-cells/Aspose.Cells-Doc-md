---
title: Modifiche all API pubblica in Aspose.Cells 8.0.1
type: docs
weight: 30
url: /it/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Questa pagina elenca le modifiche all'API pubblica introdotte in Aspose.Cells 8.0.1. Essa include non solo nuovi metodi pubblici e obsoleti, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells che possono influire sul codice esistente. Qualsiasi comportamento introdotto che possa essere considerato come una regressione e modifichi il comportamento esistente è particolarmente importante e viene documentato qui.

{{% /alert %}} 
## **Aggiunta la proprietà MemorySetting alla classe Cells**
La classe Cells ha esposto i metodi setMemorySetting e getMemorySetting che possono essere utilizzati per ottimizzare l'uso della memoria per i dati delle celle, riducendo così il costo complessivo della memoria. L'esempio seguente mostra come scrivere dati voluminosi in un foglio di lavoro in modalità ottimizzata.

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

Le impostazioni di memoria non funzioneranno per il foglio predefinito creato automaticamente dal Workbook. Per cambiare le impostazioni di memoria dei fogli esistenti, si prega di applicare manualmente le impostazioni di memoria prima di eseguire qualsiasi manipolazione dati. 

{{% /alert %}} {{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Ottimizzazione della memoria durante il lavoro con grandi set di dati](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
