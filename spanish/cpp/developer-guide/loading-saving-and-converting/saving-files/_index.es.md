---
title: Guardar archivos
type: docs
weight: 20
url: /es/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells permite crear y guardar archivos, y manipular archivos existentes. Este artículo explica las diversas formas en que se pueden guardar archivos.

{{% /alert %}} 
##  **Diferentes formas de guardar archivos**
 Aspose.Cells proporciona la[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Excel Microsoft y proporciona los métodos necesarios para trabajar con archivos de Excel. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) clase proporciona la[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Método utilizado para guardar archivos de Excel. El[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) El método tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes maneras. El formato de archivo en el que se guarda el archivo lo decide el[Guardar formato](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)enumeración.
##  **Guardar archivo en alguna ubicación**
Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (completo con la ruta de almacenamiento) y el formato de archivo deseado (de la[Guardar formato](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeración) al llamar al[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objetos[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **Guardar archivo para transmitir**
 Para guardar archivos en una secuencia, cree un objeto MemoryStream o FileStream y guarde el archivo en ese objeto de secuencia llamando al[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objetos[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) método. Especifique el formato de archivo deseado usando el[Guardar formato](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeración al llamar al[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)método.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
