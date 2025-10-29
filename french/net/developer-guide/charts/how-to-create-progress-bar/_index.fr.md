---
title: Comment créer une barre de progression
description: Apprenez comment créer une barre de progression avec Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, Barre de progression, créer une barre de progression, ajouter une barre de progression, insérer une barre de progression.
type: docs
weight: 73
url: /fr/net/how-to-create-a-progress-bar/
---

## **Scénarios d'utilisation possibles**
La raison principale de créer une barre de progression dans Excel est de transformer des chiffres bruts en une métrique visuelle compréhensible instantanément, simplifiant la compréhension de données complexes en un coup d'œil.

1. Clarté Visuelle Accrue et Aperçu Instantané : Un tableau avec des chiffres comme "75%", "8/10" ou "15000/20000" nécessite un effort cognitif pour interpréter. Une barre de progression permet à quiconque, d'un cadre supérieur à un membre de l'équipe, de comprendre le statut, la performance ou le niveau d'achèvement instantanément sans lire et traiter les chiffres.

2. Identification Rapide du Statut et des Tendances : Notre cerveau est câblé pour traiter l'information visuelle comme la longueur et la couleur plus rapidement que le texte. Vous pouvez rapidement voir : Qu'est-ce qui est en bonne voie ? (Longues barres vertes), Qu'est-ce qui est en retard ? (Courtes barres rouges) et Qu'est-ce qui est presque terminé ? (Barres presque pleines). Cela permet une prise de décision et une priorisation plus rapides.

3. Amélioration des Tableaux de Bord et Rapports : Les barres de progression sont une pierre angulaire des tableaux de bord efficaces. Elles rendent les rapports plus attractifs, professionnels et faciles à présenter. Un tableau de bord avec des barres de progression pour les indicateurs clés de performance (KPI) est bien plus efficace qu'une feuille pleine de chiffres.

4. Motivation et Suivi de la Performance : Pour les équipes de vente, les suivis de projet ou les objectifs personnels, voir une représentation visuelle de la progression peut être très motivant. Cela offre un sentiment clair et satisfaisant d'accomplissement lorsque la barre se remplit.

5. Communication Efficace : Lors de réunions ou présentations, une barre de progression transmet le message bien plus efficacement que de dire : "Nous sommes à 72,5 % de notre objectif trimestriel." La représentation visuelle fait passer le message, gagnant du temps et évitant les malentendus.


## **Comment créer une barre de progression dans Excel**

Créer une barre de progression dans Excel est un excellent moyen de visualiser l'achèvement d'une tâche, l'avancement d'un projet ou les tendances de données. Voici un guide sur comment en créer une en utilisant différentes méthodes, ainsi que quelques astuces pour la personnalisation.

### **Utilisation du format conditionnel (Barres de données)**
1. Préparez vos données : Ayez au moins une colonne de valeurs représentant l'avancement, de préférence en pourcentage (par exemple, 0,5 pour 50%). Vous pouvez calculer cela avec une formule comme =Valeur_Courante/ but_Valeur.
2. Sélectionnez les cellules : Mettez en surbrillance les cellules contenant vos valeurs en pourcentage.
3. Appliquez des barres de données : Allez dans l'onglet Accueil > Mise en forme conditionnelle > Barres de données. Choisissez soit remplissage dégradé, soit remplissage uni.
4. Personnalisez (optionnel) : Pour plus de contrôle, allez dans Mise en forme conditionnelle > Gérer les règles > Modifier la règle.
5. Définissez les types Min et Max sur Nombre, avec des valeurs 0 et 1, respectivement, pour garantir un affichage précis de 0-100%.
6. Ajustez ici les couleurs et styles de bordure. Pour afficher à la fois le nombre et la barre, modifiez la règle et assurez-vous que "Afficher uniquement la barre" n'est pas coché.

### **Utilisation de la fonction REPT (Barre basée sur du texte)**
1. Entrez la formule : Dans une cellule, utilisez une formule comme =REPT("█", B2*10) & REPT("░", 10 - B2*10), où B2 contient le pourcentage d'avancement. Cet exemple crée une barre de 10 caractères : carrés remplis (█) pour l'achèvement et carrés légers (░) pour les restantes.
2. Ajustez et formatez : Ajoutez un multiplicateur (par exemple, *20 pour une barre de 20 caractères) selon la longueur désirée. Utilisez une police à largeur fixe comme Courier New pour un alignement correct.

### **Utilisation d’un graphique (Pour tableaux de bord)**
1. Structurer les données : Créez un tableau pour calculer les valeurs :
|**Numéro**|**A**|**B**|
| :- | :- | :- |
|1|Avancement|Restant|
|2|=Valeur_Courante/ but_Valeur|=1-A2|
<br>
2. Insérer le graphique : Sélectionnez les données > Onglet Insertion > Graphiques > Graphique à barres empilées en 2D.
3. Formater le graphique : Supprimez le titre du graphique, la légende et les lignes de quadrillage pour un rendu épuré. Clic droit sur la série de données "Restant" > Format de la série de données > Remplissage > Sans remplissage. Clic droit sur la série "Avancement" > Format de la série de données > Ajustez le chevauchement des séries à 100% et la largeur de l’interligne à 0%. Formatez l’axe horizontal : définit les limites > Minimum à 0 et Maximum à 1.

## **Comment créer une barre de progression dans Aspose.Cells**

### **Utilisez la fonction REPT (Barre textuelle) pour créer une barre de progression**
Veuillez voir l'exemple de code suivant. Il crée un nouveau classeur et ajoute quelques données d'exemple. Ensuite, il ajoute la fonction REPT (Barre textuelle) basée sur les données initiales. Enfin, il enregistre le classeur au format xlsx. La capture d'écran suivante montre la mise en forme conditionnelle (Barres de données) créée par Aspose.Cells dans le fichier Excel en sortie.
<br>
<img src="formula.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-Formula.cs" >}}

### **Utilisez la Mise en forme conditionnelle (Barres de données) pour créer une barre de progression**
Veuillez voir l'exemple de code suivant. Il crée un nouveau classeur et ajoute quelques données d'exemple. Ensuite, il ajoute une mise en forme conditionnelle (Barres de données) basée sur les données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format xlsx. La capture d'écran suivante montre la mise en forme conditionnelle (Barres de données) créée par Aspose.Cells dans le fichier Excel en sortie.
<br>
<img src="databar.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-ConditionalFormats.cs" >}}


### **Utilisez le graphique en barres empilées pour créer une barre de progression**
Veuillez voir l'exemple de code suivant. Il charge le [fichier Excel d'exemple](sample.xlsx) contenant quelques données d'exemple. Ensuite, il crée le graphique en barres empilées basé sur les données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format XLSX. La capture d'écran suivante montre la barre de progression créée par Aspose.Cells dans le fichier Excel en sortie.

<br>
<img src="barchart.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Use-BarStacked-Chart.cs" >}}
