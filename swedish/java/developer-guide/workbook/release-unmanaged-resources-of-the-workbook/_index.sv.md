---
title: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 290
url: /sv/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) metod för att frigöra de icke-hanterade resurserna för [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) objektet. Disposeringsmönstret används endast för objekt som får tillgång till icke-hanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntande handtag eller pekare till block av icke-hanterat minne. Detta eftersom garbage collector är mycket effektiv på att återvinna oanvända hanterade objekt, men inte kan återvinna icke-hanterade objekt.

{{% /alert %}} 
## **Frigör ohanterade resurser för arbetsboken**
Följande exempel visar hur man använder [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
