---
title: Aggiungere firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: Questo articolo descrive come aggiungere una firma digitale a un file Excel già firmato usando codici C# con Aspose.Cells per Python via .NET.
keywords: Aggiungere una firma digitale a un documento Excel già firmato, Come aggiungere una firma digitale a un documento Excel già firmato.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells per Python via .NET offre il metodo [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) che puoi usare per aggiungere una firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si prega di notare che, durante l'aggiunta di una firma digitale a un documento Excel già firmato, se il documento originale è stato generato con Aspose.Cells per Python via .NET, funziona correttamente. Ma se il documento originale è stato generato da altri motori (ad esempio Microsoft Excel, ecc.), Aspose.Cells per Python via .NET potrebbe non mantenere il file identico dopo il caricamento e il salvataggio, rendendo invalida la firma originale.

{{% /alert %}}

## **Come Aggiungere una Firma Digitale a un Documento Excel Già Firmato**

Il seguente codice di esempio ha dimostrato come utilizzare il metodo [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) per aggiungere una firma digitale a un file Excel già firmato. Si prega di controllare il [file Excel di esempio](50528280.xlsx) utilizzato in questo codice. Questo file è già firmato digitalmente. Si prega di controllare il [file Excel di output](50528281.xlsx) generato dal codice. Abbiamo utilizzato il certificato demo chiamato [AsposeDemo.pfx](50528279.pfx) in questo codice che ha una password **aspose**. La schermata mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
