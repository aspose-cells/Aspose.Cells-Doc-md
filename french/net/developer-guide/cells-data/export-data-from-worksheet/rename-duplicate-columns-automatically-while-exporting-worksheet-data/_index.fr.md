---
title: Renommez automatiquement les colonnes en double lors de l exportation des données de la feuille de calcul
type: docs
weight: 250
url: /fr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Apprenez comment renommer automatiquement les colonnes en double lors de l exportation des données de la feuille de calcul via l API Aspose.Cells for .NET.
keywords: Renommer les colonnes en double lors de l exportation des données de la feuille de calcul, renommer automatiquement les colonnes en double lors de l exportation vers DataTable
---

## **Scénarios d'utilisation possibles**

Parfois, l'utilisateur est confronté à un problème de colonnes en double lors de l'exportation de données de la feuille de calcul vers le tableau de données. DataTable ne peut pas avoir de colonnes en double, donc les colonnes en double doivent être renommées avant de pouvoir exporter les données de la feuille de calcul vers le tableau de données. Aspose.Cells peut renommer automatiquement les colonnes en double selon la stratégie que vous avez spécifiée avec la propriété [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy). Si vous spécifiez [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit, les colonnes seront renommées comme colonne1, colonne2, colonne3, etc. et si vous spécifiez [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, alors les colonnes seront renommées comme colonneA, colonneB, colonneC, etc.

## **Renommer automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul**

Le code d'exemple suivant ajoute des données dans les trois premières colonnes de la feuille de calcul, mais toutes les colonnes ont le même nom, c'est-à-dire *Personnes*. Ensuite, il exporte les données de la feuille de calcul vers le tableau de données en spécifiant la stratégie [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter. Il imprime ensuite les noms des colonnes du tableau de données généré par Aspose.Cells. La capture d'écran suivante montre le tableau de données avec les données exportées dans le visualiseur. Comme vous pouvez le voir, les colonnes en double ont été renommées en PersonnesA, PersonnesB, etc.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
