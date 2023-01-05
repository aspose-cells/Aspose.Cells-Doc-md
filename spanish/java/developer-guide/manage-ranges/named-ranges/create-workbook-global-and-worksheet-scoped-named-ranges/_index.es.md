---
title: Crear libros de trabajo (globales) y hojas de trabajo con alcance de rangos con nombre
type: docs
weight: 10
url: /es/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios definir rangos con nombre con dos ámbitos diferentes: libro de trabajo (también conocido como ámbito global) y hoja de trabajo.

- Se puede acceder a los rangos con nombre con un alcance de libro de trabajo desde cualquier hoja de trabajo dentro de ese libro simplemente usando su nombre.
- Se accede a los rangos con nombre en el ámbito de la hoja de trabajo con la referencia de la hoja de trabajo en particular en la que se creó.

Aspose.Cells proporciona la misma funcionalidad que Microsoft Excel para agregar rangos con nombre en el ámbito de libros y hojas de trabajo. Al crear un rango con nombre en el ámbito de la hoja de trabajo, la referencia de la hoja de trabajo debe usarse en el rango con nombre para especificarlo como un rango con nombre en el ámbito de la hoja de trabajo.

{{% /alert %}}

 Los siguientes ejemplos de código muestran cómo crear rangos de nombres de libros y hojas de trabajo utilizando el[**Rango**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) clase.

## **Agregar un rango con nombre con el alcance del libro de trabajo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Adición de un rango con nombre con ámbito de hoja de cálculo**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
