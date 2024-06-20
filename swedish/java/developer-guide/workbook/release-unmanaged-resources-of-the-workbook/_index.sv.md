---
title: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 290
url: /sv/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) metoden för att frigöra de ohanterade resurserna för [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) objektet. Dispose-mönstret används endast för objekt som har tillgång till ohanterade resurser, såsom fil- och rörhandtag, registerhandtag, vänta handtag eller pekare till block med ohanterat minne. Detta beror på att sophanteraren är mycket effektiv på att återta oanvända hanterade objekt, men den kan inte återta ohanterade objekt.

{{% /alert %}} 
## **Frigör ohanterade resurser för arbetsboken**
Den följande provkoden visar hur man använder [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) metoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
