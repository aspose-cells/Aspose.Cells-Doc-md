---
title: Hämta eller ställ in klassidentifieraren för det inbäddade OLE-objektet
type: docs
weight: 920
url: /sv/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Möjliga användningsscenarier**
 Aspose.Cells tillhandahåller[OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)egenskap som du kan använda för att hämta eller ställa in klassidentifieraren för ett inbäddat ole-objekt. Ole Object Class Identifiers är faktiskt GUID, dvs globalt unika identifierare. GUID är alltid 16 byte lång, därför är klassidentifierare också 16 byte långa. De finns ofta i Windows-registret och ger information till värdapplikationen om hur man öppnar inbäddade ole-objekt som innehåller olika inbäddade resurser i klientapplikationen.
## **Hämta eller ställ in klassidentifieraren för det inbäddade OLE-objektet**
 Följande skärmdump visar Ole Object Class Identifier dvs GUID som har lästs från[exempel på excel-fil](5473378.xls) som innehåller det inbäddade PowerPoint ole-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Exempelkod**
 Se följande exempelkod som körs med[exempel på excel-fil](5473378.xls) och dess konsolutgång som skriver ut*Klassidentifierare*av Ole Object dvs GUID. Den utskrivna GUID är exakt densamma som visas på skärmdumpen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Konsolutgång**
 Detta är konsolutgången för ovanstående exempelkod när den körs med[exempel på excel-fil](5473378.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
