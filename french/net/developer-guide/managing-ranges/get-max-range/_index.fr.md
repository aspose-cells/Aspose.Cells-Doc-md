---
title: Obtenir la plage maximale dans une feuille de calcul
type: docs
weight: 360
url: /fr/net/get-max-range-in-a-worksheet/
description: Cet article décrit comment obtenir la plage max, la plage de données max, et la plage d affichage max des fichiers Excel avec Aspose.Cells pour .Net.
---

{{% alert color="primary" %}} 

Lors de la lecture de données de la feuille de calcul, nous devons connaître la zone maximale.

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la zone maximale.

Lors de l'exportation d'une zone spécifiée en html et pdf, nous devons connaître la zone maximale.

Aspose.Cells pour .Net contient différentes façons de trouver la plage maximale dans une feuille de calcul. 


{{% /alert %}} 



## **Obtenir la plage maximale**
Dans Aspose.Cells, si les objets [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) et [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) sont initialisés, ces lignes et colonnes seront comptées dans la zone maximale, même s'il n'y a pas de données dans les lignes ou colonnes vides.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Obtenir la plage de données maximale**
Dans la plupart des cas, nous n'avons besoin d'obtenir que toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.
Et les paramètres concernant les formes, tableaux et tableaux croisés dynamiques seront ignorés.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Obtenir la plage d'affichage maximale**
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.
Les codes suivants montrent comment rendre la plage d'affichage maximale en html :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Voici le [fichier excel source](Book1.xlsx).
{{< app/cells/assistant language="csharp" >}}
