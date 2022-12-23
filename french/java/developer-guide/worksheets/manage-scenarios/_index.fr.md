---
title: Créer, manipuler ou supprimer des scénarios des feuilles de travail
linktitle: Gérer les scénarios
type: docs
weight: 120
url: /fr/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un modèle de simulation nommé qui inclut des cellules d'entrée variables liées entre elles par une ou plusieurs formules. Avant de créer un scénario, concevez une feuille de calcul de sorte qu'elle contienne au moins une formule qui dépend de cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios d'une feuille de calcul à l'aide des API Aspose.Cells.

{{% /alert %}}

 Aspose.Cells fournit quelques classes utiles, par exemple[**ScénarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scénario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScénarioInputCellCollectionScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) et[**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell) . Il fournit également la[**Feuille de travail. Scénarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)la propriété. L'exemple de code ci-dessous ouvre un fichier Excel XLSX (qui contient certains scénarios) et supprime un scénario existant de la feuille de calcul. Il ajoute également un nouveau scénario avant d'enregistrer le fichier Excel. Il utilise un fichier modèle très simple qui contient un scénario.

Après l'exécution du code, un scénario existant est supprimé et un nouveau scénario est ajouté à la feuille de calcul.

**Le fichier de sortie**

![tâche : image_autre_texte](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
