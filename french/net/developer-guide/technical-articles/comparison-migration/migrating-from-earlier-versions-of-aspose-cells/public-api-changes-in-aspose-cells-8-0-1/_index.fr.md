---
title: Public API Changements dans Aspose.Cells 8.0.1
type: docs
weight: 20
url: /fr/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Cette page répertorie les modifications API publiques qui ont été introduites dans Aspose.Cells 8.0.1. Il comprend non seulement des méthodes publiques nouvelles et obsolètes, mais également une description de tout changement dans le comportement en arrière-plan de Aspose.Cells susceptible d'affecter le code existant. Tout comportement introduit qui pourrait être considéré comme une régression et qui modifie un comportement existant est particulièrement important et est documenté ici.

{{% /alert %}} 
## **Propriété MemorySetting ajoutée à la classe Cells**
La classe Cells a exposé la propriété MemorySetting qui peut être utilisée pour optimiser l'utilisation de la mémoire pour les données des cellules, et donc réduire le coût global de la mémoire. L'exemple suivant montre comment écrire des données volumineuses dans une feuille de calcul en mode optimisé.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

Les paramètres de mémoire ne fonctionneront pas pour la feuille par défaut créée automatiquement par l'objet Workbook. Afin de modifier les paramètres de mémoire des feuilles existantes, veuillez appliquer le paramètre de mémoire manuellement avant d'effectuer toute manipulation de données.

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Optimiser la mémoire tout en travaillant avec de grands ensembles de données](/cells/fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
