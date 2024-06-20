---
title: Ta bort oanvända stilar inne i arbetsboken
type: docs
weight: 470
url: /sv/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Oanvända stilar i excelfilen tar inte bara plats utan orsakar även prestandaproblem vid konvertering till olika format som PDF, HTML, etc. Aspose.Cells tillhandahåller [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)) för att ta bort alla oanvända stilar i arbetsboken.

{{% /alert %}} 
## **Ta bort oanvända stilar i arbetsboken**
Följande kod förklarar användningen av [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)). Koden laddar [mallen för excelfil](5473451.xlsx) som du kan ladda ner från den angivna länken. Den innehåller en oanvänd stil med namnet **AsposeStyle**, denna stil och alla andra oanvända stilar kommer att tas bort efter att koden har exekverats. Var god se den följande skärmbilden för mer illustration.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
