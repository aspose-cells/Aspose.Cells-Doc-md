---
title: Insertion d’une image dans une cellule
linktitle: Insertion d’une image dans une cellule
description: Aspose.Cells est une bibliothèque Java permettant de travailler avec des fichiers de tableur. Cet article explique comment ajuster exactement une image à une seule cellule, soit en plaçant une image flottante sur la cellule, soit en incorporant l’image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, insertion d’une image, incorporation d’une image, image dans une cellule, ajustement d’une image à une cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux Ways distinctes d’associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul et qui se superpose visuellement à une plage de cellules, tandis qu’une image incorporée est stockée dans la cellule elle-même et se redimensionne automatiquement pour s’adapter à la zone d’affichage de la cellule. Choisissez l’approche qui correspond le mieux à vos exigences de mise en page.
{{% /alert %}}

## **Introduction**
L’ajustement exact d’une image à une seule cellule est une exigence courante lors de la conception de feuilles de calcul qui servent de rapports visuels, de catalogues de produits, de répertoires d’employés, de tableaux de bord ou de listes d’inventaire. Au lieu d’étirer une image sur de nombreuses cellules ou de la placer sans contrainte sur une feuille de calcul, vous pouvez vouloir une image nette, liée à une cellule et maintenue alignée sur la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez sa propriété `Placement` sur `MOVE_AND_SIZE`, puis ajustez ses cellules d’ancrage (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) afin que l’image couvre exactement une cellule.
- **Approche 2 — Incorporer une image directement dans une cellule.** Affectez les octets de l’image à l’accesseur `getEmbeddedImage()` de la cellule. L’image est automatiquement redimensionnée pour s’adapter à la zone d’affichage de la cellule et se déplace avec elle.
La suite de cet article présente les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image flottante sur une cellule**
Une image flottante est un objet `Picture` qui se trouve sur la couche de dessin de la feuille de calcul. Bien qu’elle ne fasse partie d’aucune cellule précise, elle est ancrée à une plage de cellules. Les cellules d’ancrage de l’image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s’étend sur plusieurs cellules.
Pour faire couvrir à une image flottante **exactement une cellule**, vous devez :
1. Ajouter l’image à l’aide de `Worksheet.getPictures().add(int row, int column, InputStream stream)`, ce qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d’ancrage afin que le rectangle englobant de l’image coïncide avec la cellule cible.
3. Affecter à `Picture.setPlacement()` la valeur `PlacementType.MOVE_AND_SIZE` afin que l’image se déplace et se redimensionne avec la cellule sous-jacente lorsque l’utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l’image à une seule cellule**
L’ancrage de l’image est défini par quatre propriétés d’indexation utilisant une base zéro :
- `Picture.getUpperLeftRow()` — l’index de ligne du bord supérieur de l’image.
- `Picture.getUpperLeftColumn()` — l’index de colonne du bord gauche de l’image.
- `Picture.getLowerRightRow()` — l’index de ligne du bord inférieur de l’image. Pour que le bord inférieur de l’image se situe au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.getLowerRightColumn()` — l’index de colonne du bord droit de l’image. Pour que le bord droit de l’image se situe à l’extrémité droite de la colonne `c`, définissez cette valeur sur `c + 1`.

{{% alert color="primary" %}}
Les indices de ligne et de colonne dans Aspose.Cells sont **basés sur zéro**. La cellule C6 possède l’index de ligne 5 et l’index de colonne 2. Les décalages d’une unité au niveau de l’ancrage inférieur droit sont la cause la plus fréquente d’images qui semblent recouvrir la cellule adjacente.
{{% /alert %}}

### **Contrôle du comportement de placement**
`Picture.getPlacement()` renvoie une énumération de type `PlacementType` qui contrôle le comportement de l’image lorsque l’utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image occupant une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui fait que l’image se déplace et se redimensionne avec sa cellule sous-jacente, tout en conservant son ajustement exact.

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible à partir de `workbook.getWorksheets().get(0)`.
3. Ouvrez le fichier d’image sur le disque dans un `InputStream` (tel qu’un `FileInputStream`) à l’aide d’un bloc try-with-resources, afin que le flux soit correctement fermé.
4. Appelez `worksheet.getPictures().add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Récupérez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d’ancrage afin que l’image couvre uniquement la cellule C6 : `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Définissez `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` pour maintenir l’image alignée sur C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d’exemple dans les cellules voisines afin d’illustrer que seule la cellule C6 contient l’image.
8. Enregistrez le classeur sur le disque dans un fichier `.xlsx`.
Le code suivant illustre l’approche complète.

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

## **Approche 2 : Incorporer une image directement dans une cellule**
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la méthode `Cell.setEmbeddedImage(byte[])`. L’affectation d’octets d’image à cette propriété attache l’image à la cellule elle-même, comme s’il s’agissait de contenu intégré.

### **Fonctionnement des images incorporées**
- L’image est stockée dans le contenu de la cellule plutôt que sous la forme d’une forme sur la couche de dessin.
- L’image est automatiquement redimensionnée pour s’adapter à l’intérieur des limites affichées de la cellule. Aucune coordonnée d’ancrage ni aucun paramètre de placement n’est requis.
- La cellule reste une véritable cellule, avec une adresse réelle, pouvant être référencée par des formules, triée avec les autres cellules d’une ligne ou utilisée dans d’autres opérations au niveau de la cellule.
Cela fait de `setEmbeddedImage()` l’option la plus concise lorsque votre objectif est simplement d’obtenir « une image qui réside dans cette cellule ».

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible à partir de `workbook.getWorksheets().get(0)`.
3. Lisez le fichier d’image sur le disque dans un tableau `byte[]` (par exemple, en lisant le fichier à l’aide de `Files.readAllBytes()` à partir de `java.nio.file`).
4. Obtenez une référence vers la cellule cible, soit avec `worksheet.getCells().get("C6")`, soit avec `worksheet.getCells().get(5, 2)`.
5. Affectez le tableau d’octets à la cellule avec `cell.setEmbeddedImage(bytes)`.
6. Ajustez éventuellement la hauteur de la ligne et la largeur de la colonne ciblées afin de rendre l’image incorporée plus saillante.
7. Enregistrez le classeur sur le disque dans un fichier `.xlsx`.
Le code suivant illustre l’approche complète.

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
// Intégrer directement l'image dans la cellule
cell.setEmbeddedImage(imageData);
// Facultativement, ajuster la hauteur des lignes et la largeur des colonnes afin de mieux afficher l'image intégrée
worksheet.getCells().setColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Ligne 6 (index 5)
// Enregistrer le classeur obtenu dans un fichier .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Choix de l’approche appropriée**
Les deux approches produisent une image qui tient dans une seule cellule, mais elles diffèrent par le mode de stockage de l’image et par son comportement :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d’un contrôle plus précis du placement, de l’ordre de superposition ou de l’alignement avec d’autres objets de dessin.
  - Vous souhaitez que l’image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d’autres formes.
  - Vous devez assurer la rétrocompatibilité avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer dynamiquement les coordonnées d’ancrage en fonction de la disposition de la feuille de calcul.
- **Utilisez une image incorporée (Approche 2) lorsque :**
  - Vous souhaitez effectuer l’insertion la plus simple possible d’une image dans une cellule.
  - L’image doit se déplacer avec la cellule comme tout autre contenu de cellule.

## Articles connexes
- [Caméra Excel dans Aspose.Cells for Java](/cells/fr/java/excel-camera/)

{{< app/cells/assistant language="java" >}}