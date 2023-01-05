---
title: Kombinera flera arbetsböcker till en enda arbetsbok
linktitle: Sammanslagning av arbetsbok
type: docs
weight: 66
url: /sv/net/combine-multiple-workbooks-into-a-single-workbook/
---
{{% alert color="primary" %}}

Ibland måste du kombinera arbetsböcker med olika innehåll som bilder, diagram och data till en enda arbetsbok. Aspose.Cells stöder den här funktionen. Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio och kombinerar arbetsböcker med några enkla kodrader med Aspose.Cells.

{{% /alert %}}

## **Kombinera arbetsböcker med bilder och diagram**

Exempelkoden kombinerar två arbetsböcker till en enda arbetsbok med Aspose.Cells. Koden laddar källarbetsböckerna, använder[**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)metod för att kombinera dem och sparar utdataarbetsboken.

### **Källarbetsböcker**

- [charts.xlsx](5473097.xlsx)
- [bild.xlsx](5473096.xlsx)

### **Utdata arbetsböcker**

- [kombinerad.xlsx](5473095.xlsx)

### **Skärmdumpar**

Nedan finns skärmdumpar av käll- och utdataarbetsböckerna.

{{% alert color="primary" %}}

Du kan använda alla källarbetsböcker. Dessa bilder är bara för illustrationsändamål.

{{% /alert %}}

**Det första kalkylbladet i diagramarbetsboken - staplat** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Andra kalkylbladet med diagram arbetsbok - linje** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Första arbetsbladet i bildarbetsboken - bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alla tre kalkylbladen i den kombinerade arbetsboken - staplade, rad, bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Förhandsämnen**
- [Kombinera flera kalkylblad till ett enda kalkylblad](/cells/sv/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Slå samman filer](/cells/sv/net/merge-files/)
