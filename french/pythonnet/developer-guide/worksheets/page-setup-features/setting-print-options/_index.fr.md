---
title: Réglage des options d impression
type: docs
weight: 40
url: /fr/python-net/setting-print-options/
description: Cet article démontre comment définir de manière programmatique les Options d Impression de la fonctionnalité Configuration de la page de Feuille de calcul Excel en utilisant l API Aspose.Cells pour Python via .NET. Vous pouvez définir la zone d impression, les titres et l ordre des pages.
keywords: Bibliothèque Python Excel, Définir la zone d impression Excel en Python, Définir les titres d impression Excel en Python, Comment définir l ordre des pages Excel en Python, Comment définir les options d impression en Python, Comment définir la zone d impression en Python, Comment définir les titres d impression en Python. 
---

{{% alert color="primary" %}}

Les paramètres de configuration de page de Microsoft Excel offrent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul.

{{% /alert %}}

## **Comment définir les options d'impression**

Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique sur une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

Aspose.Cells pour Python via .NET prend en charge toutes les options d’impression proposées par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul en utilisant les propriétés offertes par la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Comment ces propriétés sont utilisées est discuté ci-dessous plus en détail.

## **Comment définir la zone d'impression**

Par défaut, la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la propriété [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) de la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Attribuez à cette propriété une plage de cellules définissant la zone d'impression.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Comment définir les titres d'impression**

Aspose.Cells pour Python via .NET vous permet de désigner les en-têtes de lignes et de colonnes à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) et [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) de la classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Comment définir d'autres options d'impression**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fournit également plusieurs autres propriétés pour définir les options d'impression générales comme suit :

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/) : une propriété booléenne qui définit l'impression ou non des quadrillages.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/) : une propriété booléenne qui définit l'impression ou non des en-têtes de lignes et de colonnes.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/) : une propriété booléenne qui définit l'impression ou non de la feuille de calcul en mode noir et blanc.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) : définit l'affichage des commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/) : une propriété booléenne qui définit l'impression de la feuille sans graphiques.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) : définit l'impression des erreurs de cellule telles qu'elles sont affichées, vides, trait d'union ou N/A.

Pour définir les propriétés [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) et [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors), Aspose.Cells fournit également deux énumérations, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) et [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype), qui contiennent des valeurs prédéfinies à attribuer aux propriétés [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) et [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) respectivement.

Les valeurs prédéfinies de l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) sont répertoriées ci-dessous avec leurs descriptions.

|**Types de commentaires d'impression**|**Description**|
| :- | :- |
|IMPRIMER_SUR_PLACE|Spécifie d'imprimer les commentaires tels qu’affichés dans la feuille de calcul.|
|IMPRIMER_SANS_COMMENTAIRES|Spécifie de ne pas imprimer les commentaires.|
|IMPRIMER_FIN_FEUILLE|Spécifie d'imprimer les commentaires à la fin de la feuille de calcul.|

Les valeurs prédéfinies de l'énumération [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) sont répertoriées ci-dessous avec leurs descriptions.



|**Types d'erreurs d'impression**|**Description**|
| :- | :- |
|IMPRIMER_ERREURS_VIDE|Spécifie de ne pas imprimer les erreurs.|
|IMPRIMER_ERREURS_TIRET|Spécifie d'imprimer les erreurs comme "--".|
|IMPRIMER_ERREURS_AFFICHEES|Spécifie d'imprimer les erreurs telles qu’affichées.|
|IMPRIMER_ERREURS_NA|Spécifie d'imprimer les erreurs comme "#N/A".|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Comment définir l'ordre des pages**

La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fournit la propriété [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) qui est utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit.

- **En bas puis à droite :** imprime toutes les pages en bas avant d'imprimer les pages à droite.
- **À droite puis en bas :** imprime les pages de gauche à droite avant d'imprimer les pages en dessous.

Aspose.Cells fournit une énumération, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) qui contient tous les types d'ordre prédéfinis.

Les valeurs prédéfinies de l'énumération [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) sont répertoriées ci-dessous.

|**Types d'ordre d'impression**|**Description**|
| :- | :- |
|DESSUS_PUIS_DESSOUS|Représente l'ordre d'impression comme de haut en bas, puis de gauche à droite.|
|DESSOUS_PUIS_DESSUS|Représente l'ordre d'impression comme de gauche à droite, puis de haut en bas.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
