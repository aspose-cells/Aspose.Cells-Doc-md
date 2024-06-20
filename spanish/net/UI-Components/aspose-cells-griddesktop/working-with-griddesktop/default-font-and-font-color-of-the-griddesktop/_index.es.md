---
title: Fuente e color de fuente por defecto de GridDesktop
type: docs
weight: 70
url: /es/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop,fuente,color
description: Este artículo presenta la fuente y el color de fuente por defecto en GridDesktop.
---

## **Escenarios de uso posibles**
A veces, deseas cambiar la fuente y el color de fuente por defecto de GridDesktop. Por favor, usa las siguientes dos propiedades para este propósito. Puedes acceder a estas propiedades en el Tiempo de Diseño o en Tiempo de Ejecución según tus necesidades.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Cambiar Fuente Predeterminada y Color de Fuente en Tiempo de Diseño**
La siguiente captura de pantalla muestra cómo cambiar la fuente predeterminada y el color de fuente de GridDesktop en Tiempo de Diseño.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Cambiar Fuente Predeterminada y Color de Fuente en Tiempo de Ejecución**
El siguiente código de muestra explica cómo cambiar la fuente predeterminada y el color de fuente de GridDesktop en Tiempo de Ejecución.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
