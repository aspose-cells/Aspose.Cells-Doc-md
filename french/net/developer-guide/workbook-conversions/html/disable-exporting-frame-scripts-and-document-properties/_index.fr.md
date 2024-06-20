---
title: Désactiver l exportation des scripts de trame et des propriétés du document
type: docs
weight: 310
url: /fr/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells exporte des scripts de trame et des propriétés de document lors de la conversion d'un classeur en HTML. La version 8.6.0 de Aspose.Cells for .NET introduit une option qui vous permet de désactiver facultativement l'exportation des scripts de trame et des propriétés du document. Veuillez utiliser la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties pour désactiver l'exportation.

{{% /alert %}}

## **Désactiver l'exportation des scripts de trame et des propriétés du document**

Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
