---
title: Formater un objet Liste  Tableau
type: docs
weight: 50
url: /fr/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

Pour gérer et analyser un groupe de données connexes, il est possible de transformer une plage de cellules en objet liste (également connu sous le nom de tableau Excel). Un tableau est une série de lignes et de colonnes contenant des données connexes gérées indépendamment des données dans les autres lignes et colonnes. Par défaut, chaque colonne du tableau a la fonction de filtre activée dans la ligne d'en-tête afin que vous puissiez filtrer ou trier rapidement vos données d'objet liste. Vous pouvez ajouter une ligne totale (une ligne spéciale dans une liste qui propose une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de la ligne totale. Aspose.Cells propose des options pour créer et gérer des listes (ou tableaux).

{{% /alert %}}

## **Formatage d'un Objet Liste**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) offre un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) dans une feuille de calcul, utilisez la propriété de collection [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), qui offre également la méthode add pour ajouter un objet List et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) est créé dans la feuille de calcul par Aspose.Cells. Utilisez des attributs (par exemple, [**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType-) de la classe [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)) pour formater le tableau selon vos besoins.

L'exemple ci-dessous ajoute des données d'exemple à une feuille de calcul, ajoute un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) et lui applique des styles par défaut. Les styles [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) sont pris en charge par Microsoft Excel 2007/2010.

La sortie suivante est générée lorsque le code est exécuté.

**Un tableau formaté est créé dans la feuille de calcul** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
{{< app/cells/assistant language="java" >}}
