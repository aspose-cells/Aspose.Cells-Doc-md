---
title: Cómo Migrar a Aspose.Cells 7.0.0 o Superior
type: docs
weight: 10
url: /es/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

En este artículo, hemos compartido los cambios destacados en la API que se han realizado en la versión 7.0.0 de Aspose.Cells for Java y versiones posteriores en comparación con las versiones anteriores de Aspose.Cells for Java. Este artículo ayudará a los usuarios a migrar rápidamente de la API antigua a la nueva API al comprender los cambios realizados y llevarlos a cabo en sus aplicaciones.

{{% /alert %}}

## **Cambios destacados para los usuarios existentes**

Desde el lanzamiento de Aspose.Cells for Java v7.0.0, hemos realizado algunas modificaciones importantes en la API y hemos añadido todas aquellas características que están presentes en Aspose.Cells for .NET hasta la fecha. Por lo tanto, tanto Aspose.Cells for Java como .NET ahora serán comparables en términos de características e incluso en términos de nombres de métodos y propiedades.

Al igual que en el enfoque anterior, solo puedes importar una declaración de importación en tu aplicación para obtener todas las clases, interfaces, etc.

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Hemos renombrado ciertos conjuntos de API para limpiar la estructura de la API y que coincida con Aspose.Cells for .NET. Ahora hemos añadido algunas clases de colección y las hemos reemplazado con las clases de colección existentes. Por ejemplo, la clase Worksheets ha sido reemplazada por **WorksheetCollection**. De manera similar, la clase Shapes ha sido reemplazada por **ShapeCollection**. Sin embargo, la funcionalidad de las clases no se ha visto afectada, sino mejorada.

Si deseas migrar a la nueva API, entonces es posible que necesites realizar los siguientes cambios en tu aplicación para que las cosas funcionen en tu entorno. La siguiente lista contiene los cambios realizados en las clases y sus respectivos métodos también.

## **Resumen de los cambios en la API**

1) Las colecciones en v2.5.4 o anteriores cuyos nombres terminan con 's' se han renombrado. En v7.0.0 o superior, las colecciones tienen el siguiente nombre:
p. ej., Shapes (Antiguo) -> ShapeCollection (Nuevo), Worksheets (Antiguo) -> WorksheetCollection (Nuevo), ..., etc.

2) Obtener un elemento de la colección ha cambiado. Por ejemplo, en v2.5.4 o anterior solíamos hacerlo como getXXX(int), en v7.0.0 o superior, ahora lo hacemos como get(int):
p. ej., Worksheets.getSheet(int) (Antiguo) -> WorksheetCollection.get(int) (Nuevo), ...etc.

3) Obtener el tamaño (cantidad de elementos) de una colección ha cambiado. En v2.5.4 o anterior, solíamos hacerlo con size(), en v7.0.0 o superior, ahora lo hacemos con getCount():
Worksheets.size() (Antiguo) -> WorksheetCollection.getCount() (Nuevo), ..., etc.

4) Los métodos getter de propiedades booleanas cuyos nombres comienzan con 'is' en v2.5.4 o anteriores han cambiado. En v7.0.0, estos comienzan con "get":
p. ej., PageSetup.isBlackAndWhite() (Antiguo) -> PageSetup.getBlackAndWhite() (Nuevo), ..., etc.
{{< app/cells/assistant language="java" >}}
