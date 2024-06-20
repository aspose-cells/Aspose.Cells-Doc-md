---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.1.1
type: docs
weight: 60
url: /it/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Questo documento descrive i cambiamenti dell'API di Aspose.Cells dalla versione 8.1.0 alla 8.1.1, che potrebbero interessare agli sviluppatori di moduli e applicazioni. Include non solo [nuovi e aggiornati metodi pubblici](/cells/it/java/public-api-changes-in-aspose-cells-8-1-1/), ma anche una descrizione di eventuali [modifiche nel comportamento](/cells/it/java/public-api-changes-in-aspose-cells-8-1-1/) dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Proprietà e Funzionalità Aggiunte**
### **Aggiunta la proprietà HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions ha esposto metodi getter/setter per la proprietà PresentationPreference che può essere utilizzata per rendere i risultati con una migliore disposizione durante l'esportazione di fogli di calcolo in HTML o MHTML. Il valore predefinito è false, mentre se impostato su true, l'API Aspose.Cells esporta i contenuti del foglio di lavoro con una migliore presentazione.

{{% alert color="primary" %}} 

Si prega di verificare l'articolo dettagliato su [Utilizzare l'opzione PresentationPreference per una migliore disposizione](/cells/it/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Aggiunto il supporto per gli scenari del foglio di lavoro**
Uno scenario è un modello ipotetico che include celle di input variabili collegate insieme da una o più formule. Aspose.Cells ha reso disponibile un getter e un setter per la proprietà Worksheet.Scenarios insieme alle seguenti classi per aiutare gli sviluppatori a creare, manipolare e rimuovere scenari.

1. Scenario: Rappresenta uno scenario individuale.
1. ScenarioCollection: Rappresenta una collezione di scenari.
1. ScenarioInputCellCollection: Rappresenta un elenco di celle di input per uno scenario specifico.
1. ScenarioInputCell: Rappresenta una cella di input dalla collezione di input-cells per uno scenario specifico.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Come Creare, Manipolare o Rimuovere Scenari dai Fogli di Lavoro](/cells/it/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Modifica del comportamento per CellsException**
Con le versioni precedenti dell'API Aspose.Cells for Java, quando un foglio di calcolo eventualmente danneggiato veniva caricato in un'istanza di Workbook, l'API tendeva a generare un messaggio generico senza specificare dove potesse essere il problema. Abbiamo modificato questo comportamento per la versione 8.1.1 in modo che l'API generi un'eccezione con un messaggio significativo che indica dove (quale cella) e cosa (espressione della formula) causa l'eccezione durante la lettura del file modello.
