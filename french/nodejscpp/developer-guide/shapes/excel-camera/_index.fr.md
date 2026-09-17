---
title: Excel Camera dans Aspose.Cells for Node.js via C++
linktitle: Excel Camera dans Aspose.Cells for Node.js via C++
description: Apprenez à utiliser Excel Camera dans Aspose.Cells for Node.js via C++ pour créer une image dynamique liée à une plage de cellules qui se rafraîchit avec les données sources et préserve toute la mise en forme source.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel Camera, image dynamique, image liée, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /fr/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera est un objet de feuille de calcul qui restitue une image en direct d'une plage de cellules et flotte sur la couche de dessin comme une image ordinaire. Aspose.Cells prend en charge deux modes de création, une image dynamique qui se rafraîchit automatiquement dès que les données sources changent et une image statique qui capture un instantané ponctuel d'une plage. Cet article présente les deux approches afin que vous puissiez choisir celle qui correspond à votre mise en page.

## Qu'est-ce qu'Excel Camera ?
Excel Camera est essentiellement un objet image ancré à une ligne et une colonne spécifiques sur la couche de dessin de la feuille de calcul. Contrairement à une image insérée classique, l'Excel Camera est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Chaque fois qu'une cellule de cette plage change, l'image de l'Excel Camera est rafraîchie automatiquement pour refléter le nouveau contenu. L'Excel Camera préserve toute la mise en forme de la zone source — bordures, couleurs d'arrière-plan, polices et formats numériques — de sorte que tout ce qui est visible dans les cellules apparaît également dans l'image de l'Excel Camera. Cela rend l'Excel Camera particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez un aperçu visible d'une région éloignée sans faire défiler ni répéter les données. Deux mises en garde s'appliquent : vous devez appeler `updateSelectedValue()` avant d'enregistrer le classeur, et le fichier sera exporté au format HTML ou PDF, car ces formats reposent sur les données d'image intégrées plutôt que sur un recalcul en direct.

## Méthode 1 — Ajouter une image dynamique de l'Excel Camera
L'Excel Camera dynamique est l'approche la plus courante et correspond le mieux à l'outil Excel Camera intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu initial, puis en lui attribuant une `Formula` qui référence la plage source. Une fois la formule attribuée, l'appel de `updateSelectedValue()` rafraîchit les données d'image intégrées pour qu'elles soient synchronisées avec les cellules qu'elles reflètent. L'Excel Camera n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type standard `Picture`.
Les API clés sont :
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — ajoute une image ancrée à la ligne et à la colonne données. Passer `null` pour le paramètre `stream` crée une image vide qui sert d'espace réservé pour une Excel Camera dynamique. La méthode retourne l'index de la nouvelle image.
- `pictures.get(index)` — récupère une `Picture` spécifique de la collection par index.
- `Picture.formula` — une propriété de chaîne de caractères (get/set) contenant la référence de style A1 à la plage source que l'Excel Camera reflète, telle que `"A1:F10"`.
- `Picture.updateSelectedValue()` — une méthode vide qui rafraîchit les données d'image intégrées à partir des cellules référencées par `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DOIT être appelée avant l'enregistrement lorsque la sortie est au format HTML ou PDF ; sinon le fichier exporté ne contiendra pas les données d'image et l'Excel Camera apparaîtra vide dans la sortie rendue.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 colonne 6, la lie à la plage source `A1:F10` via la propriété `Formula`, rafraîchit les données d'image intégrées et enregistre le classeur.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Caméra Dynamique : ajouter une image vide, la lier via Formule à A1:F10, puis actualiser
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Méthode 2 — Ajouter une image statique de l'Excel Camera
L'Excel Camera statique est essentiellement un aperçu rendu une seule fois d'une plage de cellules. Au lieu de maintenir un lien en direct, vous restituez la plage en octets d'image une fois, enveloppez ces octets dans une `Buffer` et les ajoutez comme une image classique. Le contenu de l'image est alors fixé au moment de la création et ne se rafraîchit pas automatiquement lorsque les cellules sources changent.
Les API clés sont :
- `Cells.createRange(address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — restitue la plage en octets d'image. Passer `null` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `new Buffer(byte[] buffer)` — enveloppe les octets d'image rendus dans une `Buffer` qui peut être alimentée à `getPictures().add`.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — ajoute l'image ancrée à la ligne et à la colonne données, en passant cette fois la `Buffer` produite par le rendu.
Le code suivant crée un classeur, construit une `Range` pour `A1:F10`, la restitue en octets d'image via `range.toImage(null)`, enveloppe les octets dans une `Buffer`, ajoute l'image ancrée à la ligne 10 colonne 6, et enregistre le classeur.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Camera statique : construire la plage, rendre en octets, envelopper dans un MemoryStream, ajouter comme image
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Choisir entre dynamique et statique
- **Excel Camera dynamique :** se met à jour à chaque recalcul, prend en charge l'export HTML et PDF après `updateSelectedValue()`, et préserve le comportement de lien en direct tout au long de la durée de vie du fichier.
- **Excel Camera statique :** un rendu ponctuel qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel fixe intégré au moment de la génération plutôt qu'un miroir en direct des données.
Aspose.Cells prend en charge à la fois une Excel Camera dynamique à rafraîchissement automatique construite sur `Picture.formula` plus `updateSelectedValue()` et une Excel Camera statique à capture unique construite sur `Range.toImage` plus une `Buffer`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules sources, et choisissez l'approche statique lorsque vous avez uniquement besoin d'un instantané visuel fixe au moment de la génération.

{{< app/cells/assistant language="nodejs-cpp" >}}