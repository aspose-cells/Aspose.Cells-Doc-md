---
title: Gérer les feuilles de calcul
type: docs
weight: 20
url: /fr/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans des fichiers Microsoft Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Ce sujet décrit les approches pour ajouter et supprimer des feuilles de calcul dans des fichiers Microsoft Excel.

{{% /alert %}}

Aspose.Cells propose une classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) permettant d’accéder à chaque feuille.

Une feuille est représentée par la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) propose une large gamme de méthodes pour gérer une feuille.

## **Ajout de feuilles de calcul à un nouveau fichier Excel**

Pour créer un nouveau fichier Excel de manière programmatique:

1. Créez un objet de la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).
1. Appelez la méthode [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) de la collection [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/). Une feuille vide est automatiquement ajoutée au fichier Excel. Elle peut être référencée en passant index de la feuille à la collection [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
1. Obtenez une référence de feuille de calcul.
1. Travaillez sur les feuilles de calcul.
1. Enregistrez le nouveau fichier Excel avec ses nouvelles feuilles en appelant la méthode [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) de la classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Accès aux feuilles de calcul à l'aide de l'indice de la feuille**

Le code d'exemple suivant montre comment accéder à une feuille de calcul ou en obtenir une en spécifiant son indice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**

La suppression de feuilles par nom fonctionne bien lorsque le nom de la feuille est connu. Si vous ne connaissez pas le nom de la feuille, utilisez une version surchargée de la méthode [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) qui prend l’indice de la feuille au lieu de son nom.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
