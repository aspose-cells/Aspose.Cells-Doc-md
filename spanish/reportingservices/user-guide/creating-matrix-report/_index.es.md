---
title: Creación de informe de matriz
type: docs
weight: 10
url: /es/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services te permite diseñar una matriz en Microsoft Excel. 

{{% /alert %}} 
### **Plantilla de Matriz**
En una plantilla de informe Aspose.Cells, una matriz consta de esquinas, grupos de filas, grupos de columnas y partes de datos. A continuación se muestra una muestra de matriz.

**Una muestra de matriz** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Esquina de la matriz**: ubicada en la esquina superior izquierda, o esquina superior derecha para diseños de derecha a izquierda (RTL). Esta área se crea automáticamente cuando agregas tanto grupos de filas como grupos de columnas a una región de datos de matriz. En esta área, puedes combinar celdas de elementos de informe de cuadros de texto incrustados.
- **Área de grupos de columnas de la matriz**: ubicada en la esquina superior derecha (esquina superior izquierda para diseño RTL). Esta área se crea automáticamente al agregar un grupo de columnas. Las celdas en esta área representan miembros de la jerarquía de grupos de columnas y muestran los valores de instancia del grupo de columnas. En la figura, las celdas que muestran OrderYear es un grupo de columnas anidado, y la celda que muestra OrderQtr es un grupo de columnas adyacente.
- **Área de grupos de filas de la matriz**: ubicada en la esquina inferior izquierda (inferior derecha para diseño RTL). Esta área se crea automáticamente al agregar un grupo de filas. Las celdas en esta área representan miembros de la jerarquía de grupos de filas y muestran los valores de instancia del grupo de filas. En la figura, estas celdas son grupos de filas anidados.
- **Área de datos de la matriz**: ubicada en la esquina inferior derecha (inferior izquierda para diseño RTL). Los datos de la matriz muestran datos detallados y agrupados. En este ejemplo, solo se utilizan datos agregados. Por defecto, las celdas en una fila o columna de grupo que contienen expresiones simples que no incluyen una función de agregado, se evalúan al primer valor del grupo. En la figura, las celdas muestran los totales agregados para los totales de línea de todas las órdenes de venta.
#### **Creación de una Plantilla de Matriz**
Antes de crear un informe de matriz, crea las fuentes de datos, los conjuntos de datos y los parámetros de informe (opcional). (Sigue las instrucciones en [Fuentes de datos y consultas](/cells/es/reportingservices/data-sources-and-queries/) si necesitas ayuda.) En el ejemplo, utilizamos la base de datos de ejemplo AdventureWorks que se incluye con SQL Server Reporting Services 2008.

Para crear una nueva matriz:

1. Abre Microsoft Excel.
1. Haz clic en **Abrir Informe** para abrir un archivo de informe RDL que contenga las fuentes de datos, conjuntos de datos y parámetros de informe creados con antelación.
   Una vez que el archivo se haya abierto con éxito, toda su información estará disponible para su uso. Por ejemplo, sus conjuntos de datos se enumeran en la lista de **Conjunto de Datos**.
1. Abre una hoja de cálculo de Microsoft Excel y selecciona un conjunto de datos. 

![todo:image_alt_text](creating-matrix-report_2.png)




1. Define grupos de filas y grupos de columnas a través de **Definir Grupo**. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Fusiona celdas para establecer la esquina de la matriz.

![todo:image_alt_text](creating-matrix-report_4.png)




1. Establece la esquina de la matriz mediante la inserción de una fórmula. 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. Haz clic en **Establecer Atributo** para configurar el atributo de la matriz. 

![todo:image_alt_text](creating-matrix-report_7.png)



Consiste en nombre, rango, grupo y orden.

1. Al hacer clic en modificar atributo, se verifican y modifican todos los atributos de matriz de la hoja de cálculo actual.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Guardar, publicar y revisar informe.
