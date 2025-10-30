---
title: Guardar archivos
type: docs
weight: 20
url: /es/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells permite crear y guardar archivos, y manipular archivos existentes. Este artículo explica las diversas formas en que se pueden guardar archivos.

{{% /alert %}} 
## **Diferentes formas de guardar archivos**
Aspose.Cells proporciona la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), la cual representa un archivo de Microsoft Excel y proporciona los métodos necesarios para trabajar con archivos de Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) proporciona el método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) utilizado para guardar archivos de Excel. El método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes formas. El formato de archivo al que se guarda el archivo es decidido por la enumeración [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).
## **Guardar archivo en alguna ubicación**
Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (completo con la ruta de almacenamiento) y el formato de archivo deseado (de la enumeración [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) al llamar al método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) del objeto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Guardar archivo en un flujo**
Para guardar archivos en un flujo, cree un objeto MemoryStream o FileStream y guarde el archivo en ese objeto de flujo llamando al método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) del objeto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Especifique el formato de archivo deseado usando la enumeración [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) al llamar al método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **Guardar archivo en PDF**
Para guardar el contenido deseado en un archivo PDF usando la biblioteca Aspose.Cells for C++, cree un nuevo objeto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) o construya un objeto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) leyendo un archivo de Excel existente, y luego [guarde](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) el archivo en PDF llamando al método Save del objeto [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Al llamar al método Save, use la enumeración [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) para especificar el formato de archivo deseado.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
