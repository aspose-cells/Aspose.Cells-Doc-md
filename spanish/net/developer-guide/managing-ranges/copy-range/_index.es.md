---
title: Copiar rangos de Excel
linktitle: Copiar rangos
type: docs
weight: 105
url: /es/net/copy-ranges-of-Excel/
---
## **Introducción**

En Excel, puede seleccionar un rango, copiar el rango y luego pegarlo con opciones específicas en la misma hoja de trabajo, otras hojas de trabajo u otros archivos.

## **Copiar rangos usando Aspose.Cells**

 Aspose.Cells proporciona cierta sobrecarga[Rango.Copiar](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) métodos para copiar el rango.
 Y[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) solo el estilo de copia del rango;[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) solo el valor de copia del rango

## **Copiar rango**

Crear dos rangos: el rango de origen, el rango de destino, luego copiar el rango de origen al rango de destino con el método Range.Copy.

Ver el siguiente código:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Pegar rango con opciones**

Aspose.Cells admite pegar el rango con un tipo específico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Solo copiar datos del rango.**
También puede copiar los datos con el método Range.CopyData como los siguientes códigos:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Temas avanzados**
- [Copiar alturas de fila del rango de origen al rango de destino](/cells/es/net/copy-row-heights-of-source-range-to-destination-range/)


