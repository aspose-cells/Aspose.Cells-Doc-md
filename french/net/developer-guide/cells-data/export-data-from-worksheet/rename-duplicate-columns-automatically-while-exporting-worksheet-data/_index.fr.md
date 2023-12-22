---
title: Renommez automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul
type: docs
weight: 250
url: /fr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Découvrez comment renommer automatiquement les colonnes en double lors de l'exportation des données d'une feuille de calcul via le Aspose.Cells for .NET API.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Scénarios d'utilisation possibles**

 Parfois, l'utilisateur est confronté à un problème de colonnes en double lors de l'exportation de données d'une feuille de calcul vers le tableau de données. DataTable ne peut pas avoir de colonnes en double, les colonnes en double doivent donc être renommées avant de pouvoir exporter les données de la feuille de calcul vers la table de données. Aspose.Cells peut renommer automatiquement les colonnes en double selon la stratégie spécifiée par vous avec[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) propriété. Si vous précisez[**Renommer la stratégie**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, les colonnes seront renommées comme colonne1, colonne2, colonne3, etc. et si vous spécifiez[**Renommer la stratégie**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Lettre, les colonnes seront renommées comme colonneA, colonneB, colonneC, etc.

##  **Renommez automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul**

L'exemple de code suivant ajoute des données dans les trois premières colonnes de la feuille de calcul, mais toutes les colonnes portent le même nom, c'est-à-dire *Personnes*. Ensuite, il exporte les données de la feuille de calcul vers la table de données en spécifiant[**Renommer la stratégie**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Stratégie des lettres. Il imprime ensuite les noms de colonnes de la table de données générée par Aspose.Cells. La capture d'écran suivante montre la table de données avec les données exportées dans le visualiseur. Comme vous pouvez le constater, les colonnes en double ont été renommées PeopleA, PeopleB, etc.

![tâche : image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Sortie console**

Voici la sortie console de l’exemple de code ci-dessus pour référence.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
