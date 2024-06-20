---
title: Définir la largeur de la colonne à une unité scalable telle que em ou pourcentage
type: docs
weight: 130
url: /fr/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

La génération d'un fichier HTML à partir d'une feuille de calcul est très courante. La taille des colonnes est définie en "pt" ce qui fonctionne dans de nombreux cas. Cependant, il peut arriver que cette taille fixe ne soit pas nécessaire. Par exemple, si la largeur du conteneur est de 600px où cette page HTML est affichée. Dans ce cas, vous pouvez avoir une barre de défilement horizontale si la largeur du tableau généré est plus grande. Il était nécessaire que cette taille fixe soit modifiée en une unité évolutive comme em ou pourcentage pour obtenir une meilleure présentation. Le code d'exemple suivant peut être utilisé où [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) est défini sur **true** pour créer une largeur évolutive.

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés à partir des liens suivants:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
