---
title: Guardar archivos
type: docs
weight: 20
url: /es/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells hace posible crear y guardar archivos y manipular archivos existentes. Este artículo explica las varias maneras en que los archivos pueden ser guardados.

{{% /alert %}}

## **Diferentes formas de guardar archivos**

Aspose.Cells proporciona el [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), que representa un archivo de Microsoft Excel y proporciona métodos necesarios para trabajar con archivos de Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) ofrece el método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) para guardar archivos de Excel. Este método tiene muchas sobrecargas que se usan para guardar archivos de diferentes maneras. El formato de archivo en el que se guarda se decide por la enumeración [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/).

## **Guardar archivo en alguna ubicación**

Para guardar archivos en una ubicación de almacenamiento, especifica el nombre del archivo (con la ruta completa del almacenamiento) y el formato de archivo deseado (de la enumeración [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/)) al llamar al método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) del objeto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Guardar archivo en un flujo**

Para guardar archivos en un stream, crea un objeto MemoryStream o FileStream y guarda el archivo en ese stream llamando al método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) del objeto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Especifica el formato de archivo deseado usando la enumeración [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) al llamar al método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_saveFormat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **Guardar archivo en PDF**

Para guardar el contenido deseado en un archivo PDF usando la librería Aspose.Cells for Go via C++, crea un nuevo objeto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) o construye uno leyendo un archivo Excel existente, y luego guarda el archivo en PDF llamando al método Save del objeto [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Cuando llames al método Save, usa la enumeración [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) para especificar el formato de archivo deseado.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
