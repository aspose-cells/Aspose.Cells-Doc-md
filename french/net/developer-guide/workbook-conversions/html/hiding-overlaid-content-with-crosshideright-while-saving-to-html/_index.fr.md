---
title: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croix pour les chaînes de cellules. Par défaut, Aspose.Cells génère du HTML conformément à Microsoft Excel, mais lorsque vous changez le type de croix en [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), alors il masque toutes les chaînes à droite de la cellule qui sont superposées ou en chevauchement avec la chaîne de cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716894.xlsx) et l'enregistre en [HTML de sortie](64716893.zip) après avoir défini [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) comme [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). La capture d'écran explique comment [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) affecte le HTML de sortie par rapport à la sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}
