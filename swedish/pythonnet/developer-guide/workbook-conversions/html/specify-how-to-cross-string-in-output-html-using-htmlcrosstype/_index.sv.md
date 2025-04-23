---
title: Ange hur texten ska korsas i utdata HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Möjliga användningsscenario**

När cellen innehåller text eller sträng men är större än cellens bredd, så överlappar strängen om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i HTML kan du styra detta överlapp genom att ange korsningstypen med användning av [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Den har följande värden

- **HtmlCrossType.DEFAULT**: Visar som MS Excel, beror på nästa cell. Om nästa cell är null, kommer texten att korsas eller kapas.

- **HtmlCrossType.MS_EXPORT**: Visar strängen som MS Excel exporterar till HTML.

- **HtmlCrossType.CROSS**: Visar HTML-korsad sträng, prestandan för att skapa stora HTML-filer är mer än tio gånger snabbare än att ställa in värdet till Default eller FitToCell.

- **HtmlCrossType.CROSS_HIDE_RIGHT**: Visar HTML-korsad sträng och döljer den högra strängen när texterna överlappar.

- **HtmlCrossType.FIT_TO_CELL**: Visar endast strängen inom cellens bredd.

## **Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType**

Följande provkod laddar [prov Excel-filen](51740732.xlsx) och sparar den i HTML-format genom att ange olika [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Vänligen ladda ner de [utmatnings-HTML-filer](51740734.zip) som genereras med denna kod. Provexcelfilen innehåller bilden omgiven av röd färg som visas i den här skärmbilden som visar effekten av de [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)-värden på utmatnings-HTML-filen.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
