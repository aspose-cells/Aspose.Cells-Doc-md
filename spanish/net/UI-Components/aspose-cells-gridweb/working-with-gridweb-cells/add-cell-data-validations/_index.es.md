---
title: Agregar Cell Validaciones de datos
type: docs
weight: 90
url: /es/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells. GridWeb le permite agregar**Validación de datos** utilizando el método GridWorksheet.Validations.Add(). Usando este método, usted tiene que especificar el**Cell gama** Pero si desea crear una Validación de datos en un solo GridCell, puede hacerlo directamente utilizando el método GridCell.CreateValidation(). Del mismo modo, puede eliminar**Validación de datos** de un GridCell utilizando el método GridCell.RemoveValidation().

{{% /alert %}} 
## **Crear validación de datos en un GridCell de GridWeb**
 El siguiente código de ejemplo crea un**Validación de datos** en una celda B3. Si ingresa cualquier valor que no esté entre 20 y 40, la celda B3 mostrará**Error de validacion** en forma de**Rojo XXXX** como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
