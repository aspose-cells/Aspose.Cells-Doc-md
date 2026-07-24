---
title: Précisez si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique
type: docs
weight: 880
url: /fr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit la propriété [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) que vous pouvez utiliser pour spécifier si le PivotTable est compatible avec Excel2003 lors de l'actualisation du PivotTable. Si **true**, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne dépasse 255 caractères, elle sera tronquée. Si **false**, une chaîne n'aura pas la restriction mentionnée ci-dessus. La valeur par défaut est **true**.

{{% /alert %}} 
## **Spécifiez si le PivotTable est compatible pour Excel2003 lors de l'actualisation du PivotTable**
Le code d'exemple suivant explique l'utilisation de la propriété [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible). La chaîne d'origine fait 383 caractères. Mais lorsque la propriété [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) est définie sur **true** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et elle fait 255 caractères de long. Cependant, lorsque la propriété [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) est définie sur **false** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez télécharger le [fichier Excel d'exemple](5472558.xlsx) utilisé dans ce code, le [fichier Excel de sortie](5472557.xlsx) généré par celui-ci et sa sortie console pour votre référence. Veuillez également lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Sortie console**
Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](5472558.xlsx) fourni.



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
