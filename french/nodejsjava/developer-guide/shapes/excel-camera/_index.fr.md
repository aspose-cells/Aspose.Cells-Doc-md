---
title: Caméra Excel dans Aspose.Cells for Node.js via Java
linktitle: Caméra Excel dans Aspose.Cells for Node.js via Java
description: Apprenez à utiliser la Caméra Excel dans Aspose.Cells for Node.js via Java pour créer une image dynamique liée à une plage de cellules qui s'actualise avec les données sources et préserve toute la mise en forme source.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Caméra Excel, image dynamique, image liée, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /fr/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Caméra Excel est un objet de feuille de calcul qui affiche une image dynamique d'une plage de cellules et flotte sur la couche de dessin comme une image ordinaire. Aspose.Cells prend en charge deux modes de création : une image dynamique qui s'actualise automatiquement lorsque les données sources changent, et une image statique qui capture un instantané ponctuel d'une plage. Cet article présente les deux approches afin que vous puissiez choisir celle qui convient à votre mise en page.

## Qu'est-ce que la Caméra Excel ?
La Caméra Excel est essentiellement un objet image ancré à une ligne et une colonne spécifiques sur la couche de dessin de la feuille de calcul. Contrairement à une image insérée classique, la Caméra est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Chaque fois qu'une cellule de cette plage change, l'image de la Caméra s'actualise automatiquement pour refléter le nouveau contenu. La Caméra préserve la mise en forme complète de la zone source — bordures, couleurs d'arrière-plan, polices et formats de nombres — ainsi, tout ce qui est visible dans les cellules apparaît également dans l'image de la Caméra. Cela rend la Caméra particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez un aperçu visible d'une région distante sans défilement ni répétition des données. Deux mises en garde s'appliquent : vous devez appeler `updateSelectedValue()` avant d'enregistrer le classeur, et le fichier sera exporté en HTML ou PDF, car ces formats s'appuient sur les données d'image intégrées plutôt que sur un recalcul en temps réel.

## Méthode 1 — Ajouter une image de Caméra dynamique
La Caméra dynamique est l'approche la plus courante et correspond le mieux à l'outil Caméra intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu initial, puis en lui attribuant une `Formula` qui référence la plage source. Une fois la formule attribuée, l'appel de `updateSelectedValue()` actualise les données d'image intégrées pour qu'elles soient synchronisées avec les cellules qu'elles reflètent. La Caméra n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type standard `Picture`.
Les API clés sont :
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Passer `null` pour le paramètre `stream` crée une image vide qui sert d'espace réservé pour une Caméra dynamique. La méthode retourne l'index de la nouvelle image.
- `worksheet.getPictures().get(index)` — accès via indexeur pour récupérer une `Picture` spécifique de la collection.
- `Picture.Formula` — propriété de chaîne (`getFormula()`/`setFormula()`) contenant la référence de style A1 à la plage source que la Caméra reflète, telle que `"A1:F10"`.
- `Picture.updateSelectedValue()` — méthode vide qui actualise les données d'image intégrées à partir des cellules référencées par `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DOIT être appelé avant l'enregistrement lorsque la sortie est HTML ou PDF ; sinon le fichier exporté ne contiendra pas les données d'image et la Caméra apparaîtra vide dans la sortie rendue.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 colonne 6, la lie à la plage source `A1:F10` via la propriété `Formula`, actualise les données d'image intégrées et enregistre le classeur.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Caméra dynamique : ajouter une image vide, la lier via une formule à A1:F10, puis actualiser
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## Méthode 2 — Ajouter une image de Caméra statique
La Caméra statique est essentiellement un aperçu rendu une seule fois d'une plage de cellules. Plutôt que de maintenir un lien dynamique, vous rendez la plage en octets d'image une seule fois, enveloppez ces octets dans un `ByteArrayInputStream` et les ajoutez comme une image classique. Le contenu de l'image est alors figé au moment de la création et ne s'actualise pas automatiquement lorsque les cellules sources changent.
Les API clés sont :
- `Cells.createRange(String address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rend la plage en octets d'image. Passer `null` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `new ByteArrayInputStream(byte[] buffer)` — enveloppe les octets d'image rendus dans un `ByteArrayInputStream` qui peut être fourni à `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — ajoute l'image ancrée à la ligne et à la colonne indiquées, cette fois en passant le `ByteArrayInputStream` produit par le rendu.
Le code suivant crée un classeur, construit un `Range` pour `A1:F10`, le rend en octets d'image via `range.toImage(null)`, enveloppe les octets dans un `ByteArrayInputStream`, ajoute l'image ancrée à la ligne 10 colonne 6, et enregistre le classeur.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Caméra Statique : construire une Range, rendre en octets, envelopper dans ByteArrayInputStream, ajouter comme image
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## Choisir entre dynamique et statique
- **Caméra dynamique :** s'actualise à chaque recalcul, prend en charge l'export HTML et PDF après `updateSelectedValue()`, et préserve le comportement de lien dynamique tout au long de la durée de vie du fichier.
- **Caméra statique :** un rendu ponctuel qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel figé intégré au moment de la génération plutôt qu'un miroir dynamique des données.
Aspose.Cells prend en charge à la fois une Caméra dynamique à actualisation automatique construite sur `Picture.Formula` plus `updateSelectedValue()` et une Caméra statique à usage unique construite sur `Range.toImage` plus un `ByteArrayInputStream`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules sources, et choisissez l'approche statique lorsque vous n'avez besoin que d'un instantané visuel figé au moment de la génération.

{{< app/cells/assistant language="nodejs-java" >}}