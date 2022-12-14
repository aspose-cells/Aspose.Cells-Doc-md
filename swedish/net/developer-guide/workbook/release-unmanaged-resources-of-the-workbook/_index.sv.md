---
title: Släpp ohanterade resurser för arbetsboken
type: docs
weight: 310
url: /sv/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) metod för att frigöra de ohanterade resurserna för[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)objekt. Avyttringsmönstret används endast för objekt som har åtkomst till ohanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att sopsamlaren är mycket effektiv på att återta oanvända hanterade objekt, men den kan inte återta oanvända hanterade objekt.

{{% /alert %}}

[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) objekt implementerar nu*System.ID disponibel* gränssnitt som har en enda metod[**Kasta()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . Du kan antingen ringa direkt[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) metoden eller så kan du använda*Använder sig av*uttalande för att anropa denna metod automatiskt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
