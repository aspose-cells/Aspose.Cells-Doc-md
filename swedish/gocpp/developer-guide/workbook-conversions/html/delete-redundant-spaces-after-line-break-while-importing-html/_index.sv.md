---
title: Ta bort överflödiga mellanrum efter radbrytning när du importerar HTML med Golang via C++
linktitle: Ta bort överflödiga mellanslag efter radbrytning vid import av HTML
type: docs
weight: 20
url: /sv/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Lär dig hur man tar bort överflödiga mellanslag efter radbrytningar vid import av HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Använd [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/)-egenskapen och ställ in den på **true** för att ta bort alla överflödiga mellanslag som kommer efter radbrytnings-taggen. Som standard är den här egenskapen **false** och överskottslinjer bevaras i de utmatade Excel-filerna.

{{% /alert %}}

## Effekten av att ställa in HTMLLoadOptions.DeleteRedundantSpaces egenskapen till false och true

Följande skärmbild visar effekten av att ställa denna egenskap till **false** och **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Ta bort överflödiga mellanslag efter radbrytning vid import av HTML

### Programexempel

Följande kodexempel visar användningen av egenskapen [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/). Vänligen ange den som **true** eller **false** för att få utdata som visas i ovanstående skärmdump.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
