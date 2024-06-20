---
title: Agregar Validaciones de Datos de Celdas
type: docs
weight: 90
url: /es/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb, validación, validación de datos, GridValidation
description: Este artículo presenta cómo agregar validación de datos (GridValidation) en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb le permite agregar **Validación de Datos** utilizando el método GridWorksheet.Validations.Add(). Mediante este método, tiene que especificar el **Rango de Celdas**. Pero si desea crear una Validación de Datos en una sola GridCell, puede hacerlo directamente utilizando el método GridCell.CreateValidation(). Del mismo modo, puede eliminar **Validación de Datos** de una GridCell utilizando el método GridCell.RemoveValidation().

{{% /alert %}} 
## **Crear Validación de Datos en una Celda de GridWeb**
El siguiente código de ejemplo crea una **Validación de Datos** en una celda B3. Si ingresa cualquier valor que no esté entre 20 y 40, la celda B3 mostrará **Error de Validación** en forma de **XXX Rojos** como se muestra en esta captura de pantalla.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
