---
title: Paramètres du classeur
type: docs
weight: 250
url: /fr/net/aspose-cells-gridweb/workbook-settings/
description: Cet article décrit les paramètres du classeur pour GridWeb.
keywords: settings
---
Certains paramètres peuvent être spécifiés par set GridWorkbookSettings :

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**Nom** |**Description** |
|:- |:- |
| MaxItération| Obtient ou définit le nombre maximal d'itérations pour résoudre une référence circulaire, la valeur par défaut est 100.|
| Itération| Obtient ou définit si l'itération est utilisée pour résoudre les références circulaires.|
| ForceFullCalculate| Obtient ou définit si le calcul est complet à chaque fois qu'un calcul est déclenché.|
| Créer une chaîne de calcul|Obtient ou définit si créer une chaîne de formules calculées. La valeur par défaut est false.|
| Recalculer à l'ouverture| Obtient ou définit si recalcule toutes les formules à l'ouverture du fichier.|
| PrecisionAsDisplay| True si les calculs de ce classeur seront effectués en utilisant uniquement la précision des nombres tels qu'ils sont affichés|
| Date1904| Obtient ou définit une valeur qui indique si le classeur utilise le système de date 1904.|
| VérifierCustomNumberFormat| Obtient ou définit si la vérification du format numérique personnalisé lors de la définition de Style.Custom.|
| Auteur| Obtient et définit l'auteur du fichier.|
 


Par exemple, le code suivant définit ReCalculateOnOpen sur false pour arrêter le calcul à l'ouverture du fichier :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 le code suivant définit l'auteur du fichier :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 