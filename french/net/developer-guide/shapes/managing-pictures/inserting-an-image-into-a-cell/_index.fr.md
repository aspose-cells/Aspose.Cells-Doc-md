---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à une seule cellule, soit en plaçant une image flottante par-dessus la cellule, soit en intégrant l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque .NET, feuille de calcul, insérer une image, intégrer une image, image dans une cellule, ajuster une image à une cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux façons distinctes d'associer une image à une seule cellule. Une image flottante est une forme sur le calque de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée dans la cellule elle-même et se redimensionne automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos besoins de mise en page.

## **Introduction**
Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière lâche sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée avec la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante par-dessus une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `Placement` sur `MoveAndSize`, et ajustez ses cellules d'ancrage (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) pour que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `EmbeddedImage` de la cellule. L'image se redimensionne automatiquement pour s'adapter à la zone d'affichage de la cellule et accompagne la cellule.
Le reste de cet article détaille les deux approches, explique les API concernées et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image par-dessus une cellule**
Une image flottante est un objet `Picture` qui réside sur le calque de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule isolée, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.
Pour qu'une image flottante couvre **exactement une cellule**, vous devez :
1. Ajouter l'image à l'aide de `Worksheet.Pictures.Add(int row, int column, Stream stream)`, ce qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d'ancrage afin que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.Placement` sur `PlacementType.MoveAndSize` pour que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de la colonne ou la hauteur de la ligne.

### **Ancrer l'image à une seule cellule**
L'ancrage de l'image est défini par quatre propriétés d'index basées sur zéro :
- `Picture.UpperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `Picture.UpperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `Picture.LowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.LowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

{{% alert color="primary" %}}
Les indices de ligne et de colonne dans Aspose.Cells sont **basés sur zéro**. La cellule C6 a un index de ligne 5 et un index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent chevaucher une cellule adjacente.

### **Contrôler le comportement de placement**
`Picture.Placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui fait en sorte que l'image se déplace et se redimensionne avec sa cellule sous-jacente, en préservant l'ajustement exact.

### **Instructions étape par étape**
1. Créez un nouveau `Workbook` (ou ouvrez un classeur existant).
2. Accédez à la `Worksheet` cible via `workbook.Worksheets[0]`.
3. Ouvrez le fichier image depuis le disque dans un `FileStream` à l'aide d'un bloc `using` afin que le flux soit correctement libéré.
4. Appelez `worksheet.Pictures.Add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage pour que l'image couvre uniquement la cellule C6 : `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Définissez `picture.Placement = PlacementType.MoveAndSize` pour que l'image reste alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple aux cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Approche 2 : Intégrer une image directement dans une cellule**
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `Cell.EmbeddedImage`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu intégré.

### **Comment fonctionnent les images intégrées**
- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur le calque de dessin.
- L'image se redimensionne automatiquement pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule avec une véritable adresse, qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau des cellules.
Cela fait de `Cell.EmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui réside dans cette cellule ».

### **Instructions étape par étape**
1. Créez un nouveau `Workbook` (ou ouvrez un classeur existant).
2. Accédez à la `Worksheet` cible via `workbook.Worksheets[0]`.
3. Lisez le fichier image depuis le disque dans un tableau `byte[]` (par exemple, à l'aide de `File.ReadAllBytes`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.Cells["C6"]`, soit via `worksheet.Cells[5, 2]`.
5. Affectez le tableau d'octets à la propriété `EmbeddedImage` de la cellule.
6. Ajustez éventuellement la hauteur de la ligne et la largeur de la colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus proéminente.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Obtenir la cellule cible C6
var cell = worksheet.Cells["C6"];
// Lire le fichier image dans un tableau d'octets
byte[] imageData = File.ReadAllBytes("logo.png");
// Incorporer l'image directement dans la cellule
cell.EmbeddedImage = imageData;
// Ajuster éventuellement la hauteur de ligne et la largeur de colonne pour que l'image intégrée soit plus visible
worksheet.Cells.SetColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Ligne 6 (index 5)
// Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Choisir la bonne approche**
Les deux approches produisent une image qui s'inscrit dans une seule cellule, mais elles diffèrent par la manière dont l'image est stockée et dont elle se comporte :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme qui peut être sélectionnée, réorganisée ou groupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité ascendante avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous avez besoin de calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.
- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit accompagner la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.
{{% /alert %}}

{{% /alert %}}

## Articles connexes
- [Caméra Excel dans Aspose.Cells for .NET](/cells/fr/net/excel-camera/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)
- [Convertir une sparkline en image et HTML dans Aspose.Cells for .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)`csharp

{{< app/cells/assistant language="csharp" >}}