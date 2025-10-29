---
title: Comment rendre une série invisible avec Golang via C++
linktitle: Comment définir une série comme invisible
description: Dans un graphique Excel, vous pouvez avoir besoin de rendre une série invisible. Cet article décrit comment utiliser Aspose.Cells avec Golang via C++ pour le faire.
keywords: Graphique Excel, Série, Invisible, EstFiltré.
type: docs
weight: 74
url: /fr/go-cpp/how-to-set-series-invisible/
---

## Comment définir une série comme invisible dans un graphique Excel

Dans un graphique Excel, vous pouvez faire un clic droit sur un graphique, cliquer sur "Sélectionner des données", et dans la fenêtre contextuelle, vous pouvez définir si une série est visible en cochant ou décochant l’option. Vous pouvez télécharger le [fichier d’exemple]([SeriesFiltered.xlsx](https://example.com/SeriesFiltered.xlsx)) et l’opérer dans Excel comme indiqué dans la figure pour réaliser cette fonction. Ensuite, nous vous expliquerons comment faire cela en utilisant la bibliothèque Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Comment définir une série comme invisible en utilisant Aspose.Cells 

Nous utilisons le code suivant pour définir une série comme invisible en utilisant Aspose.Cells :

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
Vous pouvez obtenir le [Fichier d'entrée](SeriesFiltered.xlsx) et le [Fichier de sortie](output.xlsx).

Comme indiqué dans la figure ci-dessous, les deux premières séries qui étaient initialement visibles, sont devenues invisibles dans le fichier de sortie.  
![todo:image_alt_text](output.png)
