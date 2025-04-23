---
title: Intégrer la pièce jointe dans le PDF
type: docs
weight: 380
url: /fr/net/embed-attachment-to-pdf/

---

Dans Excel, vous pouvez insérer un objet Ole avec des données source ([exemple de pièce jointe intégrée.xlsx](embedded-attachments-example.xlsx)). Double-cliquez sur l'objet Ole, le fichier intégré s'ouvrira.

Généralement, lors de la conversion en PDF, l'objet Ole sera rendu sous forme d'icône ou de miniature sans les données sources de l'objet Ole. Avec l'option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/), vous pouvez intégrer les données sources de l'objet Ole en tant que pièce jointe dans le PDF. Vous pouvez double-cliquer sur l'icône ou la miniature dans le PDF pour ouvrir le fichier source de l'objet Ole.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
