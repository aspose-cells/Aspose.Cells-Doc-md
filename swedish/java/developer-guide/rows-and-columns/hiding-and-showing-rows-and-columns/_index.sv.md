---
title: Dölja och visa rader och kolumner
type: docs
weight: 50
url: /sv/java/hiding-and-showing-rows-and-columns/
---
## **Introduktion**
Ibland kan det också krävas av användare att dölja vissa rader eller kolumner i kalkylbladet och sedan visa dem senare. Microsoft Excel tillhandahåller den här funktionen och så som Aspose.Cells.
## **Kontrollera synligheten för rader och kolumner**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling som representerar alla celler i kalkylbladet. De[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.
### **Döljer rader eller kolumner**
 Utvecklare kan dölja en rad eller kolumn genom att anropa[HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) och[Dölj kolumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) metoder för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)insamling respektive. Båda metoderna tar rad/kolumnindex som en parameter för att dölja den specifika raden eller kolumnen.

{{% alert color="primary" %}} 

Notera: Det är också möjligt att dölja en rad eller kolumn om vi ställer in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Visar rader och kolumner**
 Utvecklare kan visa alla dolda rader eller kolumner genom att anropa[Visa rad](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) och[Ta fram kolumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) metoder för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)insamling respektive. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - indexet för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden som tilldelats raden eller kolumnen efter att den har visats.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

När du gör en dold kolumn/rad synlig, om du behöver återställa den till tidigare tilldelad bredd eller höjd, eller dess ursprungliga bredd eller höjd, vänligen visa kolumnen eller raden med negativ bredd eller höjd. Till exempel workheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
