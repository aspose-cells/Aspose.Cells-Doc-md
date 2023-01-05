---
title: Conversion d'un graphique en image au format SVG
type: docs
weight: 140
url: /fr/java/converting-chart-to-image-in-svg-format/
---
{{% alert color="primary" %}} 

Scalable Vector Graphics (SVG) est un format d'image vectorielle basé sur XML pour les graphiques bidimensionnels qui prend également en charge l'interactivité et l'animation. La spécification SVG est une norme ouverte développée par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'ils peuvent être recherchés, indexés, scriptés et compressés. En tant que fichiers XML, les images SVG peuvent être créées et modifiées avec n'importe quel éditeur de texte, mais sont plus souvent créées avec un logiciel de dessin.

Aspose.Cells peut enregistrer des graphiques sous forme d'images dans différents formats tels que BMP, JPEG, PNG, GIF, SVG, etc. Cet article explique comment enregistrer des graphiques sous forme d'images SVG.

{{% /alert %}} 

L'exemple de code suivant explique comment utiliser Aspose.Cells pour convertir un graphique en une image au format SVG. Le code charge le fichier Excel source, puis enregistre le premier graphique trouvé sur la première feuille de calcul dans SVG.

La capture d'écran suivante montre l'image de graphique convertie au format SVG créée avec l'exemple de code.

**Image de sortie** 

![tâche : image_autre_texte](converting-chart-to-image-in-svg-format_1.png)

Étant donné que SVG est un format basé sur XML, vous pouvez également ouvrir l'image du graphique de sortie dans un éditeur de texte tel que le Bloc-notes, comme indiqué dans cette capture d'écran.

**Sortie SCG dans un éditeur de texte** 

![tâche : image_autre_texte](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
