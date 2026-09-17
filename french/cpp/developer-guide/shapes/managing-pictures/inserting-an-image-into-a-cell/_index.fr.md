---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuille de calcul. Cet article explique comment ajuster une image à une seule cellule, soit en plaçant une image flottante par-dessus la cellule, soit en intégrant l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul, insérer une image, intégrer une image, image dans une cellule, ajuster une image à une cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux manières distinctes d'associer une image à une seule cellule. Une image flottante est une forme placée sur la couche de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et se redimensionne automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

## **Introduction**
Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, catalogues de produits, annuaires d'employés, tableaux de bord ou listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer librement sur une feuille de calcul, vous pouvez souhaiter une image nette et liée à la cellule qui reste alignée avec la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante par-dessus une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `Placement` à `MoveAndSize`, et ajustez ses cellules d'ancrage (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) pour que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `EmbeddedImage` de la cellule. L'image se redimensionne automatiquement pour s'adapter à la zone d'affichage de la cellule et se déplace avec la cellule.
Le reste de cet article présente les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approach 1: Place a Picture Over a Cell**
Une image flottante est un objet `Picture` qui vit sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule en particulier, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.
Pour qu'une image flottante couvre **exactement une cellule**, vous devez :
1. Ajouter l'image à l'aide de `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage pour que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.Placement` à `PlacementType.MoveAndSize` pour que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Anchoring the Picture to a Single Cell**
L'ancrage de l'image est défini par quatre propriétés d'index basées sur zéro :
- `Picture.UpperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `Picture.UpperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `Picture.LowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve en bas de la ligne `r`, définissez cette valeur à `r + 1`.
- `Picture.LowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur à `c + 1`.

{{% alert color="primary" %}}
Les index de ligne et de colonne dans Aspose.Cells sont **basés sur zéro**. La cellule C6 a pour index de ligne 5 et pour index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

### **Controlling Placement Behavior**
`Picture.Placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui fait que l'image se déplace et se redimensionne avec sa cellule sous-jacente, en préservant l'ajustement exact.

### **Step-by-Step Instructions**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.GetWorksheets().Get(0]`.
3. Lisez le fichier image depuis le disque dans un tampon d'octets `Vector<uint8_t>` afin que les octets de l'image soient disponibles pour l'API.
4. Appelez `worksheet.Pictures.Add(5, 2, imageData)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage pour que l'image couvre uniquement la cellule C6 : `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Définissez `picture.Placement = PlacementType.MoveAndSize` pour que l'image reste alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Vous pouvez, si vous le souhaitez, ajouter du texte d'exemple aux cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();
    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));
    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);
    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `Cell.EmbeddedImage`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu incorporé.

### **How Embedded Images Work**
- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur la couche de dessin.
- L'image se redimensionne automatiquement pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est nécessaire.
- La cellule reste une véritable cellule avec une véritable adresse qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.
Cela fait de `Cell.EmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui vit à l'intérieur de cette cellule ».

### **Step-by-Step Instructions**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.GetWorksheets().Get(0]`.
3. Lisez le fichier image depuis le disque dans un tableau d'octets `Vector<uint8_t>`.
4. Obtenez une référence à la cellule cible — soit via `worksheet.GetCells().Get("C6"]`, soit via `worksheet.GetCells().Get(5, 2]`.
5. Affectez le tableau d'octets à la propriété `EmbeddedImage` de la cellule.
6. Vous pouvez, si vous le souhaitez, ajuster la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus visible.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C6");
    // Lire le fichier image dans un tableau d'octets
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    // Convertir std::vector en Aspose::Cells::Vector en utilisant le constructeur pointeur+taille
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // Incorporer l'image directement dans la cellule
    cell.SetEmbeddedImage(imageData);
    // Optionnellement ajuster la hauteur de ligne et la largeur de colonne pour que l'image incorporée soit plus visible
    worksheet.GetCells().SetColumnWidth(2, 30);   // Colonne C (index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Ligne 6 (index 5)
    // Enregistrer le classeur résultant sous forme de fichier .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Choosing the Right Approach**
Les deux approches produisent une image qui s'insère dans une seule cellule, mais elles diffèrent par la façon dont l'image est stockée et par son comportement :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme qui peut être sélectionnée, réordonnée ou groupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité ascendante avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer les coordonnées d'ancrage de manière dynamique en fonction de la disposition de la feuille de calcul.
- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Caméra Excel dans Aspose.Cells for C++](/cells/fr/cpp/excel-camera/)
- [Ajouter des champs de filtre à un Tableau Croisé Dynamique dans Aspose.Cells for C++](/cells/fr/cpp/add-page-field-in-pivot-table/)
- [Appliquer des styles aux Tableaux Croisés Dynamiques dans Aspose.Cells for C++](/cells/fr/cpp/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un Tableau Croisé Dynamique](/cells/fr/cpp/change-page-field-layout/)
- [Convertir un Sparkline en image et HTML dans Aspose.Cells for C++](/cells/fr/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}