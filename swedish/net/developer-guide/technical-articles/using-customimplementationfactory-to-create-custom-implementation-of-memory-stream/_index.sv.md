---
title: Användning av CustomImplementationFactory för att skapa anpassad implementering av minneström
type: docs
weight: 40
url: /sv/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Möjliga användningsscenario**

Aspose.Cells har tillhandahållit ett API som heter [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) som gör det möjligt för användaren att tillhandahålla anpassad implementation såsom att använda återvinningsbar minnesimplementation istället för standard MemoryStream.

## **Användning av CustomImplementationFactory för att skapa anpassad implementation av Memory Stream**

Följande exempelkod illustrerar hur man använder [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) i ditt program. Ibland finns det tillräckligt med minne i ditt system, men minnet är inte sammanhängande. Minaströmsobjekt använder sammanhängande minne, men du kan tillhandahålla implementationen av Minaström på ett sådant sätt att den istället använder ickesammanhängande minne.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
