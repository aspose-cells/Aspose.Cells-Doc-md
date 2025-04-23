---
title: Intégrer la pièce jointe dans le PDF
type: docs
weight: 370
url: /fr/java/embed-attachment-to-pdf/

---

Dans Excel, vous pouvez insérer un objet Ole avec des données source ([exemple de pièce jointe intégrée.xlsx](embedded-attachments-example.xlsx)). Double-cliquez sur l'objet Ole, le fichier intégré s'ouvrira.

En général, lors de la conversion en PDF, l'objet Ole sera affiché comme une icône ou une miniature sans ses données source. Avec l'option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), vous pouvez intégrer la source de l'objet Ole en tant que pièce jointe dans le PDF. Double-cliquez sur l'icône ou la miniature dans le PDF pour ouvrir le fichier source de l'objet Ole.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
