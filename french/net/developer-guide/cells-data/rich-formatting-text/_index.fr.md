---
title: Accéder et mettre à jour les parties du texte enrichi du Cell
linktitle: Texte de formatage riche
type: docs
weight: 40
url: /fr/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Découvrez comment accéder et mettre à jour les portions de texte enrichi du Cell via le Aspose.Cells for .NET API.
keywords: Access and Update Rich Text of Cell, Get Rich Text of Cell, Edit Rich Text of Cell, Access Rich Text of Cell, Update Rich Text of Cell, Change Rich Text of Cell
---
{{% alert color="primary" %}}

 Aspose.Cells vous permet d'accéder et de mettre à jour les portions du texte riche de la cellule. A cet effet, vous pouvez utiliser[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) et[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthodes. Ces méthodes renverront et accepteront le tableau de[**Paramètres de police**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)objets que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de la police telles que le nom de la police, la couleur de la police, la gras, etc.

{{% /alert %}}

##  **Accéder et mettre à jour les parties du texte enrichi du Cell**

 Le code suivant montre l'utilisation de[**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) et[**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthode utilisant le[fichier Excel source](5112369.xlsx) que vous pouvez télécharger à partir du lien fourni. Le fichier Excel source contient un texte enrichi dans la cellule A1. Il comporte 3 parties et chaque partie a une police différente. L'extrait de code suivant accède à ces parties et met à jour la première partie avec un nouveau nom de police. Enfin, il enregistre le classeur sous[sortie du fichier Excel](5112366.xlsx). Lorsque vous l'ouvrirez, vous constaterez que la police de la première partie du texte a été modifiée en *"Arial"**.

###  Code C# pour accéder et mettre à jour les portions de Rich Text de Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Sortie de console générée par l'exemple de code

 Voici la sortie console de l'exemple de code ci-dessus en utilisant le[fichier Excel source](5112369.xlsx).

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

