---
title: Frigör icke hanterade resurser av arbetsboken med Golang via C++
linktitle: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 310
url: /sv/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Lär dig hur man frigör oanvända resurser i arbetsboken med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) metoden för att frigöra ohanterade resurser från [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objektet. Dispose-mönstret används endast för objekt som har åtkomst till ohanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att sop samlaren är mycket effektiv på att ta tillbaka oanvända hanterade objekt, men den kan inte ta tillbaka ohanterade objekt.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)-objektet implementerar nu *IDisposable*-gränssnittet som har en enda metod [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/). Du kan antingen direkt anropa [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/)-metoden eller använda *Using*-satset för att automatiskt anropa denna metod.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
