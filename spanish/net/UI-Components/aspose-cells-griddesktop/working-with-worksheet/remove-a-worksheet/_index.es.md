---
title: Eliminar una hoja de cálculo
type: docs
weight: 30
url: /es/net/aspose-cells-griddesktop/remove-a-worksheet/
keywords: GridDesktop, eliminar, hoja de cálculo
description: Este artículo introduce cómo eliminar una hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Este tema discute la eliminación de hojas de cálculo utilizando el control de Aspose.Cells.GridDesktop. Hay algunos enfoques simples para lograr esta tarea básica.

{{% /alert %}} 
## **Eliminación de una hoja de cálculo**
Para eliminar una hoja de cálculo utilizando el control Aspose.Cells.GridDesktop, siga los siguientes pasos:

1. Agregue el control Aspose.Cells.GridDesktop a un formulario.
1. Llame al método Remove de la colección de hojas de cálculo en el control GridDesktop.
### **Usando el Índice de la Hoja de Cálculo**
En este enfoque, simplemente pase el índice de la hoja de cálculo (en la colección de hojas de cálculo de la cuadrícula) de la hoja de cálculo a quitar.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Usando el Nombre de la Hoja de Cálculo**
Si se conoce el nombre de la hoja de cálculo, es posible eliminar una hoja de cálculo específica especificando su nombre.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove es un método. Úsalo para eliminar una hoja de cálculo usando su índice (en la colección de hojas de cálculo) o usa el método RemoveAt para eliminar la hoja de cálculo usando su índice/nombre.

{{% /alert %}}
