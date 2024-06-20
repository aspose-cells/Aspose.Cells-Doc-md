---
title: Changer le type de lien HTML cible
type: docs
weight: 320
url: /fr/python-net/change-the-html-link-target-type/
description: Ce sujet vous montre comment changer le type de cible des liens HTML en utilisant Aspose.Cells pour Python via NET.
keywords: Changer le type de cible des liens HTML, type de cible vide, type de cible parent, type de cible top, type de cible self.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via NET vous permet de changer le type de cible des liens HTML. Le lien HTML ressemble à ceci

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Comme vous pouvez le voir, l'attribut cible dans le lien HTML ci-dessus est **_self**. Vous pouvez contrôler cet attribut cible en utilisant la propriété [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Cette propriété prend l'énumération [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) qui a les valeurs suivantes.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

Le code suivant illustre l'utilisation de la propriété [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Il modifie le type de cible du lien en **BLANK**. Par défaut, c'est le **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
