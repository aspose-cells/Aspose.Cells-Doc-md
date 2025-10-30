---
title: Trabajar con fondo en archivos ODS con Golang vía C++
linktitle: Trabajar con fondo en archivos ODS
type: docs
weight: 150
url: /es/go-cpp/working-with-background-in-ods-files/
description: Aprende cómo gestionar fondos de color y gráficos en archivos ODS usando Aspose.Cells con Golang vía C++.
---

## **Fondo en archivos ODS**

Se puede agregar fondo a las hojas en archivos ODS. El fondo puede ser de color o gráfico. El fondo no es visible cuando el archivo está abierto, pero si el archivo se imprime como PDF, el fondo es visible en el PDF generado. El fondo también es visible en el cuadro de diálogo de vista previa de impresión.

Aspose.Cells proporciona la capacidad de leer la información de fondo y agregar el fondo en archivos ODS.

## **Leer información de fondo de archivo ODS**

Aspose.Cells proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la clase [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) cargando el archivo [ODS fuente](90112030.ods) y leyendo la información del fondo. Consulta la salida de consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Salida de la consola**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Agregar fondo de color al archivo ODS**

Aspose.Cells proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) para agregar un fondo de color al archivo ODS. Consulta el archivo [ODS de salida](90112031.ods) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **Agregar fondo gráfico al archivo ODS**

Aspose.Cells proporciona la clase [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) para gestionar fondos en archivos ODS. El siguiente ejemplo de código demuestra el uso de la propiedad [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) para agregar un fondo gráfico al archivo ODS. Consulta el archivo [ODS de salida](90112030.ods) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
