---
title: Modifier le type de cible de lien HTML
type: docs
weight: 450
url: /fr/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells vous permet de modifier le type de cible de lien HTML. Le lien HTML ressemble à ceci :

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Comme vous pouvez le voir, l'attribut cible dans le lien HTML ci-dessus est **_self**. Vous pouvez contrôler cet attribut cible à l'aide de la propriété [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). Cette propriété prend l'énumération [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) qui a les valeurs suivantes.

- [VIDE](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SOI](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [HAUT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **Modifier le type de cible de lien HTML**
 Le code suivant illustre l'utilisation de[HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) la propriété. Il change le type de cible du lien en**Vide**. Par défaut, c'est le**parent** . Vous pouvez obtenir le[fichier excel source](5472932.xlsx) à partir de ce lien, vous pouvez cependant utiliser n'importe quel fichier Excel contenant un lien hypertexte HTML pour exécuter ce code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
