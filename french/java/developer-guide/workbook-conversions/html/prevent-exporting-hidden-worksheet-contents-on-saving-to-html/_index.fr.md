---
title: Empêcher l'exportation du contenu masqué de la feuille de calcul lors de l'enregistrement dans HTML
type: docs
weight: 90
url: /fr/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel dans HTML. Toutefois, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu de la feuille de calcul masquée vers la sortie HTML (_ files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées vers le_répertoire de fichiers.

{{% /alert %}}

Aspose.Cells fournit le[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) la propriété. Par défaut, le[**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) la propriété est définie sur**vrai**. Si vous le réglez sur**faux**, alors Aspose.Cells n'exportera pas le contenu masqué de la feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Outre le contrôle de l'exportation ou non des feuilles de calcul masquées, vous pouvez également configurer des paramètres supplémentaires pour l'exportation du classeur vers HTML. Les articles suivants illustrent d'autres fonctionnalités prises en charge par Aspose.Cells pour l'exportation de classeurs vers HTML.

- [Convertir Excel en HTML avec en-têtes](/cells/fr/java/convert-excel-to-html-with-headings/)
- [Exclure les styles inutilisés lors de la conversion d'Excel en HTML](/cells/fr/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exporter les commentaires lors de l'enregistrement du fichier Excel au HTML](/cells/fr/java/export-comments-while-saving-excel-file-to-html/)
- [Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au HTML](/cells/fr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web](/cells/fr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
