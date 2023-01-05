---
title: Public API Changements dans Aspose.Cells 8.0.1
type: docs
weight: 30
url: /fr/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Cette page répertorie les modifications API publiques qui ont été introduites dans Aspose.Cells 8.0.1. Il comprend non seulement des méthodes publiques nouvelles et obsolètes, mais également une description de tout changement dans le comportement en arrière-plan de Aspose.Cells susceptible d'affecter le code existant. Tout comportement introduit qui pourrait être considéré comme une régression et qui modifie un comportement existant est particulièrement important et est documenté ici.

{{% /alert %}} 
## **Propriété MemorySetting ajoutée à la classe Cells**
La classe Cells a exposé les méthodes setMemorySetting et getMemorySetting qui peuvent être utilisées pour optimiser l'utilisation de la mémoire pour les données des cellules, et donc réduire le coût global de la mémoire. L'exemple suivant montre comment écrire des données volumineuses dans une feuille de calcul en mode optimisé.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

 Les paramètres de mémoire ne fonctionneront pas pour la feuille par défaut créée automatiquement par le classeur. Afin de modifier les paramètres de mémoire des feuilles existantes, veuillez appliquer les paramètres de mémoire manuellement avant d'effectuer toute manipulation de données.

{{% /alert %}} {{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Optimiser la mémoire tout en travaillant avec de grands ensembles de données](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
