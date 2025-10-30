---
title: Cómo rotar el texto de una celda con Golang a través de C++
linktitle: Cómo rotar el texto de la celda
type: docs
weight: 80
url: /es/go-cpp/how-to-rotate-text-of-cell/
description: Código en C++ para rotar el texto de la celda con la API Aspose.Cells for C++
keywords: rotar texto de celda en C++, rotar programáticamente el texto de la celda en el libro de trabajo, establecer de forma programática el ángulo de rotación de la celda en el libro de trabajo, cómo rotar el texto de la celda en Excel con C++
---

## **Rotar el texto de la celda en Aspose.Cells**

Aspose.Cells es un componente potente en C++ que permite a los desarrolladores trabajar con hojas de cálculo de Excel de manera programática. Una de las funciones proporcionadas por Aspose.Cells es la capacidad de rotar celdas, permitiéndote personalizar la orientación del texto y mejorar la presentación visual de tus datos. En este documento, exploraremos cómo rotar celdas usando Aspose.Cells.

## **Cómo rotar el texto de la celda en Excel**
Para rotar una celda en Excel, puedes seguir los siguientes pasos:
1. Abre Excel y selecciona la celda o rango de celdas que deseas rotar.
1. Haz clic derecho en la(s) celda(s) seleccionada(s) y elige "Formato de celdas" en el menú contextual. Alternativamente, puedes ir a la pestaña "Inicio" en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Celdas" y seleccionar "Formato de celdas".
1. En el cuadro de diálogo "Formato de celdas", ve a la pestaña "Alineación".
1. En la sección "Orientación", verás las opciones para rotar el texto. Puedes ingresar directamente el ángulo de rotación deseado en grados en el cuadro "Grados". Los valores positivos rotan el texto en sentido contrario a las agujas del reloj, y los valores negativos lo rotan en sentido de las agujas del reloj.
<br>
![todo:image_alt_text](alignment.png)
1. Una vez que hayas seleccionado la rotación deseada, haz clic en "Aceptar" para aplicar los cambios. La(s) celda(s) seleccionada(s) ahora se rotarán según el ángulo de rotación u orientación elegido.

## **Cómo rotar el texto de la celda utilizando la API Aspose.Cells**

La propiedad [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) hace que sea conveniente rotar celdas. Para rotar celdas en Aspose.Cells, debes seguir estos pasos:
1. Cargar el libro de trabajo de Excel
<br>
Primero, necesitas cargar el libro de Excel usando Aspose.Cells. Puedes usar la clase Workbook para abrir un archivo de Excel existente o crear uno nuevo. 

1. Accede a la hoja de cálculo
<br>
Una vez cargado el libro de trabajo, necesitas acceder a la hoja de cálculo donde quieres rotar las celdas. Puedes acceder a la hoja de cálculo por su índice o nombre. 

1. Rota el texto de la celda
<br>
Ahora que tienes acceso a la hoja de cálculo, puedes rotar las celdas modificando el objeto Style de las celdas deseadas. El objeto Style te permite establecer varias opciones de formato, incluida la rotación. 

1. Guarda el libro de trabajo
<br>
Después de rotar las celdas, puedes guardar el libro de trabajo modificado en un archivo o flujo usando el método Save.

## **Código de muestra en C++**

Consulta el siguiente código, que crea un objeto de libro de trabajo y establece diferentes ángulos de rotación para varias celdas. La captura de pantalla muestra el resultado después de la ejecución del código de ejemplo.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetRotationOfCell.go" >}}
