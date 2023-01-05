---
title: Tilldela och validera digitala signaturer
linktitle: Signatur
type: docs
weight: 100
url: /sv/java/assign-and-validate-digital-signatures/
description: Excel-fil digital signatur, verifiering. För att skydda äktheten av en arbetsboks innehåll i Excel-filen kan du lägga till en digital signatur med C#-koder med Aspose.Cells för .Net.
---
{{% alert color="primary" %}}

 En digital signatur ger en garanti för att en arbetsboksfil är giltig och att ingen har ändrat den. Du kan skapa en personlig digital signatur genom att använda**SELFCERT** verktyg levereras med Microsoft Office-paket eller något annat verktyg. Du kan till och med köpa en digital signatur. När du har skapat eller skaffat en digital signatur måste du bifoga den till din arbetsbok. Att fästa en digital signatur liknar att försegla ett kuvert. Om ett kuvert kommer förseglat har du en viss grad av säkerhet att ingen har manipulerat dess innehåll.

 Aspose.Cells for Java API tillhandahålla[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) klasser för att signera kalkylbladen samt validera dem.

{{% /alert %}}

## **Signera kalkylbladen**

Signeringsprocessen kräver ett certifikat enligt ovan. Tillsammans med certifikatet bör man också ha sitt lösenord för att framgångsrikt signera kalkylarken med Aspose.Cells API.

Följande kodavsnitt visar användningen av Aspose.Cells for Java API för att signera ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 Om det angivna lösenordet inte stämmer överens med lösenordet för certifikatet är ett undantag av typen*javax.crypto.BadPaddingException* kommer att kastas.

{{% /alert %}}

## **Validerar kalkylbladen**

Följande kodavsnitt visar användningen av Aspose.Cells for Java API för att validera kalkylarket.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
