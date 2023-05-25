---
title: Crea, manipola o rimuovi scenari dai fogli di lavoro
linktitle: Gestisci scenari
type: docs
weight: 190
url: /it/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: In questo articolo imparerai come creare, manipolare o rimuovere scenari dai fogli di lavoro di Excel a livello di programmazione utilizzando la libreria C# con .NET API.
keywords: create scenario worksheet c#, remove scenario excel worksheet c#, manipulate scenario worksheet c#
---
{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un "e se?" modello che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progettare il foglio di lavoro in modo che contenga almeno una formula che dipenda dalle celle in cui è possibile inserire valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro in una cartella di lavoro tramite le API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce alcune classi utili, ad esempio,[**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , E[**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) classi. Fornisce inoltre il[**Foglio di lavoro.Scenari**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)proprietà. Il codice di esempio seguente apre un file Excel XLSX che contiene alcuni scenari e rimuove uno scenario esistente. Aggiunge inoltre un nuovo scenario al foglio di lavoro prima di salvare il file Excel. L'esempio utilizza un file modello molto semplice che contiene uno scenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
