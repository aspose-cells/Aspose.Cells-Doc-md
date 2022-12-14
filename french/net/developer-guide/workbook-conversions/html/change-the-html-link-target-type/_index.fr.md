---
title: Modifier le type de cible du lien HTML
type: docs
weight: 320
url: /fr/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells vous permet de changer le type de cible du lien HTML. Le lien HTML ressemble à ceci

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Comme vous pouvez le voir, l'attribut cible dans le lien HTML ci-dessus est **_self**. Vous pouvez contrôler cet attribut cible à l'aide de la propriété [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Cette propriété prend l'énumération [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) qui a les valeurs suivantes.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Le code suivant illustre l'utilisation de[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) propriété. Il change le type de cible du lien en**Vide**. Par défaut, c'est le**parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
