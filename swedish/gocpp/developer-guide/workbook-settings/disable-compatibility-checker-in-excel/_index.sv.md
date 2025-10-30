---
title: Inaktivera kompatibilitetskontroll i Excel med Golang via C++
linktitle: Inaktivera kompatibilitetskoll
type: docs
weight: 170
url: /sv/go-cpp/disable-compatibility-checker-in-excel/
description: Denna artikel visar hur man inaktiverar kompatibilitetskoll via API n Aspose.Cells for C++.
keywords: C++ Inaktivera kompatibilitetskoll, Excel inaktiverar kompatibilitetskoll i C++, Inaktivera kompatibilitetskoll i arbetsbok. 
---

## Inaktivera kompatibilitetskoll i Excel-arbetsblad i C++

{{% alert color="primary" %}}

Microsoft Excels kompatibilitetskontroll flaggar för när en fil sparas i ett tidigare filformat kan orsaka funktionalitetsproblem eller förlust av fidelitet. Kompatibilitetskontrollen är en funktion i Microsoft Office Excel 2007 och Microsoft Excel 2010.

När du sparar en arbetsbok i en tidigare version, Excel 97 genom Excel 2003, från Excel 2007 eller Excel 2010 skannar kompatibilitetskontrollen arbetsboken för att se om den innehåller funktioner som inte stöds av den tidigare versionen. För att hjälpa dig fatta beslut om hur du hanterar kompatibilitetsproblem visar kompatibilitetskontrollen dialogrutor med alternativ. Den kan också användas för att skapa en rapport om eventuella problem i arbetsboken eller inaktivera funktionen.

Ibland behöver du inaktivera Kompatibilitetskontrollen för en viss kalkylblad. Med Aspose.Cells-API kan du göra detta programmatiskt så att användare inte blir frustrerade eller förvirrade av dialogrutan för Kompatibilitetskontroll som dyker upp när de sparar filen i Microsoft Excel manuellt.

{{% /alert %}}

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Microsoft Excel**

För att inaktivera kompatibilitetskontrollen i Microsoft Excel (t.ex. Microsoft Excel 2007/2010):

- (Excel 2007) Klicka på Office-knappen, klicka på **Förbered**, klicka på **Kör kompatibilitetskontroll**, och avmarkera sedan alternativet **Kontrollera kompatibilitet när du sparar arbetsboken**.
- (Excel 2010) På fliken Fil klickar du på **Info**, sedan **Sök efter problem**, klickar på **Kontrollera kompatibilitet** och avmarkerar till sist alternativet **Kontrollera kompatibilitet när du sparar den här arbetsboken**.

## **Hur man inaktiverar kompatibilitetskontrollen med hjälp av Aspose.Cells API:er**

Ställ in egenskapen [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcheckcompatibility/) till **False** för att inaktivera Microsoft Excels kompatibilitetskontroll.

### **Kodexempel**

Följande kodexempel visar hur man inaktiverar kompatibilitetskoll med Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCompatibilityCheckerInExcel.go" >}}
