---
title: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes, placer une image flottante au-dessus de la cellule, ou intégrer l'image directement dans la cellule.
keywords: Aspose.Cells, NET library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells propose deux manières distinctes d'associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et se met à l'échelle automatiquement par rapport à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à la taille d'une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter obtenir une image nette, liée à la cellule, qui reste alignée avec la cellule à laquelle elle appartient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante au-dessus d'une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez son `Placement` sur `MoveAndSize`, et ajustez ses cellules d'ancrage (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) de sorte que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `EmbeddedImage` de la cellule. L'image se met à l'échelle automatiquement pour s'adapter à la zone d'affichage de la cellule et se déplace avec la cellule.

La suite de cet article présente les deux approches, explique les API concernées, et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image au-dessus d'une cellule**

Une image flottante est un objet `Picture` qui réside sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule particulière, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une cellule**, vous devez :

1. Ajouter l'image en utilisant `Worksheet.Pictures.Add(int row, int column, Stream stream)`, qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d'ancrage de sorte que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.Placement` sur `PlacementType.MoveAndSize` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index à base zéro :

- `Picture.UpperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `Picture.UpperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `Picture.LowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.LowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

Par exemple, pour ajuster l'image exactement à la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, et `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Les indices de ligne et de colonne dans Aspose.Cells sont **à base zéro**. La cellule C6 a pour index de ligne 5 et pour index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

{{% /alert %}}

### **Contrôle du comportement de placement**

`Picture.Placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui provoque le déplacement et le redimensionnement de l'image conjointement avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez un classeur existant).
2. Accédez à la `Worksheet` cible via `workbook.Worksheets[0]`.
3. Ouvrez le fichier image depuis le disque dans un `FileStream` en utilisant un bloc `using` afin que le flux soit correctement libéré.
4. Appelez `worksheet.Pictures.Add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Conservez la référence `Picture` retournée.
5. Définissez les quatre coordonnées d'ancrage de sorte que l'image ne couvre que la cellule C6 : `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Définissez `picture.Placement = PlacementType.MoveAndSize` pour maintenir l'image alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

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

Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `Cell.EmbeddedImage`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu en ligne.

### **Fonctionnement des images intégrées**

- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur la couche de dessin.
- L'image se met à l'échelle automatiquement pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule avec une véritable adresse qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `Cell.EmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui vit dans cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez un classeur existant).
2. Accédez à la `Worksheet` cible via `workbook.Worksheets[0]`.
3. Lisez le fichier image depuis le disque dans un tableau `byte[]` (par exemple, en utilisant `File.ReadAllBytes`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.Cells["C6"]`, soit via `worksheet.Cells[5, 2]`.
5. Affectez le tableau d'octets à la propriété `EmbeddedImage` de la cellule.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus visible.
7. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Obtenir la cellule cible C6
var cell = worksheet.Cells["C6"];

// Lire le fichier image dans un tableau d'octets
byte[] imageData = File.ReadAllBytes("logo.png");

// Intégrer l'image directement dans la cellule
cell.EmbeddedImage = imageData;

// Ajuster éventuellement la hauteur de ligne et la largeur de colonne pour que l'image intégrée soit plus visible
worksheet.Cells.SetColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Ligne 6 (index 5)

// Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'inscrit dans une seule cellule, mais elles diffèrent dans la manière dont l'image est stockée et dans son comportement :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réorganisée ou regroupée avec d'autres formes.
  - Vous exigez une compatibilité ascendante avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.

- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes au-dessus d'un ensemble de cellules et intégrer des images directement dans d'autres cellules, car les deux mécanismes utilisent des couches de stockage différentes dans le fichier.

{{% /alert %}}

## **Articles connexes**

- [Comment insérer une image dans une cellule](/cells/fr/net/how-to-place-image-to-cell/)
- [Comment ajuster une image à la largeur et à la hauteur d'une cellule](/cells/fr/net/how-to-fit-image-to-cell-width-height/)
- [Ajouter des hyperliens d'image](/cells/fr/net/add-image-hyperlinks/)
- [Charger une image web depuis une URL dans une feuille de calcul Excel](/cells/fr/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipuler la position, la taille et le graphique du concepteur](/cells/fr/net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="csharp" >}}