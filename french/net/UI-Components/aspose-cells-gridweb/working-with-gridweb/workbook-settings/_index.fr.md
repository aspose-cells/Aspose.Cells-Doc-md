---
title: Paramètres du classeur
type: docs
weight: 250
url: /fr/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Cet article décrit les paramètres du classeur dans GridWeb.
keywords: GridWeb, paramètres
---


Il existe certains paramètres que nous pouvons spécifier en définissant GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

|**Nom** |**Description** |
| :- | :- |
|MaxIteration |Définit ou obtient le nombre maximal d'itérations pour résoudre une référence circulaire, la valeur par défaut est de 100. |
|Iteration | Définit ou obtient si utilise l'itération pour résoudre les références circulaires. |
|ForceFullCalculate | Obtient ou définit si effectue entièrement des calculs à chaque fois qu'un calcul est déclenché. |
|CreateCalcChain | Obtient ou définit si créer une chaîne de formules calculées. Par défaut, c'est faux. |
|ReCalculateOnOpen | Obtient ou définit si recalculer toutes les formules lors de l'ouverture du fichier. |
|PrecisionAsDisplayed | Vrai si les calculs dans ce classeur seront effectués en utilisant uniquement la précision des nombres telle qu'elle est affichée. |
|Date1904 | Obtient ou définit une valeur qui représente si le classeur utilise le système de date 1904. |
|CheckCustomNumberFormat | Obtient ou définit la vérification du format de nombre personnalisé lors de la définition de Style.Custom. |
|Author | Obtient et définit l'auteur du fichier. |



Par exemple, le code suivant définit ReCalculateOnOpen sur false pour arrêter le calcul à l'ouverture du fichier :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 le code suivant définit l'auteur du fichier :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


