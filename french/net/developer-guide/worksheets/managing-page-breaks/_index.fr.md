---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/net/managing-page-breaks/
---
{{% alert color="primary" %}}

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et la suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page se termine et le reste des données après le saut de page est imprimé sur la page suivante lors de l'impression. En termes simples, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul lors de l'exécution à l'aide de Aspose.Cells. Aspose.Cells permet aux développeurs d'ajouter deux types de sauts de page :

- Saut de page horizontal
- Saut de page vertical

Dans le reste de la discussion, nous décrirons comment ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul en utilisant Aspose.Cells.

{{% /alert %}}

## **Sauts de page**

Aspose.Cells fournit un[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)fournit un large éventail de propriétés et de méthodes utilisées pour gérer une feuille de calcul.

 Pour ajouter des sauts de page, utilisez le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Sauts de page horizontaux**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) et[**Sauts de page verticaux**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Propriétés.

 Le[**Sauts de page horizontaux**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) et[**Sauts de page verticaux**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks)Les propriétés sont des collections qui peuvent contenir plusieurs sauts de page. Chaque collection contient plusieurs méthodes de gestion des sauts de page horizontaux et verticaux.

### **Ajouter des sauts de page**

 Pour ajouter un saut de page dans une feuille de calcul, insérez des sauts de page verticaux et horizontaux dans la cellule spécifiée en appelant la commande[**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) et[**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index) méthodes. Chaque**Ajouter** prend le nom de la cellule où la rupture doit être ajoutée.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

Dans les modes d'aperçu des sauts de page ou d'aperçu avant impression, vous pouvez voir comment ces sauts de page fonctionnent.

{{% /alert %}}

### **Effacer tous les sauts de page**

 Pour effacer tous les sauts de page dans une feuille de calcul, appelez le[**HorizontalPageBreakCollectionHorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) et[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) collections'[**Dégager()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear)méthodes.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Suppression d'un saut de page spécifique**

 Pour supprimer un saut de page spécifique, appelez le[**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) et[**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat) méthodes. Chaque**Supprimer à**prend l'index du saut de page sur le point d'être supprimé.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Important à savoir**

 Lorsque vous définissez**FitToPages** propriétés (c'est-à-dire[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) et[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) dans les paramètres de mise en page, les paramètres de saut de page sont affectés. Par conséquent, si vous imprimez la feuille de calcul, les paramètres de saut de page ne sont pas pris en compte bien qu'ils soient toujours définis.
