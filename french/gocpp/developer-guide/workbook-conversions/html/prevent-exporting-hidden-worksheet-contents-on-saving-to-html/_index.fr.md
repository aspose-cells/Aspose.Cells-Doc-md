---
title: Empêcher l exportation du contenu de la feuille masquée lors de l enregistrement en HTML avec Golang via C++
linktitle: Empêcher l exportation du contenu des feuilles de calcul masquées
type: docs
weight: 210
url: /fr/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Apprenez comment empêcher l exportation du contenu des feuilles masquées lors de la sauvegarde des classeurs Excel en HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel en HTML. Cependant, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu des feuilles de calcul masquées dans le répertoire de sortie HTML (_files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées dans le répertoire _files.

{{% /alert %}}

Aspose.Cells fournit la propriété [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/). Par défaut, elle est définie sur **true** et les feuilles de calcul masquées sont exportées en HTML. Si vous la définissez sur **false**, Aspose.Cells n'exportera pas le contenu des feuilles de calcul masquées.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
