---
title: Insertion, suppression des lignes et des colonnes
type: docs
weight: 40
url: /fr/go-cpp/inserting-deleting-rows-and-columns/
---

## **Introduction**

Que ce soit pour créer une nouvelle feuille de calcul à partir de zéro ou pour travailler sur une feuille de calcul existante, nous pouvons avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, nous pouvons également avoir besoin de supprimer des lignes ou des colonnes à des positions spécifiées dans la feuille de calcul. Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, discutées ci-dessous.

### **Gestion des lignes et des colonnes**

Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) permettant d’accéder à chaque feuille de calcul. Une feuille est représentée par la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre une collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/) où sont stockées toutes les cellules de la feuille.

La collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/) propose plusieurs méthodes pour gérer les lignes et colonnes d’une feuille. Certaines sont expliquées ci-dessous.

{{% alert color="primary" %}}

Lors de l'ajout de lignes ou de colonnes, le contenu de la feuille de calcul est déplacé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est déplacé vers le haut ou la gauche.

{{% /alert %}}

Insérez une ligne dans la feuille à n’importe quel emplacement en appelant la méthode [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). La méthode [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) prend en paramètre l’indice de la ligne où la nouvelle ligne sera insérée.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Insertion de plusieurs lignes**

Pour insérer plusieurs lignes dans une feuille, appelez la méthode [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). La méthode [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) prend deux paramètres :

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Suppression de plusieurs lignes**

Pour supprimer plusieurs lignes d’une feuille, utilisez la méthode [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Elle prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes à supprimer.

#### **Insérer une colonne**

Les développeurs peuvent également insérer une colonne à n’importe quel endroit de la feuille en utilisant la méthode [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). La méthode [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) nécessite l’indice de la colonne où la nouvelle colonne sera insérée.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

Pour supprimer une colonne de la feuille à n’importe quel emplacement, appelez la méthode [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). La méthode [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) prend l’indice de la colonne à supprimer.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
