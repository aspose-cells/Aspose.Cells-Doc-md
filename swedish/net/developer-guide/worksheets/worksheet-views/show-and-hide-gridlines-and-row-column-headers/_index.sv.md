---
title: Visa och dölj rutnätslinjer och radkolumnrubriker
type: docs
weight: 30
url: /sv/net/show-and-hide-gridlines-and-row-column-headers/
description: Den här artikeln innehåller exempelkod för att använda biblioteket C# API eller .NET för att programmatiskt dölja eller visa rutnätslinjer, rad- och kolumnrubriker i ett Excel-kalkylblad.
---
{{% alert color="primary" %}}

Aspose.Cells stöder att dölja och visa rutnätslinjer för kalkylbladet som är synliga som standard. Det ger också kontroll över kalkylbladets radkolumnrubriker.

{{% /alert %}}

## **Visa och dölj rutnätslinjer**

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att mata in data i särskilda celler. Gridlines gör det möjligt för oss att se ett kalkylblad som en samling celler, där varje cell är lätt att identifiera.

### **Styra rutnätets synlighet**

Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som låter utvecklare komma åt varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att kontrollera synligheten för rutnät, använd[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) fast egendom.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller**falsk** värde.

#### **Gör rutnät synliga**

 Gör rutnätslinjerna synliga genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) egendom till**Sann**.

#### **Dölja rutnät**

 Dölj rutnät genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) egendom till**falsk**.

 Ett komplett exempel ges nedan som visar användningen av[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)egenskap genom att öppna en excel-fil(book1.xls), dölja rutnätslinjerna på det första kalkylbladet och spara den ändrade filen som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Visa och dölj radkolumnrubriker**

Alla kalkylblad i en Excel-fil är sammansatta av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och för att identifiera enskilda celler. Till exempel är rader numrerade – 1, 2, 3, 4, etc. – och kolumner ordnas i alfabetisk ordning – A, B, C, D, etc. Rad- och kolumnvärdena visas i rubrikerna. Med hjälp av Aspose.Cells kan utvecklare kontrollera synligheten för dessa rad- och kolumnrubriker.

### **Styra arbetsbladens synlighet**

Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som låter utvecklare komma åt varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att kontrollera synligheten för rad- och kolumnrubriker använder du[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) fast egendom.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller**falsk**värde.

#### **Gör rad-/kolumnrubriker synliga**

 Gör rad- och kolumnrubriker synliga genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) egendom till**Sann**.

#### **Döljer rad-/kolumnrubriker**

 Dölj rad- och kolumnrubriker genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) egendom till**falsk**.

Ett komplett exempel ges nedan som visar hur man använder[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)egenskapen genom att öppna en excel-fil (book1.xls), dölja rad- och kolumnrubriken på det första kalkylbladet och spara den ändrade filen som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 Det är också möjligt att använda[**Visa rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) och[**Visa kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) klass för att göra flera rader och kolumner synliga.

{{% /alert %}}
