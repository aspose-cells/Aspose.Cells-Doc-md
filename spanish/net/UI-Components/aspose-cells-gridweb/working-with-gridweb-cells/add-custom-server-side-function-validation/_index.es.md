---
title: Agregar validación de función personalizada del lado del servidor
type: docs
weight: 110
url: /es/net/add-custom-server-side-function-validation/
---
## **Posibles escenarios de uso**
A veces, es posible que necesite implementar la validación de datos en el lado del servidor. Aspose.Cells. GridWeb le permite agregar una validación de datos personalizada del lado del servidor. Tienes que especificar el rango de celdas o el área. También puede configurar funciones de validación del lado del cliente para devoluciones de llamada con validación personalizada del lado del servidor.
## **Agregar validación de función personalizada del lado del servidor**
 Debe configurar la clase de validación del servidor que implementa el**GridCustomServerValidation** interfaz a través de**GridValidation.ServerValidation** atributo. También debe configurar la función de validación del lado del cliente (debe estar escrita en JavaScript en el lado del cliente), esta función es obligatoria para validar los datos en el extremo del cliente en la devolución de llamada. Puede configurar la cadena del mensaje de error a través de**GridValidation.ErrorMessage** y título a través de**GridValidation.ErrorTitle**propiedades para sus necesidades. Consulte una serie de capturas de pantalla que muestran cómo funciona (paso a paso) en un escenario determinado después de ejecutar el código de muestra a continuación. En el ejemplo, no puede actualizar los datos en las celdas B2:C3. Cuando intente editar esas celdas en la hoja, aparecerán algunos mensajes de error y se restaurará el valor anterior. Puede abrir la ventana Consola (en su navegador) para imprimir la información/detalles de la celda para ciertos eventos.

![todo:imagen_alternativa_texto](add-custom-server-side-function-validation_1.png)

![todo:imagen_alternativa_texto](add-custom-server-side-function-validation_2.png)

![todo:imagen_alternativa_texto](add-custom-server-side-function-validation_3.png)

![todo:imagen_alternativa_texto](add-custom-server-side-function-validation_4.png)

![todo:imagen_alternativa_texto](add-custom-server-side-function-validation_5.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
