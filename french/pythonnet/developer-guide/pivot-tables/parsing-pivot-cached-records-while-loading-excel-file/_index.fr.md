---
title: Analyse des enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel
type: docs
weight: 70
url: /fr/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Comment analyser les enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells pour Python Excel, bibliothèque Excel Python, Comment analyser les enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel avec la bibliothèque Aspose.Cells pour Python Excel.
---

## **Scénarios d'utilisation possibles**

Lorsque vous créez un tableau croisé dynamique, Microsoft Excel prend une copie des données sources et les enregistre dans le cache du tableau croisé dynamique. Le cache du tableau croisé dynamique est conservé dans la mémoire de Microsoft Excel. Vous ne pouvez pas le voir, mais ce sont les données auxquelles le tableau croisé dynamique fait référence lorsque vous construisez votre tableau croisé dynamique ou modifiez une sélection de filtre ou déplacez des lignes/colonnes. Cela permet à Microsoft Excel de réagir très rapidement aux modifications du tableau croisé dynamique, mais cela peut également doubler la taille de votre fichier. Après tout, le cache du tableau croisé dynamique est simplement une copie de vos données sources, il est donc logique que la taille de votre fichier puisse être potentiellement doublée.

Lorsque vous chargez votre fichier Excel à l'intérieur de l'objet Workbook, vous pouvez décider si vous souhaitez également charger les enregistrements du cache du tableau croisé dynamique ou non, en utilisant la propriété [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). La valeur par défaut de cette propriété est false. Si le cache du tableau croisé dynamique est assez volumineux, cela peut améliorer les performances. Mais si vous souhaitez également charger les enregistrements du cache du tableau croisé dynamique, vous devez définir cette propriété sur true.

## **Comment analyser les enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel**

Le code d'exemple suivant explique l'utilisation de la propriété [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). Il charge le [fichier Excel d'exemple](61767773.xlsx) tout en analysant les enregistrements mis en cache du tableau croisé dynamique. Ensuite, il actualise le tableau croisé dynamique et l'enregistre sous le nom de [fichier Excel de sortie](61767774.xlsx).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
