---
title: Creare, manipolare o rimuovere scenari dai fogli di lavoro
linktitle: Gestire gli scenari
type: docs
weight: 190
url: /it/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: In questo articolo imparerai come creare, manipolare o rimuovere scenari dai fogli di calcolo di Excel in modo programmato utilizzando la libreria C# con API .NET.
keywords: creare foglio di lavoro scenario c#, rimuovere foglio di lavoro scenario excel c#, manipolare foglio di lavoro scenario c#
---

{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello 'cosa succederebbe se?' che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progetta il foglio di lavoro in modo che contenga almeno una formula che dipende da celle in cui possono essere inseriti valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro in un libro tramite le API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce alcune classi utili, ad esempio, classi [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) e [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell). Fornisce anche la proprietà [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios). Il codice di esempio di seguito apre un file Excel XLSX che contiene alcuni scenari e rimuove uno scenario esistente. Aggiunge anche un nuovo scenario al foglio di lavoro prima di salvare il file Excel. L'esempio utilizza un file di modello molto semplice che contiene uno scenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
