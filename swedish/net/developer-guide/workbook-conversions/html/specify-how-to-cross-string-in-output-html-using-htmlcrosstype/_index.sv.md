---
title: Ange hur strängen ska korsas i utdata HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Möjliga användningsscenarier**

När cellen innehåller text eller sträng men den är större än cellens bredd, svämmar strängen över om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i HTML kan du kontrollera detta överflöde genom att ange korstypen med hjälp av[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) uppräkning. Den har följande värden

- **HtmlCrossType.Default**: Visa som MS Excel, beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller trunkeras.

- **HtmlCrossType.MSExport**: Visa strängen som MS Excel som exporterar HTML.

- **HtmlCrossType.Cross**: Visa HTML korssträng, prestandan för att skapa stora HTML-filer kommer att vara mer än tio gånger snabbare än att ställa in värdet på Default eller FitToCell.

- **HtmlCrossType.FitToCell**: Visar endast strängen inom cellens bredd.

## **Ange hur strängen ska korsas i utdata HTML med HtmlCrossType**

 Följande exempelkod laddar[exempel på Excel-fil](51740732.xlsx) och sparar den till HTML-format genom att ange olika[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) . Vänligen ladda ner[mata ut HTMLs](51740734.zip) genereras med denna kod. Exemplet i Excel-filen innehåller bilden kantad med röd färg som visas i den här skärmdumpen som visar effekten av[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) värden på utgång HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
