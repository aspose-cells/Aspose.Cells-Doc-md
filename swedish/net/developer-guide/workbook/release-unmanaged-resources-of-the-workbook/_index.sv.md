---
title: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 310
url: /sv/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) metoden för att frigöra ohanterade resurser från [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objektet. Dispose-mönstret används endast för objekt som har åtkomst till ohanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att sop samlaren är mycket effektiv på att ta tillbaka oanvända hanterade objekt, men den kan inte ta tillbaka ohanterade objekt.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objekt implementerar nu *System.IDisposable* gränssnitt som har en enda metod [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose). Du kan antingen direkt anropa [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) metoden eller så kan du använda *Using*-satsen för att automatiskt anropa denna metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
