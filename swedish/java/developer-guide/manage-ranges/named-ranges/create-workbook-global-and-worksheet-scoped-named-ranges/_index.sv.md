---
title: Skapa arbetsbok (global) och kalkylblad med omfattning av namngivna intervall
type: docs
weight: 10
url: /sv/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel tillåter användare att definiera namngivna intervall med två olika omfång: arbetsbok (även känd som globalt omfång) och kalkylblad.

- Namngivna intervall med ett arbetsboksomfång kan nås från vilket kalkylblad som helst i den arbetsboken genom att helt enkelt använda dess namn.
- Namngivna intervall med kalkylbladsomfattningar nås med referensen till det särskilda kalkylblad där det skapades.

Aspose.Cells tillhandahåller samma funktionalitet som Microsoft Excel för att lägga till arbetsbok och kalkylblad med omfattning av namngivna intervall. När du skapar ett kalkylblad med scoped named range, bör kalkylbladsreferensen användas i det namngivna intervallet för att specificera det som ett kalkylblad scoped namngivet intervall.

{{% /alert %}}

 Följande kodexempel visar hur du skapar arbetsbok- och kalkylbladsomfångade namnintervall med hjälp av[**Räckvidd**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) klass.

## **Lägga till ett namngivet område med arbetsbokens omfattning**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Lägga till ett namngivet område med arbetsbladsomfång**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
