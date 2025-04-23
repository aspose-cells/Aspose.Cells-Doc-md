---
title: Implementera subtotal eller grand total märken på andra språk
type: docs
weight: 50
url: /sv/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Möjliga användningsscenario**

Ibland vill du visa subtotal- och grand total-etiketter på icke-engelska språk som kinesiska, japanska, arabiska, hindi etc. Aspose.Cells gör det möjligt att göra detta med hjälp av [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klass och [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) egenskap. Se denna artikel om hur du kan använda [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) klassen

- [Användning av klassen GlobalizationSettings för anpassade subtotalmärken och andra märken för cirkeldiagram](/cells/sv/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementera subtotal eller grand total-märken på andra språk**

Följande exempelkod laddar [exempel på excel-filen](5115151.xlsx) och implementerar subtotal- och grand total-namn på kinesiska.  Se den [utdata av excel-filen](5115152.xlsx) som genererats av koden som referens. Vi skapar först en klass av [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) och använder den sedan i vår kod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Använd nu ovan skapad klass i koden som nedan:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
