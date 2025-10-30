---
title: Licensiering
type: docs
weight: 50
url: /sv/cpp/licensing/
---

## **Begränsningar för utvärderingsversionen**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Använd licens med fil eller strömobjekt**
Licensen kan laddas från en fil eller strömobjekt. Aspose.Cells for C++ kommer att försöka hitta licensen på följande platser:

1. Explicit sökväg.
1. Mappen som innehåller Aspose.Cells.dll.
1. Mappen som innehåller sammansättningen som kallade Aspose.Cells.dll.
1. Mappen som innehåller startassemblyn (din .exe).
1. En inbäddad resurs i sammansättningen som kallade Aspose.Cells.dll.

Det enklaste sättet att ange en licens är att lägga licensfilen i samma mapp som Aspose.Cells.dll-filen och ange filnamnet, utan sökväg, enligt exemplet nedan.
### **Ladda en licens från fil**
Det enklaste sättet att tillämpa en licens är att placera licensfilen i samma mapp som Aspose.Cells.dll-filen och ange bara filnamnet utan sökväg.

{{% alert color="primary" %}} 

När du anropar SetLicense-metoden ska licensnamnet som du skickar vara namnet på licensfilen. Till exempel, om du ändrar licensfilnamnet till "Aspose.Cells.lic.xml", skicka det filnamnet till Cells->SetLicense(…) metoden.

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Ladda en licens från en strömföremål**
Följande exempel visar hur du laddar en licens från en ström.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
