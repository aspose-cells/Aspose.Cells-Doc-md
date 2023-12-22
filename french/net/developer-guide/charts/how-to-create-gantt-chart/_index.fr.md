---
title: Comment créer un diagramme de Gantt
linktitle: Comment créer un diagramme de Gantt
type: docs
weight: 72
url: /fr/net/how-to-create-gantt-chart/
description: Comment créer un diagramme de Gantt dans Aspose.Cells.
keywords: create/insert Gantt Chart Excel Aspose
---
##  Qu'est-ce qu'un diagramme de Gantt

Un diagramme de Gantt vous aide à planifier les tâches de votre projet, puis à suivre votre progression.

##  Ajouter un diagramme de Gantt dans Excel

Besoin d'afficher l'état d'un calendrier de projet simple avec un diagramme de Gantt ? Bien qu'Excel ne dispose pas de type de diagramme de Gantt prédéfini, vous pouvez en simuler un en personnalisant un diagramme à barres empilées pour afficher les dates de début et de fin des tâches, comme ceci :

![tâche : image_alt_text](00.png)

![tâche : image_alt_text](0.png)

##  Comment créer

-  Sélectionnez les données que vous souhaitez représenter graphiquement. Dans notre exemple, c'est B1:B7, puis Insérer**Barre empilée** graphique.

![tâche : image_alt_text](1.png)

- Sélectionnez le graphique,**Sélectionnez les données**->**Ajouter**, définir le **Nom de la série** et**Valeurs de série** comme suit

![tâche : image_alt_text](2.png)

-  Sélectionnez le graphique, modifiez le**Étiquettes d'axe horizontal (catégorie)**

![tâche : image_alt_text](3.png)

- **Formater l'axe** l'axe Y, sélectionnez**Catégories dans l'ordre inverse**
-  Sélectionnez le**Série bleue** et réglez le**Remplir -> NON Remplir**
- **Formater l'axe** l'axe X, définissez le *Mininum et le Maxinum** (1/5/2019:43470,1/30/2019:43494)

![tâche : image_alt_text](4.png)

- **Ajouter des fichiers de données** pour le graphique
Vous obtenez maintenant un diagramme de Gantt.

## Ajouter un diagramme de Gantt dans Aspose.Cells

 L'exemple de code suivant crée un diagramme de Gantt en ouvrant un[exemple de fichier](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

 Vous obtiendrez un fichier similaire à[fichier de résultat](result.xlsx).Dans le fichier, vous verrez ce qui suit :

![tâche : image_alt_text](5.png)

