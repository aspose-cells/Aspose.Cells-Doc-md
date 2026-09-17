---
title: Caméra Excel dans Aspose.Cells for Java
linktitle: Caméra Excel dans Aspose.Cells for Java
description: Apprenez à utiliser la Caméra Excel dans Aspose.Cells for Java pour créer une image dynamique liée à une plage de cellules qui se rafraîchit avec les données sources et préserve toute la mise en forme d'origine.
keywords: Aspose.Cells, Java, Caméra Excel, image dynamique, image liée, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /fr/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Caméra Excel est un objet de feuille de calcul qui restitue une image dynamique d'une plage de cellules et qui flotte sur le calque de dessin comme une image ordinaire. Aspose.Cells prend en charge deux modes de création : une image dynamique qui se rafraîchit automatiquement à chaque modification des données sources, et une image statique qui capture un instantané ponctuel d'une plage. Cet article présente ces deux approches afin que vous puissiez choisir celle qui correspond à votre mise en page.

## What Is Excel Camera?
La Caméra Excel est essentiellement un objet image ancré à une ligne et une colonne spécifiques du calque de dessin de la feuille de calcul. Contrairement à une image insérée classique, la Caméra est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Chaque fois qu'une cellule de cette plage change, l'image de la Caméra est rafraîchie automatiquement pour refléter le nouveau contenu. La Caméra préserve la mise en forme complète de la zone source — bordures, couleurs d'arrière-plan, polices et formats numériques — de sorte que tout ce qui est visible à l'intérieur des cellules apparaît également dans l'image de la Caméra. Cela rend la Caméra particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez obtenir un aperçu visible d'une zone distante sans défilement ni répétition des données. Deux points importants s'appliquent : vous devez appeler `updateSelectedValue()` avant d'enregistrer le classeur, et le fichier sera exporté au format HTML ou PDF, car ces formats reposent sur les données d'image intégrées plutôt que sur un recalcul dynamique.

## Method 1 — Add a Dynamic Camera Picture
La Caméra dynamique est l'approche la plus courante et la plus proche de l'outil Caméra intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu initial, puis en lui attribuant une `Formula` qui référence la plage source. Une fois la formule assignée, l'appel à `updateSelectedValue()` rafraîchit les données d'image intégrées pour qu'elles soient synchronisées avec les cellules qu'elle reflète. La Caméra n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type standard `Picture`.
Les API clés sont :
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Passer `null` pour le paramètre `stream` crée une image vide qui sert d'espace réservé pour une Caméra dynamique. La méthode renvoie l'index de la nouvelle image.
- `worksheet.getPictures().get(index)` — accès par indexeur pour récupérer une `Picture` spécifique de la collection.
- `Picture.setFormula(String value)` — définit la référence de style A1 vers la plage source que la Caméra reflète, telle que `"A1:F10"`.
- `Picture.updateSelectedValue()` — une méthode void qui rafraîchit les données d'image intégrées à partir des cellules référencées par `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DOIT être appelé avant l'enregistrement lorsque la sortie est HTML ou PDF ; sinon le fichier exporté ne contiendra pas les données de l'image et la Caméra apparaîtra vide dans le rendu.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 colonne 6, la lie à la plage source `A1:F10` via `setFormula`, rafraîchit les données d'image intégrées et enregistre le classeur.

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## Method 2 — Add a Static Camera Picture
La Caméra statique est essentiellement un aperçu rendu une seule fois d'une plage de cellules. Au lieu de maintenir un lien dynamique, vous rendez la plage en octets d'image une seule fois, enveloppez ces octets dans un `ByteArrayInputStream`, puis les ajoutez en tant qu'image classique. Le contenu de l'image est alors figé au moment de la création et ne se rafraîchit pas automatiquement lorsque les cellules sources changent.
Les API clés sont :
- `Cells.createRange(String address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rend la plage en octets d'image. Passer `null` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `new ByteArrayInputStream(byte[] buffer)` — enveloppe les octets d'image rendus dans un `ByteArrayInputStream` qui peut être transmis à `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — ajoute l'image ancrée à la ligne et à la colonne indiquées, en transmettant cette fois le `ByteArrayInputStream` produit par le rendu.
Le code suivant crée un classeur, construit une `Range` pour `A1:F10`, la rend en octets d'image via `Range.toImage(null)`, enveloppe les octets dans un `ByteArrayInputStream`, ajoute l'image ancrée à la ligne 10 colonne 6 et enregistre le classeur.

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## Choosing Between Dynamic and Static
- **Caméra dynamique :** se met à jour à chaque recalcul, prend en charge l'export HTML et PDF après `updateSelectedValue()`, et conserve le comportement de lien dynamique pendant toute la durée de vie du fichier.
- **Caméra statique :** un rendu ponctuel qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel fixe intégré au moment de la génération plutôt qu'un reflet dynamique des données.
Aspose.Cells prend en charge à la fois une Caméra dynamique à rafraîchissement automatique construite sur `Picture.Formula` plus `updateSelectedValue()`, et une Caméra statique en un seul tir construite sur `Range.toImage` plus un `ByteArrayInputStream`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules sources, et choisissez l'approche statique lorsque vous n'avez besoin que d'un instantané visuel fixe au moment de la génération.

## Related Articles
- [Convertir un sparkline en image et HTML dans Aspose.Cells for Java](/cells/fr/java/convert-sparkline-to-image-and-html/)
- [Insertion d'une image dans une cellule](/cells/fr/java/inserting-an-image-into-a-cell/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Java](/cells/fr/java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for Java](/cells/fr/java/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/java/change-page-field-layout/)

{{< app/cells/assistant language="java" >}}