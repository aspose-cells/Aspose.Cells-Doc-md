---
title: Aggiungere firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/net/add-digital-signature-to-an-already-signed-excel-file/
description: Questo articolo descrive come Aggiungere una Firma Digitale a un file Excel già firmato utilizzando codici C# con Aspose.Cells for .Net.
keywords: Aggiungere una firma digitale a un documento Excel già firmato, Come aggiungere una firma digitale a un documento Excel già firmato.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce il metodo [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) che puoi usare per aggiungere una firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si prega di notare che aggiungendo una firma digitale a un documento Excel già firmato, se il documento originale è un documento generato da Aspose.Cells, funziona bene. Ma se il documento originale è stato generato da altri motori (ad es. Microsoft Excel, ecc.), Aspose.Cells non può mantenere lo stesso file dopo il caricamento e il re-salvataggio, rendendo la firma originale non valida.

{{% /alert %}}

## **Come Aggiungere una Firma Digitale a un Documento Excel Già Firmato**

Il seguente codice di esempio ha dimostrato come utilizzare il metodo [**Workbook.AddDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) per aggiungere una firma digitale a un file Excel già firmato. Si prega di controllare il [file Excel di esempio](50528280.xlsx) utilizzato in questo codice. Questo file è già firmato digitalmente. Si prega di controllare il [file Excel di output](50528281.xlsx) generato dal codice. Abbiamo utilizzato il certificato demo chiamato [AsposeDemo.pfx](50528279.pfx) in questo codice che ha una password **aspose**. La schermata mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
