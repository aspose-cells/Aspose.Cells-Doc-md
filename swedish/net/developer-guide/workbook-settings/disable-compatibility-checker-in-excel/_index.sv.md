---
title: Inaktivera kompatibilitetskontrollen i Excel
type: docs
weight: 170
url: /sv/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## Inaktivera kompatibilitetskontroll i Excel-kalkylblad i C#

{{% alert color="primary" %}}

Microsoft Excels flaggor för kompatibilitetskontroll när du sparar en fil i ett tidigare filformat kan orsaka funktionsproblem eller förlust av trovärdighet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007 och Microsoft Excel 2010.

När du sparar en arbetsbok i en tidigare version, Excel 97 till Excel 2003, från Excel 2007 eller Excel 2010, genomsöker kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du ska hantera kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken, eller inaktivera funktionen.

Ibland måste du inaktivera kompatibilitetskontrollen för ett visst kalkylblad. Med Aspose.Cells' API:er kan du göra detta programmatiskt så att användare inte blir frustrerade eller förvirrade av dialogrutan Kompatibilitetskontroll som dyker upp när de manuellt sparar filen i Microsoft Excel.

{{% /alert %}}

## **Använder Microsoft Excel**

Så här inaktiverar du kompatibilitetskontrollen i Microsoft Excel (till exempel Microsoft Excel 2007/2010):

-  (Excel 2007) Klicka på Office-knappen**Förbereda** , då**Kör kompatibilitetskontrollen** , och rensa sedan**Kontrollera kompatibiliteten när du sparar den här arbetsboken** alternativ.
-  (Excel 2010) Klicka på fliken Arkiv**Info** , då**Kontrollera om det finns problem** , klick**Kontrollera kompatibilitet** , och slutligen, rensa**Kontrollera kompatibiliteten när du sparar den här arbetsboken** alternativ.

## **Använder Aspose.Cells API:er**

 Ställ in[**Arbetsbok.Inställningar.Kontrollera kompatibilitet**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) egendom till**Falsk** för att inaktivera Microsoft Excels kompatibilitetskontroll.

### **Kodexempel**

Kodexemplen som följer visar hur du inaktiverar kompatibilitetskontrollen med Aspose.Cells för .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
