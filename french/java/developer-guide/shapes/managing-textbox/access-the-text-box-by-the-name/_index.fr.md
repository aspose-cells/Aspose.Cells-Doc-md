---
title: Accéder à la zone de texte par le nom
type: docs
weight: 580
url: /fr/java/access-the-text-box-by-the-name/
---

{{% alert color="primary" %}} 

Auparavant, les zones de texte étaient accessibles par index dans la collection [Workheet.getTextBoxes()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) mais vous pouvez maintenant également accéder à la zone de texte par nom dans cette collection. Il s'agit d'un moyen pratique et rapide d'accéder à votre zone de texte si vous connaissez déjà son nom.

{{% /alert %}} 
## **Accéder à la zone de texte par le nom**
Le code d'exemple suivant crée d'abord une zone de texte et lui attribue un texte et un nom. Ensuite, dans les lignes suivantes, nous accédons à la même zone de texte par son nom et affichons son texte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessTextBoxName-AccessTextBoxName.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 This is MyTextBox

{{< /highlight >}}
