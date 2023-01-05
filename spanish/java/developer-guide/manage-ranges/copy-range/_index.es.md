---
title: Copiar rangos de Excel
linktitle: Copiar rangos
type: docs
weight: 30
url: /es/java/copy-ranges-of-Excel/
---
## **Introducción**

En Excel, puede seleccionar un rango, copiar el rango y luego pegarlo con opciones específicas en la misma hoja de trabajo, otras hojas de trabajo u otros archivos.

## **Copiar rangos usando Aspose.Cells**

 Aspose.Cells proporciona cierta sobrecarga[Rango.Copiar](https://reference.aspose.com/cells/java/com.aspose.cells/range) métodos para copiar el rango.
## **Copiar rango**

Crear dos rangos: el rango de origen, el rango de destino, luego copiar el rango de origen al rango de destino con el método Range.Copy.

Ver el siguiente código:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Pegar rango con opciones**

Aspose.Cells admite pegar el rango con un tipo específico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Solo copiar datos del rango.**
También puede copiar los datos con el método Range.CopyData como los siguientes códigos:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


