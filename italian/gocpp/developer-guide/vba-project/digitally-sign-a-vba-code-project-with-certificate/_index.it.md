---
title: Firmare digitalmente un progetto di codice VBA con Certificato in C++
linktitle: Firma digitalmente un progetto di codice VBA con certificato
type: docs
weight: 110
url: /it/go-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Impara come firmare digitalmente il tuo progetto di codice VBA utilizzando Aspose.Cells for C++ con un certificato.
---

{{% alert color="primary" %}} 

Puoi firmare digitalmente il progetto di codice VBA usando Aspose.Cells con il suo metodo [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/). Segui questi passaggi per verificare se il file Excel è firmato digitalmente con un certificato.

- Clicca su **Visual Basic** dalla scheda **Sviluppatore** per aprire **Visual Basic for Applications IDE**.
- Clicca su **Strumenti** > **Digital Signatures...** di **Visual Basic for Applications IDE**.

Mostrerà il **Modulo Firma Digitale** indicando se il documento è firmato digitalmente con un certificato o meno.

{{% /alert %}} 

## **Firmare digitalmente un progetto di codice VBA con Certificato in C++**

Il seguente esempio di codice illustra come usare il metodo [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/). Qui ci sono i file di input e output del codice di esempio. Puoi usare qualsiasi file Excel e qualsiasi certificato per testare questo codice.

- [File Excel di origine](5115028.xlsm) utilizzato nel codice di esempio.
- [File pfx di esempio](5115039.pfx) per creare una firma digitale. Si prega di installarlo sul computer per eseguire questo codice. La password è 1234.
- [File Excel di output](5115029.xlsm) generato dal codice di esempio.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DigitallySignAVbaCodeProjectWithCertificate.go" >}}
