---
title: Extrahera OLE objekt från arbetsboken
type: docs
weight: 110
url: /sv/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Ibland behöver du faktiskt extrahera OLE-objekt från en arbetsbok. Aspose.Cells stöder att extrahera och spara dessa Ole-objekt.

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio.Net och extraherar olika OLE-objekt från en arbetsbok med några enkla rader med kod.

{{% /alert %}}

## **Extrahera OLE-objekt från en arbetsbok**

### **Skapa en mallarbok**

1. Skapade en arbetsbok i Microsoft Excel.
1. Lägg till ett Microsoft Word-dokument, en Excel-arbetsbok och ett PDF-dokument som OLE-objekt på första arbetsbladet.

|**Mall-dokument med OLE-objekt (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Nästa extrahera OLE-objekten och spara dem på hårddisken med sina respektive filtyper.

### **Ladda ner och installera Aspose.Cells**

1. [Ladda ned Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installera det på din utvecklingsdator.

Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.

### **Skapa ett projekt**

Starta **Visual Studio.Net** och skapa en ny konsolapplikation. Detta exempel kommer att visa en C# konsolapplikation, men du kan också använda VB.NET.

1. Lägg till referenser
   1. Lägg till en hänvisning till Aspose.Cells-komponenten till ditt projekt, till exempel lägg till en hänvisning till ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Extrahera OLE-objekt**

Nedan gör koden det faktiska arbetet med att hitta och extrahera OLE-objekt. OLE-objekten (DOC, XLS och PDF-filer) sparas på disk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
