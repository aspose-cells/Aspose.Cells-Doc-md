---
title: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet
type: docs
weight: 200
url: /sv/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)-egenskapen som du kan använda för att hämta eller ställa in den klassidentifierare för inbäddat ole-objekt. Ole Object Class Identifier är faktiskt GUID:er dvs Globalt Unika Identifikatorer. GUID är alltid 16 byte långt, därför är Class Identifier också 16 byte långt. De finns ofta inuti Windows-registret och ger information till värdapplikationen om hur man öppnar inbäddat ole-objekt med olika inbäddade resurser inuti klientapplikationen.
## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**
Följande skärmbild visar Ole Object Class Identifier dvs GUID som har lästs från [provexempel Excel-filen](5115190.xls) som innehåller det inbäddade PowerPoint ole-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Exempelkod**
Vänligen se den följande provkoden som körs med [provexempelfilen](5115190.xls) och dess konsoloutput som skriver ut Class Identifier för Ole Object dvs GUID. Den utskrivna GUID är exakt densamma som visas inuti skärmbilden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Konsoloutput**
Detta är konsoloutputen av ovanstående provkod när den kördes med [provexempelfilen](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
