---
title: Kryptera och dekryptera ODS filer
type: docs
weight: 10
url: /sv/python-net/encrypt-and-decrypt-ods-files/
description: Lösenordsskydda och kryptera ODS filer med Aspose.Cells för Python via .NET som är ett rent net bibliotek.
---

{{% alert color="primary" %}}
OpenOffice.org är en komplett kontorspaket som stöder lösenordsskydd och kryptering av filer. En krypterad ODS-fil kan endast öppnas av OpenOffice efter att lösenordet har angetts. Excel kan inte öppna den krypterade ODS-filen och kan möjligen höja varningsmeddelande. Krypteringsalternativen är inte tillämpliga för ODS-filer som för andra filtyper. 
Aspose.Cells för Python via .NET tillåter att kryptera och dekryptera ODS-filer. Dekrypterade ODS-filer kan öppnas både i Excel och OpenOffice. 
{{% /alert %}}

## **Kryptera med OpenOffice Calc**
1. Välj **Spara som** och klicka på **Spara med lösenord**-rutan.
1. Klicka på **Spara**-knappen.
1. Skriv ditt önskade lösenord i både **Ange lösenord för att öppna** och **Bekräfta lösenord**-fälten i dialogrutan Ange lösenord som öppnas. 
1. Klicka på **OK**-knappen för att spara filen.

## **Kryptera ODS-fil med Aspose.Cells för Python via .NET**
För att kryptera en ODS-fil, ladda in filen och ställ in [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password)-värdet till det faktiska lösenordet innan du sparar den. Den utmatade krypterade ODS-filen kan öppnas i OpenOffice endast.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Dekryptera ODS-fil med Aspose.Cells för Pythohn via .NET**

För att dekryptera en ODS-fil, ladda in filen genom att ange ett lösenord i [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). När filen har laddats, ställ in strängen för [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) till null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
