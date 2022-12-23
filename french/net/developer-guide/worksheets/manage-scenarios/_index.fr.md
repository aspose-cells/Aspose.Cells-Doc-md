---
title: Créer, manipuler ou supprimer des scénarios des feuilles de travail
linktitle: Gérer les scénarios
type: docs
weight: 190
url: /fr/net/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un « et si ? modèle qui comprend des cellules d'entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul de sorte qu'elle contienne au moins une formule qui dépend des cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios d'une feuille de calcul dans un classeur via les API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit quelques classes utiles, par exemple,[**ScénarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scénario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScénarioInputCellCollectionScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) , et[**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) Des classes. Il fournit également la[**Feuille de travail. Scénarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)la propriété. L'exemple de code ci-dessous ouvre un fichier Excel XLSX qui contient certains scénarios et supprime un scénario existant. Il ajoute également un nouveau scénario à la feuille de calcul avant d'enregistrer le fichier Excel. L'exemple utilise un fichier modèle très simple qui contient un scénario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
