---
title: Cómo migrar a Aspose.Cells 7.0.0 o superior
type: docs
weight: 10
url: /es/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

En este artículo, hemos compartido los cambios notables en el API que se realizaron en las versiones Aspose.Cells for Java 7.0.0 y posteriores en comparación con las versiones anteriores de Aspose.Cells for Java. Este artículo ayudará a los usuarios a migrar rápidamente del antiguo API al nuevo API al comprender los cambios realizados y llevarlos a cabo en sus aplicaciones.

{{% /alert %}}

## **Cambios notables para los usuarios existentes**

Desde el lanzamiento de Aspose.Cells for Java v7.0.0, hemos realizado algunas modificaciones importantes en API y hemos agregado todas las funciones que están presentes en Aspose.Cells for .NET hasta la fecha. Entonces, tanto Aspose.Cells for Java como .NET serán comparables ahora en términos de características e incluso en términos de métodos y nombres de propiedades.

De manera similar al enfoque anterior, puede importar solo una declaración de importación en su aplicación para obtener todas las clases, interfaces, etc.

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

Hemos cambiado el nombre de ciertos conjuntos de API para limpiar la estructura API para que coincida con Aspose.Cells for .NET. Hemos agregado algunas clases de colección ahora y las hemos reemplazado con clases de colección existentes. La clase Like Worksheets ha sido reemplazada por**Colección de hojas de trabajo** . Del mismo modo, la clase Shapes ha sido reemplazada por**ShapeCollection**. Sin embargo, la funcionalidad de las clases no se ha visto afectada sino mejorada.

Si desea migrar al nuevo API, es posible que deba realizar los siguientes cambios en su aplicación para que todo funcione en su extremo. La siguiente lista contiene los cambios realizados en las clases y sus respectivos métodos también.

## **Resumen de los Cambios en el API**

1) Colecciones en v2.5.4 o anteriores cuyos nombres que terminan con 's' se renombran. En v7.0.0 o superior, las colecciones se nombran como:
por ejemplo, Formas (Antiguo) -> ShapeCollection (Nuevo), Hojas de trabajo (Antiguo) -> WorksheetCollection (Nuevo), ..., etc.

2) Se cambia la obtención del elemento de la Colección. Por ejemplo, en la v2.5.4 o anterior solíamos hacerlo como getXXX(int), en la v7.0.0 o superior, ahora lo hacemos como get(int):
por ejemplo, Worksheets.getSheet(int) (Antiguo) -> WorksheetCollection.get(int) (Nuevo), ...etc.

3) Se cambia la obtención del tamaño (recuento de elementos) de una colección. En v2.5.4 o anterior, solíamos hacerlo con size(), en v7.0.0 o superior, ahora lo hacemos con getCount():
Worksheets.size() (Antiguo) -> WorksheetCollection.getCount() (Nuevo), ..., etc.

4) Métodos getter de propiedades booleanas en v2.5.4 o anteriores cuyos nombres que comienzan con 'is' se cambian. En v7.0.0, estos se inician con "get":
por ejemplo, PageSetup.isBlackAndWhite() (antiguo) -> PageSetup.getBlackAndWhite() (nuevo), ..., etc.
