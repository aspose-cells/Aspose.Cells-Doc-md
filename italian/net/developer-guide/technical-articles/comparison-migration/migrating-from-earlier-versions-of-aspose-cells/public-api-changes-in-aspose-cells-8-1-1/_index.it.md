---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.1.1
type: docs
weight: 50
url: /it/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.1.0 alla 8.1.1, che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **Aggiunta la Proprietà HtmlSaveOptions.PresentationPreference**
La classe HtmlSaveOptions ha esposto la proprietà PresentationPreference che può essere utilizzata per rendere i risultati con una migliore presentazione durante l'esportazione dei fogli di calcolo in HTML o MHTML. Il valore predefinito è false. mentre se impostato su true, l'API di Aspose.Cells esporterà i contenuti del foglio di lavoro con una migliore presentazione.

{{% alert color="primary" %}} 

Si prega di consultare l'articolo dettagliato su [Usa l'opzione PresentationPreference per una migliore presentazione](/cells/it/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Aggiunto il supporto per gli scenari del foglio di lavoro**
Uno scenario è un modello ipotetico che include celle di input variabili collegate da una o più formule di conseguenza. L'API di Aspose.Cells ha esposto la proprietà Worksheet.Scenarios insieme alle seguenti classi al fine di facilitare agli utenti la creazione, la manipolazione e la rimozione degli scenari dai fogli di calcolo, 

1. Scenario: Rappresenta uno scenario individuale.
1. ScenarioCollection: Rappresenta una collezione di scenari.
1. ScenarioInputCellCollection: Rappresenta un elenco di celle di input per uno scenario particolare.
1. ScenarioInputCell: Rappresenta una cella di input dalla raccolta di celle di input per uno scenario particolare.

{{% alert color="primary" %}} 

Si prega di controllare l'articolo dettagliato su [Come Creare, Manipolare o Rimuovere Scenari da Fogli di Lavoro](/cells/it/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
