---
title: Cambiar el separador decimal desde el teclado numérico
type: docs
weight: 150
url: /es/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb, decimal, separador decimal
description: Este artículo presenta cómo cambiar el separador decimal en GridWeb.
---

## **Escenarios de uso posibles**
De forma predeterminada, Aspose.Cells.GridWeb muestra datos numéricos según la configuración regional del equipo. Puede cambiar el separador decimal desde el teclado numérico programáticamente utilizando la API de Aspose.Cells.GridWeb. Por lo tanto, cuando un archivo se importa a una matriz GridWeb o se introduce algún dato numérico (desde el teclado numérico) en una celda de hoja de cálculo nueva, debería tener configurado visualmente su separador decimal deseado. 
## **Cambiar el separador decimal desde el teclado numérico**
Usando la propiedad **GridWorksheetCollection.NumberDecimalSeparator**, puede cambiar el separador decimal desde el teclado numérico programáticamente. Consulte las capturas de pantalla que muestran cómo funciona.

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Tenga en cuenta que el cambio del separador decimal es solo para la experiencia visual de los usuarios en GridWeb. Cuando edite y guarde su libro de trabajo, seguirá almacenando los valores numéricos (en la hoja de cálculo) según su separador decimal regional.

{{% /alert %}}
