---
title: Désactiver l'exportation des scripts de cadre et des propriétés du document
type: docs
weight: 310
url: /fr/net/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}}

Aspose.Cells exporte des scripts de cadre et des propriétés de document lors de la conversion d'un classeur en HTML. La version 8.6.0 de Aspose.Cells for .NET introduit une option qui vous permet de désactiver éventuellement l'exportation de scripts de cadre et de propriétés de document. Veuillez utiliser la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties pour désactiver l'exportation.

{{% /alert %}}

## **Désactiver l'exportation des scripts de cadre et des propriétés du document**

L'exemple de code suivant vous permet de désactiver l'exportation de scripts de cadre et de propriétés de document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de cadre ni aucune propriété de document.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
