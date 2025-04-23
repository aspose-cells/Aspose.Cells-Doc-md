---
title: Inaktivera kompatibilitetskontroll i Excel
type: docs
weight: 270
url: /sv/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excels kompatibilitetskontroll flaggar när du sparar en fil i ett tidigare filformat att sparandet av filen kan orsaka funktionalitetsproblem eller förlust av noggrannhet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007, 2010 och 2013.

När du sparar en arbetsbok i en tidigare version, Excel 97 genom Excel 2003, från Excel 2007 eller Excel 2010 skannar kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du hanterar kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken eller inaktivera funktionen.

Ibland behöver du inaktivera kompatibilitetskontrollen för en specifik kalkylblad. Med Aspose.Cells API:er kan du göra detta dynamiskt så att användarna inte blir frustrerade eller förvirrade av att kompatibilitetskontrollens dialogruta dyker upp när de sparar filen i Microsoft Excel manuellt.

{{% /alert %}}

## **Använda Microsoft Excel**

För att inaktivera kompatibilitetskontrollen i Microsoft Excel (t.ex. Microsoft Excel 2007/2010):

- (Excel 2007) Klicka på Office-knappen, klicka på **Förbered**, klicka på **Kör kompatibilitetskontroll**, och avmarkera sedan alternativet **Kontrollera kompatibilitet när du sparar arbetsboken**.
- (Excel 2010 och 2013) Klicka på fliken **Fil**, klicka på **Info**, klicka på **Sök efter problem**, klicka på **Kontrollera kompatibilitet**, och avmarkera slutligen alternativet **Kontrollera kompatibilitet när du sparar arbetsboken**.

## **Använda Aspose.Cells API:er**

Ställ in egenskapen [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) till **False** för att inaktivera Microsoft Excels kompatibilitetskontroll.

Antag att vi har en mall XLS-fil. När en användare sparar eller sparar om den i MS Excel 2007/2010/2013 visas dialogrutan Kompatibilitetskontroll, som visas i skärmbilden nedan.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

Följande kod visar hur du inaktiverar kompatibilitetskontrollen med Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
{{< app/cells/assistant language="java" >}}
