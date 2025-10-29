---
title: Obtenir la plage maximale dans une feuille de calcul avec Golang via C++
linktitle: Obtenir la plage maximale dans une feuille de calcul
type: docs
weight: 360
url: /fr/go-cpp/get-max-range-in-a-worksheet/
description: Cet article décrit comment obtenir la plage maximale, la plage de données maximale et la plage de visualisation maximale des fichiers Excel avec la bibliothèque Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Lors de la lecture de données de la feuille de calcul, nous devons connaître la zone maximale.

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la zone maximale.

Lors de l'exportation d'une zone spécifiée en HTML et PDF, nous devons connaître la zone maximale.

Aspose.Cells for C++ propose différentes manières de trouver la plage maximale dans une feuille de calcul. 

{{% /alert %}} 

## **Obtenir la plage maximale**
Dans Aspose.Cells, si les objets [**Row**](https://reference.aspose.com/cells/go-cpp/row/) et [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) sont initialisés, ces lignes et colonnes seront comptabilisées jusqu'à la zone maximale, même s'il n'y a aucune donnée dans les lignes ou colonnes vides.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **Obtenir la plage de données maximale**
Dans la plupart des cas, nous n'avons besoin d'obtenir que toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.
Et les paramètre concernant les formes, les tableaux et les tableaux croisés dynamiques seront ignorés.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **Obtenir la plage d'affichage maximale**
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.
Les codes suivants montrent comment rendre la plage d'affichage maximale en HTML :

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
Voici le [fichier excel source](Book1.xlsx).
