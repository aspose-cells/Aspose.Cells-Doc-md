---
title: Comment créer un diagramme de Gantt
linktitle: Comment créer un diagramme de Gantt
type: docs
weight: 72
url: /fr/net/how-to-create-gantt-chart/
description: Comment créer un diagramme de Gantt dans Aspose.Cells.
keywords: Créer/insérer un diagramme de Gantt dans Excel avec Aspose
---
## Qu'est-ce qu'un diagramme de Gantt

Un diagramme de Gantt vous aide à planifier les tâches de votre projet, puis vous aide à suivre votre progression.

## Ajouter un diagramme de Gantt dans Excel

Besoin d'afficher l'état d'un calendrier de projet simple avec un diagramme de Gantt ? Bien qu'Excel n'ait pas de type de diagramme de Gantt prédéfini, vous pouvez en simuler un en personnalisant un graphique à barres empilées pour montrer les dates de début et de fin des tâches, comme ceci :

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## Comment créer

- Sélectionnez les données que vous voulez représenter sur le graphique. Dans notre exemple, ce sont les cellules B1 à B7, puis insérez un **graphique à barres empilées**.

![todo:image_alt_text](1.png)

- Sélectionnez le graphique, **Sélectionner des données**->**Ajouter**, définissez le **nom de la série** et les **valeurs de la série** comme suit

![todo:image_alt_text](2.png)

- Sélectionnez le graphique, Éditez les **Libellés de l'axe horizontal (catégorie)**

![todo:image_alt_text](3.png)

- **Formater l'axe** des ordonnées, sélectionnez **Catégories dans l'ordre inverse**
- Sélectionnez la **série bleue** et définissez le **Remplissage->Aucun remplissage**
- **Formater l’axe** des X, définissez le **Minimum et Maximum** (1/5/2019:43470, 1/30/2019:43494)

![todo:image_alt_text](4.png)

- **Ajoutez des étiquettes de données** pour le graphique
Maintenant, vous obtenez un diagramme de Gantt.

## Ajouter un diagramme de Gantt dans Aspose.Cells

Le code d’exemple suivant crée un diagramme de Gantt en ouvrant un [fichier d’exemple](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

Vous obtiendrez un fichier similaire au [fichier résultant](result.xlsx). Dans le fichier, vous verrez ce qui suit :

![todo:image_alt_text](5.png)

