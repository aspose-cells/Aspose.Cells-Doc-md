---
title: Accéder et mettre à jour les parties du texte enrichi de la cellule
linktitle: Texte enrichi avec formatage
type: docs
weight: 40
url: /fr/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Apprenez à accéder et mettre à jour les parties du texte enrichi de la cellule grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Accès et mise à jour du texte enrichi de la cellule en Python, Obtenir le texte enrichi de la cellule en Python, Modifier le texte enrichi de la cellule en Python, Accéder au texte enrichi de la cellule en Python, Mettre à jour le texte enrichi de la cellule en Python, Changer le texte enrichi de la cellule en Python.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET vous permet d'accéder et de mettre à jour les parties du texte enrichi de la cellule. À cette fin, vous pouvez utiliser les méthodes [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) et [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list). Ces méthodes retourneront et accepteront le tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de police telles que le nom de la police, la couleur de la police, la graisse, etc.

{{% /alert %}}

## **Accéder et mettre à jour les parties du texte enrichi de la cellule**

Le code suivant démontre l'utilisation des méthodes [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) et [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) à l'aide du [fichier excel source](5112369.xlsx) que vous pouvez télécharger depuis le lien fourni. Le fichier excel source contient un texte enrichi dans la cellule A1. Il a 3 parties et chaque partie a une police différente. L'extrait de code suivant accède à ces parties et met à jour la première partie avec un nouveau nom de police. Enfin, il enregistre le classeur sous la forme du [fichier excel de sortie](5112366.xlsx). Lorsque vous l'ouvrirez, vous verrez que la police de la première partie du texte a été changée en **"Arial"**.

### Code C# pour accéder et mettre à jour les parties du texte enrichi de la cellule

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

### Sortie de la console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus en utilisant le [fichier Excel source](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
