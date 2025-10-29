---
title: Modifier le type de cible de lien HTML avec Golang via C++
linktitle: Changer le type de lien HTML cible
type: docs
weight: 320
url: /fr/go-cpp/change-the-html-link-target-type/
description: Apprenez comment changer le type de cible du lien HTML en utilisant Aspose.Cells for C++. Contrôlez l attribut cible dans les liens HTML de manière programmatique.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de changer le type de lien HTML cible. Le lien HTML ressemble à ceci

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Comme vous pouvez le voir, l'attribut cible dans le lien HTML ci-dessus est **_self**. Vous pouvez contrôler cet attribut cible en utilisant la propriété [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Cette propriété prend l'énumération [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) qui a les valeurs suivantes.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Le code suivant illustre l'utilisation de la propriété [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Il change le type de cible du lien en **blank**. Par défaut, c'est le **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
