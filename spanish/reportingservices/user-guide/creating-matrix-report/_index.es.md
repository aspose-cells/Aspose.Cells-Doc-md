---
title: Crear informe de matriz
type: docs
weight: 10
url: /es/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells para Reporting Services le permite diseñar una matriz en Microsoft Excel.

{{% /alert %}} 
### **Plantilla de matriz**
En una plantilla de informe Aspose.Cells, una matriz consta de esquinas, grupos de filas, grupos de columnas y porciones de datos. A continuación se muestra una matriz de muestra.

**Una matriz de muestra** 

![todo:imagen_alternativa_texto](creating-matrix-report_1.png)

- **Esquina de la matriz**ubicado en la esquina superior izquierda o en la esquina superior derecha para diseños de derecha a izquierda (RTL). Esta área se crea automáticamente cuando agrega grupos de filas y grupos de columnas a una región de datos de matriz. En esta área, puede combinar elementos de informe de cuadros de texto incrustados de celdas.
- **Área de grupos de columnas de matriz**: ubicado en la esquina superior derecha (esquina superior izquierda para el diseño RTL). Esta área se crea automáticamente cuando agrega un grupo de columnas. Las celdas de esta área representan miembros de la jerarquía de grupos de columnas y muestran los valores de instancia del grupo de columnas. En la figura, las celdas que muestran OrderYear son un grupo de columnas anidadas y la celda que muestra OrderQtr es un grupo de columnas adyacente.
- **Área de grupos de filas de matriz**: ubicado en la esquina inferior izquierda (abajo a la derecha para el diseño RTL). Esta área se crea automáticamente cuando agrega un grupo de filas. Las celdas de esta área representan miembros de la jerarquía de grupos de filas y muestran valores de instancia de grupos de filas. En la figura, estas celdas son grupos de filas anidados.
- **Área de datos de matriz**: ubicado en la esquina inferior derecha (abajo a la izquierda para el diseño RTL). Los datos de matriz muestran datos detallados y agrupados. En este ejemplo, solo se utilizan datos agregados. De forma predeterminada, las celdas de una fila o columna de grupo que contienen expresiones simples que no incluyen una función de agregación se evalúan como el primer valor del grupo. En la figura, las celdas muestran los totales agregados de los totales de línea de todos los pedidos de venta.
#### **Creación de una plantilla de matriz**
 Antes de crear un informe de matriz, cree las fuentes de datos, los conjuntos de datos y los parámetros del informe (opcional). (Siga las instrucciones en[Fuentes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/) si necesita ayuda). En el ejemplo, usamos la base de datos de ejemplo AdventureWorks que se incluye con SQL Server Reporting Services 2008.

Para crear una nueva matriz:

1. Abra Microsoft Excel.
1.  Hacer clic**Abrir informe** para abrir un archivo de informe RDL que contiene las fuentes de datos, los conjuntos de datos y los parámetros de informe creados con anterioridad.
Una vez que el archivo se ha abierto con éxito, toda su información está disponible para su uso, por ejemplo, sus conjuntos de datos se enumeran en el**conjunto de datos** lista.
1.  Abra una hoja de cálculo de Excel Microsoft y seleccione un conjunto de datos.

![todo:imagen_alternativa_texto](creating-matrix-report_2.png)




1.  Establecer grupos de filas y grupos de columnas a través de**Establecer grupo**. 

![todo:imagen_alternativa_texto](creating-matrix-report_3.png)




1. Combinar celdas para establecer la esquina de la matriz.

![todo:imagen_alternativa_texto](creating-matrix-report_4.png)




1.  Establezca la esquina de la matriz mediante la inserción de una fórmula.

![todo:imagen_alternativa_texto](creating-matrix-report_5.png)




![todo:imagen_alternativa_texto](creating-matrix-report_6.png)




1.  Hacer clic**Establecer atributo** para establecer el atributo de matriz.

![todo:imagen_alternativa_texto](creating-matrix-report_7.png)



Consta de nombre, rango, grupo y orden.

1. Al hacer clic en modificar atributos, se verifican y modifican todos los atributos de matriz de la hoja de cálculo actual.

![todo:imagen_alternativa_texto](creating-matrix-report_8.png)




1. Guardar, publicar y revisar el informe.
