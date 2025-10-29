---
title: Empêcher l exportation du contenu de la feuille de calcul masqué lors de l enregistrement en HTML
type: docs
weight: 210
url: /fr/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel en HTML. Cependant, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu des feuilles de calcul masquées dans le répertoire de sortie HTML (_files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées dans le répertoire _files.

{{% /alert %}}

Aspose.Cells fournit la propriété [**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet). Par défaut, elle est définie sur **true** et les feuilles de calcul masquées sont exportées en HTML. Si vous la définissez sur **false**, Aspose.Cells n'exportera pas le contenu des feuilles de calcul masquées.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}

{{< app/cells/assistant language="python-net" >}}
