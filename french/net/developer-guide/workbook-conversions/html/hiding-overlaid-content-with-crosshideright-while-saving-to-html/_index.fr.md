---
title: Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML
type: docs
weight: 100
url: /fr/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---
## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel au format HTML, vous pouvez spécifier différents types croisés pour les chaînes de cellules. Par défaut, Aspose.Cells génère du HTML selon Microsoft Excel mais lorsque vous changez le type croisé en[**CroixMasquerDroite**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), puis il masque toutes les chaînes du côté droit de la cellule qui sont superposées ou qui se chevauchent avec la chaîne de cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format Html**

 L'exemple de code suivant charge le[exemple de fichier Excel](64716894.xlsx) et l'enregistre dans[sortie HTML](64716893.zip) après avoir réglé le[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)comme[**CroixMasquerDroite**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). La capture d'écran explique comment[**CroixMasquerDroite**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)affecte la sortie HTML de la sortie par défaut.

![tâche : image_autre_texte](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
