---
title: Conserver les séparateurs pour les lignes vides lors de l'exportation des feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Conserver les séparateurs pour les lignes vides lors de l'exportation des feuilles de calcul au format CSV**

Aspose.Cells offre la possibilité de conserver les séparateurs de lignes lors de la conversion des feuilles de calcul au format CSV. Pour cela, vous pouvez utiliser le**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**propriété de**[TxtSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions)**classer.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**est une propriété booléenne. Pour conserver les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez le**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**propriété à**vrai**.

L'exemple de code suivant charge le[fichier Excel source](84378743.xlsx). Il fixe**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**propriété à**vrai** et l'enregistre sous[sortie.csv](84378744.csv) . La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion de la feuille de calcul en CSV et la sortie générée en définissant**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** à**vrai**.

![tâche : image_autre_texte](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
