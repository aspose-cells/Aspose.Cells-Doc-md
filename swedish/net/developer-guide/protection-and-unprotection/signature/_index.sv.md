---
title: Tilldela och validera digitala signaturer
linktitle: Signatur
type: docs
weight: 140
url: /sv/net/assign-and-validate-digital-signatures/
description: Excelfil digital signatur, verifiering. För att skydda äktheten av en arbetsboks innehåll i Excelfilen kan du lägga till en digital signatur med C# koder med Aspose.Cells för .Net.
keywords: Excel filens digitala signatur, Lägg till digital signatur för Excel, Så här validerar du digital signatur.
---

{{% alert color="primary" %}}

En digital signatur ger försäkran om att en arbetsboksfil är giltig och att ingen har ändrat den. Du kan skapa en personlig digital signatur med Microsoft Selfcert.exe eller något annat verktyg, eller så kan du köpa en digital signatur. När du har skapat en digital signatur måste du bifoga den till din arbetsbok. Att bifoga en digital signatur är liknande att försegla ett kuvert. Om ett kuvert kommer förseglad har du en viss nivå av försäkran om att ingen har manipulerat dess innehåll.

{{% /alert %}}

## **Introduktion**

Använd Digital Signature dialogrutan för att bifoga en digital signatur. Digital Signature dialogrutan listar giltiga certifikat. Du kan använda Digital Signature dialogrutan för att visa certifikat och välja det du vill använda. Om en arbetsbok har en digital signatur, visas namnet på signaturen i fältet Certifikatnamn. Om du klickar på knappen Ta bort i Digital Signature dialogrutan, tar Microsoft Excel bort den digitala signaturen också.

## **Så här lägger du till digital signatur för Excel**

Aspose.Cells tillhandahåller namespace [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature) för att utföra uppgiften (tilldela och validera digitala signaturer). Namespace har några användbara funktioner för att lägga till och validera digitala signaturer.

Se följande exempelkod som beskriver hur du kan utföra uppgiften med hjälp av Aspose.Cells for .NET APIen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Fortsatta ämnen**
- [Lägg till digital signatur i en redan signerad Excel-fil](/cells/sv/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Lägg till signaturraden i arbetsbladet](/cells/sv/net/add-signature-line/)
- [Stöd för XAdES-signatur](/cells/sv/net/support-for-xades-signature/)
