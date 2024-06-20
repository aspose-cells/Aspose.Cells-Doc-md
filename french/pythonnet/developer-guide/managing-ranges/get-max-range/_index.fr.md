---
title: Obtenir la plage maximale dans une feuille de calcul
type: docs
weight: 360
url: /fr/python-net/get-max-range-in-a-worksheet/
description: Cet article décrit comment obtenir la plage maximale, la plage de données maximale, la plage d affichage maximale des fichiers Excel avec la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Python obtenir la plage maximale, Python obtenir la plage de données maximale, Python obtenir la plage d affichage maximale.
---

{{% alert color="primary" %}} 

Lors de la lecture de données de la feuille de calcul, nous devons connaître la zone maximale.

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la zone maximale.

Lors de l'exportation d'une zone spécifiée en html et pdf, nous devons connaître la zone maximale.

Aspose.Cells pour Python via .NET contient différentes façons de trouver la plage maximale dans une feuille de calcul. 


{{% /alert %}} 



## **Comment obtenir la plage maximale**
Dans Aspose.Cells pour Python via .NET, si les objets [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) et [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) sont initialisés, ces lignes et colonnes seront comptées dans la zone maximale, même s'il n'y a pas de données dans les lignes ou colonnes vides.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **Comment obtenir la plage de données maximale**
Dans la plupart des cas, nous n'avons besoin d'obtenir que toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.
Et les paramètres concernant les formes, tableaux et tableaux croisés dynamiques seront ignorés.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **Comment obtenir la plage d'affichage maximale**
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.
Les codes suivants montrent comment rendre la plage d'affichage maximale en html :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

Voici le [fichier excel source](Book1.xlsx).
