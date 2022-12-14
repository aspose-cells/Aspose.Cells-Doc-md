---
title: Comment réparer l'erreur java.lang.OutOfMemoryError lors du chargement de feuilles de calcul volumineuses
type: docs
weight: 20
url: /fr/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Il y a de bonnes chances que le constructeur Workbook lance java.lang.OutOfMemoryError lors du chargement de feuilles de calcul volumineuses. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul dans la mémoire. Par conséquent, la feuille de calcul doit être chargée tout en activant le[Préférences de mémoire](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Comment réparer le java.lang.OutOfMemoryError lors du chargement d'une grande feuille de calcul**
Les API Aspose.Cells fournissent des préférences de mémoire pour optimiser la consommation de mémoire lors du chargement et du traitement des feuilles de calcul. Ces options sont également utiles pour charger efficacement les grandes feuilles de calcul contenant d'énormes ensembles de données dans l'objet Workbook, comme illustré ci-dessous.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
