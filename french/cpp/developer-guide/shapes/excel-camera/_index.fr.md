---
title: Excel Camera dans Aspose.Cells for C++
linktitle: Excel Camera dans Aspose.Cells for C++
description: Apprenez à utiliser Excel Camera dans Aspose.Cells for C++ pour créer une image dynamique liée à une plage de cellules qui s'actualise avec les données source et préserve toute la mise en forme source.
keywords: Aspose.Cells, C++, Excel Camera, image dynamique, image liée, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /fr/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera est un objet de feuille de calcul qui restitue une image en direct d'une plage de cellules et qui flotte sur la couche de dessin comme une image ordinaire. Aspose.Cells prend en charge deux modes de création, une image dynamique qui s'actualise automatiquement dès que les données source changent, et une image statique qui capture un instantané ponctuel d'une plage. Cet article présente les deux approches afin que vous puissiez choisir celle qui convient à votre mise en page.

## Qu'est-ce qu'Excel Camera ?
Excel Camera est essentiellement un objet image ancré à une ligne et une colonne spécifiques sur la couche de dessin de la feuille de calcul. Contrairement à une image insérée classique, la Camera est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Dès qu'une cellule de cette plage est modifiée, l'image de la Camera est actualisée automatiquement pour refléter le nouveau contenu. La Camera préserve la mise en forme complète de la zone source — bordures, couleurs d'arrière-plan, polices et formats numériques — de sorte que tout ce qui est visible à l'intérieur des cellules apparaît également dans l'image de la Camera. Cela rend la Camera particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez un aperçu visible d'une zone distante sans avoir à faire défiler ou répéter les données. Deux remarques s'appliquent : vous devez appeler `UpdateSelectedValue()` avant d'enregistrer le classeur, et le fichier doit être exporté au format HTML ou PDF, car ces formats s'appuient sur les données d'image intégrées plutôt que sur un recalcul en direct.

## Méthode 1 — Ajouter une image Camera dynamique
La Camera dynamique est l'approche la plus courante et correspond le mieux à l'outil Camera intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu initial, puis en lui attribuant une `Formula` qui référence la plage source. Une fois la formule attribuée, l'appel à `UpdateSelectedValue()` actualise les données d'image intégrées afin qu'elles soient synchronisées avec les cellules qu'elles reflètent. La Camera n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type `Picture` standard.
Les principales API sont :
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Passer un `Vector<uint8_t>()` vide crée une image vide qui sert d'espace réservé pour une Camera dynamique. La méthode retourne l'index de la nouvelle image.
- `worksheet.GetPictures().Get(int index)` — récupère une `Picture` spécifique de la collection par index.
- `Picture.SetFormula(U16String value)` — définit la référence de style A1 à la plage source que la Camera doit refléter, par exemple `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — actualise les données d'image intégrées à partir des cellules référencées par `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` DOIT être appelée avant l'enregistrement lorsque la sortie est au format HTML ou PDF ; sinon, le fichier exporté ne contiendra pas les données d'image et la Camera apparaîtra vide dans le rendu.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10, colonne 6, la lie à la plage source `A1:F10` via la propriété `Formula`, actualise les données d'image intégrées, puis enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Caméra Dynamique : ajouter une image vide, la lier via une Formule à A1:F10, puis actualiser
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Méthode 2 — Ajouter une image Camera statique
La Camera statique est essentiellement un aperçu rendu une seule fois d'une plage de cellules. Au lieu de maintenir un lien en direct, vous restituez la plage dans un tampon d'octets `Vector<uint8_t>` une seule fois, puis transmettez ce tampon directement à `Pictures.Add(row, col, data)`. Le contenu de l'image est alors figé au moment de la création et ne s'actualise pas automatiquement lorsque les cellules source changent.
Les principales API sont :
- `Cells.CreateRange(U16String address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` — restitue la plage dans un tampon d'octets `Vector<uint8_t>`. Passer `nullptr` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — ajoute l'image ancrée à la ligne et à la colonne indiquées, en passant cette fois le tampon d'octets produit par `Range.ToImage`.
Le code suivant crée un classeur, construit un `Range` pour `A1:F10`, le restitue en octets d'image via `Range.ToImage(nullptr)`, ajoute l'image ancrée à la ligne 10, colonne 6, puis enregistre le classeur.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Caméra statique : construire une plage, rendre en octets, ajouter comme image
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Choisir entre dynamique et statique
- **Camera dynamique :** s'actualise à chaque recalcul, prend en charge l'export HTML et PDF après `UpdateSelectedValue()`, et préserve le comportement de lien en direct pendant toute la durée de vie du fichier.
- **Camera statique :** un rendu ponctuel qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel figé intégré au moment de la génération plutôt qu'un miroir en direct des données.
Aspose.Cells prend en charge à la fois une Camera dynamique et auto-actualisable, construite sur `Picture.Formula` associée à `UpdateSelectedValue()`, et une Camera statique à usage unique, construite sur `Range.ToImage` associée à `Vector<uint8_t>`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules source, et choisissez l'approche statique lorsque vous n'avez besoin que d'un instantané visuel figé au moment de la génération.

{{< app/cells/assistant language="cpp" >}}