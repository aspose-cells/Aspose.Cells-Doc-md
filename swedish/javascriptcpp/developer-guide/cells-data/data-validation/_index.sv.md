---
title: Datavalidering
type: docs
weight: 90
url: /sv/javascript-cpp/data-validation/
description: Lär dig att lägga till data validering med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Lägg till datavalidering JavaScript via C++, Hämta valideringsvärde JavaScript via C++, Lägg till helnummerdatavalidering JavaScript via C++, Lägg till listdatavalidering JavaScript via C++, Lägg till datumvalidering JavaScript via C++, Lägg till tidsvalidering JavaScript via C++, Lägg till textlängdsvalidering JavaScript via C++, Lägg till CellArea till befintlig validering JavaScript via C++, Kontrollera om validering i cellen är dropdown JavaScript via C++, Lägg till anpassad validering JavaScript via C++
---

{{% alert color="primary" %}}
Microsoft Excel erbjuder bra funktioner för automatisk filtrering eller validering av kalkylbladets data. Aspose.Cells stöder fullt ut Microsoft Excels data validerings- och autofilterfunktioner. Denna artikel förklarar hur man använder funktionerna i Microsoft Excel och hur man kodar dem med Aspose.Cells for JavaScript via C++.
{{% /alert %}}

## **Datavalideringstyper och utförande**

Datavalidering är förmågan att ställa regler om data som skrivs in på ett arbetsblad. Använd till exempel validering för att säkerställa att en kolumn märkt DATUM endast innehåller datum, eller att en annan kolumn endast innehåller siffror. Du skulle även kunna säkerställa att en kolumn märkt DATUM endast innehåller datum inom ett visst intervall. Med datavalidering kan du kontrollera vad som skrivs in i celler på arbetsbladet.

Microsoft Excel stöder ett antal olika typer av datavalidering. Varje typ används för att styra vilken typ av data som skrivs in i en cell eller cellområde. Nedan illustrerar kodsnuttar hur man validerar att:

- Siffror är hela, det vill säga att de inte har en decimaldel.
- Decimaltal följer rätt struktur. Kodexemplet definierar att en rad celler ska ha två decimaler.
- Värden är begränsade till en lista med värden. Listvalidering definierar en separat lista med värden som kan tillämpas på en cell eller cellområde.
- Datum ligger inom ett specifikt intervall.
- En tid ligger inom ett specifikt intervall.
- En text är inom en given teckenlängd.

### **Datavalidering med Microsoft Excel**

För att skapa valideringar med Microsoft Excel:

1. I ett kalkylblad, välj de celler till vilka du vill applicera validering.
1. Från menyn **Data**, välj **Validering**. Valideringsdialogen visas.
1. Klicka på fliken **Inställningar** och ange inställningar.

### **Datasäkringsvalidering med Aspose.Cells for JavaScript via C++**

Datavalidering är en kraftfull funktion för att validera information som matas in i kalkylblad. Med datavalidering kan utvecklare tillhandahålla användare med en lista över val, begränsa datamatare till en specifik typ eller storlek, osv.
I Aspose.Cells for JavaScript via C++, har varje [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klass en [**validations**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#validations--) samling som representerar en samling av [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation)-objekt. För att ställa in validering, ställ in några av [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) klassens egenskaper enligt följande:

- Typ – representerar valideringstypen, som kan specificeras genom att använda ett av de fördefinierade värdena i enum [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype).
- Operator – representerar operatorn som ska användas i valideringen, som kan specificeras genom att använda ett av de fördefinierade värdena i enum [**OperatorType**](https://reference.aspose.com/cells/javascript-cpp/operatortype).
- Formel1 - representerar värdet eller uttrycket associerat med den första delen av datavalideringen.
- Formel2 - representerar värdet eller uttrycket associerat med den andra delen av datavalideringen.

När egenskaperna för [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation) objektet har konfigurerats, kan utvecklare använda strukturen [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) för att lagra information om cellområdet som ska valideras med hjälp av den skapade valideringen.

#### **Typer av Datavalidering**

Enum [**ValidationType**](https://reference.aspose.com/cells/javascript-cpp/validationtype) har följande medlemmar:

| **Medlemsnamn** | **Beskrivning** |
| :- | :- |
|AnyValue|Betecknar ett värde av valfri typ.
|WholeNumber|Betecknar valideringstyp för heltal.
|Decimal|Betecknar valideringstyp för decimaltal.
|List|Betecknar valideringstyp för nedrullningslistan.
|Date|Betecknar valideringstyp för datum.
|Time|Betecknar valideringstyp för tid.
|TextLength|Betecknar valideringstyp för längden av text.
|Custom|Betecknar anpassad valideringstyp.

##### **Heltalsdatavalidering**

Med denna typ av validering kan användare endast mata in hela tal inom ett specificerat intervall i de validerade cellerna. De följande kodexemplen visar hur man implementerar helnummervalidering. Exemplet skapar samma datavalidering med Aspose.Cells for JavaScript via C++ som vi gjorde med Microsoft Excel ovan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');

            if (fileInput.files.length > 0) {
                // If a file is provided, we will open it; otherwise create a new workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                // Instantiate workbook from uploaded file
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook
                var workbook = new Workbook();
            }

            // Create a worksheet and get the first worksheet.
            const ExcelWorkSheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Creating a Validation object
            const idx = validations.add(ca);
            const validation = validations.get(idx);

            // Setting the validation type to whole number
            validation.type = AsposeCells.ValidationType.WholeNumber;

            // Setting the operator for validation to Between
            validation.operator = AsposeCells.OperatorType.Between;

            // Setting the minimum value for the validation
            validation.formula1 = "10";

            // Setting the maximum value for the validation
            validation.formula2 = "1000";

            // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
            const area = new AsposeCells.CellArea();
            area.startRow = 0;
            area.endRow = 1;
            area.startColumn = 0;
            area.endColumn = 1;

            // Adding the cell area to Validation
            validation.addArea(area);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Validation added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Listvalidering**

Denna typ av validering tillåter användaren att mata in värden från en nedrullningslista. Det tillhandahåller en lista: en serie rader som innehåller data. I exemplet läggs ett andra kalkylblad till för att hålla listkällan. Användare kan endast välja värden från listan. Valideringsområdet är cellområdet A1:A5 i det första kalkylbladet.

Det är viktigt här att du ställer in egenskapen [**Validation.inCellDropDown(boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown-boolean-) på **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // This example creates a new workbook in the browser (file input is optional here).
            const workbook = new Workbook();

            // Get the first worksheet.
            const worksheet1 = workbook.worksheets.get(0);

            // Add a new worksheet and access it.
            const i = workbook.worksheets.add();
            const worksheet2 = workbook.worksheets.get(i);

            // Create a range in the second worksheet.
            const range = worksheet2.cells.createRange("E1", "E4");

            // Name the range.
            range.name = "MyRange";

            // Fill different cells with data in the range.
            range.get(0, 0).value = "Blue";
            range.get(1, 0).value = "Red";
            range.get(2, 0).value = "Green";
            range.get(3, 0).value = "Yellow";

            // Get the validations collection.
            const validations = worksheet1.validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Create a new validation to the validations list.
            const validation = validations.get(validations.add(ca));

            // Set the validation type.
            validation.type = ValidationType.List;

            // Set the operator.
            validation.operator = OperatorType.None;

            // Set the in cell drop down.
            validation.inCellDropDown = true;

            // Set the formula1.
            validation.formula1 = "=MyRange";

            // Enable it to show error.
            validation.showError = true;

            // Set the alert type severity level.
            validation.alertStyle = ValidationAlertType.Stop;

            // Set the error title.
            validation.errorTitle = "Error";

            // Set the error message.
            validation.errorMessage = "Please select a color from the list";

            // Specify the validation area.
            const area = new CellArea();
            area.startRow = 0;
            area.endRow = 4;
            area.startColumn = 0;
            area.endColumn = 0;

            // Add the validation area.
            validation.addArea(area);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation list created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **Datumdata validering**

Med denna typ av validering anger användare datumvärden inom ett angivet intervall eller enligt specifika kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange datum mellan 1970 och 1999. Här är valideringsområdet cell B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Date Validation Example</h1>
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
            // This example creates a new workbook in the browser (no file input required)
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into the A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter Date b/w 1/1/1970 and 12/31/1999";

            // Set row height and column width for the cells by accessing row/column objects
            const row0 = cells.rows.get(0);
            row0.height = 31;
            const col0 = cells.columns.get(0);
            col0.width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = AsposeCells.ValidationType.Date;

            // Set the operator for the data validation
            validation.operator = AsposeCells.OperatorType.Between;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "1/1/1970";

            // The value or expression associated with the second part of the data validation.
            validation.formula2 = "12/31/1999";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = AsposeCells.ValidationAlertType.Stop;

            // Set the title of the data-validation error dialog box
            validation.errorTitle = "Date Error";

            // Set the data validation error message.
            validation.errorMessage = "Enter a Valid Date";

            // Set and enable the data validation input message.
            validation.inputMessage = "Date Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and validation added. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

##### **Tidsdata validering**

Med denna typ av validering kan användare ange tider inom ett angivet intervall eller enligt vissa kriterier i de validerade cellerna. I exemplet är användaren begränsad att ange tider mellan 09:00 och 11:30 förmiddag. Här är valideringsområdet cell B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Time Validation Example</h1>
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
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtain the cells of the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Put a string value into A1 cell.
            const a1 = cells.get("A1");
            a1.value = "Please enter Time b/w 09:00 and 11:30 'o Clock";

            // Set the row height and column width for the cells using row/column objects.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = worksheet.validations;

            // Create Cell Area
            const ca = new AsposeCells.CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation and obtain it.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type and other properties.
            validation.type = AsposeCells.ValidationType.Time;
            validation.operator = AsposeCells.OperatorType.Between;
            validation.formula1 = "09:00";
            validation.formula2 = "11:30";
            validation.showError = true;
            validation.alertStyle = AsposeCells.ValidationAlertType.Information;
            validation.errorTitle = "Time Error";
            validation.errorMessage = "Enter a Valid Time";
            validation.inputMessage = "Time Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new AsposeCells.CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **Textlängd data validering**

Med denna typ av validering kan användare ange textvärden av en angiven längd i de validerade cellerna. I exemplet är användaren begränsad att ange strängvärden med högst 5 tecken. Valideringsområdet är cell B1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Text Length Validation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, OperatorType, ValidationAlertType } = AsposeCells;

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
            // Create a new workbook.
            const workbook = new Workbook();

            // Obtain the cells of the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Put a string value into A1 cell.
            const cellA1 = cells.get("A1");
            cellA1.value = "Please enter a string not more than 5 chars";

            // Set row height and column width for the cell.
            cells.rows.get(0).height = 31;
            cells.columns.get(0).width = 35;

            // Get the validations collection.
            const validations = workbook.worksheets.get(0).validations;

            // Create Cell Area
            const ca = new CellArea();
            ca.startRow = 0;
            ca.endRow = 0;
            ca.startColumn = 0;
            ca.endColumn = 0;

            // Add a new validation.
            const validationIndex = validations.add(ca);
            const validation = validations.get(validationIndex);

            // Set the data validation type.
            validation.type = ValidationType.TextLength;

            // Set the operator for the data validation.
            validation.operator = OperatorType.LessOrEqual;

            // Set the value or expression associated with the data validation.
            validation.formula1 = "5";

            // Enable the error.
            validation.showError = true;

            // Set the validation alert style.
            validation.alertStyle = ValidationAlertType.Warning;

            // Set the title of the data-validation error dialog box.
            validation.errorTitle = "Text Length Error";

            // Set the data validation error message.
            validation.errorMessage = " Enter a Valid String";

            // Set and enable the data validation input message.
            validation.inputMessage = "TextLength Validation Type";
            validation.ignoreBlank = true;
            validation.showInput = true;

            // Set a collection of CellArea which contains the data validation settings.
            const cellArea = new CellArea();
            cellArea.startRow = 0;
            cellArea.endRow = 0;
            cellArea.startColumn = 1;
            cellArea.endColumn = 1;

            // Add the validation area.
            validation.addArea(cellArea);

            // Save the Excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Data valideringsregler**

När datavalideringar implementeras kan valideringen kontrolleras genom att tilldela olika värden i cellerna. [**cell.validationValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) kan användas för att hämta valideringsresultatet. Följande exempel visar den här funktionen med olika värden. Exempelfilen kan hämtas via länken nedan för testning:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Data Validation Check Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            const messages = [];

            // Enter 3 inside this cell
            // Since it is not between 10 and 20, it should fail the validation
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const isValid3 = cell.validationValue;
            messages.push(`Is 3 a Valid Value for this Cell: ${isValid3}`);

            // Enter 15 inside this cell
            // Since it is between 10 and 20, it should succeed the validation
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const isValid15 = cell.validationValue;
            messages.push(`Is 15 a Valid Value for this Cell: ${isValid15}`);

            // Enter 30 inside this cell
            // Since it is not between 10 and 20, it should fail the validation again
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const isValid30 = cell.validationValue;
            messages.push(`Is 30 a Valid Value for this Cell: ${isValid30}`);

            // Display results
            resultDiv.innerHTML = messages.map(m => `<p>${m}</p>`).join('');

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```


## **Kontrollera om valideringen i cellen är rullgardinsmeny**

Som vi har sett finns det många typer av valideringar som kan implementeras inom en cell. Om du vill kontrollera om valideringen är en rullgardinslista, kan [**validation.inCellDropDown**](https://reference.aspose.com/cells/javascript-cpp/validation/#inCellDropDown--)-metoden användas för att testa detta. Följande exempel visar användningen av denna egenskap. En testfil kan laddas ner via länken nedan:

[sampleValidation.xlsx](79527947.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Data Validation Drop-downs</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the worksheet named "Sheet1"
            const sheet = workbook.worksheets.get("Sheet1");
            const cells = sheet.cells;

            const appendMessage = (msg, color = 'black') => {
                const p = document.createElement('p');
                p.style.color = color;
                p.textContent = msg;
                resultDiv.appendChild(p);
            };

            const checkDropDown = (cell, cellRef) => {
                const validation = cell.validation;
                if (validation.inCellDropDown) {
                    appendMessage(`${cellRef} is a dropdown`, 'green');
                } else {
                    appendMessage(`${cellRef} is NOT a dropdown`, 'orange');
                }
            };

            checkDropDown(cells.get("A2"), "A2");
            checkDropDown(cells.get("B2"), "B2");
            checkDropDown(cells.get("C2"), "C2");
        });
    </script>
</html>
```


## **Lägg till CellArea till befintlig validering**

Det kan finnas situationer där du vill lägga till [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) till befintliga [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation). När du lägger till [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) med [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-) kontrollerar Aspose.Cells alla befintliga områden för att se om det nya området redan finns. Om filen har många valideringar kan detta påverka prestandan. För att lösa detta finns metoden [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-). Parametern *checkIntersection* anger om korsningen mellan ett givet område och befintliga valideringsområden ska kontrolleras. Att sätta den till **false** kommer att inaktivera kontroll av andra områden. Parametern *checkEdge* indikerar om de tillämpade områdena ska kontrolleras. Om det nya området blir det övre vänstra området, byggs interna inställningar om. Om du är säker på att det nya området inte är det övre vänstra, kan du ange denna parameter som **false**.

Följande kodsnutt visar användningen av [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/javascript-cpp/validation/#addArea-cellarea-boolean-boolean-)-metoden för att lägga till en ny [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea) till befintliga [**Validation**](https://reference.aspose.com/cells/javascript-cpp/validation).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Validations</title>
    </head>
    <body>
        <h1>Validations Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Accessing the Validations collection of the worksheet
            const validation = worksheet.validations.get(0);

            // Create your cell area.
            const cellArea = AsposeCells.CellArea.createCellArea("D5", "E7");

            // Adding the cell area to Validation
            validation.addArea(cellArea, false, false);

            // Save the output workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ValidationsSample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Validation area added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Käll- och utdataexcelfilerna är bilagda som referens.

[Källfil](96928093.xlsx)

[Utdatafil](96928220.xlsx)

## **Fortsatta ämnen**
- [Hämta cellvalidering i ODS-filer](/cells/sv/javascript-cpp/get-cell-validation-in-ods-files/)
- [Få validering som tillämpas på en cell](/cells/sv/javascript-cpp/get-validation-applied-on-a-cell/)
- [Verifiera att cellvärdet uppfyller datavalideringsreglerna](/cells/sv/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/)
