---
title: Ta bort redundanta blanksteg efter radbrytning när du importerar HTML
type: docs
weight: 20
url: /sv/net/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}}

 Snälla använd[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) egendom och ställ in den**Sann** för att ta bort alla redundanta mellanslag som kommer efter radbrytningstaggen. Som standard är den här egenskapen**falsk** och redundanta utrymmen bevaras i utdata Excel-filer.

{{% /alert %}}

## Effekten av att sätta egenskapen HTMLLoadOptions.DeleteRedundantSpaces till false och true

 Följande skärmdump visar effekten av att ställa in den här egenskapen till**falsk** och**Sann**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Ta bort redundanta blanksteg efter radbrytning när du importerar HTML

### Programmeringsexempel

 Följande exempelkod visar användningen av[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) fast egendom. Vänligen ställ in det**Sann** eller**falsk** för att få utdata som visas i skärmdumpen ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
