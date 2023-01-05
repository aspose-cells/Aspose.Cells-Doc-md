---
title: Fuente predeterminada y color de fuente de GridDesktop
type: docs
weight: 70
url: /es/net/default-font-and-font-color-of-the-griddesktop/
---
## **Posibles escenarios de uso**
A veces, desea cambiar la fuente predeterminada y el color de fuente de GridDesktop. Utilice las siguientes dos propiedades para este propósito. Puede acceder a estas propiedades en tiempo de diseño o en tiempo de ejecución, según sus necesidades.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Cambiar la fuente predeterminada y el color de la fuente en tiempo de diseño**
La siguiente captura de pantalla muestra cómo cambiar la fuente y el color de fuente predeterminados de GridDesktop en tiempo de diseño.

![todo:imagen_alternativa_texto](default-font-and-font-color-of-the-griddesktop_1.png)
## **Cambiar la fuente predeterminada y el color de la fuente en tiempo de ejecución**
El siguiente código de ejemplo explica cómo cambiar la fuente y el color de fuente predeterminados de GridDesktop en tiempo de ejecución.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
