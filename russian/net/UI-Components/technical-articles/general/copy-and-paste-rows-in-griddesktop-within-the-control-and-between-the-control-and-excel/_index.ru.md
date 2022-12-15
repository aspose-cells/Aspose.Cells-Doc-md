---
title: Скопируйте и вставьте строки в GridDesktop внутри элемента управления и между элементом управления и Excel.
type: docs
weight: 70
url: /ru/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Если вы хотите включить копирование и вставку строк в GridDesktop внутри элемента управления или между элементом управления и Excel, задайте для свойства GridDesktop.ClipboardCopyPaste значение true. Это свойство можно установить во время разработки или в коде. Значение по умолчанию этого свойства — false. В настоящее время он может только копировать и вставлять значения ячеек, и он не будет копировать никакие другие настройки ячейки, такие как формат, стиль границы и т. д.

{{% /alert %}} 
## **Установка свойства GridDesktop.ClipboardCopyPaste в режиме разработки и во время выполнения**
 В следующем примере кода свойство GridDesktop.ClipboardCopyPaste задается в**Время работы**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
