---
title: Visa och dölj rullningslister
type: docs
weight: 140
url: /sv/net/display-and-hide-scroll-bars/
---
{{% alert color="primary" %}}

Rullningslister är användbara för att navigera i innehållet i kalkylblad som är breda och djupa, det vill säga som har många rader och kolumner. De flesta applikationer stöder två typer av rullningslist:

- Vertikal rullningslist
- Horisontell rullningslist

Båda dessa finns i Microsoft Excel.

Aspose.Cell:s GridDesktop API tillhandahåller horisontella och vertikala rullningslister för att rulla igenom innehållet i ett kalkylblad. Med API:erna Aspose.Cells.GridDesktop kan utvecklare kontrollera synligheten för båda dessa rullningslister.

{{% /alert %}}

## **Styra rullningslistens synlighet**

För att kontrollera rullningslistens synlighet i GridDesktop, använd egenskaperna IsVerticalScrollBarVisible och IsHorizontalScrollBarVisible. Exemplen nedan visar hur man döljer och visar rullningslister.

### **Programmeringsexempel: Döljer rullningslister**

Om du vill dölja rullningslister ställer du in egenskaperna som styr synligheten till false.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **Programmeringsexempel: Gör rullningslister synliga**

Om du vill göra rullningslister synliga ställer du in egenskaperna som styr synlighet till sant.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
