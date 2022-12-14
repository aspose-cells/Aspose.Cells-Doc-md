---
title: Mettre en forme un objet de liste - Tableau
type: docs
weight: 50
url: /fr/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

Pour gérer et analyser un groupe de données liées, il est possible de transformer une plage de cellules en un objet liste (également appelé tableau Excel). Un tableau est une série de lignes et de colonnes qui contiennent des données associées gérées indépendamment des données des autres lignes et colonnes. Par défaut, chaque colonne du tableau a un filtrage activé dans la ligne d'en-tête afin que vous puissiez filtrer ou trier rapidement les données d'objet de votre liste. Vous pouvez ajouter une ligne de total (une ligne spéciale dans une liste qui fournit une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet de liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de ligne de total. Aspose.Cells fournit des options pour créer et gérer des listes (ou des tables).

{{% /alert %}}

## **Formater un objet de liste**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Créer un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) dans une feuille de calcul, utilisez[**ListeObjets**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) propriété de collection de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. Chaque[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) est en fait un objet de la[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, qui fournit en outre la méthode add pour ajouter un objet List et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) est créé dans la feuille de calcul par Aspose.Cells. Utilisez des attributs (par exemple,[**Type de style de table**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType) ) de la[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)class pour formater la table selon vos besoins.

 L'exemple ci-dessous ajoute des exemples de données à une feuille de calcul, ajoute un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) et lui applique les styles par défaut.[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)les styles sont pris en charge par Microsoft Excel 2007/2010.

La sortie suivante est générée lorsque le code est exécuté.

**Un tableau formaté est créé dans la feuille de calcul** 

![tâche : image_autre_texte](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
