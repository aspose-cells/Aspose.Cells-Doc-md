---
title: Convertir libro de Excel a PDF
type: docs
weight: 80
url: /es/go-cpp/convert-excel-workbook-to-pdf/
---

## **Conversión de libro de Excel a PDF**

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}}

Aspose.Cells escribe directamente la información sobre API y número de versión en los documentos de salida. Por ejemplo, al renderizar el Documento a PDF, Aspose.Cells for Go via C++ llena el campo **Aplicación** con el valor 'Aspose.Cells' y el campo **Productor PDF** con el valor, por ejemplo, 'Aspose.Cells v24.12.0'.

Tenga en cuenta que no puede instruir a Aspose.Cells for Go via C++ para cambiar o eliminar esta información de los Documentos de salida.

{{% /alert %}}

### **Conversión Directa**

Siga los siguientes pasos para convertir directamente las hojas de cálculo de Excel al formato PDF:

1. Instanciar un objeto de la clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente o saltarse este paso si está creando el libro de trabajo desde cero.
1. Realiza cualquier trabajo (ingreso de datos, aplicación de formato, definición de fórmulas, inserción de imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo usando las APIs de Aspose.Cells.
1. Cuando el código de la hoja de cálculo esté completo, llame al método [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) para guardar la hoja de cálculo.

El formato de archivo debe ser PDF, así que seleccione el valor predefinido PDF en la enumeración SaveFormat para generar el documento PDF final.

Por favor, vea el siguiente código de ejemplo, su [archivo de Excel de ejemplo](67338368.xlsx) y el [PDF de salida](67338369.pdf) para su referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
