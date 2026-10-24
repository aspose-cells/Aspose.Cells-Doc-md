---
title: Caméra Excel dans Aspose.Cells for .Net
linktitle: Caméra Excel dans Aspose.Cells for .Net
description: Découvrez comment utiliser la caméra Excel dans Aspose.Cells for .Net pour créer une image dynamique liée à une plage de cellules qui s’actualise avec les données source et préserve toute la mise en forme de la zone source.
keywords: Aspose.Cells, .NET, caméra Excel, image dynamique, image liée, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /fr/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La caméra Excel est un objet de feuille de calcul qui rend une image en direct d’une plage de cellules et se superpose au calque de dessin à la manière d’une image ordinaire. Aspose.Cells prend en charge deux modes de création : une image dynamique qui s’actualise automatiquement chaque fois que les données source changent et une image statique qui capture un instantané d’une plage, réalisé une seule fois. Cet article présente les deux approches afin de vous permettre de choisir celle qui convient à votre mise en page.

## Qu’est-ce que la caméra Excel ?
La caméra Excel est essentiellement un objet d’image ancré à une ligne et à une colonne précises sur le calque de dessin de la feuille de calcul. Contrairement à une image ordinaire insérée, la caméra est liée à une plage source au moyen d’une formule au format A1, telle que `"A1:F10"`. Chaque fois qu’une cellule de cette plage change, l’image de la caméra est actualisée automatiquement pour refléter le nouveau contenu. La caméra préserve toute la mise en forme de la zone source — les bordures, les couleurs d’arrière-plan, les polices et les formats numériques — de sorte que tout ce qui est visible dans les cellules apparaît également dans son image. Elle est particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez afficher un aperçu d’une zone distante sans avoir à faire défiler la feuille de calcul ni à répéter les données. Deux précautions sont à prendre : vous devez appeler `UpdateSelectedValue()` avant d’enregistrer le classeur, et le fichier doit être exporté au format HTML ou PDF, car ces formats reposent sur les données d’image incorporées plutôt que sur un recalcul en direct.

## Méthode 1 — Ajouter une image dynamique de la caméra
La caméra dynamique est l’approche la plus courante et la plus proche de l’outil Caméra intégré à Excel. Le principe consiste à ajouter une image sans contenu initial, puis à lui attribuer une `Formula` qui référence la plage source. Après l’attribution de la formule, l’appel à `UpdateSelectedValue()` actualise les données d’image incorporées afin de les synchroniser avec les cellules que la caméra reflète. La caméra n’est pas implémentée au moyen d’une classe dédiée — elle repose entièrement sur le type standard `Picture`.
Les principales API sont :
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Le passage de `null` au paramètre `stream` crée une image vide qui sert d’espace réservé pour une caméra dynamique. La méthode retourne l’index de la nouvelle image.
- `worksheet.Pictures[index]` — permet d’accéder à un `Picture` précis dans la collection au moyen de l’indexeur.
- `Picture.Formula` — propriété de type chaîne (get/set) qui contient la référence au format A1 de la plage source reflétée par la caméra, telle que `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — méthode `void` qui actualise les données d’image incorporées à partir des cellules référencées par `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` DOIT être appelée avant l’enregistrement lorsque la sortie est au format HTML ou PDF ; sinon, le fichier exporté ne contiendra pas les données d’image et la caméra apparaîtra vide dans le résultat rendu.
Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 et à la colonne 6, la relie à la plage source `A1:F10` via la propriété `Formula`, actualise les données d’image incorporées, puis enregistre le classeur.
{{% /alert %}}

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Caméra dynamique : ajouter une image vide, la lier à A1:F10 via Formula, puis actualiser
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Méthode 2 — Ajouter une image statique de la caméra
La caméra statique est essentiellement un aperçu d’une plage de cellules, rendu une seule fois. Au lieu de maintenir un lien actif, vous rendez la plage sous forme d’octets d’image une seule fois, encapsulez ces octets dans un `MemoryStream`, puis les ajoutez comme une image ordinaire. Le contenu de l’image est ensuite figé au moment de sa création et ne s’actualise pas automatiquement lorsque les cellules source changent.
Les principales API sont :
- `Cells.CreateRange(string address)` — construit un objet `Range` à partir d’une adresse au format A1, telle que `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — rend la plage sous forme d’octets d’image. Le passage de `null` utilise les options de rendu par défaut ; des surcharges existent pour offrir un contrôle plus précis sur la sortie.
- `new MemoryStream(byte[] buffer)` — encapsule les octets de l’image rendue dans un `MemoryStream` qui peut être transmis à la méthode `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — ajoute l’image ancrée à la ligne et à la colonne indiquées, cette fois en transmettant le `MemoryStream` produit par le rendu.
Le code suivant crée un classeur, construit un objet `Range` pour `A1:F10`, le rend sous forme d’octets d’image via `Range.ToImage(null)`, encapsule les octets dans un `MemoryStream`, ajoute l’image ancrée à la ligne 10 et à la colonne 6, puis enregistre le classeur.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Caméra statique : construire la plage, rendre en octets, envelopper dans MemoryStream, ajouter comme image
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choix entre une caméra dynamique et une caméra statique
- **Caméra dynamique :** se met à jour lors de chaque recalcul, prend en charge l’exportation vers les formats HTML et PDF après l’appel à `UpdateSelectedValue()` et conserve le comportement de lien actif pendant toute la durée de vie du fichier.
- **Caméra statique :** propose un rendu unique qui ne se met jamais à jour, utile lorsque vous souhaitez incorporer un instantané visuel fixe au moment de la génération plutôt qu’un miroir dynamique des données.
Aspose.Cells prend en charge une caméra dynamique à actualisation automatique, fondée sur `Picture.Formula` et `UpdateSelectedValue()`, ainsi qu’une caméra statique à rendu unique, fondée sur `Range.ToImage` et un `MemoryStream`. Choisissez l’approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules source et l’approche statique lorsque vous avez uniquement besoin d’un instantané visuel fixe au moment de la génération.

## Articles connexes
- [Convertir une Sparkline en image et HTML dans Aspose.Cells for .Net](/cells/fr/net/convert-sparkline-to-image-and-html/)
- [Insérer une image dans une cellule](/cells/fr/net/inserting-an-image-into-a-cell/)
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for .Net](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for .Net](/cells/fr/net/apply-style-to-pivot-table/)
- [Modifier la disposition du champ de page dans un tableau croisé dynamique](/cells/fr/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}