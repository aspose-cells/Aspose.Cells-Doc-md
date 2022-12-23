---
title: Pubblico API Modifiche Aspose.Cells 8.1.1
type: docs
weight: 50
url: /it/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.1.0 alla 8.1.1, che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta proprietà HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions ha esposto la proprietà PresentationPreference che può essere utilizzata per eseguire il rendering dei risultati con un layout migliore durante l'esportazione di fogli di calcolo in HTML o MHTML. Il valore predefinito è false. mentre se impostato su true, Aspose.Cells API esporterà il contenuto del foglio di lavoro con una migliore presentazione.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Usa l'opzione PresentationPreference per un layout migliore](/cells/it/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Aggiunto il supporto per gli scenari del foglio di lavoro**
 Uno scenario è denominato modello what-if che include celle di input variabili collegate tra loro da una o più formule di conseguenza. Aspose.Cells API ha esposto la proprietà Worksheet.Scenarios insieme alle seguenti classi per facilitare gli utenti nella creazione, manipolazione e rimozione di scenari dai fogli di lavoro,

1. Scenario: rappresenta uno scenario individuale.
1. ScenarioCollection: rappresenta una raccolta di scenari.
1. ScenarioInputCellCollection: rappresenta un elenco di celle di input per un particolare scenario.
1. ScenarioInputCell: rappresenta una cella di input dalla raccolta di celle di input per un particolare scenario.

{{% alert color="primary" %}} 

 Si prega di controllare l'articolo dettagliato su[Come creare, manipolare o rimuovere scenari dai fogli di lavoro](/cells/it/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
