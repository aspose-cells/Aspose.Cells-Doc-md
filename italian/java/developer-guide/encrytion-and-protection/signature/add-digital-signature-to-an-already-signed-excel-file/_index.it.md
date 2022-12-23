---
title: Aggiungi la firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **Possibili scenari di utilizzo**

Aspose.Cells fornisce il[**Workbook.addDigitalSignature(DigitalSignatureCollectiondigitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) che è possibile utilizzare per aggiungere la firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si noti che durante l'aggiunta di una firma digitale a un documento Excel già firmato, se il documento originale è un documento generato Aspose.Cells, funziona bene. Ma se il documento originale è generato da altri motori (ad es. Microsoft Excel ecc.), Aspose.Cells non può mantenere lo stesso file dopo averlo caricato e risalvato, ciò renderà la firma originale non valida.

{{% /alert %}}

## **Aggiungi la firma digitale a un file Excel già firmato**

Il seguente codice di esempio spiega come utilizzare[**Workbook.addDigitalSignature(DigitalSignatureCollectiondigitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) metodo per aggiungere una firma digitale al file Excel già firmato. Si prega di controllare[esempio di file Excel](50528287.xlsx)utilizzato in questo codice. Questo file è già firmato digitalmente. Si prega di controllare[file Excel di output](50528288.xlsx)generato dal codice. Abbiamo utilizzato il certificato demo denominato[AsposeTest.pfx](50528289.pfx)in questo codice che ha una password*asporre*Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![cose da fare:immagine_alt_testo](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
