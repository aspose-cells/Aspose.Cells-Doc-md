---
title: Caméra Excel dans Aspose.Cells for Python via Java
linktitle: Caméra Excel dans Aspose.Cells for Python via Java
description: Apprenez à utiliser la Caméra Excel dans Aspose.Cells for Python via Java pour créer une image dynamique liée à une plage de cellules qui se rafraîchit avec les données source et préserve toute la mise en forme d'origine.
keywords: Aspose.Cells, Python via Java, Caméra Excel, image dynamique, image liée, Picture.formula, updateSelectedValue, createRange, toImage, tableau d'octets
type: docs
weight: 90
url: /fr/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Caméra Excel est un objet de feuille de calcul qui restitue une image dynamique d'une plage de cellules et qui flotte sur le calque de dessin comme une image ordinaire. Aspose.Cells for Python via Java prend en charge deux modes de création : une image dynamique qui se rafraîchit automatiquement à chaque modification des données source et une image statique qui capture un instantané unique d'une plage. Cet article décrit les deux approches afin que vous puissiez choisir celle qui convient à votre mise en page.

## Qu'est-ce que la Caméra Excel ?
La Caméra Excel est essentiellement un objet image ancré à une ligne et une colonne spécifiques du calque de dessin de la feuille de calcul. Contrairement à une image insérée classique, la Caméra est liée à une plage source via une formule de style A1 telle que `"A1:F10"`. Dès qu'une cellule de cette plage est modifiée, l'image de la Caméra est automatiquement rafraîchie pour refléter le nouveau contenu. La Caméra préserve la mise en forme complète de la zone source — bordures, couleurs d'arrière-plan, polices et formats numériques — de sorte que tout ce qui est visible dans les cellules apparaît également dans l'image de la Caméra. Cela rend la Caméra particulièrement utile pour les tableaux de bord, les résumés, les panneaux latéraux et les mises en page de rapports où vous souhaitez obtenir un aperçu visible d'une zone distante sans faire défiler l'affichage ni répéter les données. Deux mises en garde s'appliquent : vous devez appeler `updateSelectedValue()` avant d'enregistrer le classeur, et le fichier sera exporté au format HTML ou PDF, car ces formats s'appuient sur les données d'image intégrées plutôt que sur un recalcul dynamique.

## Méthode 1 — Ajouter une image de Caméra dynamique
La Caméra dynamique est l'approche la plus courante et correspond le mieux à l'outil Caméra intégré d'Excel. Elle fonctionne en ajoutant une image sans contenu initial, puis en lui attribuant une formule qui référence la plage source. Une fois la formule attribuée, l'appel de `updateSelectedValue()` rafraîchit les données d'image intégrées pour qu'elles soient synchronisées avec les cellules qu'elles reflètent. La Caméra n'est pas implémentée via une classe dédiée — elle est entièrement construite sur le type standard `Picture`.
Les principales API sont :
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — ajoute une image ancrée à la ligne et à la colonne indiquées. Le passage de `None` pour le paramètre `stream` crée une image vide qui sert de conteneur pour une Caméra dynamique. La méthode renvoie l'index de la nouvelle image.
- `worksheet.getPictures().get(index)` — accesseur pour récupérer un `Picture` spécifique de la collection.
- `Picture.getFormula()` / `Picture.setFormula()` — obtient/définit la référence de style A1 à la plage source que la Caméra reflète, par exemple `"A1:F10"`.
- `Picture.updateSelectedValue()` — méthode vide qui rafraîchit les données d'image intégrées à partir des cellules référencées par la formule.

{{% alert color="primary" %}}
`updateSelectedValue()` DOIT être appelé avant l'enregistrement lorsque la sortie est au format HTML ou PDF ; sinon, le fichier exporté ne contiendra pas les données de l'image et la Caméra apparaîtra vide dans la sortie rendue.
{{% /alert %}}

Le code suivant crée un classeur, ajoute une image vide ancrée à la ligne 10, colonne 6, la lie à la plage source `A1:F10` via la méthode `setFormula`, rafraîchit les données d'image intégrées, puis enregistre le classeur.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Caméra dynamique : ajouter une image vide, la lier via une formule à A1:F10, puis actualiser
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Méthode 2 — Ajouter une image de Caméra statique
La Caméra statique est essentiellement un aperçu rendu une seule fois d'une plage de cellules. Au lieu de maintenir un lien dynamique, vous rendez la plage en octets d'image une seule fois, vous enveloppez ces octets dans un tableau `byte[]` et vous les ajoutez en tant qu'image classique. Le contenu de l'image est alors figé au moment de la création et ne se rafraîchit pas automatiquement lorsque les cellules source changent.
Les principales API sont :
- `Cells.createRange(String address)` — construit un objet `Range` à partir d'une adresse de style A1 telle que `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — restitue la plage en octets d'image. Le passage de `None` utilise les options de rendu par défaut ; des surcharges existent pour un contrôle plus fin de la sortie.
- `byte[] array(byte[] buffer)` — enveloppe les octets d'image rendus dans un tableau `byte[]` qui peut être fourni à `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — ajoute l'image ancrée à la ligne et à la colonne indiquées, en passant cette fois le tableau `byte[]` produit par le rendu.
Le code suivant crée un classeur, construit un `Range` pour `A1:F10`, le restitue en octets d'image via `Range.toImage(None)`, enveloppe les octets dans un tableau `byte[]`, ajoute l'image ancrée à la ligne 10, colonne 6, puis enregistre le classeur.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Caméra statique : construire Range, rendre en octets, envelopper dans ByteArrayInputStream, ajouter comme image
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Choisir entre Dynamique et Statique
- **Caméra dynamique :** se met à jour à chaque recalcul, prend en charge l'export HTML et PDF après `updateSelectedValue()`, et conserve le comportement de lien dynamique pendant toute la durée de vie du fichier.
- **Caméra statique :** un rendu unique qui ne se met jamais à jour, utile lorsque vous souhaitez un instantané visuel figé intégré au moment de la génération plutôt qu'un reflet dynamique des données.
Aspose.Cells for Python via Java prend en charge à la fois une Caméra dynamique et à rafraîchissement automatique construite sur `setFormula` plus `updateSelectedValue()`, et une Caméra statique en une seule passe construite sur `toImage` plus un tableau `byte[]`. Choisissez l'approche dynamique lorsque votre sortie doit rester synchronisée avec les cellules source, et choisissez l'approche statique lorsque vous n'avez besoin que d'un instantané visuel figé au moment de la génération.

{{< app/cells/assistant language"python" >}}