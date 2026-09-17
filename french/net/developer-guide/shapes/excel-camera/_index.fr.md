---
title: Excel Camera in Aspose.Cells for .NET
linktitle: Excel Camera
description: Learn how to use Excel Camera in Aspose.Cells for .NET to create a dynamic picture linked to a cell range that refreshes with the source data and preserves all source formatting.
keywords: Aspose.Cells, .NET, Excel Camera, dynamic picture, linked picture, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /fr/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Caméra Excel est un objet de feuille de calcul qui restitue une image en direct d'une plage de cellules et flotte sur la couche de dessin comme une image ordinaire. Aspose.Cells prend en charge deux modes de création : une image dynamique qui se rafraîchit automatiquement à chaque changement des données source, et une image statique qui capture un instantané ponctuel d'une plage. Cet article présente les deux approches afin que vous puissiez choisir celle qui correspond à votre mise en page.

## Qu'est-ce que la Caméra Excel ?
La Caméra Excel est essentiellement un objet image ancré à une ligne et à une colonne spécifiques sur la couche de dessin de la feuille de calcul. Contrairement à une image insérée ordinaire, la Caméra est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Chaque fois qu'une cellule à l'intérieur de cette plage change, l'image de la Caméra est rafraîchie automatiquement pour refléter le nouveau contenu. La Caméra préserve la mise en forme complète de la zone source — bordures, couleurs d'arrière-plan, polices et formats numériques — de sorte que tout ce qui est visible à l'intérieur des cellules apparaît également dans l'image de la Caméra. Cela rend la Caméra particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez un aperçu visible d'une région éloignée sans défilement ni répétition des données. Deux mises en garde s'appliquent : vous devez appeler `UpdateSelectedValue()` avant d'enregistrer le classeur, et le fichier sera exporté au format HTML ou PDF, car ces formats reposent sur les données d'image intégrées plutôt que sur un recalcul en direct.

## Méthode 1 — Ajouter une image de Caméra dynamique
La Caméra dynamique est l'approche la plus courante et correspond le mieux à l'outil Caméra intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu image initial, puis en lui attribuant une `Formula` qui référence la plage source. Une fois la formule attribuée, l'appel à `UpdateSelectedValue()` rafraîchit les données d'image intégrées pour qu'elles soient synchronisées avec les cellules qu'elles reflètent. La Caméra n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type standard `Picture`.
Les API clés sont :
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Passer `null` pour le paramètre `stream` crée une image vide qui sert d'espace réservé pour une Caméra dynamique. La méthode renvoie l'index de la nouvelle image.
- `worksheet.Pictures[index]` — accès par indexeur pour récupérer une `Picture` spécifique de la collection.
- `Picture.Formula` — propriété de chaîne (get/set) contenant la référence de style A1 à la plage source que la Caméra reflète, telle que `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — méthode vide qui rafraîchit les données d'image intégrées à partir des cellules référencées par `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` DOIT être appelé avant l'enregistrement lorsque la sortie est au format HTML ou PDF ; sinon, le fichier exporté ne contiendra pas les données d'image et la Caméra apparaîtra vide dans la sortie rendue.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 colonne 6, la lie à la plage source `A1:F10` via la propriété `Formula`, rafraîchit les données d'image intégrées et enregistre le classeur.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Méthode 2 — Ajouter une image de Caméra statique
La Caméra statique est essentiellement un aperçu rendu ponctuel d'une plage de cellules. Au lieu de maintenir un lien en direct, vous restituez la plage en octets d'image une seule fois, vous encapsulez ces octets dans un `MemoryStream`, puis vous les ajoutez comme image ordinaire. Le contenu de l'image est alors figé au moment de la création et ne se rafraîchit pas automatiquement lorsque les cellules source changent.
Les API clés sont :
- `Cells.CreateRange(string address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — restitue la plage en octets d'image. Passer `null` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `new MemoryStream(byte[] buffer)` — encapsule les octets d'image rendus dans un `MemoryStream` qui peut être passé à `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — ajoute l'image ancrée à la ligne et à la colonne indiquées, en passant cette fois le `MemoryStream` produit par le rendu.
Le code suivant crée un classeur, construit un `Range` pour `A1:F10`, le restitue en octets d'image via `Range.ToImage(null)`, encapsule les octets dans un `MemoryStream`, ajoute l'image ancrée à la ligne 10 colonne 6 et enregistre le classeur.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choisir entre dynamique et statique
- **Caméra dynamique :** se met à jour à chaque recalcul, prend en charge l'export HTML et PDF après `UpdateSelectedValue()`, et préserve le comportement de lien en direct pendant toute la durée de vie du fichier.
- **Caméra statique :** un rendu ponctuel qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel fixe intégré au moment de la construction plutôt qu'un miroir en direct des données.
Aspose.Cells prend en charge à la fois une Caméra dynamique à rafraîchissement automatique construite sur `Picture.Formula` plus `UpdateSelectedValue()`, et une Caméra statique à prise unique construite sur `Range.ToImage` plus un `MemoryStream`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules source, et choisissez l'approche statique lorsque vous n'avez besoin que d'un instantané visuel fixe au moment de la construction.

## Articles connexes
- [Convertir une Sparkline en image et HTML dans Aspose.Cells pour .NET](/cells/fr/net/convert-sparkline-to-image-and-html/)
- [Insertion d'une image dans une cellule](/cells/fr/net/inserting-an-image-into-a-cell/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells pour .NET](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells pour .NET](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}