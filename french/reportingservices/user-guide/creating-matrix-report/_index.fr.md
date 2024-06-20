---
title: Création de rapport matriciel
type: docs
weight: 10
url: /fr/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services vous permet de concevoir une matrice dans Microsoft Excel. 

{{% /alert %}} 
### **Modèle de matrice**
Dans un modèle de rapport Aspose.Cells, une matrice est composée des coins, des groupes de lignes, des groupes de colonnes et des portions de données. Une matrice d'exemple est présentée ci-dessous.

**Une matrice d'exemple** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Coin de la matrice**: situé dans le coin supérieur gauche, ou dans le coin supérieur droit pour les mises en page de droite à gauche (RTL). Cette zone est automatiquement créée lorsque vous ajoutez à la région de données de la matrice à la fois des groupes de lignes et des groupes de colonnes. Dans cette zone, vous pouvez fusionner des cellules avec un élément de rapport de zone de texte intégré.
- **Zone des groupes de colonnes de la matrice**: située dans le coin supérieur droit (coin supérieur gauche pour la mise en page RTL). Cette zone est automatiquement créée lorsque vous ajoutez un groupe de colonnes. Les cellules de cette zone représentent les membres de la hiérarchie des groupes de colonnes et affichent les valeurs d'instances des groupes de colonnes. Dans la figure, les cellules qui affichent OrderYear sont un groupe de colonnes imbriqué, et la cellule qui affiche OrderQtr est un groupe de colonnes adjacent.
- **Zone des groupes de lignes de la matrice**: située dans le coin inférieur gauche (coin inférieur droit pour la mise en page RTL). Cette zone est automatiquement créée lorsque vous ajoutez un groupe de lignes. Les cellules de cette zone représentent les membres de la hiérarchie des groupes de lignes et affichent les valeurs d'instances des groupes de lignes. Dans la figure, ces cellules sont des groupes de lignes imbriqués.
- **Zone de données de la matrice**: située dans le coin inférieur droit (coin inférieur gauche pour la mise en page RTL). Les données de la matrice affichent les données détaillées et regroupées. Dans cet exemple, seules des données agrégées sont utilisées. Par défaut, les cellules dans une ligne ou une colonne de groupe qui contiennent des expressions simples ne contenant pas une fonction d'agrégation, évaluent la première valeur dans le groupe. Dans la figure, les cellules affichent les totaux agrégés pour les totaux par ligne de toutes les commandes de vente.
#### **Création d'un modèle de matrice**
Avant de créer un rapport matriciel, créez les sources de données, les ensembles de données et les paramètres de rapport (facultatif). (Suivez les instructions dans [Sources de données et requêtes](/cells/fr/reportingservices/data-sources-and-queries/) si vous avez besoin d'aide.) Dans l'exemple, nous utilisons la base de données d'exemple AdventureWorks livrée avec SQL Server Reporting Services 2008.

Pour créer une nouvelle matrice :

1. Ouvrez Microsoft Excel.
1. Cliquez sur **Ouvrir le rapport** pour ouvrir un fichier de rapport RDL qui contient les sources de données, les ensembles de données et les paramètres de rapport créés à l'avance.
   Une fois que le fichier a été ouvert avec succès, toutes ses informations sont disponibles pour utilisation, par exemple, ses ensembles de données sont répertoriés dans la liste **Ensemble de données**.
1. Ouvrez une feuille de calcul Microsoft Excel et sélectionnez un ensemble de données. 

![todo:image_alt_text](creating-matrix-report_2.png)




1. Définissez les groupes de lignes et les groupes de colonnes via **Définir le groupe**. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Fusionnez les cellules pour définir le coin de la matrice.

![todo:image_alt_text](creating-matrix-report_4.png)




1. Définissez le coin de la matrice en insérant une formule. 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. Cliquez sur **Définir l'attribut** pour définir l'attribut de la matrice. 

![todo:image_alt_text](creating-matrix-report_7.png)



Il se compose de nom, plage, groupe et ordre.

1. Cliquer sur modifier attribut vérifie et modifie tous les attributs de matrice de la feuille de calcul actuelle.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Enregistrer, publier et examiner le rapport.
