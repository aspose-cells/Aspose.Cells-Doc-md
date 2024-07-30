---
title: Joindre une pièce jointe à un PDF
type: docs
weight: 380
url: /fr/net/embed-attachment-to-pdf/

---

Dans Excel, vous pouvez insérer un objet Ole avec les données source ([exemple-de-pièces-jointes-intégrées.xlsx](exemple-de-pièces-jointes-intégrées.xlsx)). Double-cliquez sur l'objet Ole, le fichier intégré sera ouvert.

Généralement, lors de la conversion en pdf, l'objet Ole sera rendu sous forme d'icône ou de vignette sans les données source de l'objet Ole. Avec l'option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), vous pouvez intégrer les données source de l'objet Ole en tant que pièce jointe dans le PDF. Vous pouvez double-cliquer sur l'icône ou la vignette dans le PDF pour ouvrir le fichier source de l'objet Ole.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![pièce-jointe-intégrée.png](pièce-jointe-intégrée.png)
