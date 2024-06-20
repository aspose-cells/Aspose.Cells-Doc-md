---
title: Ta bort överflödiga mellanslag efter radbrytning vid import av HTML
type: docs
weight: 20
url: /sv/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Använd egenskapen [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) och ange den som **true** för att ta bort alla överflödiga mellanslag som kommer efter radbrytningstaggen. Som standard är den här egenskapen **false** och överflödiga mellanslag bevaras i de resulterande Excel-filerna.

{{% /alert %}}

## Effekten av att ställa in HTMLLoadOptions.DeleteRedundantSpaces egenskapen till false och true

Följande skärmbild visar effekten av att ställa denna egenskap till **false** och **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Ta bort överflödiga mellanslag efter radbrytning vid import av HTML

### Programexempel

Följande kodexempel visar användningen av egenskapen [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces). Vänligen ange den som **true** eller **false** för att få utdata som visas i ovanstående skärmdump.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
