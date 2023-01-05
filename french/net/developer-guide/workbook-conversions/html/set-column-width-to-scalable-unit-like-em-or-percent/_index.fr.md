---
title: Définissez la largeur de la colonne sur une unité évolutive comme em ou pourcentage
type: docs
weight: 130
url: /fr/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
La génération d'un fichier HTML à partir d'une feuille de calcul est très courante. La taille des colonnes est définie en "pt" ce qui fonctionne dans de nombreux cas. Cependant, il peut arriver que cette taille fixe ne soit pas nécessaire. Par exemple, si la largeur d'un panneau de conteneur est de 600 pixels, cette page HTML est affichée. Dans ce cas, vous pouvez obtenir une barre de défilement horizontale si la largeur du tableau généré est plus grande. Il était nécessaire que cette taille fixe soit changée en une unité évolutive comme em ou pourcentage pour obtenir une meilleure présentation. L'exemple de code suivant peut être utilisé là où[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) est réglé sur**vrai** pour créer une largeur évolutive.

Un exemple de fichier source et de fichiers de sortie peut être téléchargé à partir des liens suivants :

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
