---
title: Réglage des options d impression
type: docs
weight: 40
url: /fr/net/setting-print-options/
description: Cet article montre comment définir de manière programmatique les options d impression de la fonctionnalité Mise en page de la page de feuille de calcul Excel en utilisant l API C# et la bibliothèque .NET. Vous pouvez définir la zone d impression, les titres d impression et l ordre des pages.
keywords: définir la zone d impression excel c#, définir les titres d impression excel c#, définir l ordre des pages excel c#
---

{{% alert color="primary" %}}

Les paramètres de configuration de page de Microsoft Excel offrent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul.

{{% /alert %}}

## **Réglage des options d'impression**

Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique sur une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

Aspose.Cells prend en charge toutes les options d'impression proposées par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul en utilisant les propriétés offertes par la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Comment ces propriétés sont utilisées est discuté ci-dessous de manière plus détaillée.

### **Définir la zone d'impression**

Par défaut, la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la propriété [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Attribuez à cette propriété une plage de cellules définissant la zone d'impression.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Définir les titres d'impression**

Aspose.Cells vous permet de désigner les en-têtes de lignes et de colonnes à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) et [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Définir d'autres options d'impression**

La classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) fournit également plusieurs autres propriétés pour définir les options d'impression générales comme suit :

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines) : une propriété booléenne qui définit l'impression ou non des quadrillages.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings) : une propriété booléenne qui définit l'impression ou non des en-têtes de lignes et de colonnes.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite) : une propriété booléenne qui définit l'impression ou non de la feuille de calcul en mode noir et blanc.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) : définit l'affichage des commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft) : une propriété booléenne qui définit l'impression de la feuille sans graphiques.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) : définit l'impression des erreurs de cellule telles qu'elles sont affichées, vides, trait d'union ou N/A.

Pour définir les propriétés [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) et [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors), Aspose.Cells fournit également deux énumérations, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) et [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype), qui contiennent des valeurs prédéfinies à attribuer aux propriétés [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) et [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) respectivement.

Les valeurs prédéfinies de l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) sont répertoriées ci-dessous avec leurs descriptions.

|**Types de commentaires d'impression**|**Description**|
| :- | :- |
|PrintInPlace| Spécifie d'imprimer les commentaires tels qu'ils apparaissent sur la feuille de calcul.
|PrintNoComments| Spécifie de ne pas imprimer les commentaires.
|PrintSheetEnd| Spécifie d'imprimer les commentaires à la fin de la feuille de calcul.

Les valeurs prédéfinies de l'énumération [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) sont répertoriées ci-dessous avec leurs descriptions.



|**Types d'erreurs d'impression**|**Description**|
| :- | :- |
|PrintErrorsBlank|Indique de ne pas imprimer les erreurs.|
|PrintErrorsDash|Indique d'imprimer les erreurs sous forme de "--".|
|PrintErrorsDisplayed|Indique d'imprimer les erreurs telles qu'elles sont affichées.|
|PrintErrorsNA|Indique d'imprimer les erreurs sous forme de "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Définir l'ordre des pages**

La classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) fournit la propriété [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) qui est utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit.

- **En bas puis à droite :** imprime toutes les pages en bas avant d'imprimer les pages à droite.
- **À droite puis en bas :** imprime les pages de gauche à droite avant d'imprimer les pages en dessous.

Aspose.Cells fournit une énumération, [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) qui contient tous les types d'ordre prédéfinis.

Les valeurs prédéfinies de l'énumération [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) sont répertoriées ci-dessous.

|**Types d'ordre d'impression**|**Description**|
| :- | :- |
|DownThenOver|Représente l'ordre d'impression en bas puis à droite.|
|OverThenDown|Représente l'ordre d'impression à droite puis en bas.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
