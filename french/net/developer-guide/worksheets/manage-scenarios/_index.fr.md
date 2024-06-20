---
title: Créer, manipuler ou supprimer des scénarios des feuilles de calcul
linktitle: Gérer des scénarios
type: docs
weight: 190
url: /fr/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Dans cet article, vous apprendrez comment créer, manipuler ou supprimer des scénarios des feuilles de calcul Excel de manière programmatique en utilisant la bibliothèque C# avec l API .NET.
keywords: Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un modèle nommé qu est ce que si? qui inclut des cellules d entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul de sorte qu elle contienne au moins une formule qui dépend de cellules dans lesquelles différentes valeurs peuvent être insérées. L exemple suivant montre comment créer et supprimer des scénarios à partir d une feuille de calcul dans un classeur via les API Aspose.Cells.
---

{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un modèle nommé de 'et si ?' qui inclut des cellules d'entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul de manière à ce qu'elle contienne au moins une formule dépendant de cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios à partir d'une feuille de calcul dans un classeur via les API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit quelques classes utiles, par exemple les classes [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection), et [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell). Il fournit également la propriété [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios). Le code d'exemple ci-dessous ouvre un fichier Excel XLSX contenant des scénarios et supprime un scénario existant. Il ajoute également un nouveau scénario à la feuille de calcul avant d'enregistrer le fichier Excel. L'exemple utilise un fichier modèle très simple contenant un scénario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
