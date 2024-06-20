---
title: Accéder et mettre à jour les parties du texte enrichi de la cellule
linktitle: Texte enrichi avec formatage
type: docs
weight: 40
url: /fr/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Apprenez comment accéder et mettre à jour les parties du texte enrichi d une cellule grâce à l API Aspose.Cells for .NET.
keywords: Accéder et mettre à jour le texte enrichi de la cellule, obtenir le texte enrichi de la cellule, modifier le texte enrichi de la cellule, accéder au texte enrichi de la cellule, mettre à jour le texte enrichi de la cellule, changer le texte enrichi de la cellule
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'accéder et de mettre à jour les différentes parties du texte enrichi de la cellule. À cette fin, vous pouvez utiliser les méthodes [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) et [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). Ces méthodes retourneront et accepteront un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de la police, telles que le nom de la police, la couleur de la police, le gras, etc.

{{% /alert %}}

## **Accéder et mettre à jour les parties du texte enrichi de la cellule**

Le code suivant démontre l'utilisation de la méthode [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) et [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) en utilisant le [fichier Excel source](5112369.xlsx) que vous pouvez télécharger à partir du lien fourni. Le fichier Excel source contient un texte enrichi dans la cellule A1. Il comporte 3 parties et chaque partie a une police différente. L'extrait de code suivant accède à ces parties et met à jour la première partie avec un nouveau nom de police. Enfin, il enregistre le classeur sous forme de [fichier Excel de sortie](5112366.xlsx). Lorsque vous l'ouvrirez, vous constaterez que la police de la première partie du texte a été changée en « Arial ». 

### Code C# pour accéder et mettre à jour les parties du texte enrichi de la cellule

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

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

