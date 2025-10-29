---
title: Gérer le classeur avec Golang via C++
linktitle: Classeur
type: docs
weight: 60
url: /fr/go-cpp/managing-workbooks-and-worksheets/
description: Apprenez comment gérer un classeur via les API Aspose.Cells for C++.
keywords: Comment gérer un classeur en C++, gérer les classeurs et les feuilles de calcul en C++, opérer sur le classeur et les feuilles de calcul en C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ fournit une API puissante et flexible pour gérer les classeurs et les feuilles de calcul. Cette section explique comment créer, ouvrir, et manipuler les classeurs et les feuilles de calcul de manière programmatique.

{{% /alert %}}

## **Création d'un nouveau classeur**
Pour créer un nouveau classeur :

1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/fr-cpp/workbook/).
2. Ajoutez des feuilles de calcul au classeur en utilisant la classe [WorksheetCollection](https://reference.aspose.com/cells/fr-cpp/worksheetcollection/).
3. Enregistrez le classeur en utilisant la méthode [Save](https://reference.aspose.com/cells/fr-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **Ouvrir un classeur existant**
Pour ouvrir un classeur existant :

1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/fr-cpp/workbook/) et passez le chemin du fichier au constructeur.
2. Accédez aux feuilles de calcul en utilisant la classe [WorksheetCollection](https://reference.aspose.com/cells/fr-cpp/worksheetcollection/).
3. Modifiez le classeur selon les besoins.
4. Enregistrez le classeur en utilisant la méthode [Save](https://reference.aspose.com/cells/fr-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **Gérer les feuilles de calcul**
Aspose.Cells for C++ propose une large gamme de méthodes pour gérer les feuilles de calcul, y compris l'ajout, la suppression et le renommage des feuilles.

### **Ajout d'une feuille de calcul**
Pour ajouter une nouvelle feuille de calcul :

1. Accédez à la classe [WorksheetCollection](https://reference.aspose.com/cells/fr-cpp/worksheetcollection/) du classeur.
2. Utilisez la méthode [Add](https://reference.aspose.com/cells/fr-cpp/worksheetcollection/add_sheettype/) pour ajouter une nouvelle feuille.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **Suppression d'une feuille de calcul**
Pour supprimer une feuille de calcul :

1. Accédez à la classe [WorksheetCollection](https://reference.aspose.com/cells/fr-cpp/worksheetcollection/) du classeur.
2. Utilisez la méthode [RemoveAt](https://reference.aspose.com/cells/fr-cpp/worksheetcollection/removeat_string/) pour supprimer une feuille par son index.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **Renommer une feuille de calcul**
Pour renommer une feuille :

1. Accédez à la classe [Worksheet](https://reference.aspose.com/cells/fr-cpp/worksheet/) du classeur.
2. Utilisez la méthode [SetName](https://reference.aspose.com/cells/fr-cpp/worksheet/setname/) pour renommer la feuille.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **Conclusion**
Aspose.Cells for C++ fournit un ensemble complet d'outils pour gérer les classeurs et les feuilles de calcul. Que vous ayez besoin de créer un nouveau classeur, d’en ouvrir un existant ou de manipuler des feuilles, Aspose.Cells facilite le travail avec les fichiers Excel de manière programmatique.
