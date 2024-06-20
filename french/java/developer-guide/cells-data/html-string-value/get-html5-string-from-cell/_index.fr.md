---
title: Obtenir la chaîne HTML5 à partir de la cellule
type: docs
weight: 90
url: /fr/java/get-html5-string-from-cell/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells retourne la chaîne HTML de la cellule en utilisant la méthode [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString). Si vous passez **false** comme paramètre, elle vous renverra HTML normal. Mais si vous passez **true** comme paramètre, elle vous renverra une chaîne HTML5.

## **Obtenir une chaîne HTML5 à partir de la cellule**

Le code d'exemple suivant crée un objet classeur et ajoute un texte dans la cellule A1 de la première feuille de calcul. Il obtient ensuite la chaîne HTML normale et HTML5 à partir de la cellule A1 en utilisant la méthode [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) et les imprime sur la console.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Sortie console**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
