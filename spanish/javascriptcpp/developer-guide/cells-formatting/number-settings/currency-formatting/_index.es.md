---
title: Cómo formatear número como moneda
type: docs
weight: 10
url: /es/javascript-cpp/format-number-to-currency/
description: Este artículo mostrará cómo formatear números a moneda usando Aspose.Cells for JavaScript vía C++ API.
keywords: formatear número como moneda, configuración de número en celda, formatear número a moneda, configuración de moneda, formato de moneda.
---

## **Escenarios de uso posibles**
Formatear números como moneda en Excel es importante por varias razones, especialmente cuando se trabaja con datos financieros. Aquí por qué es beneficioso el formato de moneda:

1. Clarifica valores financieros: formatear un número como moneda hace claro que el valor representa dinero. Por ejemplo, en lugar de ver 1000, que podría significar cualquier cosa, $1,000 indica claramente que el valor es una cantidad monetaria.
1. Incluye símbolos de moneda: al tratar con monedas internacionales o múltiples monedas, formatear números con el símbolo de moneda apropiado (ej., $, €, £) aclara el tipo de moneda, reduciendo confusiones en informes o transacciones multinacionales.
1. Mejora la presentación profesional: valores en moneda bien formateados parecen pulidos y profesionales, lo cual es especialmente importante en informes, presentaciones y documentos comerciales. $10,000.00 parece más creíble y organizado que 10000.
1. Mejora la legibilidad: el formateo como moneda añade comas como separadores de miles y decimales, haciendo que números grandes sean más fáciles de leer. Por ejemplo, 1000000 se convierte en $1,000,000.00, más legible y fácil de entender a simple vista.
1. Asegura la coherencia: al aplicar un formato de moneda coherente, aseguras que todos los valores monetarios en un conjunto de datos se muestren en el mismo formato. Esta coherencia es importante para precisión financiera y comunicación profesional, especialmente en hojas grandes con muchos números.
1. Muestra precisión: el formato de moneda suele incluir dos decimales, facilitando ver montos monetarios exactos. Por ejemplo, $100.50 es claramente diferente de $100.00, lo cual es importante en informes financieros donde la precisión cuenta.
1. Simplifica cálculos financieros: al realizar cálculos financieros (como sumar totales o promediar costos), el formato de moneda ayuda a Excel y a los usuarios a entender que los datos están en términos monetarios. Ayuda a Excel a aplicar el formato apropiado en fórmulas y funciones, asegurando que los resultados sean coherentes.
1. Reduce la mala interpretación: sin el formato de moneda, los números podrían ser mal interpretados como valores numéricos generales en lugar de cantidades de dinero. Por ejemplo, 500 podría confundirse como un conteo de artículos o unidades, mientras que $500.00 claramente representa una cantidad financiera.
1. Funciona con funciones de contabilidad: el formato de moneda se alinea bien con las funciones contables en Excel, como balances o informes de flujo de efectivo. Hace que los valores sean más fáciles de usar en estados financieros donde el dinero es el enfoque principal.
<br>
En resumen, formatear números como moneda ayuda a distinguir los valores monetarios de otros tipos de números, incrementa la claridad y hace que los datos sean más fáciles de interpretar, especialmente en contextos financieros.

## **Cómo formatear un número como moneda en Excel**
Para formatear números como moneda en Excel, sigue estos pasos:

### **Usando la opción de formato de moneda**
1. Selecciona las celdas que deseas formatear como moneda.
1. Ve a la pestaña Inicio en la cinta de opciones.
1. En el grupo Número, haz clic en la flecha desplegable junto a la caja de formato de número (esto puede mostrar "General" por defecto).
<br>
<img src="1.png" width=60% />
1. Elige Moneda en la lista.

### **Usando el cuadro de diálogo de Formato de celdas**
1. Selecciona las celdas que deseas formatear.
1. Haz clic derecho en las celdas seleccionadas y elige Formato de celdas para abrir el cuadro de diálogo Formato de celdas.
1. En la pestaña Número, selecciona Moneda en la lista de la izquierda.
<br>
<img src="2.png" width=60% />
1. Puedes personalizar lo siguiente: Decimales, Símbolo, Números negativos.
1. Haz clic en Aceptar para aplicar el formato.

## **Cómo formatear números como moneda en Aspose.Cells**

Para formatear números como moneda en la biblioteca Aspose.Cells for JavaScript vía C++ para trabajar con archivos de Excel, puedes aplicar el formato de moneda a las celdas programáticamente. Aquí se explica cómo hacerlo usando Aspose.Cells for JavaScript vía C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
