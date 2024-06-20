---
title: Modifiche all API pubblica in Aspose.Cells 8.0.1
type: docs
weight: 20
url: /it/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Questa pagina elenca le modifiche all'API pubblica introdotte in Aspose.Cells 8.0.1. Essa include non solo nuovi metodi pubblici e obsoleti, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells che possono influire sul codice esistente. Qualsiasi comportamento introdotto che possa essere considerato come una regressione e modifichi il comportamento esistente è particolarmente importante e viene documentato qui.

{{% /alert %}} 
## **Proprietà MemorySetting aggiunta alla classe Cells**
La classe Cells ha esposto la proprietà MemorySetting che può essere utilizzata per ottimizzare l'utilizzo della memoria per i dati delle celle e quindi diminuire il costo complessivo della memoria.

**C#**

{{< highlight csharp >}}

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

Le impostazioni della memoria non funzioneranno automaticamente per il foglio predefinito creato dall'oggetto Workbook. Per modificare manualmente le impostazioni della memoria dei fogli esistenti, si prega di applicare le impostazioni della memoria prima di eseguire qualsiasi manipolazione dei dati.

{{% alert color="primary" %}} 

Si prega di verificare l'articolo dettagliato su [Ottimizzazione della memoria durante il lavoro con grandi set di dati](/cells/it/net/ottimizzazione-dellutilizzo-della-memoria-durante-il-lavoro-con-file-grandi-avente-grandi-insiemi-di-dati/)

{{% /alert %}}
