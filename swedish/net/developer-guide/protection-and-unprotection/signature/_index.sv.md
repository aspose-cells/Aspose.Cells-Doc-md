---
title: Tilldela och validera digitala signaturer
linktitle: Signatur
type: docs
weight: 140
url: /sv/net/assign-and-validate-digital-signatures/
description: Excel-fil digital signatur, verifiering. För att skydda äktheten av en arbetsboks innehåll i Excel-filen kan du lägga till en digital signatur med C#-koder med Aspose.Cells för .Net.
---
{{% alert color="primary" %}}

 En digital signatur ger en garanti för att en arbetsboksfil är giltig och att ingen har ändrat den. Du kan skapa en personlig digital signatur genom att använda**Microsoft Selfcert.exe** eller något annat verktyg, eller så kan du köpa en digital signatur. När du har skapat en digital signatur måste du bifoga den till din arbetsbok. Att fästa en digital signatur liknar att försegla ett kuvert. Om ett kuvert kommer förseglat har du en viss grad av säkerhet att ingen har manipulerat dess innehåll.

{{% /alert %}}

## **Introduktion**

 Använd dialogrutan Digital signatur för att bifoga en digital signatur. Dialogrutan Digital signatur listar giltiga certifikat. Du kan använda dialogrutan Digital signatur för att visa certifikat och välja det du vill använda. Om en arbetsbok har en digital signatur visas namnet på signaturen i**Certifikatnamn** fält. Om du klickar på**Ta bort** i dialogrutan Digital signatur tar Microsoft Excel också bort den digitala signaturen.

Aspose.Cells tillhandahåller[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)namnområde för att utföra jobbet (tilldela och validera digitala signaturer). Namnutrymmet har några användbara funktioner för att lägga till och validera digitala signaturer.

Se följande exempelkod som beskriver hur du kan utföra uppgiften med Aspose.Cells för .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Förhandsämnen**
- [Lägg till digital signatur i en redan signerad Excel-fil](/cells/sv/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Lägg till signaturrad i kalkylbladet](/cells/sv/net/add-signature-line/)
- [Stöd för XAdES Signature](/cells/sv/net/support-for-xades-signature/)
