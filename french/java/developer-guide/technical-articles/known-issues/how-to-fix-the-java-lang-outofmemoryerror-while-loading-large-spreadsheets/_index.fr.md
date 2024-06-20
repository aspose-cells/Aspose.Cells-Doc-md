---
title: Comment résoudre l erreur java.lang.OutOfMemoryError lors du chargement de grandes feuilles de calcul
type: docs
weight: 20
url: /fr/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Il y a de fortes chances que le constructeur Workbook puisse déclencher java.lang.OutOfMemoryError lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul en mémoire, donc la feuille de calcul doit être chargée tout en activant les [Préférences de mémoire](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Comment résoudre l'erreur java.lang.OutOfMemoryError lors du chargement d'une grande feuille de calcul**
Les API Aspose.Cells fournissent des Préférences de Mémoire pour optimiser la consommation de mémoire lors du chargement et du traitement de feuilles de calcul. Ces options sont également utiles pour charger efficacement de grandes feuilles de calcul contenant de grands ensembles de données dans l'objet Workbook, comme le montre l'exemple ci-dessous. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
