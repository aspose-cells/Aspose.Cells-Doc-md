---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/net/managing-page-breaks/
description: Cet article fournit un code source d exemple et explique comment ajouter des sauts de page, effacer des sauts de page ou supprimer des sauts de page spécifiques dans des feuilles de calcul Excel de manière programmative en utilisant l API C# ou la bibliothèque .NET.
keywords: sauts de page c#, sauts de page excel c#, effacer un saut de page c#, supprimer un saut de page spécifique c#
---

{{% alert color="primary" %}}

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et où la page suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page se termine et le reste des données après le saut de page est imprimé sur la page suivante lors de l'impression. En termes simples, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul à l'exécution à l'aide d'Aspose.Cells. Aspose.Cells permet aux développeurs d'ajouter deux types de sauts de page :

- Saut de page horizontal
- Saut de page vertical

Dans le reste de la discussion, nous décrirons comment ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul à l'aide d'Aspose.Cells.

{{% /alert %}}

## **Sauts de page**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes utilisées pour gérer une feuille de calcul.

Pour ajouter les sauts de page, utilisez les propriétés de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) et [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks).

Les propriétés [**HorizontalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/horizontalpagebreaks) et [**VerticalPageBreaks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/verticalpagebreaks) sont des collections qui peuvent contenir plusieurs sauts de page. Chaque collection contient plusieurs méthodes pour gérer les sauts de page horizontaux et verticaux.

### **Ajout de sauts de page**

Pour ajouter un saut de page dans une feuille de calcul, insérez des sauts de page verticaux et horizontaux à la cellule spécifiée en appelant les méthodes [**HorizontalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/add/index) et [**VerticalPageBreakCollection.Add()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/add/index). Chaque méthode **Ajouter** prend le nom de la cellule où le saut doit être ajouté.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-AddingPageBreaks-1.cs" >}}

{{% alert color="primary" %}}

En mode Aperçu des sauts de page ou Aperçu avant impression, vous pouvez voir comment fonctionnent ces sauts de page.

{{% /alert %}}

### **Effacement de tous les sauts de page**

Pour effacer tous les sauts de page dans une feuille de calcul, appelez les méthodes [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection) et [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection) des collections [**Clear()**](https://docs.microsoft.com/en-us/dotnet/api/system.collections.collectionbase.clear?redirectedfrom=MSDN&view=netframework-4.7.2#System_Collections_CollectionBase_Clear).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-ClearAllPageBreaks-1.cs" >}}

### **Suppression d'un saut de page spécifique**

Pour supprimer un saut de page spécifique, appelez les méthodes [**HorizontalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/horizontalpagebreakcollection/methods/removeat) et [**VerticalPageBreakCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/verticalpagebreakcollection/methods/removeat). Chaque méthode **RemoveAt** prend l'index du saut de page à supprimer.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-RemoveSpecificPageBreak-1.cs" >}}

## **Important à savoir**

Lorsque vous définissez les propriétés **FitToPages** (c'est-à-dire [**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) et [**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)) dans les paramètres de mise en page, les paramètres de saut de page sont affectés. Ainsi, si vous imprimez la feuille de calcul, les paramètres de saut de page ne sont pas pris en compte bien qu'ils soient toujours définis.
