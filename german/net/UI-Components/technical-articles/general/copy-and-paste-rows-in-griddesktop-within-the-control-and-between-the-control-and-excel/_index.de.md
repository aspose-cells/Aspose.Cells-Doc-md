---
title: Kopieren und Einfügen von Zeilen in GridDesktop innerhalb des Steuerelements und zwischen dem Steuerelement und Excel
type: docs
weight: 70
url: /de/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Wenn Sie das Kopieren und Einfügen von Zeilen in GridDesktop innerhalb des Steuerelements oder zwischen Steuerelement und Excel aktivieren möchten, setzen Sie die Eigenschaft GridDesktop.ClipboardCopyPaste auf „true“. Sie können diese Eigenschaft in der Entwurfszeit oder im Code festlegen. Der Standardwert dieser Eigenschaft ist false. Derzeit können nur Zellwerte kopiert und eingefügt werden, und es werden keine anderen Einstellungen der Zelle wie Format, Rahmenstil usw. kopiert.

{{% /alert %}} 
## **Festlegen der GridDesktop.ClipboardCopyPaste-Eigenschaft im Entwurfsmodus und zur Laufzeit**
 Der folgende Beispielcode legt die GridDesktop.ClipboardCopyPaste-Eigenschaft fest**Laufzeit**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
