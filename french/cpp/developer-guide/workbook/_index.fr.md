---
title: Gérer le classeur avec C++
linktitle: Classeur
type: docs
weight: 60
url: /fr/cpp/managing-workbooks-and-worksheets/
description: Apprenez comment gérer un classeur via les API Aspose.Cells for C++.
keywords: Comment gérer un classeur en C++, gérer les classeurs et les feuilles de calcul en C++, opérer sur le classeur et les feuilles de calcul en C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ fournit une API puissante et flexible pour gérer les classeurs et les feuilles de calcul. Cette section explique comment créer, ouvrir, et manipuler les classeurs et les feuilles de calcul de manière programmatique.

{{% /alert %}}

## **Création d'un nouveau classeur**
Pour créer un nouveau classeur :

1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
2. Ajoutez des feuilles de calcul au classeur en utilisant la classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Enregistrez le classeur en utilisant la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **Ouvrir un classeur existant**
Pour ouvrir un classeur existant :

1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) et passez le chemin du fichier au constructeur.
2. Accédez aux feuilles de calcul en utilisant la classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Modifiez le classeur selon les besoins.
4. Enregistrez le classeur en utilisant la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Gérer les feuilles de calcul**
Aspose.Cells for C++ propose une large gamme de méthodes pour gérer les feuilles de calcul, y compris l'ajout, la suppression et le renommage des feuilles.

### **Ajout d'une feuille de calcul**
Pour ajouter une nouvelle feuille de calcul :

1. Accédez à la classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) depuis le classeur.
2. Utilisez la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) pour ajouter une nouvelle feuille de calcul.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Suppression d'une feuille de calcul**
Pour supprimer une feuille de calcul :

1. Accédez à la classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) depuis le classeur.
2. Utilisez la méthode [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) pour supprimer une feuille par index.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Renommer une feuille de calcul**
Pour renommer une feuille :

1. Accédez à la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) depuis le classeur.
2. Utilisez la méthode [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) pour renommer la feuille.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Conclusion**
Aspose.Cells for C++ fournit un ensemble complet d'outils pour gérer les classeurs et les feuilles de calcul. Que vous ayez besoin de créer un nouveau classeur, d’en ouvrir un existant ou de manipuler des feuilles, Aspose.Cells facilite le travail avec les fichiers Excel de manière programmatique.
{{< app/cells/assistant language="cpp" >}}
