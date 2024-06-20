---
title: Copiar Rangos de Excel
linktitle: Copiar Rangos
type: docs
weight: 105
url: /es/net/copy-ranges-of-Excel/
---

## **Introducción**

En Excel, puede seleccionar un rango, copiarlo y luego pegarlo con opciones específicas en la misma hoja de cálculo, en otras hojas de cálculo o en otros archivos.

## **Copiar Rangos Usando Aspose.Cells**

Aspose.Cells provee algunos métodos de sobrecarga [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) para copiar el rango.
Y [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) para copiar solo el estilo del rango; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) para copiar solo el valor del rango

## **Copiar Rango**

Creando dos rangos: el rango de origen, el rango de destino, luego copiando el rango de origen al rango de destino con el método Range.Copy.

Vea el siguiente código:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Pegar Rango Con Opciones**

Aspose.Cells admite pegar el rango con un tipo específico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Solo copiar datos del rango**
También puedes copiar los datos con el método Range.CopyData como en los siguientes códigos:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Temas avanzados**
- [Copiar alturas de fila del rango de origen al rango de destino](/cells/es/net/copy-row-heights-of-source-range-to-destination-range/)


