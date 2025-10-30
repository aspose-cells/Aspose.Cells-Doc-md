---
title: Teckensnittsinställningar med Golang via C++
linktitle: Fontinställningar
type: docs
weight: 30
url: /sv/go-cpp/cells-font-settings/
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stöder inställning av teckensnitt för celler, vilket gör det möjligt för användare att anpassa stil och egenskaper för teckensnitt. Denna artikel visar hur man använder Aspose.Cells biblioteket för att ställa in teckensnitt i celler.
keywords: Aspose.Cells, Cells, Fontinställningar, Stilar, Egenskaper
---

{{% alert color="primary" %}}

Utseendet och känslan av en text kan styras genom att ändra teckensnittsinställningar. Teckensnittsinställningarna kan inkludera namn, stil, storlek, färg och andra effekter för teckensnitt. Precis som Microsoft Excel stöder Aspose.Cells konfiguration av teckensnitt i cellerna.

{{% /alert %}}

## **Konfigurera fontinställningar**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som möjliggör åtkomst till varje kalkylblad i en Excelfil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samling. Varje objekt i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells tillhandahåller klassens [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) metoder [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) och [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/) som används för att hämta och ställa in cellens formateringsstil. Klassen [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) tillhandahåller egenskaper för att konfigurera fontinställningar.

### **Ange fontnamn**

Utvecklare kan tillämpa vilken font som helst på text inuti en cell genom att använda [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) objektets [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) egenskap.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Ange fontstil till Fetstil**

Utvecklare kan göra texten fet genom att ställa in objektets [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) egenskap [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) till **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Inställning av fontstorlek**

Ställ in fontstorlek med objektets [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) egenskap [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Sätt Typsnittsfärg**

 Använd [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) objektets [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) egenskap för att ställa in teckensnittfärgen. Välj vilken färg som helst från Color-enum (del av C++-ramverket) och tilldela den till [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) egenskapen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Inställning av font underlinjetyp**

Använd objektets [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) egenskap [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) för att understryka text. Aspose.Cells erbjuder olika fördefinierade teckenstilunderstrykningstyper i [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)-utseendet.

|**Font Underline Types**|**Beskrivning**|
| :- | :- |
|Accounting|Enkel redovisningsunderstrykning|
|Double|Dubbel understrykning|
|DoubleAccounting|Dubbel redovisningsunderstrykning|
|None|Ingen understrykning|
|Single|Enkel understrykning|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Inställning för överstruken effekt**

Tillämpa överstrykning genom att ställa in objektets [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) egenskap [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) till **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Inställning av understreckningseffekt**

Tillämpa understreckning genom att ställa in objektets [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) egenskap [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) till **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Inställning av överstruken effekt på font**

Utvecklare kan applicera överstruken effekt på fonten genom att ställa in [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) egenskapen för objektet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) till **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Fortsatta ämnen**
- [Applicera Superscript- och Subscript-effekter på typsnitt](/cells/sv/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över typsnitt som används i en kalkylblad eller arbetsbok](/cells/sv/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
