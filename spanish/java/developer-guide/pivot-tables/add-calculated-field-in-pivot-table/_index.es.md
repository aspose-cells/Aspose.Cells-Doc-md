---
title: Agregar campo calculado en tabla dinámica
type: docs
weight: 130
url: /es/java/add-calculated-field-in-pivot-table/
description: Cómo agregar un campo calculado en una tabla dinámica con Aspose.Cells.
keywords: Agregar un campo calculado en una tabla dinámica.
---

## **Escenarios de uso posibles**
Cuando crea una tabla dinámica basada en datos conocidos, se encuentra con que los datos no son los que desea. Los datos que desea es la combinación de estos datos originales. Por ejemplo, necesita sumar, restar, multiplicar y dividir los datos originales antes de querer los datos. En ese momento, necesita crear un campo calculado y establecer la fórmula correspondiente para el cálculo. Luego realizar algunas estadísticas y otras operaciones en el campo calculado. 

## **Añadir campo calculado en tabla dinámica en Excel**
Para insertar un campo calculado en una tabla dinámica en Excel, siga estos pasos:

1. Seleccione la tabla dinámica a la que desea agregar un campo calculado. 
2. Vaya a la pestaña Analizar tabla dinámica en la cinta.
3. Haga clic en "Campos, elementos y conjuntos" y luego seleccione "Campo calculado" en el menú desplegable.
4. En el campo "Nombre", ingrese un nombre para el campo calculado.
5. En el campo "Fórmula", ingrese la fórmula que desea realizar utilizando los nombres de campo de Tabla Dinámica apropiados y operadores matemáticos. 
<br>
<img src="1.png" width=80% />
6. Haga clic en "ok" para crear el campo calculado.
7. El nuevo campo calculado aparecerá en la Lista de campos de la Tabla Dinámica bajo la sección de Valores.
8. Arrastre el campo calculado a la sección de Valores de la Tabla Dinámica para mostrar los valores calculados.
<br>
<img src="2.png" width=80% />

## **Agregar campo calculado en Tabla Dinámica**
Por favor, vea el siguiente código de muestra. El código primero establece los datos originales y crea una tabla dinámica. Luego crea el campo calculado según el PivotField existente en la tabla dinámica y agrega el campo calculado al área de datos. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](out.xlsx). Después de ejecutar el código de ejemplo, se agrega una tabla dinámica con campo calculado a la hoja de cálculo.

## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
