---
title: Comment créer un graphique de Gantt
linktitle: Comment créer un graphique de Gantt
type: docs
weight: 72
url: /fr/python-net/how-to-create-gantt-chart/
description: Apprenez comment créer un graphique de Gantt avec Aspose.Cells pour Python via .NET API.
keywords: Python créer un graphique de Gantt, ajouter un graphique de Gantt, insérer un graphique de Gantt
---

## **Qu’est-ce qu’un graphique de Gantt**

Un graphique de Gantt est un type de diagramme à barres qui illustre un calendrier de projet. Il montre les dates de début et de fin des différents éléments d’un projet. Chaque tâche ou activité est représentée par une barre, dont la longueur correspond à sa durée. Les graphiques de Gantt indiquent également les dépendances entre les tâches, permettant aux gestionnaires de visualiser la séquence dans laquelle les tâches doivent être accomplies. Ils sont largement utilisés en gestion de projet pour planifier, programmer et suivre efficacement les projets.

## **Comment créer un graphique de Gantt dans Excel**

Vous pouvez créer un graphique de Gantt dans Excel en suivant ces étapes :
1. Ajoutez des données pour le graphique de Gantt. 
<br>
<img src="00.png" width=50% />
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un graphique en colonnes ou barres --> Graphique à barres empilées. Dans notre exemple, c’est B1:B7, puis insérez un **graphique à barres empilées**.
<br>
<img src="1.png" width=50% />

1. Sélectionnez le graphique,**Sélectionner les données**->**Ajouter**, définissez le **Nom de la série** et les **valeurs de la série** comme suit.
<br>
<img src="2.png" width=50% />

1. Sélectionnez le graphique, modifiez les **Labels de l’axe horizontal (catégorie)**.
<br>
<img src="3.png" width=50% />

1. **Mettre en forme l’axe** Y, sélectionnez **Catégories en ordre inverse**.
1. Sélectionnez la **Série bleue** et définissez la **Remplissage->Aucun remplissage**.
1. **Formatage de l’axe** de l’axe X, définissez le **Minimum** et le **Maximum** (1/5/2019 : 43470, 1/30/2019 : 43494).
<br>
<img src="4.png" width=50% />

1. **Ajouter des étiquettes de données** pour le graphique, vous obtiendrez maintenant un graphique de Gantt.
<br>
<img src="0.png" width=50% />


## **Comment ajouter un graphique de Gantt dans Aspose.Cells pour la bibliothèque Excel Python**
Veuillez voir l'exemple de code ci-dessous. Il charge le [fichier Excel d’exemple](sample.xlsx) qui contient des données d'exemple. Il crée ensuite le graphique à barres empilées basé sur les données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format [ XLSX de sortie](result.xlsx). La capture d'écran suivante montre le graphique de Gantt créé par Aspose.Cells pour Python via .NET dans le fichier Excel de sortie.
<br>
<img src="5.png" width=60% />

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-gantt-chart.py" >}}

{{< app/cells/assistant language="python-net" >}}
