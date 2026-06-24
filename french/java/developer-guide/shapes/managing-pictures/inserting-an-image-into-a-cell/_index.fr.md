---
title: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Java pour travailler avec des fichiers de tableur. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes, placer une image flottante sur la cellule, ou intégrer l'image directement dans la cellule.
keywords: Aspose.Cells, Java library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme sur la couche de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et s'adapte automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos besoins de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de tableurs servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer librement sur une feuille de calcul, vous pouvez souhaiter une image propre, liée à la cellule, qui reste alignée avec la cellule qui la contient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `Placement` sur `MOVE_AND_SIZE`, et ajustez ses cellules d'ancrage (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) pour que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image au setter `getEmbeddedImage()` de la cellule. L'image s'adapte automatiquement à la zone d'affichage de la cellule et se déplace avec elle.

Le reste de cet article présente les deux approches, explique les API concernées et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image sur une cellule**

Une image flottante est un objet `Picture` qui se trouve sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule à proprement parler, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une cellule**, vous devez :

1. Ajouter l'image en utilisant `Worksheet.getPictures().add(int row, int column, InputStream stream)`, qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage pour que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.setPlacement()` sur `PlacementType.MOVE_AND_SIZE` pour que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index de base zéro :

- `Picture.getUpperLeftRow()` — l'index de ligne du bord supérieur de l'image.
- `Picture.getUpperLeftColumn()` — l'index de colonne du bord gauche de l'image.
- `Picture.getLowerRightRow()` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.getLowerRightColumn()` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

Par exemple, pour ajuster l'image exactement dans la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)` et `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Les index de ligne et de colonne dans Aspose.Cells sont **de base zéro**. La cellule C6 a pour index de ligne 5 et index de colonne 2. Les erreurs d'une unité sur l'ancre inférieure droite sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

{{% /alert %}}

### **Contrôle du comportement de placement**

`Picture.getPlacement()` renvoie une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui fait que l'image se déplace et se redimensionne avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Ouvrez le fichier image depuis le disque dans un `InputStream` (tel qu'un `FileInputStream`) en utilisant un bloc try-with-resources afin que le flux soit correctement fermé.
4. Appelez `worksheet.getPictures().add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage pour que l'image ne couvre que la cellule C6 : `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Définissez `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` pour maintenir l'image alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}

workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Approche 2 : Intégrer une image directement dans une cellule**

Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la méthode `Cell.setEmbeddedImage(byte[])`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu en ligne.

### **Fonctionnement des images intégrées**

- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur la couche de dessin.
- L'image s'adapte automatiquement aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une vraie cellule avec une vraie adresse qui peut être référencée par des formules, triée dans une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `setEmbeddedImage()` l'option la plus concise lorsque votre objectif est simplement « une image qui vit à l'intérieur de cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Lisez le fichier image depuis le disque dans un tableau `byte[]` (par exemple, en lisant le fichier via `Files.readAllBytes()` de `java.nio.file`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.getCells().get("C6")`, soit via `worksheet.getCells().get(5, 2)`.
5. Affectez le tableau d'octets à la cellule en utilisant `cell.setEmbeddedImage(bytes)`.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus visible.
7. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Obtenir la cellule cible C6
Cell cell = worksheet.getCells().get("C6");

// Lire le fichier image dans un tableau d'octets
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));

// Incorporer l'image directement dans la cellule
cell.setEmbeddedImage(imageData);

// Optionnellement ajuster la hauteur de la ligne et la largeur de la colonne pour que l'image intégrée soit plus visible
worksheet.getCells().setColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Ligne 6 (index 5)

// Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'insère dans une seule cellule, mais elles diffèrent par la manière dont l'image est stockée et dont elle se comporte :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réordonnée ou groupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité descendante avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la mise en page de la feuille de calcul.

- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes sur un ensemble de cellules et intégrer des images directement dans d'autres cellules, car les deux mécanismes utilisent des couches de stockage différentes dans le fichier.

{{% /alert %}}



{{< app/cells/assistant language="java" >}}