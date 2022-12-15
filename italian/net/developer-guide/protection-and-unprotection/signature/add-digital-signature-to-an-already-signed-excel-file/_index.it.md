---
title: Aggiungi la firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/net/add-digital-signature-to-an-already-signed-excel-file/
---
## **Possibili scenari di utilizzo**

 Aspose.Cells fornisce il[**Workbook.AddDigitalSignature(DigitalSignatureCollectiondigitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature)metodo che puoi utilizzare per aggiungere la firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si noti che durante l'aggiunta di una firma digitale a un documento Excel già firmato, se il documento originale è un documento generato Aspose.Cells, funziona bene. Ma se il documento originale è generato da altri motori (ad es. Microsoft Excel ecc.), Aspose.Cells non può mantenere lo stesso file dopo averlo caricato e risalvato, ciò renderà la firma originale non valida.

{{% /alert %}}

## **Aggiungi la firma digitale a un file Excel già firmato**

Il seguente codice di esempio ha dimostrato come utilizzare[**Workbook.AddDigitalSignature(DigitalSignatureCollectiondigitalSignatureCollection)**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/adddigitalsignature) metodo per aggiungere la firma digitale al file Excel già firmato. Si prega di controllare[esempio di file Excel](50528280.xlsx) utilizzato in questo codice. Questo file è già firmato digitalmente. Si prega di controllare[file Excel di output](50528281.xlsx) generato dal codice. Abbiamo utilizzato il certificato demo denominato[AsposeDemo.pfx](50528279.pfx) in questo codice che ha una password**asporre**. Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![cose da fare:immagine_alt_testo](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.cs" >}}
