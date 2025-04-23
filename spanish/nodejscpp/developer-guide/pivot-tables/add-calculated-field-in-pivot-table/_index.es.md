---
title: Agregar campo calculado en tabla dinámica
type: docs
weight: 130
url: /es/nodejs-cpp/add-calculated-field-in-pivot-table/
description: Cómo agregar un campo calculado en tabla dinámica con Aspose.Cells for Node.js via C++
keywords: Aspose.Cells for Node.js via C++ Excel, biblioteca Excel Node.js, Agregar un campo calculado en tabla dinámica usando la biblioteca Excel de Node.js.
---

## **Escenarios de uso posibles**
Cuando crea una tabla dinámica basada en datos conocidos, se encuentra con que los datos no son los que desea. Los datos que desea es la combinación de estos datos originales. Por ejemplo, necesita sumar, restar, multiplicar y dividir los datos originales antes de querer los datos. En ese momento, necesita crear un campo calculado y establecer la fórmula correspondiente para el cálculo. Luego realizar algunas estadísticas y otras operaciones en el campo calculado. 

## **Cómo agregar un campo calculado en una tabla dinámica en Excel**
Para insertar un campo calculado en una tabla dinámica en Excel, siga estos pasos:

1. Seleccione la tabla dinámica a la que desea agregar un campo calculado. 
2. Vaya a la pestaña Analizar tabla dinámica en la cinta.
3. Haga clic en "Campos, elementos y conjuntos" y luego seleccione "Campo calculado" en el menú desplegable.
4. En el campo "Nombre", ingrese un nombre para el campo calculado.
5. En el campo "Fórmula", ingresa la fórmula para el cálculo que deseas realizar utilizando los nombres adecuados de los campos de la tabla dinámica y los operadores matemáticos correspondientes. 
<br>
<img src="1.png" width=80% />
6. Haga clic en "ok" para crear el campo calculado.
7. El nuevo campo calculado aparecerá en la Lista de campos de la Tabla Dinámica bajo la sección de Valores.
8. Arrastre el campo calculado a la sección de Valores de la Tabla Dinámica para mostrar los valores calculados.
<br>
<img src="2.png" width=80% />

## **Cómo agregar un campo calculado en Tabla dinámica usando la biblioteca Aspose.Cells for Node.js via C++**
Agregar campo calculado al archivo Excel usando Aspose.Cells for Node.js via C++. Consulta el siguiente código de ejemplo. Después de ejecutar el ejemplo, se añade una tabla dinámica con campo calculado en la hoja.
1. Establece los datos originales y crea una tabla dinámica. 
2. Crea el campo calculado de acuerdo con el CampoPivote existente en la tabla dinámica.
3. Agrega el campo calculado al área de datos. 
4. Finalmente, guarda el libro en formato [XLSX de salida](out.xlsx). 

## **Código de muestra**
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-Add-calculated-field-in-PivotTable.js" >}}
