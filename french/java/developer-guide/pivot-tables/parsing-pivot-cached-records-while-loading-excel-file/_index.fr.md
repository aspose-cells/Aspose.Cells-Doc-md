---
title: Analyse des enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel
type: docs
weight: 100
url: /fr/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Scénarios d'utilisation possibles**

Lorsque vous créez un tableau croisé dynamique, Microsoft Excel prend une copie des données sources et les enregistre dans le cache du tableau croisé dynamique. Le cache du tableau croisé dynamique est conservé dans la mémoire de Microsoft Excel. Vous ne pouvez pas le voir, mais ce sont les données auxquelles le tableau croisé dynamique fait référence lorsque vous construisez votre tableau croisé dynamique ou modifiez une sélection de filtre ou déplacez des lignes/colonnes. Cela permet à Microsoft Excel de réagir très rapidement aux modifications du tableau croisé dynamique, mais cela peut également doubler la taille de votre fichier. Après tout, le cache du tableau croisé dynamique est simplement une copie de vos données sources, il est donc logique que la taille de votre fichier puisse être potentiellement doublée.

Lorsque vous chargez votre fichier Excel dans l'objet Workbook, vous pouvez décider si vous voulez également charger les enregistrements du cache des tableaux croisés dynamiques ou non, en utilisant la propriété [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). La valeur par défaut de cette propriété est **fausse**. Si le cache des tableaux croisés dynamiques est assez gros, cela peut améliorer les performances. Mais si vous voulez également charger les enregistrements du cache des tableaux croisés dynamiques, vous devez définir cette propriété sur **true**.

## **Analyse des enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel**

Le code d'exemple suivant explique l'utilisation de la propriété [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Il charge le [fichier Excel d'exemple](61767786.xlsx) tout en analysant les enregistrements mis en cache des tableaux croisés dynamiques. Ensuite, il rafraîchit le tableau croisé dynamique et l'enregistre en tant que [fichier Excel de sortie](61767785.xlsx).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
