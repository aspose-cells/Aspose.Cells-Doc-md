---
title: Copie y pegue filas en GridDesktop dentro del Control y entre el Control y Excel
type: docs
weight: 70
url: /es/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Si desea habilitar copiar y pegar filas en GridDesktop dentro del control o entre el control y Excel, establezca la propiedad GridDesktop.ClipboardCopyPaste en verdadero. Puede establecer esta propiedad en tiempo de diseño o en el código. El valor por defecto de esta propiedad es "falso". Actualmente, solo puede copiar y pegar valores de celda y no copiará ninguna otra configuración de la celda como formato, estilo de borde, etc.

{{% /alert %}} 
## **Configuración de la propiedad GridDesktop.ClipboardCopyPaste en modo de diseño y tiempo de ejecución**
 El siguiente código de ejemplo establece la propiedad GridDesktop.ClipboardCopyPaste en**Tiempo de ejecución**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
