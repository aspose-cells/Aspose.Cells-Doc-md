---
title: Accéder à la zone de texte par le nom
type: docs
weight: 230
url: /fr/net/access-the-text-box-by-the-name/
---

## Accéder à la zone de texte par le nom

Auparavant, les zones de texte étaient accessibles par index à partir de la collection [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes), mais maintenant vous pouvez également accéder à la zone de texte par nom à partir de cette collection. Il s'agit d'une manière pratique et rapide d'accéder à votre zone de texte si vous connaissez déjà son nom.

Le code d'exemple suivant crée d'abord une zone de texte et lui attribue un texte et un nom. Ensuite, dans les lignes suivantes, nous accédons à la même zone de texte par son nom et affichons son texte.

### Code C# pour accéder à la zone de texte par nom

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AccessTextBoxName-AccessTextBoxName.cs" >}}

### Sortie de la console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
