---
title: Inaktivera kompatibilitetskontrollen i Excel
type: docs
weight: 270
url: /sv/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft Excels kompatibilitetskontroll flaggar när du sparar en fil i ett tidigare filformat att sparande av filen kan orsaka funktionsproblem eller förlust av trovärdighet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007, 2010 och 2013.

När du sparar en arbetsbok i en tidigare version, Excel 97 till Excel 2003, från Excel 2007 eller Excel 2010, genomsöker kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du ska hantera kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken, eller inaktivera funktionen.

Ibland måste du inaktivera kompatibilitetskontrollen för ett visst kalkylblad. Med Aspose.Cells' API:er kan du göra detta dynamiskt så att användarna inte blir frustrerade eller förvirrade av dialogrutan Kompatibilitetskontroll som dyker upp när de manuellt sparar filen i Microsoft Excel.

{{% /alert %}}

## **Använder Microsoft Excel**

Så här inaktiverar du kompatibilitetskontrollen i Microsoft Excel (till exempel Microsoft Excel 2007/2010):

-  (Excel 2007) Klicka på Office-knappen**Förbereda** , då**Kör kompatibilitetskontrollen** , och rensa sedan**Kontrollera kompatibiliteten när du sparar den här arbetsboken** alternativ.
-  (Excel 2010 & 2013) Klicka på fliken Arkiv**Info** , då**Kontrollera om det finns problem** , klick**Kontrollera kompatibilitet** , och slutligen, rensa**Kontrollera kompatibiliteten när du sparar den här arbetsboken** alternativ.

## **Använder Aspose.Cells API:er**

 Ställ in[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) egendom till**Falsk** för att inaktivera Microsoft Excels kompatibilitetskontroll.

Anta att vi har en mall XLS-fil. När en användare sparar eller sparar om det i MS Excel 2007/2010/2013, visas dialogrutan Kompatibilitetskontroll, som visas i skärmdumpen nedan.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

Följande kod visar hur du inaktiverar kompatibilitetskontrollen med Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
