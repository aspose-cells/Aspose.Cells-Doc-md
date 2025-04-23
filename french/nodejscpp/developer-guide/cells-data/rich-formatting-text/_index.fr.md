---
title: Accéder et mettre à jour les parties du texte enrichi de la cellule
linktitle: Texte enrichi avec formatage
type: docs
weight: 40
url: /fr/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Apprenez comment accéder et mettre à jour les parties du texte enrichi d une cellule via l API Aspose.Cells for Node.js via C++.
keywords: Accéder et mettre à jour le texte enrichi de la cellule, obtenir le texte enrichi de la cellule, modifier le texte enrichi de la cellule, accéder au texte enrichi de la cellule, mettre à jour le texte enrichi de la cellule, changer le texte enrichi de la cellule
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ vous permet d'accéder et de mettre à jour les parties du texte enrichi de la cellule. À cette fin, vous pouvez utiliser les méthodes [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) et [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). Ces méthodes retourneront et accepteront un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de la police comme le nom de la police, la couleur, le gras, etc.

{{% /alert %}}

## **Accéder et mettre à jour les parties du texte enrichi de la cellule**

Le code suivant démontre l'utilisation des méthodes [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) et [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) en utilisant le [fichier excel source](5112369.xlsx) que vous pouvez télécharger à partir du lien fourni. Le fichier source Excel possède un texte enrichi dans la cellule A1. Il comporte 3 parties, chacune avec une police différente. Le code ci-dessous accède à ces parties et met à jour la première avec un nouveau nom de police. Enfin, il enregistre le classeur sous le nom [fichier excel de sortie](5112366.xlsx). Lorsque vous l'ouvrirez, vous constaterez que la police de la première partie du texte a changé en **"Arial"**.

### Code Node.js pour accéder et mettre à jour les parties du texte enrichi d'une cellule

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

