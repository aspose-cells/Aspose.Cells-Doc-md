---
title: Extrahera OLE objekt från arbetsbok med Golang via C++
linktitle: Extrahera OLE objekt från arbetsboken
type: docs
weight: 110
url: /sv/go-cpp/extract-ole-objects-from-workbook/
description: Lär dig att extrahera OLE objekt från en arbetsbok med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

Ibland behöver du extrahera OLE-objekt från en arbetsbok. Aspose.Cells stöder att extrahera och spara dessa OLE-objekt.

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio och extraherar olika OLE-objekt från en arbetsbok med några enkla kodrader.

{{% /alert %}}

## **Extrahera OLE-objekt från en arbetsbok**

### **Skapa en mallarbok**

1. Skapa en arbetsbok i Microsoft Excel.
1. Lägg till ett Microsoft Word-dokument, en Excel-arbetsbok och ett PDF-dokument som OLE-objekt på det första arbetsbladet.

|**Mall-dokument med OLE-objekt (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Nästa steg, extrahera OLE-objekten och spara dem på hårddisken med respektive filtyper.

### **Ladda ner och installera Aspose.Cells**

1. [Ladda ner Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
1. Installera det på din utvecklingsdator.

Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.

### **Skapa ett projekt**

Starta **Visual Studio** och skapa en ny konsolapplikation. Detta exempel visar en C++-konsolapplikation.

1. Lägg till referenser
   1. Lägg till en referens till Aspose.Cells-komponenten i ditt projekt, till exempel, lägg till en referens till ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extrahera OLE-objekt**

Koden nedan utför det faktiska arbetet med att hitta och extrahera OLE-objekt. OLE-objekten (DOC, XLS och PDF-filer) sparas på disken.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
