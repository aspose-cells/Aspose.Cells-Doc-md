---
title: Intégrer une pièce jointe dans un PDF avec Golang via C++
linktitle: Intégrer la pièce jointe dans le PDF
type: docs
weight: 380
url: /fr/go-cpp/embed-attachment-to-pdf/
description: Apprenez à intégrer des pièces jointes dans un PDF en utilisant Aspose.Cells avec Golang via C++.
---

Dans Excel, vous pouvez insérer un objet OLE avec des données source ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double-cliquez sur l'objet OLE, le fichier incorporé s'ouvrira.

En général, lors de la conversion en PDF, l'objet Ole sera rendu sous forme d'une icône ou d'une miniature sans les données source de l'objet Ole. Avec l'option [PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getembedattachments/), vous pouvez intégrer les données source de l'objet Ole en tant que pièce jointe dans le PDF. Vous pouvez double-cliquer sur l'icône ou la miniature dans le PDF pour ouvrir le fichier source de l'objet Ole.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EmbedAttachmentToPdf.go" >}}
![embedded-attachment.png](embedded-attachment.png)
