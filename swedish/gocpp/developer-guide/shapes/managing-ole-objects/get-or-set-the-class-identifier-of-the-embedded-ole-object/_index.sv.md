---
title: Få eller sätt klassidentifieraren för det inbäddade OLE objektet med Golang via C++
linktitle: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet
type: docs
weight: 200
url: /sv/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Lär dig att få eller sätta klassidentifieraren för inbäddade OLE objekt med Aspose.Cells och Golang via C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller egenskapen [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) som du kan använda för att få eller sätta klassidentifieraren för inbäddat OLE-objekt. Klassidentifierare för OLE-objekt är egentligen GUIDs, det vill säga globala unika identifierare. GUID är alltid 16 byte lång, därför är även Klassidentifierare 16 byte långa. De finns ofta i Windows-registret och ger information till värdprogrammet om hur man öppnar inbäddade OLE-objekt som innehåller olika inbäddade resurser i klientprogrammet.

## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**
Följande skärmdump visar OLE-objektklassidentifieraren, dvs. GUID, som har lästs från [exempel Excel-fil](5115190.xls) med det inbäddade PowerPoint-OLE-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Exempelkod**
Se följande exempelprogram som körs med den [exempel Excel-fil](5115190.xls) och dess konsolutmatning som skriver ut klassidentifieraren för OLE-objektet, dvs. GUID. Den utskrivna GUID är exakt densamma som visas i skärmbilden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **Konsoloutput**
Detta är konsoloutputen av ovanstående provkod när den kördes med [provexempelfilen](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
