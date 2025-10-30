---
title: Avancerade skyddsinställningar sedan Excel XP
type: docs
weight: 30
url: /sv/python-net/advanced-protection-settings-since-excel-xp/
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

Aspose.Cells för Python via .NET stöder alla avancerade skyddsinställningar som erbjuds av Excel XP eller senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

För att visa de tillgängliga skyddsinställningarna i Excel XP:

1. Från **Verktyg**-menyn, välj **Skydda** följt av **Skydda kalkylblad**. En dialogruta kommer att visas.

För att se de tillgängliga skyddsinställningarna i Excel 2016

1. Från **Arkiv**-menyn, välj **Skydda arbetsbok** följt av **Skydda aktuellt kalkylblad**.
1. Välj **Skydda kalkylblad** i **Granska**-menyn.

Att följa stegen ovan kommer att visa en dialogruta där du kan tillåta eller begränsa kalkylbladsfunktioner eller tillämpa ett lösenord på kalkylbladet.

### **Avancerade skyddsinställningar med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET stödjer alla avancerade skyddsinställningar.

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) samling som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen.

Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller egenskapen [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) som används för att tillämpa dessa avancerade skyddsinställningar. Egenskapen [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) är faktiskt ett objekt av klassen [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) som kapslar in flera booleska egenskaper för att inaktivera eller aktivera begränsningar.

Nedan finns en liten exempelapplikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

Ring inte klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) metoden [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) när du använder egenskapen [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection). Spara också filen i formatet Excel97To2003 eller Xlsx eftersom de avancerade skyddsinställningarna endast stöds av Excel XP och senare versioner.

{{% /alert %}}

### **Cellåsningsproblem**

Om du vill begränsa användare från att redigera celler måste cellerna vara låsta innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om kalkylbladet är skyddat. I Microsoft Excel XP kan celler låsas med följande dialogruta:

|**Dialogruta för att låsa celler i Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Det är möjligt att låsa celler med Aspose.Cells för Python via .NET API också. Varje cell kan få [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) formatering som innehåller en Boolean egenskap, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Sätt [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) egenskapen till **true** eller **false** för att låsa eller låsa upp cellen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
