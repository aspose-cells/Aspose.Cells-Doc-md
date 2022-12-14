---
title: Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique
type: docs
weight: 880
url: /fr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells fournit le[Tableau croisé dynamique.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)propriété que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique. Si**vrai** , une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si**faux** , une chaîne n'aura pas la restriction susmentionnée. La valeur par défaut est**vrai**.

{{% /alert %}} 
## **Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique**
 L'exemple de code suivant explique l'utilisation de[Tableau croisé dynamique.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) propriété. La chaîne d'origine comporte 383 caractères. Mais quand[Tableau croisé dynamique.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) la propriété est définie sur**vrai** et que le tableau croisé dynamique est rafraîchi, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères. Cependant, lorsque[Tableau croisé dynamique.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) la propriété est définie**faux** et que le tableau croisé dynamique est à nouveau rafraîchi, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez télécharger le[exemple de fichier excel](5472558.xlsx) utilisé dans ce code,[fichier excel de sortie](5472557.xlsx) généré par celui-ci et sa sortie console pour votre référence. Veuillez également lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Sortie console**
Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le donné[exemple de fichier excel](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
