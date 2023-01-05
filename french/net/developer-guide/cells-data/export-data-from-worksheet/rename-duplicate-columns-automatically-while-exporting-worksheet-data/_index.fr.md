---
title: Renommer automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul
type: docs
weight: 250
url: /fr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **Scénarios d'utilisation possibles**

Parfois, l'utilisateur est confronté à un problème de colonnes en double lors de l'exportation des données de la feuille de calcul vers la table de données. DataTable ne peut pas avoir de colonnes en double, les colonnes en double doivent donc être renommées avant de pouvoir exporter des données de feuille de calcul vers la table de données. Aspose.Cells peut renommer automatiquement les colonnes en double selon la stratégie que vous avez spécifiée avec[**ExportTableOptions.RenameStrategyExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) la propriété. Si vous spécifiez[**RenommerStratégie**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, les colonnes seront renommées comme colonne1, colonne2, colonne3, etc. et si vous spécifiez[**RenommerStratégie**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, puis les colonnes seront renommées comme columnA, columnB, columnC, etc.

## **Renommer automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul**

 L'exemple de code suivant ajoute des données dans les trois premières colonnes de la feuille de calcul, mais toutes les colonnes portent le même nom, c'est-à-dire*Gens* . Ensuite, il exporte les données de la feuille de calcul dans la table de données en spécifiant[**RenommerStratégie**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Stratégie de la lettre. Il imprime ensuite les noms de colonne de la table de données générée par Aspose.Cells. La capture d'écran suivante montre la table de données avec les données exportées dans le visualiseur. Comme vous pouvez le voir, les colonnes en double ont été renommées en PeopleA, PeopleB etc.

![tâche : image_autre_texte](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Sortie console**

Voici la sortie console de l'exemple de code ci-dessus pour référence.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
