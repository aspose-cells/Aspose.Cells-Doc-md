---
title: Empêcher l'exportation du contenu masqué de la feuille de calcul lors de l'enregistrement dans HTML
type: docs
weight: 210
url: /fr/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel dans HTML. Toutefois, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu de la feuille de calcul masquée vers la sortie HTML (_ files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées vers le_répertoire de fichiers.

{{% /alert %}}

 Aspose.Cells fournit le[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) la propriété. Par défaut, il est réglé sur**vrai** et les feuilles de calcul masquées sont exportées vers HTML. Si vous le définissez**faux**, Aspose.Cells n'exportera pas le contenu masqué de la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

