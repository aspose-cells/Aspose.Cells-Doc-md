---
title: Guardar archivos
type: docs
weight: 20
url: /es/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells permite crear y guardar archivos y manipular archivos existentes. Este artículo explica las diversas formas en que se pueden guardar los archivos.

{{% /alert %}} 
## **Diferentes formas de guardar archivos**
 Aspose.Cells proporciona el[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft y proporciona los métodos necesarios para trabajar con archivos de Excel. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)la clase proporciona la[Ahorrar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) método utilizado para guardar archivos de Excel. los[Ahorrar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) El método tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes maneras. El formato de archivo en el que se guarda el archivo lo decide el[Guardar formato](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)enumeración.
## **Guardar archivo en alguna ubicación**
 Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (completo con la ruta de almacenamiento) y el formato de archivo deseado (del[Guardar formato](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) enumeración) al llamar al[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) objetos[Ahorrar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **Guardar archivo en transmisión**
 Para guardar archivos en un flujo, cree un objeto MemoryStream o FileStream y guarde el archivo en ese objeto de flujo llamando al[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) objetos[Ahorrar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349) método. Especifique el formato de archivo deseado usando el[Guardar formato](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a) enumeración al llamar al[Ahorrar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
