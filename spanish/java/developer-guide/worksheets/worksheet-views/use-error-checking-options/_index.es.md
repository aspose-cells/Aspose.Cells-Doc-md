---
title: Usar opciones de comprobación de errores
type: docs
weight: 60
url: /es/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel permite a los usuarios definir opciones y reglas de comprobación de errores. Los usuarios a menudo ven verificaciones de errores al crear fórmulas, un pequeño triángulo en la esquina superior derecha de una celda resalta cuando hay un problema con una celda. Excel proporciona información que ayuda a los usuarios a corregir problemas comunes.

{{% /alert %}} 
## **Tipos de errores**
Los errores que significan que la fórmula no puede devolver un resultado, como dividir un número por cero, requieren atención inmediata y se muestra un valor de error en la celda. Al hacer clic en el triángulo verde se muestra un signo de exclamación, al hacer clic se abre una lista de opciones.

El error puede resolverse utilizando las opciones o ignorarse. Ignorar un error significa que ese error no aparecerá en otras verificaciones de errores.

Aspose.Cells proporciona funciones de opción de verificación de errores. La clase ErrorCheckOptions gestiona diferentes tipos de comprobaciones de errores, por ejemplo, números almacenados como texto, errores de cálculo de fórmulas y errores de validación. Utilice la enumeración ErrorCheckType para establecer la comprobación de errores deseada.
## **Numbers Almacenado como texto**
Ocasionalmente, los números pueden formatearse y almacenarse en celdas como texto. Esto puede causar problemas con los cálculos o generar órdenes de clasificación confusos. Numbers que tienen formato de texto se alinean a la izquierda en lugar de a la derecha en la celda. Si una fórmula que debería realizar una operación matemática en las celdas no devuelve un valor, verifique la alineación en las celdas a las que se refiere la fórmula; algunas o todas esas celdas pueden ser números con formato de texto.

Puede usar las opciones de verificación de errores para convertir rápidamente números almacenados como texto en números reales. En Microsoft Excel 2003:

1.  Sobre el**Herramientas** menú, haga clic**Opciones**.
1. Seleccione la pestaña Comprobación de errores.
   **Número almacenado como texto** La opción está marcada por defecto.
1. Desactívelo.
 Vea la imagen a continuación sobre cómo se muestra el triángulo verde para los datos en MS Excel.

![todo:imagen_alternativa_texto](use-error-checking-options_1.png)

 El siguiente código de ejemplo muestra cómo deshabilitar los números almacenados como opción de verificación de errores de texto para una hoja de cálculo en el archivo de plantilla XLS mediante las API Aspose.Cells.

**Java**

{{< highlight "csharp" >}}

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
