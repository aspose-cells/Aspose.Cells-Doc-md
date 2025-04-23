---
title: Creare, manipolare o rimuovere scenari dai fogli di lavoro
linktitle: Gestire gli scenari
type: docs
weight: 120
url: /it/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello ipotetico che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progetta un foglio di lavoro in modo che contenga almeno una formula che dipende dalle celle in cui possono essere inseriti valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro utilizzando le API di Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce alcune classi utili, ad esempio [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) e [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). Fornisce anche la proprietà [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios). Il codice di esempio seguente apre un file Excel XLSX (che contiene alcuni scenari) e rimuove uno scenario esistente dal foglio di lavoro. Aggiunge inoltre un nuovo scenario prima di salvare il file Excel. Utilizza un file di modello molto semplice che contiene uno scenario.

Dopo aver eseguito il codice, viene rimosso uno scenario esistente e ne viene aggiunto uno nuovo al foglio di lavoro.

**Il file di output

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
