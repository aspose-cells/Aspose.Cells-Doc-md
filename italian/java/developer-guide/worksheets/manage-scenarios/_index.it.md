---
title: Crea, manipola o rimuovi scenari dai fogli di lavoro
linktitle: Gestisci scenari
type: docs
weight: 120
url: /it/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello what-if denominato che include celle di input variabili collegate tra loro da una o più formule. Prima di creare uno scenario, progettare un foglio di lavoro in modo che contenga almeno una formula che dipende dalle celle in cui è possibile inserire valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro utilizzando le API Aspose.Cells.

{{% /alert %}}

 Aspose.Cells fornisce alcune lezioni utili, ad esempio[**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) e[**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . Fornisce inoltre il[**Foglio di lavoro.Scenari**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)proprietà. Il codice di esempio seguente apre un file Excel XLSX (che contiene alcuni scenari) e rimuove uno scenario esistente dal foglio di lavoro. Aggiunge anche un nuovo scenario prima di salvare il file Excel. Utilizza un file modello molto semplice che contiene uno scenario.

Dopo aver eseguito il codice, uno scenario esistente viene rimosso e un nuovo scenario viene aggiunto al foglio di lavoro.

**Il file di output**

![cose da fare:immagine_alt_testo](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
