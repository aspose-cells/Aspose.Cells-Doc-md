---
title: Skapa arbetsbok (Global) och arbetsbladsscoped namngivna områden
type: docs
weight: 10
url: /sv/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells tillhandahåller samma funktionalitet som Microsoft Excel för att lägga till arbetsbok och arbetsbladscoped namngivna områden. Vid skapande av ett arbetsbladscoped namngivet område bör arbetsbladsreferensen användas i det namngivna området för att specificera det som ett arbetsbladscoped namngivet område.

{{% /alert %}}

Följande kodexempel visar hur man skapar arbetsbok och arbetsbladscoped namngivna områden med hjälp av [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-klassen.

## **Lägg till ett namngivet område med arbetsbokomfång**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Lägg till ett namngivet område med arbetsbladomfång**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
{{< app/cells/assistant language="java" >}}
