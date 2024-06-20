---
title: Crear rangos con nombre de ámbito de libro de trabajo (Global) y hoja de cálculo
type: docs
weight: 10
url: /es/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de cálculo.

- Los rangos con nombre con ámbito de libro de trabajo se pueden acceder desde cualquier hoja de cálculo dentro de ese libro de trabajo simplemente utilizando su nombre.
- Los rangos con nombre de ámbito de hoja de cálculo se acceden con la referencia de la hoja de cálculo particular en la que se creó.

Aspose.Cells proporciona la misma funcionalidad que Microsoft Excel para agregar rangos con nombre a nivel de libro de trabajo y de hoja de cálculo. Al crear un rango con nombre de ámbito de hoja de cálculo, se debe utilizar la referencia de la hoja de cálculo en el rango con nombre para especificarlo como un rango con nombre de ámbito de hoja de cálculo.

{{% /alert %}}

Los siguientes ejemplos de código muestran cómo crear rangos con nombre de ámbito de libro de trabajo y hoja de cálculo utilizando la clase [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range).

## **Agregar un rango con nombre de ámbito de libro de trabajo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Agregar un Rango con Nombre de Alcance de Hoja de Cálculo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
