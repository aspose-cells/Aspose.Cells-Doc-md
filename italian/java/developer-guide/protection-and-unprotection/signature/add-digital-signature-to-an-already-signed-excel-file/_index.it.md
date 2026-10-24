---
title: Aggiungere firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce il metodo [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) che puoi utilizzare per aggiungere una firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si prega di notare che aggiungendo una firma digitale a un documento Excel già firmato, se il documento originale è un documento generato da Aspose.Cells, funziona bene. Ma se il documento originale è stato generato da altri motori (ad es. Microsoft Excel, ecc.), Aspose.Cells non può mantenere lo stesso file dopo il caricamento e il re-salvataggio, rendendo la firma originale non valida.

{{% /alert %}}

## **Aggiungi firma digitale a un file Excel già firmato**

Il seguente codice di esempio spiega come utilizzare il metodo [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) per aggiungere una firma digitale a un file Excel già firmato. Controlla il [file Excel di esempio](50528287.xlsx) utilizzato in questo codice. Questo file è già firmato digitalmente. Controlla il [file Excel di output](50528288.xlsx) generato dal codice. Abbiamo utilizzato il certificato dimostrativo chiamato [AsposeTest.pfx](50528289.pfx) in questo codice che ha una password *aspose*. La schermata mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
