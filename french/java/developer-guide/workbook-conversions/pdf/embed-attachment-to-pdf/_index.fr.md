---
title: Joindre une pièce jointe à un PDF
type: docs
weight: 370
url: /fr/java/embed-attachment-to-pdf/

---

Dans Excel, vous pouvez insérer un objet Ole avec les données source ([exemple-de-pièces-jointes-intégrées.xlsx](exemple-de-pièces-jointes-intégrées.xlsx)). Double-cliquez sur l'objet Ole, le fichier intégré sera ouvert.

Généralement, lors de la conversion en pdf, l'objet Ole sera rendu sous forme d'icône ou de vignette sans les données source de l'objet Ole. Avec l'option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), vous pouvez intégrer les données source de l'objet Ole en tant que pièce jointe dans le PDF. Vous pouvez double-cliquer sur l'icône ou la vignette dans le PDF pour ouvrir le fichier source de l'objet Ole.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![pièce-jointe-intégrée.png](pièce-jointe-intégrée.png)

