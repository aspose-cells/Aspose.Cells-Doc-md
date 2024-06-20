---
title: Ange hur texten ska korsas i utdata HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Möjliga användningsscenario**

När cellen innehåller text eller sträng men är större än cellens bredd, så överlappar strängen om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i HTML kan du styra detta överlapp genom att ange korsningstypen med användning av [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Den har följande värden

- **HtmlCrossType.Default**: Visa som MS Excel, beror på nästa cell. Om nästa cell är null kommer strängen att överlappa eller den kommer att avkortas.

- **HtmlCrossType.MSExport**: Visa strängen som MS Excel exporterar HTML.

- **HtmlCrossType.Cross**: Visa HTML-korssträngen, prestandan för att skapa stora HTML-filer kommer att vara mer än tio gånger snabbare än att ställa in värdet till Default eller FitToCell.

- **HtmlCrossType.FitToCell**: Visa endast strängen inom cellens bredd.

## **Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType**

Följande provkod laddar [prov Excel-filen](51740732.xlsx) och sparar den i HTML-format genom att ange olika [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Vänligen ladda ner de [utmatnings-HTML-filer](51740734.zip) som genereras med denna kod. Provexcelfilen innehåller bilden omgiven av röd färg som visas i den här skärmbilden som visar effekten av de [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)-värden på utmatnings-HTML-filen.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
