---
title: Comment créer un diagramme de Gantt
linktitle: Comment créer un diagramme de Gantt
type: docs
weight: 72
url: /fr/net/how-to-create-gantt-chart/
description: Apprenez à créer un diagramme de Gantt avec l API Aspose.Cells for .NET.
keywords: C# crée un diagramme de Gantt, ajoute un diagramme de Gantt, insère un diagramme de Gantt
---

## **Qu'est-ce qu'un diagramme de Gantt**

Un diagramme de Gantt est un type de diagramme à barres qui illustre un planning de projet. Il montre les dates de début et de fin des différents éléments d'un projet. Chaque tâche ou activité est représentée par une barre, sa longueur correspondant à sa durée. Les diagrammes de Gantt indiquent également les dépendances entre les tâches, permettant aux chefs de projet de visualiser la séquence dans laquelle les tâches doivent être accomplies. Ils sont largement utilisés dans la gestion de projet pour planifier, programmer et suivre efficacement les projets.

## **Comment créer un diagramme de Gantt dans Excel**

Vous pouvez créer un diagramme de Gantt dans Excel en suivant ces étapes :
1. Ajouter des données pour le diagramme de Gantt. 
<br>
<img src="00.png" width=50% />
1. Sélectionnez les données et allez à Insertion --> Graphiques --> Insérer un diagramme en colonnes ou à barres --> Diagramme à barres empilées. Dans notre exemple, il s'agit de B1:B7, puis insérez le diagramme à barres empilées.
<br>
<img src="1.png" width=50% />

1. Sélectionnez le diagramme, **Sélection des données**->**Ajouter**, définissez le **Nom de série** et les **Valeurs de série** comme suit.
<br>
<img src="2.png" width=50% />

1. Sélectionnez le diagramme, éditez les **Libellés d'axe horizontal (Catégorie)**.
<br>
<img src="3.png" width=50% />

1. **Formater l'axe** des Y, sélectionnez **Catégories dans l'ordre inverse**.
1. Sélectionnez la **Série bleue** et définissez le **Remplissage->Aucun remplissage**.
1. **Formater l'axe** des X, définissez les **Minimum et Maximum**(1/5/2019:43470,1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Ajoutez des étiquettes de données** pour le diagramme, maintenant vous obtiendrez un diagramme de Gantt.
<br>
<img src="0.png" width=50% />


## **Comment ajouter un diagramme de Gantt dans Aspose.Cells**
Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](sample.xlsx) qui contient des données d'exemple. Ensuite, il crée le diagramme à barres empilées basé sur les données initiales et défini les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](result.xlsx). La capture d'écran suivante montre le diagramme de Gantt créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="5.png" width=60% />

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

