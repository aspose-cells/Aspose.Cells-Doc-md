---
title: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet
type: docs
weight: 920
url: /sv/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller egenskapen [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier) som du kan använda för att hämta eller ange klassidentifieraren för ett inbäddat ole-objekt. Ole-objektens klassidentifierare är faktiskt GUID:er, dvs globalt unika identifierare. GUID är alltid 16 byte lång, därför är klassidentifierarna också 16 byte långa. De återfinns ofta i Windows-registret och ger information till värdprogrammet om hur man öppnar inbäddade ole-objekt som innehåller olika inbäddade resurser i klientprogrammet.
## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**
Bilden nedan visar Ole-objektets klassidentifierare dvs. GUID som har lästs från den [provexmelfilen](5473378.xls) som innehåller det inbäddade PowerPoint-ole-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Exempelkod**
Se kodexemplet nedan som körs med [provexmelfilen](5473378.xls) och dess konsoloutput som skriver ut *Klassidentifieraren* för Ole-objektet dvs. GUID. Den utskrivna GUID:en är exakt samma som visas i skärmbilden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Konsoloutput**
Det här är konsoloutputen från det ovanstående kodexemplet när det körs med [provexmelfilen](5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
