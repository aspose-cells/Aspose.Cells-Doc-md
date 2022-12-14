---
title: Acceso a la hoja de trabajo
type: docs
weight: 10
url: /es/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Una hoja de trabajo es una parte integral de un archivo de Excel. De hecho, un archivo de Excel se compone de una o más hojas de cálculo. Cada hoja de cálculo puede estar compuesta por hasta 65 536 filas y 256 columnas solamente. Es la hoja de trabajo que contiene datos en un archivo de Excel.

Aspose.Cells.GridDesktop puede crear y manipular archivos de Excel existentes y nuevos, por lo que existe, por supuesto, una forma de acceder a las hojas de trabajo usando Aspose.Cells.GridDesktop. Este tema trata sobre cómo.

{{% /alert %}} 
## **Uso del índice de la hoja de trabajo**
Los desarrolladores pueden acceder a una instancia de cualquier hoja de trabajo utilizando el índice de la hoja de trabajo de cualquier hoja de trabajo deseada, como se muestra a continuación en el ejemplo. Este enfoque es bueno para iterar a través de varias hojas de trabajo en un archivo de Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Uso del nombre de la hoja de trabajo**
Si se conoce el nombre de la hoja de trabajo, es posible acceder a una hoja de trabajo usando su nombre como se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Acceso a una hoja de trabajo activa**
Es posible que un archivo de Excel tenga más de una hoja de cálculo. La hoja en la que está trabajando un usuario se llama hoja de trabajo activa. Es posible acceder a la hoja activa.

Para acceder a una hoja de trabajo activa, Aspose.Cells.GridDesktop ofrece dos enfoques:
### **Uso de la propiedad AcriveSheetIndex**
Una forma de acceder a una hoja de trabajo activa usando el control Aspose.Cells.GridDesktop es usar la propiedad ActiveSheetIndex del control GridDesktop. Usando esta propiedad, es posible obtener el índice de la hoja de trabajo activa en el control Aspose.Cells.GridDesktop. Luego, ese índice se puede usar para acceder a la hoja de trabajo de manera tradicional, como se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Uso del método GetActiveWorksheet**
El otro enfoque es llamar al método GetActiveWorksheet del control GridDesktop. Este método proporciona una referencia de la hoja de trabajo que está actualmente activa en el control Aspose.Cells.GridDesktop como se muestra a continuación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
