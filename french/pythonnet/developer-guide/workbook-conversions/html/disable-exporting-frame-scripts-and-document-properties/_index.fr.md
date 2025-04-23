---
title: Désactiver l exportation des scripts de trame et des propriétés du document
type: docs
weight: 310
url: /fr/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET exporte les scripts de cadre et les propriétés du document lors de la conversion d’un classeur en HTML. La version 8.6.0 d’Aspose.Cells pour Python via .NET introduit une option qui permet de désactiver optionnellement l’exportation des scripts de cadre et des propriétés du document. Utilisez la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties pour désactiver l’exportation.

{{% /alert %}}

## **Désactiver l'exportation des scripts de trame et des propriétés du document**

Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
