---
title: Désactiver l exportation des scripts de trame et des propriétés du document
type: docs
weight: 410
url: /fr/java/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}} 

Aspose.Cells exporte des scripts de cadre et des propriétés de document lors de la conversion d'un classeur en HTML. La version 8.6.0 de Aspose.Cells for Java introduit une option qui vous permet de désactiver facultativement l'exportation des scripts de cadre et des propriétés de document. Veuillez utiliser la propriété [HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) pour désactiver l'exportation.

{{% /alert %}} 
## **Désactiver l'exportation des scripts de trame et des propriétés du document**
Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

Voici un code d'échantillon.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
{{< app/cells/assistant language="java" >}}
