---
title: Implementera Subtotal eller Grand Total-etiketter på andra språk
type: docs
weight: 50
url: /sv/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **Möjliga användningsscenarier**

 Ibland vill du visa delsumma och totalsumma etiketter på icke-engelska språk som kinesiska, japanska, arabiska, hindi etc. Aspose.Cells låter dig göra detta med[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass och[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) fast egendom. Se den här artikeln om hur du använder den[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)klass

- [Använda klassen GlobalizationSettings för anpassade delsummaetiketter och andra cirkeletiketter](/cells/sv/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementera Subtotal eller Grand Total-etiketter på andra språk**

 Följande exempelkod laddar[exempel på excel-fil](5115151.xlsx) och implementerar delsumma och totala namn på det kinesiska språket. Vänligen kontrollera[utdata Excel-fil](5115152.xlsx) genereras av den här koden för din referens. Vi skapar först en klass av[**Globaliseringsinställningar**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)och använd den sedan i vår kod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Använd nu ovan skapade klass i koden som nedan:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
