---
title: Kryptera och dekryptera ODS-filer
type: docs
weight: 10
url: /sv/java/encrypt-and-decrypt-ods-files/
description: lösenordsskydda och kryptera ODS-filer med Aspose.Cells for Java som är ett rent Java-bibliotek.
---
{{% alert color="primary" %}}
OpenOffice.org är en fullfjädrad kontorssvit som stöder lösenordsskyddande och kryptering av filer. Krypterad ODS-fil kan dock endast öppnas av OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan ge ett varningsmeddelande. Krypteringsalternativen är inte tillämpliga för ODS-filen till skillnad från andra filtyper.
 Aspose.Cells gör det möjligt att kryptera och dekryptera ODS-filen. Dekrypterad ODS fil kan öppnas både i Excel och OpenOffice,
{{% /alert %}}

## **Kryptera med OpenOffice Calc**
1.  Välj**Spara som** och klicka på**Spara med lösenord** låda.
1.  Klicka på**Spara** knapp.
1.  Skriv ditt önskade lösenord i både**Ange lösenord för att öppna** och**Bekräfta lösenord** fälten i fönstret Ange lösenord som öppnas.
1.  Klicka på**OK** knappen för att spara filen.

## **Kryptera/dekryptera ODS Fil:**

 För att kryptera en ODS-fil, ladda filen och skicka det faktiska lösenordet till[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)innan du sparar den. Den utdatakrypterade ODS-filen kan endast öppnas i OpenOffice. För att dekryptera en ODS-fil, ladda filen genom att ange lösenordet i[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . När filen är laddad, ring funktionen[**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) med det faktiska lösenordet som argument och skicka slutligen null till[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Exempelkod:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
