---
title: Agregar Validación Personalizada del Lado del Servidor
type: docs
weight: 110
url: /es/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GridWeb, validación del lado del servidor
description: Este artículo presenta cómo trabajar con la validación del lado del servidor en GridWeb.
---

## **Escenarios de uso posibles**
A veces, es posible que necesite implementar validación de datos en el lado del servidor. Aspose.Cells.GridWeb le permite agregar validación de datos personalizada del lado del servidor. Debe especificar el rango o área de celdas. También puede configurar funciones de validación del lado del cliente para devoluciones de llamada con validación del servidor personalizada.
## **Agregar Validación Personalizada del Lado del Servidor**
Debe establecer la clase de validación del servidor que implementa la interfaz **GridCustomServerValidation** a través del atributo **GridValidation.ServerValidation**. También debe configurar la función de validación del lado del cliente (debe estar escrita en JavaScript en el lado del cliente), esta función es obligatoria para validar los datos en el extremo del cliente en la devolución de llamada. Puede configurar la cadena de mensaje de error a través de las propiedades **GridValidation.ErrorMessage** y el título a través de las propiedades **GridValidation.ErrorTitle** según sus necesidades. Consulte una serie de capturas de pantalla que muestran cómo funciona (paso a paso) en un escenario dado después de ejecutar el código de ejemplo a continuación. En el ejemplo, no puede actualizar datos en las celdas B2:C3. Cuando intente editar esas celdas en la hoja, se le mostrarán algunos mensajes de error y se restaurará el valor anterior. Puede abrir la ventana de la consola (en su navegador) para imprimir la información/detalles de las celdas para ciertos eventos. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
