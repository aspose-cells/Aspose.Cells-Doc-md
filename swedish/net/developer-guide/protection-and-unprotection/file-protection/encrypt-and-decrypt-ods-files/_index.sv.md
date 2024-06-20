---
title: Kryptera och dekryptera ODS filer
type: docs
weight: 10
url: /sv/net/encrypt-and-decrypt-ods-files/
description: Lösenordsskydda och kryptera ODS filer med Aspose.Cells för .Net vilket är ett rent netto bibliotek.
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

## **Kryptera ODS-fil med Aspose.Cells för .Net**
För att kryptera en ODS-fil, ladda in filen och ställ in [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)-värdet till det faktiska lösenordet innan du sparar den. Den utmatade krypterade ODS-filen kan öppnas i OpenOffice endast.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Dekryptera ODS-fil med Aspose.Cells för .Net**

För att dekryptera en ODS-fil, ladda in filen genom att ange ett lösenord i [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). När filen har laddats, ställ in strängen för [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) till null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
