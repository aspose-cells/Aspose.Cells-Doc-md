---
title: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet
type: docs
weight: 200
url: /sv/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Möjliga användningsscenario**
Aspose.Cells för Python via .NET ger egenskapen [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier), som du kan använda för att hämta eller ställa in klassidentifieraren för inbäddade ole-objekt. Ole-objektsklassidentifierare är faktiskt GUID:er, dvs Globally Unique Identifiers. GUID är alltid 16 byte lång, så klassidentifierare är också 16 byte. De hittas ofta i Windows-registret och ger värdefull information till värdsapplikationen om hur man öppnar inbäddade ole-objekt som innehåller olika inbäddade resurser i klientapplikationen.

## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**
Följande skärmbild visar Ole Object Class Identifier dvs GUID som har lästs från [provexempel Excel-filen](5115190.xls) som innehåller det inbäddade PowerPoint ole-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Exempelkod**
Vänligen se den följande provkoden som körs med [provexempelfilen](5115190.xls) och dess konsoloutput som skriver ut Class Identifier för Ole Object dvs GUID. Den utskrivna GUID är exakt densamma som visas inuti skärmbilden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **Konsoloutput**
Detta är konsoloutputen av ovanstående provkod när den kördes med [provexempelfilen](5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
