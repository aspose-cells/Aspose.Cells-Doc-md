---
title: Agregar campo calculado en la tabla dinámica
type: docs
weight: 130
url: /es/python-net/add-calculated-field-in-pivot-table/
description: Cómo agregar un campo calculado en la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Adding a calculated field in pivot table.
---
##  **Posibles escenarios de uso**
Cuando crea una tabla dinámica basada en datos conocidos, descubre que los datos que contiene no son los que desea. Los datos que desea son la combinación de estos datos originales. Por ejemplo, necesita sumar, restar, multiplicar y dividir los datos originales antes de querer los datos. En este momento, debe crear un campo calculado y establecer la fórmula correspondiente para el cálculo. Luego realice algunas estadísticas y otras operaciones en el campo calculado.

##  **Agregar campo calculado en tabla dinámica en Excel**
Insertar un campo calculado en una tabla dinámica en Excel, sigue estos pasos:

1.  Seleccione la tabla dinámica a la que desea agregar un campo calculado.
2. Vaya a la pestaña Analizar de tabla dinámica en la cinta.
3. Haga clic en "Campos, elementos y conjuntos" y luego seleccione "Campo calculado" en el menú desplegable.
4. En el campo "Nombre", ingrese un nombre para el campo calculado.
5. En el campo "Fórmula", ingrese la fórmula para el cálculo que desea realizar utilizando los nombres de campo de la tabla dinámica y los operadores matemáticos apropiados.
<br>
<img src="1.png" width=80% />
6. Haga clic en "Aceptar" para crear el campo calculado.
7. El nuevo campo calculado aparecerá en la Lista de campos de la tabla dinámica en la sección Valores.
8. Arrastre el campo calculado a la sección Valores de la tabla dinámica para mostrar los valores calculados.
<br>
<img src="2.png" width=80% />

##  **Agregar campo calculado en la tabla dinámica usando C#**
Agregue el campo calculado al archivo de Excel usando Aspose.Cells for Python via .NET. Consulte el siguiente código de muestra. Después de ejecutar el código de ejemplo, se agrega a la hoja de trabajo una tabla dinámica con el campo calculado.
1.  Establezca los datos originales y cree una tabla dinámica.
2. Cree el campo calculado según el PivotField existente en la tabla dinámica.
 3. Agregue el campo calculado al área de datos.
 4. Finalmente, guarda el libro de trabajo en[salida XLSX](out.xlsx) formato.

##  **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
