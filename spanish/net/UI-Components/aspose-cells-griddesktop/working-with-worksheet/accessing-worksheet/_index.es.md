---
title: Accediendo a la hoja de cálculo
type: docs
weight: 10
url: /es/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop, hoja de cálculo
description: Este artículo presenta cómo trabajar con hojas de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Una hoja de cálculo es una parte integral de un archivo de Excel. De hecho, un archivo de Excel está compuesto por una o más hojas de cálculo. Cada hoja de cálculo puede estar compuesta por un máximo de 65.536 filas y 256 columnas solamente. Es la hoja de cálculo la que almacena los datos en un archivo de Excel.

Aspose.Cells.GridDesktop puede crear y manipular archivos de Excel existentes y nuevos, por lo que, naturalmente, hay una forma de acceder a las hojas de cálculo utilizando Aspose.Cells.GridDesktop. Este tema discute cómo hacerlo.

{{% /alert %}} 
## **Usando el Índice de la Hoja de Cálculo**
Los desarrolladores pueden acceder a una instancia de cualquier hoja de cálculo utilizando el índice de la hoja de cálculo deseada como se muestra a continuación en el ejemplo. Este enfoque es útil para iterar a través de varias hojas de cálculo en un archivo de Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Usando el Nombre de la Hoja de Cálculo**
Si se conoce el nombre de la hoja de cálculo, es posible acceder a una hoja de cálculo utilizando su nombre como se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accediendo a una Hoja de Cálculo Activa**
Es posible que un archivo de Excel tenga más de una hoja de cálculo. La que un usuario está utilizando se llama hoja de cálculo activa. Es posible acceder a la hoja activa.

Para acceder a una hoja de cálculo activa, Aspose.Cells.GridDesktop ofrece dos enfoques:
### **Usando la Propiedad AcriveSheetIndex**
Una forma de acceder a una hoja de cálculo activa utilizando el control GridDesktop de Aspose.Cells.GridDesktop es utilizar la propiedad ActiveSheetIndex del control GridDesktop. Con esta propiedad, es posible obtener el índice de la hoja de cálculo activa en el control Aspose.Cells.GridDesktop. Luego, ese índice se puede utilizar para acceder a la hoja de cálculo de la manera tradicional como se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Usando el Método GetActiveWorksheet**
El otro enfoque es llamar al método GetActiveWorksheet del control GridDesktop. Este método proporciona una referencia de la hoja de cálculo que está actualmente activa en el control Aspose.Cells.GridDesktop como se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
