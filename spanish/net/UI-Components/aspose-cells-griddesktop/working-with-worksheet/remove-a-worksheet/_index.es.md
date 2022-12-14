---
title: Quitar una hoja de trabajo
type: docs
weight: 30
url: /es/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

Este tema trata sobre la eliminación de hojas de trabajo mediante el control Aspose.Cells.GridDesktop. Hay algunos enfoques simples para lograr esta tarea básica.

{{% /alert %}} 
## **Quitar una hoja de trabajo**
Para eliminar una hoja de trabajo usando el control Aspose.Cells.GridDesktop, siga los pasos a continuación:

1. Agregue el control Aspose.Cells.GridDesktop a un formulario.
1. Llame al método Remove de la colección Worksheets en el control GridDesktop.
### **Uso del índice de la hoja de trabajo**
En este enfoque, simplemente pase el índice de la hoja de trabajo (en la colección de hojas de trabajo de la cuadrícula) de la hoja de trabajo que se eliminará.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Uso del nombre de la hoja de trabajo**
Si se conoce el nombre de la hoja de trabajo, es posible eliminar una hoja de trabajo específica especificando su nombre.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Quitar es un método. Úselo para eliminar una hoja de trabajo usando su índice (en la colección de hojas de trabajo) o use el método RemoveAt para eliminar la hoja de trabajo usando su índice/nombre.

{{% /alert %}}
