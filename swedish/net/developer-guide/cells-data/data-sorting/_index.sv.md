---
title: Datasortering
type: docs
weight: 130
url: /sv/net/sort-data-of-excel/
---
{{% alert color="primary" %}}

Datasortering är en av Microsoft Excels många användbara funktioner. Det låter användare beställa data för att göra det lättare att skanna. Aspose.Cells låter utvecklare sortera kalkylbladsdata alfabetiskt eller numeriskt, vilket fungerar på samma sätt som Microsoft Excel gör för att sortera data.

{{% /alert %}}

## **Sortera data i Microsoft Excel**

Så här sorterar du data i Microsoft Excel:

1.  Välj**Data** från**Sortera** meny. Dialogrutan Sortera kommer att visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp av data där data visas i kolumner.

## **Sortera data med Aspose.Cells**

 Aspose.Cells tillhandahåller[**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)klass som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och specificera nyckelsorteringsordningen.

 Du måste definiera nycklar och ställa in sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller[**Sortera**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)metod som används för att utföra datasortering baserat på celldata i ett kalkylblad.

 De[**Sortera**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)metoden accepterar följande parametrar:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), cellerna för det underliggande kalkylbladet.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), cellintervallet. Definiera cellområdet innan du tillämpar datasortering.

Det här exemplet använder mallfilen "Book1.xls" skapad i Microsoft Excel. Efter att ha kört koden nedan sorteras data på lämpligt sätt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Om du vill sortera*Vänster till höger* , Använd[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) attribut.

{{% /alert %}}

### **Sortera data med bakgrundsfärg**

 Excel tillhandahåller funktioner för att sortera data baserat på bakgrundsfärgen. Samma funktion tillhandahålls med Aspose.Cells med DataSorter där[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor kan användas i[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) för att sortera data baserat på bakgrundsfärgen. Alla celler som innehåller specificerad färg i[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), funktionen placeras på toppen eller botten enligt SortOrder-inställningen och ordningen på resten av cellerna ändras inte alls.

Följande är exempelfilerna som kan laddas ner för att testa den här funktionen:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Förhandsämnen**
- [Sortera data i kolumn med anpassad sorteringslista](/cells/sv/net/sort-data-in-column-with-custom-sort-list/)
- [Ange sorteringsvarning vid sortering av data](/cells/sv/net/specifying-sort-warning-while-sorting-data/)
