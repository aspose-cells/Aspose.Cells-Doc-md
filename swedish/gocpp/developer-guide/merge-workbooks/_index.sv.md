---
title: Kombinera flera arbetsböcker till en enda arbetsbok med Golang via C++
linktitle: Arbetsboksfusion
type: docs
weight: 66
url: /sv/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Lär dig hur man kombinerar flera arbetsböcker till en enda arbetsbok med Aspose.Cells för Golang via C++.
---

{{% alert color="primary" %}}

Ibland behöver du kombinera arbetsböcker med olika innehåll som bilder, diagram och data till en enda arbetsbok. Aspose.Cells stöder denna funktion. Den här artikeln visar hur man skapar en konsolapplikation i Visual Studio och kombinerar arbetsböcker med några enkla kodrader med Aspose.Cells.

{{% /alert %}}

## **Kombinera arbetsböcker med bilder och diagram**

Exempelkoden kombinerar två arbetsböcker till en enda arbetsbok med hjälp av Aspose.Cells. Koden laddar de ursprungliga arbetsböckerna, använder metoden [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) för att kombinera dem och sparar utdataarbetsboken.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Fortsatta ämnen**
- [Kombinera flera arbetsblad till ett enda arbetsblad](/cells/sv/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Sammanfoga filer](/cells/sv/cpp/merge-files/)
