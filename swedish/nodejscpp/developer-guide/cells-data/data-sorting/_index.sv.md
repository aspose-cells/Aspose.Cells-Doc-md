---
title: Data Sortering
type: docs
weight: 130
url: /sv/nodejs-cpp/sort-data-of-excel/
description: Lär dig hur man sorterar data med hjälp av API n Aspose.Cells for Node.js via C++.
keywords: Sortera data i stigande eller fallande ordning, Sortera data baserat på bakgrundsfärg
---

{{% alert color="primary" %}}

Dataskanning är en av Microsoft Excels användbara funktioner. Den tillåter användare att sortera data för att underlätta översyn. Aspose.Cells for Node.js via C++ låter utvecklare sortera kalkylblad data alfabetiskt eller numeriskt, vilket fungerar på samma sätt som Microsoft Excel för att sortera data.

{{% /alert %}}

## **Sortering av data i Microsoft Excel**

För att sortera data i Microsoft Excel:

1. Välj **Data** från **Sortera**-menyn. Sorteringsdialogen visas.
1. Välj ett sorteringsalternativ.

I allmänhet utförs sortering på en lista - definierad som en sammanhängande grupp data där data visas i kolumner.

## **Sortera data med Aspose.Cells**

Aspose.Cells for Node.js via C++ tillhandahåller klassen [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) som används för att sortera data i stigande eller fallande ordning. Klassen har några viktiga medlemmar, till exempel egenskaper som Key1 ... Key3 och Order1 ... Order3. Dessa medlemmar används för att definiera sorterade nycklar och ange ordningen för nyckelsorteringen.

Du måste definiera nycklar och ange sorteringsordningen innan du implementerar datasortering. Klassen tillhandahåller metoden [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) som används för att utföra datasortering baserat på celldata i ett arbetsblad.

Metoden [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) accepterar följande parametrar:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), cellerna för det underliggande arbetsbladet.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), cellområdet. Definiera cellområdet innan du tillämpar datasortering.

Detta exempel använder mallfilen "Bok1.xls" skapad i Microsoft Excel. Efter att koden har utförts sorteras data på lämpligt sätt.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

Om du vill sortera *FrånVänsterTillHöger*, använd attributet [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-).

{{% /alert %}}

### **Sortera data med bakgrundsfärg**

Excel tillhandahåller funktioner för att sortera data baserat på bakgrundsfärg. Samma funktion tillhandahålls med Aspose.Cells for Node.js via C++ via DataSorter där [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor kan användas i [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) för att sortera data baserat på bakgrundsfärgen. Alla celler som innehåller den angivna färgen i [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-), funktionen placeras ovanför eller längst ner enligt SortOrder-inställningen och ordningen för resten av cellerna ändras inte alls.

Följande är provfiler som kan laddas ned för att testa denna funktion:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Fortsatta ämnen**
- [Sortera Data i Kolumn med Anpassad Sorteringslista](/cells/sv/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Angivande av sorteringsvarning vid sortering av data](/cells/sv/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="nodejs-cpp" >}}
