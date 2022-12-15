---
title: Kryptera och dekryptera ODS-filer
type: docs
weight: 10
url: /sv/net/encrypt-and-decrypt-ods-files/
description: lösenordsskydda och kryptera ODS-filer med Aspose.Cells för .Net som är ett rent nätbibliotek.
---
{{% alert color="primary" %}}
 OpenOffice.org är en fullfjädrad kontorssvit som stöder lösenordsskyddande och kryptering av filer. Krypterad ODS-fil kan dock endast öppnas av OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan ge ett varningsmeddelande. Krypteringsalternativen är inte tillämpliga för ODS-filer till skillnad från andra filtyper.
 Aspose.Cells gör det möjligt att kryptera och dekryptera ODS-fil. Dekrypterad ODS-fil kan öppnas både i Excel och OpenOffice,
{{% /alert %}}

## **Kryptera med OpenOffice Calc**
1.  Välj**Spara som** och klicka på**Spara med lösenord** låda.
1.  Klicka på**Spara** knapp.
1.  Skriv ditt önskade lösenord i både**Ange lösenord för att öppna** och**Bekräfta lösenord** fälten i fönstret Ange lösenord som öppnas.
1.  Klicka på**OK** knappen för att spara filen.

## **Kryptera ODS-fil med Aspose.Cells för .Net**
 För att kryptera en ODS-fil, ladda filen och ställ in[**Arbetsbok Inställningar. Lösenord**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) värde till det faktiska lösenordet innan du sparar det. Den utdatakrypterade ODS-filen kan endast öppnas i OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Dekryptera ODS-fil med Aspose.Cells för .Net**

 För att dekryptera en ODS-fil, ladda filen genom att ange ett lösenord i[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . När filen är laddad, ställ in[**Arbetsbok Inställningar. Lösenord**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) sträng till null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
