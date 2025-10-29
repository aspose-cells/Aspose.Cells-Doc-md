---
title: Désactiver l exportation des scripts de cadre et des propriétés du document avec Golang via C++
type: docs
weight: 310
url: /fr/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Désactiver l exportation des scripts de cadre et des propriétés du document avec Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

 Aspose.Cells exporte les scripts de cadre et les propriétés du document lors de la conversion d’un classeur en HTML. La version 8.6.0 de Aspose.Cells for C++ introduit une option permettant de désactiver l’exportation des scripts de cadre et des propriétés du document. Veuillez utiliser la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties pour désactiver l’export.

{{% /alert %}}

## **Désactiver l'exportation des scripts de trame et des propriétés du document**

Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
