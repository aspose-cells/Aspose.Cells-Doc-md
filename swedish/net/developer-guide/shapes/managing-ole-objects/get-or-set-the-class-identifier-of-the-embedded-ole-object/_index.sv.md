---
title: Hämta eller ställ in klassidentifieraren för det inbäddade OLE-objektet
type: docs
weight: 200
url: /sv/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Möjliga användningsscenarier**
 Aspose.Cells tillhandahåller[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)egenskap som du kan använda för att hämta eller ställa in klassidentifieraren för det inbäddade ole-objektet. Ole Object Class Identifiers är faktiskt GUID, dvs globalt unika identifierare. GUID är alltid 16 byte lång, därför är klassidentifierare också 16 byte långa. De finns ofta i Windows-registret och ger information till värdapplikationen om hur man öppnar inbäddade ole-objekt som innehåller olika inbäddade resurser i klientapplikationen.
## **Hämta eller ställ in klassidentifieraren för det inbäddade OLE-objektet**
 Följande skärmdump visar Ole Object Class Identifier dvs GUID som har lästs från[exempel på excel-fil](5115190.xls) som innehåller det inbäddade PowerPoint ole-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Exempelkod**
 Se följande exempelkod som körs med[exempel på excel-fil](5115190.xls)och dess konsolutgång som skriver ut klassidentifieraren för Ole Object dvs GUID. Den utskrivna GUID är exakt densamma som visas på skärmdumpen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Konsolutgång**
 Detta är konsolutgången för ovanstående exempelkod när den körs med[exempel på excel-fil](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
