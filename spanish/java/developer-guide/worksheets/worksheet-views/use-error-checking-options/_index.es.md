---
title: Usar opciones de verificación de errores
type: docs
weight: 60
url: /es/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir opciones y reglas de verificación de errores. Los usuarios a menudo ven controles de errores al crear fórmulas, un triángulo pequeño en la esquina superior derecha de una celda resalta cuando hay un problema con una celda. Excel proporciona información que ayuda a los usuarios a corregir problemas comunes.

{{% /alert %}} 
## **Tipos de Errores**
Errores que significan que la fórmula no puede devolver un resultado - como dividir un número por cero - requieren atención inmediata y se muestra un valor de error en la celda. Al hacer clic en el triángulo verde se muestra un signo de exclamación, al hacer clic se abre una lista de opciones. 

El error puede resolverse utilizando las opciones, o ignorarse. Ignorar un error significa que ese error no aparecerá en futuras verificaciones de errores.

Aspose.Cells proporciona opciones de verificación de errores. La clase ErrorCheckOptions gestiona diferentes tipos de comprobaciones de errores, por ejemplo números almacenados como texto, errores de cálculo de fórmulas y errores de validación. Utilice la enumeración ErrorCheckType para establecer la verificación de errores deseada.
## **Números Almacenados como Texto**
Ocasionalmente, los números pueden formatearse y almacenarse en celdas como texto. Esto puede causar problemas con cálculos o producir órdenes de clasificación confusos. Los números formateados como texto están alineados a la izquierda en lugar de a la derecha en la celda. Si una fórmula que debería realizar una operación matemática en celdas no devuelve un valor, verifica la alineación en las celdas a las que hace referencia la fórmula; algunas o todas esas celdas pueden ser números formateados como texto.

Puedes usar las opciones de verificación de errores para convertir rápidamente los números almacenados como texto en números reales. En Microsoft Excel 2003:

1. En el menú **Herramientas**, haz clic en **Opciones**.
1. Selecciona la pestaña de Verificación de Errores.
   La opción de **Número almacenado como texto** está marcada por defecto. 
1. Desactívala.
   Observa la imagen a continuación de cómo se muestra el triángulo verde para los datos en MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

El siguiente código de muestra muestra cómo deshabilitar la opción de verificación de errores de números almacenados como texto para una hoja de cálculo en el archivo XLS de plantilla utilizando las APIs de Aspose.Cells. 

**Java**

{{< highlight csharp >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
