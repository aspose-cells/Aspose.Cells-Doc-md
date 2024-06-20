---
title: Empêcher l exportation du contenu de la feuille de calcul masqué lors de l enregistrement en HTML
type: docs
weight: 90
url: /fr/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel en HTML. Cependant, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu des feuilles de calcul masquées dans le répertoire de sortie HTML (_files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées dans le répertoire _files.

{{% /alert %}}

Aspose.Cells fournit la propriété [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet). Par défaut, la propriété [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) est définie sur **true**. Si vous la définissez sur **false**, alors Aspose.Cells n'exportera pas le contenu des feuilles de calcul masquées.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Outre le contrôle de l'exportation des feuilles de calcul masquées, vous pouvez également configurer des paramètres supplémentaires pour l'exportation du classeur au format HTML. Les articles suivants démontrent d'autres fonctionnalités prises en charge par Aspose.Cells pour l'exportation des classeurs au format HTML.

- [Convertir Excel en HTML avec des en-têtes](/cells/fr/java/convert-excel-to-html-with-headings/)
- [Exclure les styles inutilisés lors de la conversion d'Excel en HTML](/cells/fr/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML](/cells/fr/java/export-comments-while-saving-excel-file-to-html/)
- [Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML](/cells/fr/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web](/cells/fr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
