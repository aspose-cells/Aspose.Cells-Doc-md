---
title: Définir la largeur de la colonne à une unité scalable telle que em ou pourcentage
type: docs
weight: 130
url: /fr/python-net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Générer un fichier HTML à partir d'une feuille de calcul est très courant. La taille des colonnes est définie en "pt" ce qui fonctionne dans de nombreux cas. Cependant, il peut arriver qu'une taille fixe ne soit pas requise. Par exemple, si la largeur du panneau conteneur est de 600px où cette page HTML est affichée. Dans ce cas, des barres de défilement horizontales peuvent apparaître si la largeur de la table générée est plus grande. Il était nécessaire que cette taille fixe soit changée en une unité scalable telle que em ou pourcentage pour obtenir une meilleure présentation. Le code d'exemple suivant peut être utilisé où [**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable) est défini sur **true** pour créer une largeur scalable.

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés à partir des liens suivants:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
