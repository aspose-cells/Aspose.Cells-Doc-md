---
title: Tableau croisé dynamique et données sources
type: docs
weight: 30
url: /fr/net/pivot-table-and-source-data/
---

## **Données source du tableau croisé dynamique**

Il arrive parfois que vous souhaitiez créer des rapports Microsoft Excel avec des tableaux croisés dynamiques prenant des données de différentes sources de données (telles qu'une base de données) qui ne sont pas connues au moment de la conception. Cet article propose une approche pour modifier dynamiquement la source de données d'un tableau croisé dynamique.

### **Modification des données source d'un tableau croisé dynamique**

1. Création d'un nouveau modèle de concepteur.
   1. Créez un nouveau fichier de modèle de concepteur comme sur la capture d'écran ci-dessous.
   1. Ensuite, définissez une plage nommée, **DataSource**, qui fait référence à cette plage de cellules.

      **Création d'un modèle de concepteur et définition d'une plage nommée, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Création d'un tableau croisé dynamique basé sur cette plage nommée.
   1. Dans Microsoft Excel, choisissez **Données**, puis **Tableau croisé dynamique** et **Rapport de tableau croisé dynamique**.
   1. Créez un tableau croisé dynamique basé sur la plage nommée créée à l'étape précédente.

      **Création d'un tableau croisé dynamique basé sur la plage nommée, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Faites glisser le champ correspondant pour le placer dans les colonnes et les lignes du tableau croisé dynamique, puis créez le tableau croisé dynamique résultant comme sur la capture d'écran ci-dessous.

   **Création d'un tableau croisé dynamique basé sur un champ correspondant** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Cliquez avec le bouton droit sur le tableau croisé dynamique et sélectionnez **Options de tableau**.
   1. Cochez **Actualiser à l'ouverture** dans les paramètres **Options de données**.

      **Configuration des options de tableau croisé dynamique** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Maintenant, vous pouvez enregistrer ce fichier en tant que fichier de modèle de concepteur.

1. Remplir de nouvelles données et changer les données source d'un tableau croisé dynamique.
   1. Une fois que le modèle de concepteur est créé, utilisez le code suivant pour changer les données source du tableau croisé dynamique.

L'exécution du code d'exemple ci-dessous modifie les données source du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}

