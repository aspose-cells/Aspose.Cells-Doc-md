---
title: Analyse des enregistrements mis en cache par pivot lors du chargement du fichier Excel
type: docs
weight: 70
url: /fr/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Comment analyser les enregistrements pivots mis en cache lors du chargement d'un fichier Excel avec Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Scénarios d'utilisation possibles**

Lorsque vous créez un tableau croisé dynamique, Microsoft Excel prend une copie des données source et la stocke dans le cache croisé dynamique. Le cache Pivot est conservé dans la mémoire de Microsoft Excel. Vous ne pouvez pas le voir, mais ce sont les données auxquelles le tableau croisé dynamique fait référence lorsque vous créez votre tableau croisé dynamique, modifiez une sélection de slicer ou déplacez des lignes/colonnes. Cela permet à Microsoft Excel d'être très réactif aux modifications apportées au tableau croisé dynamique, mais cela peut également doubler la taille de votre fichier. Après tout, le cache Pivot n'est qu'un double de vos données sources, il est donc logique que la taille de votre fichier soit potentiellement double.

Lorsque vous chargez votre fichier Excel dans l'objet Workbook, vous pouvez décider si vous souhaitez également charger les enregistrements de Pivot Cache ou non, à l'aide de l'option[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)propriété. La valeur par défaut de cette propriété est *false**. Si Pivot Cache est assez volumineux, cela peut augmenter les performances. Mais si vous souhaitez également charger les enregistrements de Pivot Cache, vous devez définir cette propriété sur *true**.

##  **Analyse des enregistrements mis en cache par pivot lors du chargement du fichier Excel**

L'exemple de code suivant explique l'utilisation de[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)propriété. Il charge le[exemple de fichier Excel](61767773.xlsx) lors de l'analyse des enregistrements mis en cache par pivot. Ensuite, il actualise le tableau croisé dynamique et l'enregistre en tant que[sortie du fichier Excel](61767774.xlsx).

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
