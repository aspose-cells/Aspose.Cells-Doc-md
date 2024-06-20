---
title: Ta bort arbetsblad
type: docs
weight: 30
url: /sv/net/aspose-cells-gridweb/remove-worksheets/
keywords: GridWeb, ta bort, ta bort GridWorksheet, ta bort arbetsblad
description: Den här artikeln introducerar hur man tar bort arbetsblad (GridWorksheet) i GridWeb.
---

{{% alert color="primary" %}} 

Detta ämne ger information om hur man tar bort arbetsblad från Microsoft Excel-filer med hjälp av Aspose.Cells.GridWeb API. Det är möjligt att antingen ta bort ett arbetsblad genom att ange dess kalkylbladsindex eller namn.

{{% /alert %}} 
## **Ta bort ett Arbetsblad**
### **Använda bladindekset**
Koden nedan visar hur man tar bort ett arbetsblad genom att ange dess kalkylbladsindex i GridWorksheetCollection-metodens RemoveAt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **Genom att använda arknamn**
Koden nedan visar hur man tar bort ett arbetsblad genom att ange dess kalkylbladsnamn i GridWorksheetCollection-metodens RemoveAt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

Det är också möjligt att ta bort en arbetsblad med dess referens eller instans. Använd GridWorksheetCollection's Remove-metod. Denna strategi används vanligtvis.

{{% /alert %}}
