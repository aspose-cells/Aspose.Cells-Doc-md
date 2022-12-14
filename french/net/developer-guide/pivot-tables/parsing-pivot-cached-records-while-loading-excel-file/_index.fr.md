---
title: Analyse des enregistrements en cache Pivot lors du chargement du fichier Excel
type: docs
weight: 70
url: /fr/net/parsing-pivot-cached-records-while-loading-excel-file/
---
## **Scénarios d'utilisation possibles**

Lorsque vous créez un tableau croisé dynamique, Microsoft Excel prend une copie des données source et la stocke dans le cache croisé dynamique. Le Pivot Cache est conservé dans la mémoire de Microsoft Excel. Vous ne pouvez pas le voir, mais ce sont les données auxquelles le tableau croisé dynamique fait référence lorsque vous créez votre tableau croisé dynamique ou modifiez une sélection de segment ou déplacez des lignes/colonnes. Cela permet à Microsoft Excel d'être très réactif aux modifications du tableau croisé dynamique, mais il peut également doubler la taille de votre fichier. Après tout, le Pivot Cache n'est qu'un double de vos données source, il est donc logique que la taille de votre fichier soit potentiellement doublée.

Lorsque vous chargez votre fichier Excel à l'intérieur de l'objet Workbook, vous pouvez décider si vous souhaitez également charger les enregistrements du Pivot Cache ou non, en utilisant le[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) propriété. La valeur par défaut de cette propriété est**faux** . Si Pivot Cache est assez volumineux, cela peut augmenter les performances. Mais si vous souhaitez également charger les enregistrements du cache croisé dynamique, vous devez définir cette propriété comme**vrai**.

## **Analyse des enregistrements en cache Pivot lors du chargement du fichier Excel**

L'exemple de code suivant explique l'utilisation de[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) propriété. Il charge le[exemple de fichier Excel](61767773.xlsx) lors de l'analyse des enregistrements mis en cache pivot. Ensuite, il actualise le tableau croisé dynamique et l'enregistre en tant que[fichier Excel de sortie](61767774.xlsx).

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
