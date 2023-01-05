---
title: Släpp ohanterade resurser för arbetsboken
type: docs
weight: 290
url: /sv/java/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}} 

 Aspose.Cells tillhandahåller[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\) ) metod för att frigöra de ohanterade resurserna för[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)objekt. Avyttringsmönstret används endast för objekt som har åtkomst till ohanterade resurser, såsom fil- och rörhandtag, registerhandtag, väntehandtag eller pekare till block av ohanterat minne. Detta beror på att sopsamlaren är mycket effektiv på att återta oanvända hanterade objekt, men den kan inte återta oanvända hanterade objekt.

{{% /alert %}} 
## **Släpp ohanterade resurser för arbetsboken**
Följande exempelkod visar hur du använder[Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose\(\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
