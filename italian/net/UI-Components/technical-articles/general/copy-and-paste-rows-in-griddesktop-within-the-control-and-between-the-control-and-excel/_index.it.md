---
title: Copia e incolla righe in GridDesktop all'interno del controllo e tra il controllo ed Excel
type: docs
weight: 70
url: /it/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Se desideri abilitare le righe di copia e incolla in GridDesktop all'interno del controllo o tra controllo ed Excel, imposta la proprietà GridDesktop.ClipboardCopyPaste su true. È possibile impostare questa proprietà in fase di progettazione o nel codice. Il valore predefinito di questa proprietà è false. Attualmente, può solo copiare e incollare i valori delle celle e non copierà nessun'altra impostazione della cella come formato, stile del bordo e così via.

{{% /alert %}} 
## **Impostazione della proprietà GridDesktop.ClipboardCopyPaste in modalità progettazione e in fase di esecuzione**
 Il codice di esempio seguente imposta la proprietà GridDesktop.ClipboardCopyPaste in**Tempo di esecuzione**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
