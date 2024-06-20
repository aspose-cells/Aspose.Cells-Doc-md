---
title: Aplicar sombreado a filas y columnas alternas con formato condicional
type: docs
weight: 10
url: /es/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Las API de Aspose.Cells proporcionan los medios para agregar y manipular reglas de formato condicional para el objeto [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Estas reglas pueden ser personalizadas de varias maneras para obtener el formato deseado basado en condiciones o reglas. Este artículo demostrará el uso de la API Aspose.Cells for Java para aplicar sombreado a filas y columnas alternas con la ayuda de reglas de formato condicional y funciones integradas de Excel.

{{% /alert %}} 
## **Aplicar sombreado a filas y columnas alternas usando formato condicional**
Este artículo hace uso de las funciones integradas de Excel como ROW, COLUMN y MOD. Aquí hay algunos detalles de estas funciones para comprender mejor el fragmento de código proporcionado a continuación.

- La función **ROW()** devuelve el número de fila de una referencia de celda. Si se omite la referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función ROW.
- La función **COLUMN()** devuelve el número de columna de una referencia de celda. Si se omite la referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función COLUMN.
- La función **MOD()** devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto se desea encontrar y el segundo parámetro es el número utilizado para dividir el parámetro del número. Si el divisor es 0, devolverá el error #DIV/0!.

Comencemos a escribir un poco de código para lograr el objetivo con la ayuda de la API Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



La siguiente captura de pantalla muestra la hoja de cálculo resultante cargada en la aplicación de Excel.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

Para aplicar el sombreado a las columnas alternas, todo lo que tiene que hacer es cambiar la fórmula **=MOD(ROW(),2)=0** a **=MOD(COLUMN(),2)=0**, es decir, en lugar de obtener el índice de fila, modifique la fórmula para obtener el índice de columna. 
La hoja de cálculo resultante, en este caso, se verá como la siguiente imagen.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
