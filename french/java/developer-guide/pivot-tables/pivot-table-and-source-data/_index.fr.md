---
title: Tableau croisé dynamique et données sources
type: docs
weight: 110
url: /fr/java/pivot-table-and-source-data/
---

## **Données source du tableau croisé dynamique**
Il arrive parfois que vous souhaitiez créer des rapports Microsoft Excel avec des tableaux croisés dynamiques qui extraient des données de différentes sources de données (telles qu'une base de données) qui ne sont pas connues au moment de la conception. Cet article propose une approche pour changer dynamiquement la source de données d'un tableau croisé dynamique.
## **Modification des données source d'un tableau croisé dynamique**
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

L'exécution du code d'exemple ci-dessous modifie les données sources du tableau croisé dynamique et le tableau croisé dynamique ressemblera à celui ci-dessous.

**Tableau Croisé Dynamique modifié dynamiquement** 

![todo:image_alt_text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
{{< app/cells/assistant language="java" >}}
