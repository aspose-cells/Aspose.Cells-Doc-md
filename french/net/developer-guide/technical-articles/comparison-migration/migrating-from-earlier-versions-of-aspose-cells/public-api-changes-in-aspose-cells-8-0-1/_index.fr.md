---
title: Modifications de l API publique dans Aspose.Cells 8.0.1
type: docs
weight: 20
url: /fr/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Cette page répertorie les modifications de l'API publique introduites dans Aspose.Cells 8.0.1. Elle inclut non seulement les méthodes publiques nouvelles et obsolètes, mais aussi une description de toutes les modifications du comportement en arrière-plan dans Aspose.Cells qui pourraient affecter le code existant. Tout comportement introduit qui pourrait être considéré comme une régression et modifier le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}} 
## **Propriété MemorySetting ajoutée à la classe Cells**
La classe Cells a exposé la propriété MemorySetting qui peut être utilisée pour optimiser l'utilisation de la mémoire pour les données de cellules, et donc diminuer le coût global de la mémoire. L'exemple suivant montre comment écrire des données importantes dans une feuille de calcul de manière optimisée.

**C#**

{{< highlight csharp >}}

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

Les paramètres de mémoire ne fonctionneront pas pour la feuille par défaut créée automatiquement par l'objet Workbook. Pour modifier les paramètres de mémoire des feuilles existantes, veuillez appliquer manuellement le paramètre de mémoire avant d'effectuer toute manipulation des données.

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Optimiser la mémoire lors du travail avec de grands ensembles de données](/cells/fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
