---
title: Använder CustomImplementationFactory för att skapa anpassad implementering av Memory Stream
type: docs
weight: 40
url: /sv/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **Möjliga användningsscenarier**

 Aspose.Cells har angett en API namngiven[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)vilket gör det möjligt för användaren att tillhandahålla anpassad implementering som att använda återvinningsbart minnesimplementering istället för standard MemoryStream.

## **Använder CustomImplementationFactory för att skapa anpassad implementering av Memory Stream**

Följande exempelkod illustrerar hur du använder[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)i ditt program. Ibland finns det tillräckligt med minne i ditt system men minnet är inte sammanhängande. Memory Stream-objekt använder sammanhängande minne men du kan tillhandahålla implementeringen av Memory Stream på ett sådant sätt att det använder det icke-sammanhängande minnet istället,

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
