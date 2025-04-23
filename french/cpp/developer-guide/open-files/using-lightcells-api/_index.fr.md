---
title: Utilisation de l API LightCells avec C++
linktitle: Utilisation de l API LightCells
type: docs
weight: 160
url: /fr/cpp/using-lightcells-api/
description: Apprenez comment utiliser l API LightCells en C++ pour lire et écrire efficacement de grands fichiers Excel avec une consommation minimale de mémoire.
---

{{% alert color="primary" %}} 

Parfois, vous devez lire et écrire de gros fichiers Microsoft Excel avec une énorme liste de données ou de contenu dans la feuille de calcul. L'API LightCells est utile pour créer d'énormes feuilles de calcul Excel : avec celle-ci, vous avez besoin de moins de mémoire et obtenez de meilleures performances et une meilleure efficacité.

{{% /alert %}} 

# Architecture orientée événements
Aspose.Cells fournit l'API LightCells, principalement conçue pour manipuler les données de cellules une par une sans construire un bloc de modèle de données complet (en utilisant la collection Cell, etc.) en mémoire. Il fonctionne en mode orienté événements.

Pour enregistrer des classeurs, fournissez le contenu des cellules une par une lors de l'enregistrement, et le composant l'enregistre directement dans le fichier de sortie.

Lors de la lecture de fichiers de modèle, le composant analyse chaque cellule et fournit leur valeur une par une.

Dans les deux procédures, un objet Cell est traité puis jeté, l'objet Workbook ne détient pas la collection. Dans ce mode, donc, la mémoire est économisée lors de l'importation et de l'exportation d'un fichier Microsoft Excel qui a un grand ensemble de données et qui utiliserait autrement beaucoup de mémoire.

Bien que l'API LightCells traite les cellules de la même manière pour les fichiers XLSX et XLS (elle ne charge pas réellement toutes les cellules en mémoire mais traite une cellule puis la rejette), elle économise plus efficacement la mémoire pour les fichiers XLSX que pour les fichiers XLS en raison des différents modèles de données et structures des deux formats.

Cependant, **pour les fichiers XLS**, pour économiser davantage de mémoire, les développeurs peuvent spécifier un emplacement temporaire pour enregistrer les données temporaires générées pendant le processus d'enregistrement. Généralement, **utiliser l'API LightCells pour enregistrer un fichier XLSX peut économiser 50% ou plus de mémoire** que d'utiliser la méthode classique, **enregistrer un fichier XLS peut économiser environ 20 à 40% de mémoire**.

## Écriture d'un grand fichier Excel
Aspose.Cells fournit une interface, `LightCellsDataProvider`, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la sauvegarde de grands fichiers de tableur en mode léger.

Lors de la sauvegarde d'un classeur en utilisant ce mode, `StartSheet(int)` est vérifié lors de la sauvegarde de chaque feuille du classeur. Pour une feuille, si `StartSheet(int)` retourne vrai, alors toutes les données et propriétés des lignes et cellules de cette feuille à sauvegarder sont fournies par cette implémentation. Tout d'abord, `NextRow()` est appelé pour obtenir l'index de la prochaine ligne à sauvegarder. Si un index de ligne valide est retourné (l'index doit être en ordre croissant pour les lignes à sauvegarder), alors un objet `Row` représentant cette ligne est fourni pour que l'implémentation puisse définir ses propriétés via `StartRow(Row)`.

Pour une ligne, `NextCell()` est vérifié en premier. Si un index de colonne valide est retourné (l'index de colonne doit être en ordre croissant pour toutes les cellules d'une ligne à sauvegarder), alors un objet `Cell` représentant cette cellule est fourni pour que l'implémentation puisse définir ses données et propriétés via `StartCell(Cell)`. Après avoir défini les données de la cellule, la cellule est enregistrée directement dans le fichier de feuille de calcul généré et la cellule suivante est vérifiée et traitée.

### Écriture d'un grand fichier Excel : Exemple
Veuillez consulter le code d'exemple suivant pour voir le fonctionnement de l'API LightCells. Ajoutez et supprimez, ou mettez à jour les segments de code selon vos besoins.

Le programme crée un fichier énorme avec **10 000 (matrice 10000x30) enregistrements** dans une feuille de calcul et la remplit avec des données fictives. Vous pouvez spécifier votre propre matrice en modifiant les variables `rowsCount` et `colsCount` dans la méthode `Main()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Lecture de grands fichiers Excel
Aspose.Cells fournit une interface, `LightCellsDataHandler`, qui doit être implémentée dans votre programme. L'interface représente le fournisseur de données pour la lecture de grands fichiers de feuilles de calcul en mode léger.

Lors de la lecture d'un classeur en mode léger, `StartSheet` est vérifié lors de la lecture de chaque feuille de calcul du classeur. Pour une feuille, si `StartSheet` retourne vrai, alors toutes les données et propriétés des cellules dans les lignes et colonnes de cette feuille sont vérifiées et traitées par l'implémentation de cette interface. Pour chaque ligne, `StartRow` est appelé pour vérifier si elle doit être traitée. Si une ligne doit être traitée, ses propriétés sont d'abord lues et le développeur peut y accéder avec `ProcessRow`. Si les cellules de la ligne doivent également être traitées, alors `ProcessRow` doit retourner vrai et `StartCell` est appelé pour chaque cellule existante dans la ligne pour vérifier si une cellule doit être traitée. Si une cellule doit être traitée, `ProcessCell` est appelé pour traiter la cellule selon l'implémentation de cette interface.

### Lecture de grands fichiers Excel : Exemple
Veuillez consulter le code d'exemple suivant pour voir le fonctionnement de l'API LightCells. Ajoutez et supprimez, ou mettez à jour les segments de code selon vos besoins.

Le programme lit un énorme fichier avec des millions d'enregistrements dans une feuille de calcul. Il faut un peu de temps pour lire chaque feuille dans le classeur. Le code d'exemple lit le fichier et récupère le nombre total de cellules, le nombre de chaînes et le nombre de formules dans chaque feuille de calcul.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
