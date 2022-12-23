---
title: Cambiar el separador decimal del teclado numérico
type: docs
weight: 150
url: /es/net/change-the-decimal-separator-from-numeric-keypad/
---
## **Posibles escenarios de uso**
De forma predeterminada, Aspose.Cells.GridWeb muestra datos numéricos según la configuración regional/local de la máquina. Puede cambiar el separador decimal del teclado numérico mediante programación usando Aspose.Cells. GridWeb API. Por lo tanto, cuando se importa un archivo a la matriz GridWeb o ingresa algunos datos numéricos (desde el teclado numérico) en una nueva celda de la hoja de trabajo, debe tener el decimal deseado separador establecido visualmente.
## **Cambiar el separador decimal del teclado numérico**
Utilizando la**GridWorksheetCollection.NumberDecimalSeparator**propiedad, puede cambiar el separador decimal del teclado numérico mediante programación. Por favor, vea las capturas de pantalla que muestran cómo funciona

![todo:imagen_alternativa_texto](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:imagen_alternativa_texto](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Tenga en cuenta que el cambio del separador decimal es solo para la experiencia visual de los usuarios en GridWeb. Cuando edite y guarde su libro de trabajo, aún almacenará los valores numéricos (en la hoja de cálculo) según su separador decimal local/regional.

{{% /alert %}}
