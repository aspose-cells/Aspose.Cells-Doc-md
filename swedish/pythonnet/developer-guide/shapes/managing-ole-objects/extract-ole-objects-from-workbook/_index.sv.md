---
title: Extrahera OLE objekt från arbetsboken
type: docs
weight: 110
url: /sv/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Ibland behöver du extrahera OLE-objekt från en arbetsbok. Aspose.Cells för Python via .NET stöder att extrahera och spara dessa Ole-objekt.

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

### **Extrahera OLE-objekt med Aspose.Cells för Python Excel-biblioteket**

Nedan gör koden det faktiska arbetet med att hitta och extrahera OLE-objekt. OLE-objekten (DOC, XLS och PDF-filer) sparas på disk.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
