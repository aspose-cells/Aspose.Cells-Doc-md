---
title: Pubblico API Modifiche Aspose.Cells 8.1.1
type: docs
weight: 60
url: /it/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche al Aspose.Cells API dalla versione 8.1.0 alla 8.1.1, che potrebbero interessare gli sviluppatori di moduli e applicazioni. Include non solo[metodi pubblici nuovi e aggiornati](/cells/it/java/public-api-changes-in-aspose-cells-8-1-1/) , ma anche una descrizione di qualsiasi[cambiamenti nel comportamento](/cells/it/java/public-api-changes-in-aspose-cells-8-1-1/) dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Proprietà e caratteristiche aggiunte**
### **Aggiunta la proprietà HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions ha esposto la proprietà getter/setter per PresentationPreference che può essere utilizzata per eseguire il rendering dei risultati con un layout migliore durante l'esportazione di fogli di calcolo in HTML o MHTML. Il valore predefinito è falso. mentre se impostato su true, Aspose.Cells API esporta il contenuto del foglio di lavoro con una migliore presentazione.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Usa l'opzione PresentationPreference per un layout migliore](/cells/it/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Aggiunto il supporto per gli scenari del foglio di lavoro**
Uno scenario è un modello what-if che include celle di input variabili collegate tra loro da una o più formule. Aspose.Cells ha esposto un getter e un setter per la proprietà Worksheet.Scenarios insieme alle classi seguenti per aiutare gli sviluppatori a creare, manipolare e rimuovere gli scenari.

1. Scenario: rappresenta uno scenario individuale.
1. ScenarioCollection: rappresenta una raccolta di scenari.
1. ScenarioInputCellCollection: rappresenta un elenco di celle di input per un particolare scenario.
1. ScenarioInputCell: rappresenta una cella di input dalla raccolta di celle di input per un particolare scenario.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Come creare, manipolare o rimuovere scenari dai fogli di lavoro](/cells/it/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Modifica del comportamento per CellsException**
Con le versioni precedenti di Aspose.Cells for Java API, quando un foglio di calcolo eventualmente danneggiato veniva caricato in un'istanza di Workbook, API tendeva a lanciare un messaggio generico senza menzionare dove potesse essere il problema. Abbiamo modificato questo comportamento per 8.1.1 in modo che API generi un'eccezione con un messaggio significativo che indica dove (quale cella) e cosa (espressione della formula) provoca l'eccezione durante la lettura del file modello.
