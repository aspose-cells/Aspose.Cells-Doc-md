---
title: Licensiering
type: docs
weight: 50
url: /sv/cpp/licensing/
---
## **Begränsningar för utvärderingsversion**
 En gratis utvärderingsversion av Aspose.Cells for C++ kan laddas ner från nedladdningssektionen på Aspose:s webbplats på:<https://downloads.aspose.com/cells/cpp>.
## **Tillämpa licens med File eller Stream Object**
Licensen kan laddas från en fil eller ett strömobjekt. Aspose.Cells for C++ kommer att försöka hitta licensen på följande platser:

1. Explicit väg.
1. Mappen som innehåller Aspose.Cells.dll.
1. Mappen som innehåller sammansättningen som anropade Aspose.Cells.dll.
1. Mappen som innehåller postsammansättningen (din .exe).
1. En inbäddad resurs i sammansättningen som anropade Aspose.Cells.dll.

Det enklaste sättet att ställa in en licens är att lägga licensfilen i samma mapp som filen Aspose.Cells.dll och ange filnamnet, utan sökväg, som visas i exemplet nedan.
### **Laddar en licens från fil**
Det enklaste sättet att tillämpa en licens är att lägga licensfilen i samma mapp som filen Aspose.Cells.dll och ange bara filnamnet utan sökväg.

{{% alert color="primary" %}} 

När du anropar SetLicense-metoden ska licensnamnet som du skickar vara det för licensfilen. Om du till exempel ändrar licensfilnamnet till "Aspose.Cells.lic.xml" skickar du det filnamnet till metoden Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **Ladda en licens från ett strömobjekt**
Följande exempel visar hur man laddar en licens från en stream.

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
