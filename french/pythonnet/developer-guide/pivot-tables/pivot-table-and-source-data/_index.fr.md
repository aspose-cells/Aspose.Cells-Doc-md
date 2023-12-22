---
title: Tableau croisé dynamique et données sources
type: docs
weight: 30
url: /fr/python-net/pivot-table-and-source-data/
description: Cet article montre comment modifier les données sources du tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Change Pivot Table's Source Data
---
##  **Données sources du tableau croisé dynamique**

Il peut arriver que vous souhaitiez créer des rapports Excel Microsoft avec des tableaux croisés dynamiques qui prennent des données provenant de différentes sources de données (telles qu'une base de données) qui ne sont pas connues au moment de la conception. Cet article propose une approche pour modifier dynamiquement la source de données d'un tableau croisé dynamique.

###  **Modification des données source d'un tableau croisé dynamique**

1. Création d'un nouveau modèle de concepteur.
 1. Créez un nouveau fichier de modèle de concepteur comme dans la capture d'écran ci-dessous.
 1. Définissez ensuite une plage nommée, *DataSource**, qui fait référence à cette plage de cellules.

      **Création d'un modèle de concepteur et définition d'une plage nommée, DataSource** 

![tâche : image_alt_text](pivot-table-and-source-data_1.png)
   
1. Création d'un tableau croisé dynamique basé sur cette plage nommée.
1. Dans Excel Microsoft, choisissez**Données**, puis **Tableau croisé dynamique** et *Rapport de graphique croisé dynamique**.
 1. Créez un tableau croisé dynamique basé sur la plage nommée créée lors de la première étape.

      **Création d'un tableau croisé dynamique basé sur la plage nommée, DataSource** 

![tâche : image_alt_text](pivot-table-and-source-data_2.png)

   
 1. Faites glisser le champ correspondant vers la ligne et la colonne du tableau croisé dynamique, puis créez le tableau croisé dynamique obtenu comme dans la capture d'écran ci-dessous.

   **Création d'un tableau croisé dynamique basé sur un champ correspondant** 

![tâche : image_alt_text](pivot-table-and-source-data_3.png)

   
1. Cliquez avec le bouton droit sur le tableau croisé dynamique et sélectionnez *Options du tableau**.
 1. Vérifiez**Actualiser à l'ouverture** dans**Options de données** paramètres.

      **Définition des options du tableau croisé dynamique** 

![tâche : image_alt_text](pivot-table-and-source-data_4.png)


Vous pouvez maintenant enregistrer ce fichier en tant que fichier de modèle de concepteur.

1. Remplissage de nouvelles données et modification des données sources d'un tableau croisé dynamique.
 1. Une fois le modèle de concepteur créé, utilisez le code suivant pour modifier les données source du tableau croisé dynamique.

L'exécution de l'exemple de code ci-dessous modifie les données sources du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

