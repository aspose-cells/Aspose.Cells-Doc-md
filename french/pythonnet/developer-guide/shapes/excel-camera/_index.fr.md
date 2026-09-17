---
title: Excel Camera dans Aspose.Cells for Python via .NET
linktitle: Excel Camera dans Aspose.Cells for Python via .NET
description: Apprenez à utiliser Excel Camera dans Aspose.Cells for Python via .NET pour créer une image dynamique liée à une plage de cellules qui s'actualise avec les données source et préserve toute la mise en forme source.
keywords: Aspose.Cells, Python, Excel Camera, image dynamique, image liée, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /fr/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera est un objet de feuille de calcul qui restitue une image en direct d'une plage de cellules et flotte sur la couche de dessin comme une image ordinaire. Aspose.Cells prend en charge deux modes de création, une image dynamique qui s'actualise automatiquement lorsque les données source changent et une image statique qui capture un instantané unique d'une plage. Cet article présente les deux approches afin que vous puissiez choisir celle qui correspond à votre mise en page.

## Qu'est-ce qu'Excel Camera ?
L'Excel Camera est essentiellement un objet image ancré à une ligne et une colonne spécifiques sur la couche de dessin de la feuille de calcul. Contrairement à une image insérée ordinaire, la Camera est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Chaque fois qu'une cellule de cette plage change, l'image de la Camera est actualisée automatiquement pour refléter le nouveau contenu. La Camera préserve toute la mise en forme de la zone source — bordures, couleurs d'arrière-plan, polices et formats numériques — de sorte que tout ce qui est visible dans les cellules apparaît également dans l'image de la Camera. Cela rend la Camera particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez un aperçu visible d'une région distante sans faire défiler ni répéter les données. Deux mises en garde s'appliquent : vous devez appeler `update_selected_value()` avant d'enregistrer le classeur, et le fichier sera exporté en HTML ou PDF, car ces formats reposent sur les données d'image intégrées plutôt que sur un recalcul en direct.

## Méthode 1 — Ajouter une image Camera dynamique
La Camera dynamique est l'approche la plus courante et correspond le mieux à l'outil Camera intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu initial, puis en lui attribuant une `formula` qui référence la plage source. Une fois la formule attribuée, l'appel de `update_selected_value()` actualise les données d'image intégrées afin qu'elles soient synchronisées avec les cellules qu'elles reflètent. La Camera n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type `Picture` standard.
Les API clés sont :
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Passer `None` pour le paramètre `stream` crée une image vide qui sert d'espace réservé pour une Camera dynamique. La méthode renvoie l'index de la nouvelle image.
- `worksheet.pictures[index]` — accès par indexeur pour récupérer une `Picture` spécifique de la collection.
- `picture.formula` — propriété de type chaîne (get/set) contenant la référence de style A1 à la plage source que la Camera reflète, telle que `"A1:F10"`.
- `picture.update_selected_value()` — méthode sans valeur de retour qui actualise les données d'image intégrées à partir des cellules référencées par `formula`.

{{% alert color="primary" %}}
`update_selected_value()` DOIT être appelé avant l'enregistrement lorsque la sortie est HTML ou PDF ; sinon, le fichier exporté ne contiendra pas les données d'image et la Camera apparaîtra vide dans la sortie rendue.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10 colonne 6, la lie à la plage source `A1:F10` via la propriété `formula`, actualise les données d'image intégrées, et enregistre le classeur.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Caméra dynamique : ajouter une image vide, la lier via une formule à A1:F10, puis actualiser
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Méthode 2 — Ajouter une image Camera statique
La Camera statique est essentiellement un aperçu rendu une seule fois d'une plage de cellules. Au lieu de maintenir un lien dynamique, vous restituez la plage en octets d'image une fois, enveloppez ces octets dans un `BytesIO`, et les ajoutez comme une image ordinaire. Le contenu de l'image est alors fixé au moment de la création et ne s'actualise pas automatiquement lorsque les cellules source changent.
Les API clés sont :
- `Cells.create_range(string address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` — restitue la plage en octets d'image. Passer `None` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `BytesIO(byte[] buffer)` — enveloppe les octets d'image rendus dans un `BytesIO` qui peut être transmis à `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — ajoute l'image ancrée à la ligne et à la colonne indiquées, en passant cette fois le `BytesIO` produit par le rendu.
Le code suivant crée un classeur, construit un `Range` pour `A1:F10`, le restitue en octets d'image via `Range.to_image(null)`, enveloppe les octets dans un `BytesIO`, ajoute l'image ancrée à la ligne 10 colonne 6, et enregistre le classeur.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Caméra Statique : construire une Plage, rendre en octets, envelopper dans BytesIO, ajouter comme image
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Choisir entre dynamique et statique
- **Camera dynamique :** se met à jour à chaque recalcul, prend en charge l'export HTML et PDF après `update_selected_value()`, et préserve le comportement de lien dynamique pendant toute la durée de vie du fichier.
- **Camera statique :** un rendu unique qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel fixe intégré au moment de la génération plutôt qu'un miroir dynamique des données.
Aspose.Cells prend en charge à la fois une Camera dynamique à actualisation automatique construite sur `picture.formula` plus `update_selected_value()` et une Camera statique à usage unique construite sur `Range.to_image` plus un `BytesIO`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules source, et choisissez l'approche statique lorsque vous n'avez besoin que d'un instantané visuel fixe au moment de la génération.

{{< app/cells/assistant language="python-net" >}}