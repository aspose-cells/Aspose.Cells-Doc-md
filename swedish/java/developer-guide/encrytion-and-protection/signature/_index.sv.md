---
title: Tilldela och validera digitala signaturer
linktitle: Signatur
type: docs
weight: 100
url: /sv/java/assign-and-validate-digital-signatures/
description: Excelfil digital signatur, verifiering. För att skydda äktheten av en arbetsboks innehåll i Excelfilen kan du lägga till en digital signatur med C# koder med Aspose.Cells för .Net.
---

{{% alert color="primary" %}}

En digital signatur ger försäkran om att en arbetsboksfil är giltig och att ingen har ändrat den. Du kan skapa en personlig digital signatur med hjälp av verktyget **SELFCERT** som levereras med Microsoft Office-paketet eller något annat verktyg. Du kan även köpa en digital signatur. Efter att du har skapat eller skaffat en digital signatur måste du bifoga den till din arbetsbok. Att bifoga en digital signatur liknar att försegla ett kuvert. Om ett kuvert kommer förseglade har du en viss nivå av försäkran om att ingen har manipulerat dess innehåll.

Aspose.Cells for Java API tillhandahåller klasserna [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) för att signera kalkylbladen såväl som validera dem.

{{% /alert %}}

## **Att signera kalkylbladen kräver ett certifikat som diskuterats ovan. Tillsammans med certifikatet bör man också ha dess lösenord för att framgångsrikt signera kalkylbladen med hjälp av Aspose.Cells API.**

Följande kodsnutt demonstrerar användningen av Aspose.Cells for Java API för att signera en kalkylblad.

Följande kodsnutt visar användningen av Aspose.Cells for Java API för att signera ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

Om det angivna lösenordet inte matchar med lösenordet för certifikatet, kastas ett undantag av typen *javax.crypto.BadPaddingException*.

{{% /alert %}}

## **Validering av kalkylblad**

Följande kodsnutt visar användningen av Aspose.Cells for Java API för att validera kalkylarket.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
