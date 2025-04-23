---
title: Ta bort oanvända stilar inne i arbetsboken
type: docs
weight: 470
url: /sv/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Oanvända stilar i Excel-filen tar inte bara plats utan orsakar också prestandaproblem vid konvertering till olika format som PDF, HTML etc. Aspose.Cells tillhandahåller [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) för att ta bort alla oanvända stilar inuti arbetsboken.

{{% /alert %}} 
## **Ta bort oanvända stilar i arbetsboken**
Följande kod förklarar användningen av [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--). Koden laddar det [mall Excel-fil](5473451.xlsx) som du kan ladda ner via länken. Den innehåller en oanvänd stil som heter **AsposeStyle**, denna stil och alla andra oanvända stilar tas bort efter kodens körning. Se skärmbilden nedan för mer illustration.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
