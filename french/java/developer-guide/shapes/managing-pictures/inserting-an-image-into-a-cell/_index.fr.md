---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Java permettant de travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à une seule cellule, soit en plaçant une image flottante par-dessus la cellule, soit en intégrant l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, insérer une image, intégrer une image, image dans une cellule, ajuster une image à une cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul qui se superpose visuellement à une plage de cellules, tandis qu'une image intégrée est stockée dans la cellule elle-même et se met à l'échelle automatiquement par rapport à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

## **Introduction**
Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée avec la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante par-dessus une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `Placement` sur `MOVE_AND_SIZE`, et ajustez ses cellules d'ancrage (`getUpperLeftRow`, `getUpperLeftColumn`, `getLowerRightRow`, `getLowerRightColumn`) de sorte que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image au setter `getEmbeddedImage()` de la cellule. L'image se met à l'échelle automatiquement pour s'adapter à la zone d'affichage de la cellule et accompagne la cellule.
La suite de cet article présente les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approach 1: Place a Picture Over a Cell**
Une image flottante est un objet `Picture` qui réside sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.
Pour qu'une image flottante couvre **exactement une cellule**, vous devez :
1. Ajouter l'image à l'aide de `Worksheet.getPictures().add(int row, int column, InputStream stream)`, ce qui ancre la nouvelle image à la cellule spécifiée.
2. Définir les quatre propriétés d'ancrage afin que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.setPlacement()` sur `PlacementType.MOVE_AND_SIZE` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Anchoring the Picture to a Single Cell**
L'ancrage de l'image est défini par quatre propriétés d'index basées sur zéro :
- `Picture.getUpperLeftRow()` — l'index de ligne du bord supérieur de l'image.
- `Picture.getUpperLeftColumn()` — l'index de colonne du bord gauche de l'image.
- `Picture.getLowerRightRow()` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.getLowerRightColumn()` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

{{% alert color="primary" %}}
Les index de ligne et de colonne dans Aspose.Cells sont **basés sur zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs de décalage d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent chevaucher une cellule adjacente.

### **Controlling Placement Behavior**
`Picture.getPlacement()` renvoie une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui provoque le déplacement et le redimensionnement de l'image conjointement avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Step-by-Step Instructions**
1. Créer un nouveau `Workbook` (ou en ouvrir un existant).
2. Accéder à la `Worksheet` cible à partir de `workbook.getWorksheets().get(0)`.
3. Ouvrir le fichier image depuis le disque dans un `InputStream` (tel qu'un `FileInputStream`) en utilisant un bloc try-with-resources afin que le flux soit correctement fermé.
4. Appeler `worksheet.getPictures().add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturer la référence `Picture` renvoyée.
5. Définir les quatre coordonnées d'ancrage pour que l'image couvre uniquement la cellule C6 : `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Définir `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` pour maintenir l'image alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Optionnellement, ajouter du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrer le classeur sur le disque sous forme de fichier `.xlsx`.
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

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells expose également un mécanisme plus simple pour les images liées aux cellules : la méthode `Cell.setEmbeddedImage(byte[])`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait de contenu en ligne.

### **How Embedded Images Work**
- L'image est stockée comme partie du contenu de la cellule plutôt que comme forme sur la couche de dessin.
- L'image se met à l'échelle automatiquement pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de positionnement n'est requis.
- La cellule reste une véritable cellule avec une véritable adresse qui peut être référencée par des formules, triée comme partie d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.
Cela fait de `setEmbeddedImage()` l'option la plus concise lorsque votre objectif est simplement « une image qui vit à l'intérieur de cette cellule ».

### **Step-by-Step Instructions**
1. Créer un nouveau `Workbook` (ou en ouvrir un existant).
2. Accéder à la `Worksheet` cible à partir de `workbook.getWorksheets().get(0)`.
3. Lire le fichier image depuis le disque dans un tableau `byte[]` (par exemple, en lisant le fichier via `Files.readAllBytes()` de `java.nio.file`).
4. Obtenir une référence à la cellule cible — soit via `worksheet.getCells().get("C6")` soit via `worksheet.getCells().get(5, 2)`.
5. Affecter le tableau d'octets à la cellule à l'aide de `cell.setEmbeddedImage(bytes)`.
6. Optionnellement, ajuster la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus proéminente.
7. Enregistrer le classeur sur le disque sous forme de fichier `.xlsx`.
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
// Ajuster éventuellement la hauteur de ligne et la largeur de colonne pour que l'image incorporée soit plus visible
worksheet.getCells().setColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Ligne 6 (index 5)
// Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **Choosing the Right Approach**
Les deux approches produisent une image qui s'insère dans une seule cellule, mais elles diffèrent par la manière dont l'image est stockée et dont elle se comporte :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le positionnement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réorganisée ou regroupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité héritée avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer les coordonnées d'ancrage de manière dynamique en fonction de la disposition de la feuille de calcul.
- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit accompagner la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image comme une forme.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for Java](/cells/fr/java/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Java](/cells/fr/java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Java](/cells/fr/java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/fr/java/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Java](/cells/fr/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}