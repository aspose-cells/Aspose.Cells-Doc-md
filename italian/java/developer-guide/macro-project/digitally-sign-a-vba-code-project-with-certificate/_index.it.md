---
title: Firma digitalmente un progetto di codice VBA con certificato
type: docs
weight: 110
url: /it/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Puoi firmare digitalmente il tuo progetto di codice VBA utilizzando Aspose.Cells con il suo metodo [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature)). Si prega di seguire questi passaggi per verificare se il tuo file di Excel è digitalmente firmato con un certificato.

- Fare clic su **Visual Basic** dalla scheda **Sviluppo** per aprire l'**IDE di Visual Basic for Applications**
- Fare clic su **Strumenti** > **Firme digitali...** dell' **IDE di Visual Basic for Applications**

e verrà mostrato il **Modulo di firma digitale** che indica se il documento è firmato digitalmente con un certificato o meno.

{{% /alert %}} 

## **Firma digitalmente un progetto di codice VBA con certificato in C#**

Il seguente codice di esempio illustra come utilizzare il metodo [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature)). Ecco i file di input e output del codice di esempio. Puoi utilizzare qualsiasi file Excel e qualsiasi certificato per testare questo codice.

- [File Excel di origine](5115028.xlsm) utilizzato nel codice di esempio.
- [File pfx di esempio](5115039.pfx) per creare una firma digitale. Si prega di installarlo sul computer per eseguire questo codice. La password è 1234.
- [File Excel di output](5115029.xlsm) generato dal codice di esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
