---
title: Justering av radhöjd och kolumnbredd
type: docs
weight: 10
url: /sv/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på rader eller bredden på kolumner. Ibland innebär att tillämpa formatering på rader eller kolumner att den aktuella höjden eller bredden behöver ändras för att visa datan. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med hjälp av Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer vid runtime.

{{% /alert %}}

## **Arbeta med rader**

### **Justera radhöjd**

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) som ger tillgång till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Klassen [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ger en [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samling som representerar alla celler i kalkylbladet. [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen ger flera metoder för att hantera rader och kolumner i ett kalkylblad. Några av dessa behandlas mer i detalj nedan.

#### **Inställning av radhöjd**

Det är möjligt att sätta höjden för en enskild rad genom att anropa [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingens [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) metod. [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) tar följande parametrar:

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **Inställning av höjden på alla rader i ett arbetsblad**

Om utvecklare behöver sätta samma radhöjd för alla rader i kalkylbladet kan de göra detta med hjälp av [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) metoden i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **Arbeta med kolumner**

### **Inställning av bredden på en kolumn**

Sätt bredden på en kolumn genom att anropa [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingens [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) metod. [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **Inställning av bredden på alla kolumner i ett arbetsblad**

För att ställa in samma kolumnbredd för alla kolumner i kalkylbladet, använd metoden [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) i [Cells](https://reference.aspose.com/cells/go-cpp/cells/) samlingen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
