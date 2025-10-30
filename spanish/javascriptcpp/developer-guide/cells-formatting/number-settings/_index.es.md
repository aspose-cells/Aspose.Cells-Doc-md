---
title: Configuraciones numéricas
linktitle: Configuraciones numéricas
description: Aspose.Cells es una biblioteca de JavaScript para trabajar con archivos de hojas de cálculo que admite muchas configuraciones diferentes de números en las celdas. Este artículo introduce cómo usar la biblioteca Aspose.Cells para gestionar las configuraciones numéricas de las celdas y ajustar los formatos numéricos en las hojas de cálculo.
keywords: Aspose.Cells, biblioteca de JavaScript, hoja de cálculo electrónica, configuraciones de números en las celdas, formateo, gestión, formatos de números y fechas
type: docs
weight: 10
url: /es/javascript-cpp/cells-number-settings/
---

## **Cómo establecer formatos de visualización de números y fechas**  

Una función muy potente de Microsoft Excel es que permite a los usuarios establecer los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos pueden usarse para representar diferentes valores incluyendo decimal, moneda, porcentaje, fracción o valores de contabilidad, etc. Todos estos valores numéricos se muestran en diferentes formatos dependiendo del tipo de información que representan. De manera similar, existen muchos formatos en los que se puede mostrar una fecha o hora.  
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores establecer cualquier formato de visualización para un número o fecha.  

### **Cómo establecer formatos de visualización en Microsoft Excel**  

Para establecer formatos de visualización en Microsoft Excel:  

1. Haga clic derecho en cualquier celda.  
2. Seleccione **Formato de celdas**. Aparecerá un cuadro de diálogo que se usa para establecer los formatos de visualización de cualquier valor.  

En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como **General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje**, etc. Aspose.Cells soporta todos estos formatos de visualización.  

Aspose.Cells proporciona un módulo, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) que representa un archivo de Excel. El módulo [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja en el archivo de Excel. Una hoja de cálculo está representada por el módulo [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). El módulo [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) representa un objeto del módulo [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

Aspose.Cells proporciona la propiedad [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) para el módulo [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Esta propiedad se usa para obtener y establecer el formato de una celda. El módulo [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) ofrece algunas propiedades útiles para tratar los formatos de visualización de números y fechas.  

### **Cómo utilizar los formatos de números integrados**  

Aspose.Cells ofrece algunos formatos numéricos integrados para configurar los formatos de visualización de los números y fechas. Estos formatos integrados se pueden aplicar usando la propiedad [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Todos los formatos numéricos integrados tienen valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado a la propiedad [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) para aplicar el formato de visualización. Este método es rápido. Los formatos numéricos integrados compatibles con Aspose.Cells se listan a continuación.  

|**Valor**|**Tipo**|**Cadena de formato**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **Cómo utilizar formatos de números personalizados**  

Para definir tu propia cadena de formato personalizada para establecer el formato de visualización, usa la propiedad [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) del objeto [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Este método no es tan rápido como usar formatos predefinidos, pero es más flexible.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

Si usas la propiedad [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) para establecer el formato numérico, cualquier formato previo establecido usando la propiedad [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) será sobrescrito y viceversa.  

{{% /alert %}}  

## **Temas avanzados**  
- [Consulte el formato de número personalizado al configurar la propiedad Style.Custom](/cells/es/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Lista de formatos de número admitidos](/cells/es/javascript-cpp/list-of-supported-number-formats/)  
- [Renderizar formato personalizado de fecha del patrón g y ge mm dd](/cells/es/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Especificar separadores de números decimales y de grupo personalizados para el libro de trabajo](/cells/es/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Especificación de formato de patrón personalizado DBNum](/cells/es/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
