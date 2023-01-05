---
title: Accéder et mettre à jour les portions de texte enrichi de Cell
linktitle: Texte de mise en forme enrichi
type: docs
weight: 40
url: /fr/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells vous permet d'accéder et de mettre à jour les parties du texte enrichi de la cellule. A cet effet, vous pouvez utiliser[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) et[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthodes. Ces méthodes renverront et accepteront le tableau de[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)objets que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de la police comme le nom de la police, la couleur de la police, l'audace, etc.

{{% /alert %}}

## **Accéder et mettre à jour les portions de texte enrichi de Cell**

 Le code suivant illustre l'utilisation de[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) et[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthode utilisant la[fichier excel source](5112369.xlsx)que vous pouvez télécharger à partir du lien fourni. Le fichier Excel source contient un texte enrichi dans la cellule A1. Il comporte 3 parties et chaque partie a une police différente. L'extrait de code suivant accède à ces parties et met à jour la première partie avec un nouveau nom de police. Enfin, il enregistre le classeur sous[fichier excel de sortie](5112366.xlsx) . Lorsque vous l'ouvrirez, vous constaterez que la police de la première partie du texte a changé pour**"Ariel"**.

### Code C# pour accéder et mettre à jour les portions de texte enrichi de Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Sortie de la console générée par l'exemple de code

 Voici la sortie de la console de l'exemple de code ci-dessus en utilisant le[fichier excel source](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

