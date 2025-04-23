---
title: Kombinera flera arbetsböcker till en enda arbetsbok
linktitle: Arbetsboksfusion
type: docs
weight: 66
url: /sv/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Ibland måste du kombinera arbetsböcker med olika innehåll som bilder, diagram och data till ett enda arbetsblad. Aspose.Cells för Python via .NET stöder denna funktion. Den här artikeln visar hur man skapar en konsolapplikation i Visual Studio och kombinerar arbetsböcker med några enkla kodrader med Aspose.Cells för Python via .NET.

{{% /alert %}}

## **Kombinera arbetsböcker med bilder och diagram**

Exempel-koden kombinerar två arbetsböcker till en enda arbetsbok med Aspose.Cells för Python via .NET. Koden laddar in kälkarböckerna, använder [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine)-metoden för att slå ihop dem och sparar utdataarbetsboken.

### **Källarbetsböcker**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Resultatarbetsböcker**

- [combined.xlsx](5473095.xlsx)

### **Skärmbilder**

Här är skärmbilder på käll- och resultatarbetsböcker.

{{% alert color="primary" %}}

Du kan använda vilka källarbetsböcker som helst. Dessa bilder är bara för illustration.

{{% /alert %}}

**Den första arbetsbokens arbetsblad - staplad** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Andra arbetsbladet i arbetsboken - linje** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Första arbetsbladet i bildarbetsboken - bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alla tre arbetsblad i den kombinerade arbetsboken - staplad, linje, bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Fortsatta ämnen**
- [Kombinera flera arbetsblad till ett enda arbetsblad](/cells/sv/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Sammanfoga filer](/cells/sv/python-net/merge-files/)

