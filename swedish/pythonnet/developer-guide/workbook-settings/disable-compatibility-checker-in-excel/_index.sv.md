---
title: Inaktivera kompatibilitetskontroll i Excel
type: docs
weight: 170
url: /sv/python-net/disable-compatibility-checker-in-excel/
description: Denna artikel visar hur man inaktiverar kompatibilitetskollare via Aspose.Cells för Python via .NET API.
keywords: Python Inaktivera kompatibilitetskollare, Excel inaktivera kompatibilitetskollare i C#, Inaktivera kompatibilitetskollare i arbetsbok. 
---

## Inaktivera kompatibilitetskollare i Excel-ark i Python 

{{% alert color="primary" %}}

Microsoft Excels kompatibilitetskontroll flaggar för när en fil sparas i ett tidigare filformat kan orsaka funktionalitetsproblem eller förlust av fidelitet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007 och Microsoft Excel 2010.

När du sparar en arbetsbok i en tidigare version, Excel 97 genom Excel 2003, från Excel 2007 eller Excel 2010 skannar kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du hanterar kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken eller inaktivera funktionen.

Ibland behöver du inaktivera kompatibilitetskollare för ett särskilt kalkylblad. Med Aspose.Cells för Python via .NET API kan du göra detta programmatiskt så att användare inte blir frustrerade eller förvirrade av dialogrutan för kompatibilitetskollare som dyker upp när de spara om filen manuellt i Microsoft Excel.

{{% /alert %}}

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Microsoft Excel**

För att inaktivera kompatibilitetskontrollen i Microsoft Excel (t.ex. Microsoft Excel 2007/2010):

- (Excel 2007) Klicka på Office-knappen, klicka på **Förbered**, klicka på **Kör kompatibilitetskontroll**, och avmarkera sedan alternativet **Kontrollera kompatibilitet när du sparar arbetsboken**.
- (Excel 2010) På fliken Fil klickar du på **Info**, sedan **Sök efter problem**, klickar på **Kontrollera kompatibilitet** och avmarkerar till sist alternativet **Kontrollera kompatibilitet när du sparar den här arbetsboken**.

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Aspose.Cells API:er**

Ställ in egenskapen [**Workbook.settings.check_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_compatibility) till **False** för att inaktivera Microsoft Excels kompatibilitetskontroll.

### **Kodexempel**

De kodexempel som följer visar hur man inaktiverar kompatibilitetskollare med Aspose.Cells för Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-DisableCompatibilityChecker-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
