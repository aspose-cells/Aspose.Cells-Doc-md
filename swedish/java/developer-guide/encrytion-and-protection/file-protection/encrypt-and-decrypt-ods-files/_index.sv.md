---
title: Kryptera och dekryptera ODS filer
type: docs
weight: 10
url: /sv/java/encrypt-and-decrypt-ods-files/
description: lösenordsskydda och kryptera ODS filer med Aspose.Cells for Java som är ett rent Java bibliotek.
---

{{% alert color="primary" %}}
OpenOffice.org är en komplett kontorspaket som stöder lösenordsskydd och kryptering av filer. En krypterad ODS-fil kan endast öppnas av OpenOffice efter att lösenordet har angetts. Excel kan inte öppna den krypterade ODS-filen och kan möjligen höja varningsmeddelande. Krypteringsalternativen är inte tillämpliga för ODS-filer som för andra filtyper. 
Aspose.Cells tillåter att kryptera och dekryptera ODS-fil. Dekrypterad ODS-fil kan öppnas både i Excel och OpenOffice. 
{{% /alert %}}

## **Kryptera med OpenOffice Calc**
1. Välj **Spara som** och klicka på **Spara med lösenord**-rutan.
1. Klicka på **Spara**-knappen.
1. Skriv ditt önskade lösenord i både **Ange lösenord för att öppna** och **Bekräfta lösenord**-fälten i dialogrutan Ange lösenord som öppnas. 
1. Klicka på **OK**-knappen för att spara filen.

## **Kryptera/Dekryptera ODS-fil:**

För att kryptera en ODS-fil, ladda in filen och ange det faktiska lösenordet till [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) innan du sparar det. Den krypterade utmatnings-ODS-filen kan endast öppnas i OpenOffice. För att dekryptera en ODS-fil, ladda in filen och ange lösenordet till [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). När filen har laddats, anropa funktionen [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect-java.lang.String-) med det faktiska lösenordet som argument och till slut ange null till [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Exempelkod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
{{< app/cells/assistant language="java" >}}
