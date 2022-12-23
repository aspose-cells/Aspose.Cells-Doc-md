---
title: Création d'un rapport matriciel
type: docs
weight: 10
url: /fr/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services vous permet de concevoir une matrice dans Microsoft Excel.

{{% /alert %}} 
### **Modèle de matrice**
Dans un modèle de rapport Aspose.Cells, une matrice se compose d'un coin, de groupes de lignes, de groupes de colonnes et de portions de données. Un exemple de matrice est présenté ci-dessous.

**Un exemple de matrice** 

![tâche : image_autre_texte](creating-matrix-report_1.png)

- **Coin matrice**: situé dans le coin supérieur gauche ou dans le coin supérieur droit pour les mises en page de droite à gauche (RTL). Cette zone est automatiquement créée lorsque vous ajoutez des groupes de lignes et des groupes de colonnes à une région de données de matrice. Dans cette zone, vous pouvez fusionner des éléments de rapport de zone de texte incorporés dans des cellules.
- **Zone des groupes de colonnes de la matrice**situé dans le coin supérieur droit (coin supérieur gauche pour la mise en page RTL). Cette zone est automatiquement créée lorsque vous ajoutez un groupe de colonnes. Les cellules de cette zone représentent les membres de la hiérarchie des groupes de colonnes et affichent les valeurs d'instance du groupe de colonnes. Dans la figure, les cellules qui affichent OrderYear sont un groupe de colonnes imbriquées et la cellule qui affiche OrderQtr est un groupe de colonnes adjacentes.
- **Zone des groupes de lignes de la matrice**: situé dans le coin inférieur gauche (en bas à droite pour la mise en page RTL). Cette zone est créée automatiquement lorsque vous ajoutez un groupe de lignes. Les cellules de cette zone représentent les membres de la hiérarchie des groupes de lignes et affichent les valeurs d'instance de groupe de lignes. Dans la figure, ces cellules sont des groupes de lignes imbriqués.
- **Zone de données matricielles**situé dans le coin inférieur droit (en bas à gauche pour la mise en page RTL). Les données matricielles affichent des données détaillées et groupées. Dans cet exemple, seules les données agrégées sont utilisées. Par défaut, les cellules d'une ligne ou d'une colonne de groupe qui contiennent des expressions simples qui n'incluent pas de fonction d'agrégation sont évaluées à la première valeur du groupe. Dans la figure, les cellules affichent les totaux agrégés pour les totaux de ligne pour toutes les commandes client.
#### **Création d'un modèle de matrice**
 Avant de créer un rapport matriciel, créez les sources de données, les jeux de données et les paramètres de rapport (facultatif). (Suivez les instructions dans[Sources de données et requêtes](/cells/fr/reportingservices/data-sources-and-queries/) si vous avez besoin d'aide.) Dans l'exemple, nous utilisons l'exemple de base de données AdventureWorks fourni avec SQL Server Reporting Services 2008.

Pour créer une nouvelle matrice :

1. Ouvrez Microsoft Excel.
1.  Cliquez sur**Ouvrir le rapport** pour ouvrir un fichier de rapport RDL contenant les sources de données, les ensembles de données et les paramètres de rapport créés à l'avance.
Une fois que le fichier a été ouvert avec succès, toutes ses informations sont disponibles, par exemple, ses ensembles de données sont répertoriés dans le**Base de données** liste.
1.  Ouvrez une feuille de calcul Excel Microsoft et sélectionnez un ensemble de données.

![tâche : image_autre_texte](creating-matrix-report_2.png)




1.  Définissez des groupes de lignes et des groupes de colonnes via**Définir le groupe**. 

![tâche : image_autre_texte](creating-matrix-report_3.png)




1. Fusionnez les cellules pour définir le coin de la matrice.

![tâche : image_autre_texte](creating-matrix-report_4.png)




1.  Définissez le coin de la matrice en insérant une formule.

![tâche : image_autre_texte](creating-matrix-report_5.png)




![tâche : image_autre_texte](creating-matrix-report_6.png)




1.  Cliquez sur**Définir l'attribut** pour définir l'attribut de matrice.

![tâche : image_autre_texte](creating-matrix-report_7.png)



Il se compose du nom, de la plage, du groupe et de l'ordre.

1. Cliquer sur Modifier l'attribut vérifie et modifie tous les attributs de matrice de la feuille de calcul en cours.

![tâche : image_autre_texte](creating-matrix-report_8.png)




1. Enregistrez, publiez et examinez le rapport.
