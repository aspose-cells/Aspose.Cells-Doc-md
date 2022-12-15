---
title: Ta bort oanvända stilar i arbetsboken
type: docs
weight: 470
url: /sv/java/remove-unused-styles-inside-the-workbook/
---
{{% alert color="primary" %}} 

 Oanvända stilar i excel-filer tar inte bara plats utan orsakar även prestandaproblem vid konvertering till olika format som PDF, HTML, etc. Aspose.Cells tillhandahåller[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)) för att ta bort alla oanvända stilar i arbetsboken.

{{% /alert %}} 
## **Ta bort oanvända stilar i arbetsboken**
 Följande kod förklarar användningen av[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\) ). Koden laddar[mall excel-fil](5473451.xlsx) som du kan ladda ner från den medföljande länken. Den innehåller en oanvänd stil som heter**AsposeStil**kommer denna stil och alla andra oanvända stilar att tas bort efter exekvering av koden. Se följande skärmdump för mer illustration.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
