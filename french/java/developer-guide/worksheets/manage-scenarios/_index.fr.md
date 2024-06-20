---
title: Créer, manipuler ou supprimer des scénarios des feuilles de calcul
linktitle: Gérer des scénarios
type: docs
weight: 120
url: /fr/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de créer, manipuler ou supprimer des scénarios dans les feuilles de calcul. Un scénario est un modèle nommé de simulation qui comprend des cellules d'entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez une feuille de calcul de telle sorte qu'elle contienne au moins une formule dépendant de cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios à partir d'une feuille de calcul en utilisant les API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit quelques classes utiles, par exemple [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) et [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). Elle fournit également la propriété [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios). Le code d'exemple ci-dessous ouvre un fichier Excel XLSX (qui contient quelques scénarios) et supprime un scénario existant de la feuille de calcul. Il ajoute également un nouveau scénario avant d'enregistrer le fichier Excel. Il utilise un fichier de modèle très simple contenant un scénario.

Après l'exécution du code, un scénario existant est supprimé et un nouveau scénario est ajouté à la feuille de calcul.

**Le fichier de sortie**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
