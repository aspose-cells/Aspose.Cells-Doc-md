---
title: Obtenir la plage maximale dans une feuille de calcul
type: docs
weight: 360
url: /fr/net/get-max-range-in-a-worksheet/
description: Cet article décrit comment obtenir la plage maximale, la plage de données maximale et la plage d'affichage maximale des fichiers Excel avec Aspose.Cells pour la bibliothèque .Net.
---
{{% alert color="primary" %}} 

Lors de la lecture des données de la feuille de calcul, nous devons connaître la superficie maximale.

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la surface maximale.

Lors de l’exportation d’une zone spécifiée au format HTML et PDF, nous devons connaître la zone maximale.

 Aspose.Cells pour .Net contient différentes manières de trouver la plage maximale dans une feuille de calcul.


{{% /alert %}} 



##  **Obtenir la portée maximale**
 Au Aspose.Cells, si le[**rangée**](https://reference.aspose.com/cells/net/aspose.cells/row) et[**colonne**](https://reference.aspose.com/cells/net/aspose.cells/column) les objets sont initialisés, ces lignes et colonnes seront comptées dans la zone maximale, même s'il n'y a aucune donnée dans les lignes ou colonnes vides.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **Obtenir la plage de données maximale**
Dans la plupart des cas, il suffit d'obtenir toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.
Et les paramètres concernant les formes, les tableaux et les tableaux croisés dynamiques seront ignorés.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **Obtenir la plage d'affichage maximale**
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou des images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.
Les codes suivants montrent comment restituer la plage d'affichage maximale en HTML :

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

 Voici[fichier Excel source](Book1.xlsx).
