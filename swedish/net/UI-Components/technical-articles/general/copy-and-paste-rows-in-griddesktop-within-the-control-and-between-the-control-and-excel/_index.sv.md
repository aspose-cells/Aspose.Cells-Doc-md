---
title: Kopiera och klistra in rader i GridDesktop inom kontrollen och mellan kontrollen och Excel
type: docs
weight: 70
url: /sv/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Om du vill aktivera kopiera och klistra in rader i GridDesktop inom kontrollen eller mellan kontroll och excel, ställ in egenskapen GridDesktop.ClipboardCopyPaste till true. Du kan ställa in den här egenskapen i designtid eller i kod. Standardvärdet för den här egenskapen är falskt. För närvarande kan den bara kopiera och klistra in cellvärden och den kommer inte att kopiera någon annan inställning av cellen som format, kantstil och så vidare.

{{% /alert %}} 
## **Ställa in egenskapen GridDesktop.ClipboardCopyPaste i designläge och körtid**
 Följande exempelkod anger egenskapen GridDesktop.ClipboardCopyPaste i**Körtid**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
