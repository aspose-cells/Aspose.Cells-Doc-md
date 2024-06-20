---
title: Avancerade skyddsinställningar sedan Excel XP
type: docs
weight: 30
url: /sv/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Sedan utgåvan av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar.

{{% /alert %}}

## **Introduktion**

Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket annat.

Aspose.Cells stöder alla avancerade skyddsinställningar som erbjuds av Excel XP eller senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

För att visa de tillgängliga skyddsinställningarna i Excel XP:

1. Från **Verktyg**-menyn, välj **Skydda** följt av **Skydda kalkylblad**. En dialogruta kommer att visas.

För att se de tillgängliga skyddsinställningarna i Excel 2016

1. Från **Arkiv**-menyn, välj **Skydda arbetsbok** följt av **Skydda aktuellt kalkylblad**.
1. Välj **Skydda kalkylblad** i **Granska**-menyn.

Att följa stegen ovan kommer att visa en dialogruta där du kan tillåta eller begränsa kalkylbladsfunktioner eller tillämpa ett lösenord på kalkylbladet.

### **Avancerade skyddsinställningar med hjälp av Aspose.Cells**

Aspose.Cells stödjer alla avancerade skyddsinställningar.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller egenskapen [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) som används för att tillämpa dessa avancerade skyddsinställningar. Egenskapen [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) är faktiskt ett objekt av klassen [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) som kapslar in flera booleska egenskaper för att inaktivera eller aktivera begränsningar.

Nedan finns en liten exempelapplikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Ring inte klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) metoden [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) när du använder egenskapen [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection). Spara också filen i formatet Excel97To2003 eller Xlsx eftersom de avancerade skyddsinställningarna endast stöds av Excel XP och senare versioner.

{{% /alert %}}

### **Cellåsningsproblem**

Om du vill begränsa användare från att redigera celler måste cellerna vara låsta innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om kalkylbladet är skyddat. I Microsoft Excel XP kan celler låsas med följande dialogruta:

|**Dialogruta för att låsa celler i Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Det är möjligt att låsa celler med hjälp av Aspose.Cells API också. Varje cell kan få formatering som innehåller en boolesk egenskap, [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Ange egenskapen [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) till **true** eller **false** för att låsa eller låsa upp cellen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
