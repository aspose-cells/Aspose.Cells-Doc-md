---
title: Cómo rotar el texto de la celda
type: docs
weight: 80
url: /es/python-net/how-to-rotate-text-of-cell/
description: Código en C# para rotar el texto de una celda con la API Aspose.Cells para Python via .NET
keywords: Python para rotar el texto de una celda, programa en Python para rotar programáticamente el texto en una celda en el libro de trabajo, establecer de forma programática el ángulo de rotación de la celda en el libro de trabajo, Python cómo rotar el texto de una celda en Excel
---

## **Rotar texto de la celda en Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET es un poderoso componente .NET y Java que permite a los desarrolladores trabajar con hojas de cálculo de Excel de forma programática. Una de las funciones que ofrece Aspose.Cells para Python via .NET es la capacidad de rotar celdas, permitiendo personalizar la orientación del texto y mejorar la presentación visual de sus datos. En este documento, exploraremos cómo rotar celdas usando Aspose.Cells para Python via .NET.

## **Cómo rotar el texto de la celda en Excel**
Para rotar una celda en Excel, puedes seguir los siguientes pasos:
1. Abre Excel y selecciona la celda o rango de celdas que deseas rotar.
1. Haz clic derecho en la(s) celda(s) seleccionada(s) y elige "Formato de celdas" en el menú contextual. Alternativamente, puedes ir a la pestaña "Inicio" en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Celdas" y seleccionar "Formato de celdas".
1. En el cuadro de diálogo "Formato de celdas", ve a la pestaña "Alineación".
1. En la sección "Orientación", verás las opciones para rotar el texto. Puedes ingresar directamente el ángulo de rotación deseado en grados en el cuadro "Grados". Los valores positivos rotan el texto en sentido contrario a las agujas del reloj, y los valores negativos lo rotan en sentido de las agujas del reloj.
<br>
![todo:image_alt_text](alignment.png)
1. Una vez que hayas seleccionado la rotación deseada, haz clic en "Aceptar" para aplicar los cambios. La(s) celda(s) seleccionada(s) ahora se rotarán según el ángulo de rotación u orientación elegido.

## **Cómo rotar el texto de una celda usando la API Aspose.Cells para Python via .NET**

La propiedad [**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) facilita la rotación de celdas. Para rotar celdas en Aspose.Cells para Python via .NET, debe seguir estos pasos:
1. Cargar el libro de trabajo de Excel
<br>
Primero, necesita cargar el libro de Excel usando Aspose.Cells para Python via .NET. Puede usar la clase Workbook para abrir un archivo de Excel existente o crear uno nuevo. 

1. Accede a la hoja de cálculo
<br>
Una vez cargado el libro de trabajo, necesitas acceder a la hoja de cálculo donde quieres rotar las celdas. Puedes acceder a la hoja de cálculo por su índice o nombre. 

1. Rota el texto de la celda
<br>
Ahora que tienes acceso a la hoja de cálculo, puedes rotar las celdas modificando el objeto Style de las celdas deseadas. El objeto Style te permite establecer varias opciones de formato, incluida la rotación. 

1. Guarda el libro de trabajo
<br>
Después de rotar las celdas, puedes guardar el libro de trabajo modificado en un archivo o flujo usando el método Save.

## **Código de Ejemplo en Python**

Consulta el siguiente código, que crea un objeto de libro de trabajo y establece diferentes ángulos de rotación para varias celdas. La captura de pantalla muestra el resultado después de la ejecución del código de ejemplo.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

{{< app/cells/assistant language="python-net" >}}
