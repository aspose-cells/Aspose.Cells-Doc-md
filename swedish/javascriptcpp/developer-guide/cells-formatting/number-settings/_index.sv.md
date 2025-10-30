---
title: Nummerinställningar
linktitle: Nummerinställningar
description: Aspose.Cells är ett JavaScript bibliotek för att arbeta med kalkylbladsfiler som stöder många olika cellnummerinställningar. Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att hantera cellernas nummerinställningar för att justera nummerformat i kalkylblad.
keywords: Aspose.Cells, JavaScript bibliotek, elektroniskt kalkylblad, cellnummerinställningar, formatering, hantering, Format av nummer och datum
type: docs
weight: 10
url: /sv/javascript-cpp/cells-number-settings/
---

## **Hur man ställer in visningsformat för nummer och datum**  

En mycket stark funktion i Microsoft Excel är att den tillåter användare att ställa in visningsformat för numeriska värden och datum. Vi vet att numeriska data kan användas för att representera olika värden inklusive decimal, valuta, procent, bråk eller bokföringsvärden, etc. Alla dessa numeriska värden visas i olika format beroende på vilken typ av information de representerar. På samma sätt finns det många format för hur ett datum eller en tid kan visas.  
Aspose.Cells stöder denna funktion och tillåter utvecklare att ställa in vilket visningsformat som helst för ett nummer eller ett datum.  

### **Hur man ställer in visningsformat i Microsoft Excel**  

För att ställa in visningsformat i Microsoft Excel:  

1. Högerklicka på vilken cell som helst.  
2. Välj **Formatera celler**. En dialogruta kommer att öppnas och används för att ställa in visningsformat för vilken som helst slags värde.  

På vänstra sidan av dialogrutan finns många kategorier av värden som **Allmän**, **Nummer**, **Valuta**, **Bokföring**, **Datum**, **Tid**, **Procent**, etc. Aspose.Cells stödjer alla dessa visningsformat.  

Aspose.Cells tillhandahåller en modul, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Excel-fil. Målmodulen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som ger tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av modulen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Modulen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) ger en [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-modulen.  

Aspose.Cells tillhandahåller egenskapen [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) för modulet [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Denna egenskap används för att hämta och ställa in cellens formatering. Modulen [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) tillhandahåller några användbara egenskaper för att hantera visningsformaten för nummer och datum.  

### **Hur man använder inbyggda nummerformat**  

Aspose.Cells erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för nummer och datum. Dessa inbyggda nummerformat kan tillämpas med hjälp av egenskapen [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) för [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet. Alla inbyggda nummerformat ges unika numeriska värden. Utvecklare kan tilldela valfritt numeriskt värde till egenskapen [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) för [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet för att tillämpa visningsformatet. Denna metod är snabb. Nedan listas de inbyggda nummerformaten som stöds av Aspose.Cells.  

|**Värde**|**Typ**|**Formatsträng**|  
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


### **Hur man använder egna nummerformat**  

För att definiera din egen anpassade formatsträng för att ställa in visningsformatet, använd egenskapen [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) för [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-objektet. Denna metod är inte lika snabb som att använda förinställda format, men den är mer flexibel.  

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

Om du använder egenskapen [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) för att ställa in nummerformatet, överskrivs eventuellt tidigare format som ställts in med egenskapen [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) och vice versa.  

{{% /alert %}}  

## **Fortsatta ämnen**  
- [Kontrollera anpassat nummerformat vid inställning av Style.Custom-egenskap](/cells/sv/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Lista över stödda nummerformat](/cells/sv/javascript-cpp/list-of-supported-number-formats/)  
- [Rendera anpassat datumformatmönster g och ge mm dd](/cells/sv/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Ange anpassade nummerdecimaler och gruppavgränsare för Arbetsbok](/cells/sv/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Specificera DBNum anpassade mönsterformatering](/cells/sv/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
