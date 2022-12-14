---
title: Tableau croisé dynamique et données source
type: docs
weight: 30
url: /fr/net/pivot-table-and-source-data/
---
## **Données source du tableau croisé dynamique**

Il arrive parfois que vous souhaitiez créer des rapports Excel Microsoft avec des tableaux croisés dynamiques qui prennent des données de différentes sources de données (telles qu'une base de données) qui ne sont pas connues au moment de la conception. Cet article fournit une approche pour modifier dynamiquement la source de données d'un tableau croisé dynamique.

### **Modification des données source d'un tableau croisé dynamique**

1. Création d'un nouveau modèle de concepteur.
1. Créez un nouveau fichier de modèle de concepteur comme dans la capture d'écran ci-dessous.
 1. Définissez ensuite une plage nommée,**La source de données**, qui fait référence à cette plage de cellules.

      **Création d'un modèle de concepteur et définition d'une plage nommée, DataSource** 

![tâche : image_autre_texte](pivot-table-and-source-data_1.png)
   
1. Création d'un tableau croisé dynamique basé sur cette plage nommée.
 1. Dans Microsoft Excel, choisissez**Données** , alors**Tableau croisé dynamique** et**Rapport de graphique croisé dynamique**.
 1. Créez un tableau croisé dynamique basé sur la plage nommée créée à la première étape.

      **Création d'un tableau croisé dynamique basé sur la plage nommée, DataSource** 

![tâche : image_autre_texte](pivot-table-and-source-data_2.png)

   
 1. Faites glisser le champ correspondant vers la ligne et la colonne du tableau croisé dynamique, puis créez le tableau croisé dynamique résultant comme dans la capture d'écran ci-dessous.

   **Créer un tableau croisé dynamique basé sur un champ correspondant** 

![tâche : image_autre_texte](pivot-table-and-source-data_3.png)

   
1.  Cliquez avec le bouton droit sur le tableau croisé dynamique et sélectionnez**Options de tableau**.
 1. Vérifier**Actualiser à l'ouverture** dans**Options de données** réglages.

      **Paramétrer les options du tableau croisé dynamique** 

![tâche : image_autre_texte](pivot-table-and-source-data_4.png)


Maintenant, vous pouvez enregistrer ce fichier en tant que fichier de modèle de concepteur.

1. Remplir de nouvelles données et modifier les données source d'un tableau croisé dynamique.
1. Une fois le modèle de concepteur créé, utilisez le code suivant pour modifier les données source du tableau croisé dynamique.

L'exécution de l'exemple de code ci-dessous modifie les données source du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}

