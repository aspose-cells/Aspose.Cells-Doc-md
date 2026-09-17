---
title: Transposer une plage
linktitle: Transposer une plage
description: Cet article explique comment transposer ou faire pivoter des données des lignes vers les colonnes ou inversement dans des fichiers Excel à l'aide de Aspose.Cells for C++ avec trois approches différentes.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul, transposer une plage, faire pivoter les données, fonction TRANSPOSE, formule de tableau dynamique, formule matricielle, TRANSPOSE Excel, Lignes vers colonnes
type: docs
weight: 80
url: /fr/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ prend en charge la transposition (rotation) des données de sorte que les lignes deviennent des colonnes et les colonnes deviennent des lignes de trois manières différentes. La première approche utilise la méthode `Range.Transpose()` en place et fonctionne sur toutes les versions d'Excel, tandis que la deuxième utilise `Cell.SetDynamicArrayFormula()` pour écrire une formule moderne de tableau dynamique `=TRANSPOSE(...)` qui se déverse automatiquement dans Excel 365 ou Excel 2021. La troisième approche utilise `Cell.SetArrayFormula()` pour écrire une formule matricielle classique Ctrl+Shift+Entrée (CSE) compatible avec les anciennes versions d'Excel. Cet article présente chaque approche avec des instructions étape par étape et des exemples de code complets.
{{% /alert %}}

## **Introduction**
Transposer une plage signifie la faire pivoter de sorte que ce qui était une ligne devienne une colonne et ce qui était une colonne devienne une ligne, reflétant ainsi les données par rapport à sa diagonale principale. Dans Microsoft Excel, la fonction de feuille de calcul `TRANSPOSE` effectue cette opération, et la référence conceptuelle est documentée à l'adresse [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Ce concept peut être appliqué par programmation à une plage de cellules, ce qui est utile dans de nombreux scénarios métier et de reporting.
- Réorienter les rapports de ventes trimestriels ou annuels où les trimestres s'étendent normalement horizontalement et les régions verticalement, ou inversement.
- Inverser l'orientation des axes dans les tableaux de bord ou les graphiques afin qu'une série temporelle s'étende verticalement plutôt qu'horizontalement.
- Remodeler les données importées de systèmes externes afin qu'elles correspondent à la disposition attendue par les modèles d'analyse ou de reporting en aval.
Pour rendre concret le reste de l'article, chaque exemple utilise le petit tableau de ventes par région par trimestre suivant. Dans le classeur d'exemple, ce tableau occupe la plage **A1:D5**, avec **A1** laissé vide comme coin supérieur gauche, **B1:D1** contenant les en-têtes de régions, et **A2:A5** contenant les en-têtes de trimestres.
| Région            | Europe    | Asie      | Amérique du Nord |
|-------------------|-----------|-----------|------------------|
| T1                | 21704714  | 8774099   | 12094215         |
| T2                | 17987034  | 12214447  | 10873099         |
| T3                | 19485029  | 14356879  | 15689543         |
| T4                | 22567894  | 15763492  | 17456723         |
L'article présente ensuite trois façons différentes de transposer ces données à l'aide de Aspose.Cells for C++, chacune adaptée à une version d'Excel et à un cas d'utilisation différents.

## **Approche 1 — Transposer une plage en place (Range.Transpose)**
Utilisez cette approche lorsque vous souhaitez transposer des données sans impliquer la fonction de feuille de calcul `TRANSPOSE`. Elle fonctionne sur **toutes les versions d'Excel** et ne dépend pas des tableaux dynamiques, ce qui en fait l'option la plus sûre et la plus compatible entre les versions. Elle est idéale lorsque vous n'avez besoin que du résultat final transposé et que vous n'avez pas besoin de conserver la formule `TRANSPOSE` d'origine dans le classeur.

### **API utilisée**
`Range.Transpose()` est une méthode d'instance de la classe `Aspose.Cells.Range`. Son appel fait pivoter la plage en place en échangeant ses lignes et ses colonnes, de sorte que ce qui était une ligne devient une colonne et ce qui était une colonne devient une ligne. La méthode modifie directement les cellules sous-jacentes sans écrire de formule.

### **Étapes**
1. Ouvrez le classeur source avec `LoadOptions` défini sur le format `.xlsx` en créant un `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Récupérez la première feuille de calcul du classeur à l'aide de `workbook.GetWorksheets().Get(0)`.
3. Accédez à la collection de cellules de la feuille de calcul via `worksheet.GetCells()`.
4. Créez la plage source couvrant **A1:D5** en appelant `cells.CreateRange(u"A1:D5")`.
5. Appelez `source.Transpose()` pour faire pivoter la plage en place, en échangeant les lignes et les colonnes.
6. Enregistrez le classeur avec `workbook.Save(outputFile)`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approche 2 — Transposer avec une formule de tableau dynamique (Excel 365 / 2021)**
Utilisez cette approche lorsque vous souhaitez conserver la formule `=TRANSPOSE(A1:D5)` sous forme de formule vivante dans le classeur de sortie afin que le résultat se mette à jour automatiquement si les données source changent, et que le fichier Excel cible sera ouvert dans **Excel 365 / Excel 2021 ou version ultérieure** où les tableaux dynamiques et l'opérateur de débordement sont pris en charge.

### **API utilisée**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` est une méthode de `Aspose.Cells.Cell` qui définit la formule de la cellule comme une **formule de tableau dynamique**. Excel évalue la formule une seule fois et déverse automatiquement le résultat dans les cellules environnantes. Le troisième paramètre, lorsqu'il est défini sur `true`, demande à Aspose.Cells de calculer également les valeurs résultantes au moment de l'écriture.

### **Étapes**
1. Chargez le classeur source en construisant `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Récupérez la première feuille de calcul via `workbook.GetWorksheets().Get(0)` et accédez à sa collection `Cells` via `worksheet.GetCells()`.
3. Placez la formule de tableau dynamique sur la cellule **A6**, juste en dessous de la plage source, en appelant `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. L'argument `nullptr` passe les `FormulaParseOptions` par défaut, et le troisième argument `true` indique à Aspose.Cells de traiter la formule comme un tableau dynamique et de l'évaluer afin que les valeurs déversées soient écrites dans le classeur.
5. Enregistrez le classeur avec `workbook.Save(outputFile)`.
La cellule **A6** contient la formule `=TRANSPOSE(A1:D5)` et Excel déverse automatiquement le résultat dans la zone **A6:D10**, un bloc de 5 lignes par 4 colonnes correspondant aux données transposées.

{{% alert color="primary" %}}
Cette approche fonctionne **uniquement sur Excel 365 / 2021 ou version ultérieure**. Les anciennes versions d'Excel ne déverseront pas correctement les formules de tableau dynamique.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approche 3 — Transposer avec une formule matricielle classique (CSE)**
Utilisez cette approche lorsque vous souhaitez qu'une formule `TRANSPOSE` soit conservée dans le classeur mais que le fichier Excel cible puisse être ouvert dans **d'anciennes versions d'Excel (antérieures à 2021, y compris 2019, 2016, 2013, etc.)** où le débordement des tableaux dynamiques n'est pas pris en charge. La formule matricielle CSE classique (Ctrl+Shift+Entrée) est l'alternative rétrocompatible que toutes les versions d'Excel peuvent évaluer.

### **API utilisée**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` est une méthode de `Aspose.Cells.Cell` qui attribue une **formule matricielle classique (CSE)** à la cellule d'ancrage et déclare les dimensions du tableau résultant. Aspose.Cells écrit le marqueur de formule matricielle multi-cellules afin qu'Excel évalue la formule comme une seule expression de tableau qui remplit la plage déclarée.

### **Étapes**
2. Récupérez la première feuille de calcul via `workbook.GetWorksheets().Get(0)` et accédez à sa collection `Cells` via `worksheet.GetCells()`.
3. Appelez `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`. Le deuxième argument `4` est le nombre de lignes du tableau de destination et le troisième argument `5` est le nombre de colonnes.
4. Enregistrez le classeur avec `workbook.Save(outputFile)`.
La cellule **A6** est l'ancre de la formule matricielle et le tableau évalué s'étend sur 4 lignes par 5 colonnes à partir de A6, correspondant aux dimensions transposées de la source A1:D5. Excel écrit un seul marqueur de formule matricielle sur la plage résultante afin que les anciennes versions d'Excel l'évaluent correctement.

{{% alert color="primary" %}}
Les formules matricielles CSE sont la façon classique d'évaluer une expression `TRANSPOSE` dans Excel et cette approche est universellement compatible avec toutes les versions d'Excel.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Charger le classeur source avec les options de chargement xlsx
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // Accéder à la première feuille de calcul et à sa collection Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Définir la formule matricielle CSE classique sur la cellule A6.
    // La formule =TRANSPOSE(A1:D5) fait pivoter la plage source de 5 lignes x 4 colonnes
    // dans une matrice de 4 lignes x 5 colonnes. Le deuxième argument (4) est le nombre de lignes
    // et le troisième argument (5) est le nombre de colonnes de la matrice résultante.
    // Aspose.Cells écrit le marqueur de formule matricielle CSE afin qu'Excel l'évalue comme
    // une formule matricielle multi-cellules unique, compatible avec les anciennes versions d'Excel
    // (2019, 2016, 2013, etc.) qui ne prennent pas en charge le déversement dynamique des matrices.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Enregistrer le classeur pour que le marqueur de formule matricielle soit persistant
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Comparaison — Quand utiliser chaque approche**
| Approche | API / Méthode | Version d'Excel | Formule source conservée ? | Plage de sortie |
|----------|---------------|-----------------|---------------------------|-----------------|
| Approche 1 — Transposition en place | `Range.Transpose()` | Toutes les versions d'Excel | Non (valeurs uniquement) | Plage d'ancrage initiale, 5×4 |
| Approche 2 — Formule de tableau dynamique | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Oui (déversement dynamique) | Déversée depuis l'ancre |
| Approche 3 — Formule matricielle classique (CSE) | `Cell.SetArrayFormula` | Toutes les versions d'Excel | Oui (formule matricielle multi-cellules) | Taille explicite, 4×5 |
Utilisez l'**Approche 1** lorsque vous avez besoin d'une transformation rapide et compatible entre les versions et que vous n'avez besoin que des valeurs transposées écrites dans le fichier. Utilisez l'**Approche 2** lorsqu'Excel moderne est garanti et que vous souhaitez que la formule reste vivante et se mette à jour si la source change. Utilisez l'**Approche 3** lorsque vous avez besoin de la compatibilité la plus large avec une formule conservée dans toutes les versions d'Excel, y compris les anciennes versions qui ne prennent pas en charge les tableaux dynamiques.

## **Articles connexes**
- [Rendu de tableau à cellule unique SmartMarker | Aspose.Cells for C++](/cells/fr/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Insertion d'une image dans une cellule](/cells/fr/cpp/inserting-an-image-into-a-cell/)
- [Fractionnement de fichiers Excel en plusieurs fichiers](/cells/fr/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}