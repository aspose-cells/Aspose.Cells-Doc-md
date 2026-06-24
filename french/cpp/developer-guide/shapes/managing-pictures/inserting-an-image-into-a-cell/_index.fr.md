---
title: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque C++ permettant de travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes, placer une image flottante sur la cellule, ou incorporer l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul, insérer image, incorporer image, image dans cellule, ajuster image à cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur le calque de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image incorporée est stockée à l'intérieur de la cellule elle-même et se met à l'échelle automatiquement en fonction de la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul qui servent de rapports visuels, catalogues de produits, annuaires d'employés, tableaux de bord ou listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée avec la cellule qui la contient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `Placement` sur `MoveAndSize`, et ajustez ses cellules d'ancrage (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) afin que l'image couvre exactement une cellule.
- **Approche 2 — Incorporer une image directement dans une cellule.** Assignez les octets de l'image à la propriété `EmbeddedImage` de la cellule. L'image se met automatiquement à l'échelle pour s'adapter à la zone d'affichage de la cellule et se déplace avec elle.

Le reste de cet article présente les deux approches, explique les API concernées et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image sur une cellule**

Une image flottante est un objet `Picture` qui réside sur le calque de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une cellule**, vous devez :

1. Ajouter l'image à l'aide de `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage afin que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.Placement` sur `PlacementType.MoveAndSize` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrer l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index de base zéro :

- `Picture.UpperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `Picture.UpperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `Picture.LowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.LowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

Par exemple, pour ajuster l'image exactement dans la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` et `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Les indices de ligne et de colonne dans Aspose.Cells sont **de base zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit constituent la source la plus fréquente d'images qui semblent dépasser dans une cellule adjacente.

{{% /alert %}}

### **Contrôler le comportement de placement**

`Picture.Placement` est une énumération de type `PlacementType` qui contrôle la façon dont l'image se comporte lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui fait que l'image se déplace et se redimensionne avec sa cellule sous-jacente, en préservant l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez au `Worksheet` cible depuis `workbook.Worksheets[0]`.
3. Lisez le fichier image depuis le disque dans une mémoire tampon d'octets `Vector<uint8_t>` afin que les octets de l'image soient disponibles pour l'API.
4. Appelez `worksheet.Pictures.Add(5, 2, imageData)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage afin que l'image ne couvre que la cellule C6 : `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Définissez `picture.Placement = PlacementType.MoveAndSize` pour maintenir l'image alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.

Le code suivant démontre l'approche complète.

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

## **Approche 2 : Incorporer une image directement dans une cellule**

Aspose.Cells expose également un mécanisme plus simple pour les images liées aux cellules : la propriété `Cell.EmbeddedImage`. Assigner des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu intégré.

### **Fonctionnement des images incorporées**

- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur le calque de dessin.
- L'image se met automatiquement à l'échelle pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule avec une véritable adresse qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `Cell.EmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui vit dans cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez au `Worksheet` cible depuis `workbook.Worksheets[0]`.
3. Lisez le fichier image depuis le disque dans un tableau d'octets `Vector<uint8_t>`.
4. Obtenez une référence à la cellule cible — soit via `worksheet.Cells["C6"]`, soit via `worksheet.Cells[5, 2]`.
5. Assignez le tableau d'octets à la propriété `EmbeddedImage` de la cellule.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image incorporée une apparence plus visible.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.

Le code suivant démontre l'approche complète.

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

    // Intégrer l'image directement dans la cellule
    cell.SetEmbeddedImage(imageData);

    // Optionnellement ajuster la hauteur de ligne et la largeur de colonne pour rendre l'image intégrée plus visible
    worksheet.GetCells().SetColumnWidth(2, 30);   // Colonne C (index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Ligne 6 (index 5)

    // Enregistrer le classeur résultant en tant que fichier .xlsx
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'insère dans une seule cellule, mais elles diffèrent par la façon dont l'image est stockée et dont elle se comporte :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme qui peut être sélectionnée, réorganisée ou regroupée avec d'autres formes.
  - Vous exigez une compatibilité descendante avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer les coordonnées d'ancrage dynamiquement en fonction de la disposition de la feuille de calcul.

- **Utilisez une image incorporée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes sur un ensemble de cellules et incorporer des images directement dans d'autres cellules, car les deux mécanismes utilisent des calques de stockage différents dans le fichier.

{{% /alert %}}

## **Articles connexes**

- [Comment insérer une image dans une cellule](/cells/fr/cpp/how-to-place-image-to-cell/)
- [Ajouter des hyperliens d'image](/cells/fr/cpp/add-image-hyperlinks/)
- [Charger une image Web depuis une URL dans une feuille de calcul Excel](/cells/fr/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipuler la position, la taille et le graphique du concepteur](/cells/fr/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}