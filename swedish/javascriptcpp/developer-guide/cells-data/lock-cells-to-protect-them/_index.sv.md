---
title: Hur man låser celler för att skydda dem
type: docs
weight: 130
url: /sv/javascript-cpp/how-to-lock-cells-to-protect-them/
description: Denna artikel visar kod som förklarar hur man låser celler för att skydda dem med Aspose.Cells for JavaScript via C++.
keywords: JavaScript Lås celler för att skydda dem, Hur man låser celler för att skydda dem med JavaScript, Lås celler för att skydda dem i JavaScript.
---

## **Möjliga användningsscenario**
Att låsa celler för att skydda dem är en vanlig praxis i kalkylbladsapplikationer, som Microsoft Excel eller Google Sheets, av flera viktiga skäl:

1. Förebygga oavsiktliga ändringar: Att låsa celler kan förhindra att användare oavsiktligt modifierar viktig data eller formler. Detta är särskilt användbart i komplexa kalkylblad där oavsiktliga ändringar kan leda till betydande fel.

1. Upprätthållande av dataintegritet: Genom att låsa celler kan du säkerställa att kritiska data förblir konsekventa och korrekta. Detta är avgörande för finansiella dokument, rapporter och andra dokument där dataintegritet är väsentlig.

1. Kontrollad åtkomst: I samarbetsmiljöer låter låsning av celler dig kontrollera vem som kan redigera vissa delar av ett kalkylblad. Till exempel kan du vilja tillåta endast vissa teammedlemmar att redigera specifika celler samtidigt som resten av bladet är skyddat.

1. Skydda formler: Formler är ofta avgörande för beräkningar och dataanalys. Att låsa celler som innehåller formler säkerställer att dessa formler inte oavsiktligt förändras eller tas bort, vilket kan störa funktionaliteten i hela bladet.

1. Tillämpa affärsregler: I vissa fall kan specifika affärsregler eller regler kräva att viss data skyddas mot förändringar. Att låsa celler hjälper till att följa dessa krav.

1. Vägledning för användare: Genom att låsa celler och ge tydliga instruktioner om vilka celler som kan redigeras kan du vägleda användare om hur de ska interagera med kalkylbladet, vilket minskar förvirring och fel.

## **Hur låser du celler för att skydda dem i Excel**
Så här låser du celler i Microsoft Excel:

1. Välj cellerna att låsa: Välj de celler du vill låsa. Om du vill låsa hela bladet kan du hoppa över detta steg.
1. Öppna dialogrutan för formatering av celler: Högerklicka på de valda cellerna och välj "Formatera celler," eller tryck på Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Lås cellerna: I dialogrutan Formatera celler, gå till fliken "Skydd". Markera kryssrutan "Låst". Klicka på "OK."
1. Skydda arket: Gå till "Granska"-fliken på menyfliksområdet. Klicka på "Skydda blad." Ange ett lösenord (valfritt) och välj de behörigheter du vill tillåta (t.ex. välja låsta celler, formatera celler etc.). Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser celler för att skydda dem med JavaScript**

Aspose.Cells är ett kraftfullt bibliotek för att arbeta med Excel-filer programvarumässigt. För att låsa celler med Aspose.Cells for JavaScript via C++, måste du följa dessa steg: ladda [ exempel fil](sample.xlsx), lås upp alla celler först (eftersom, som standard, är alla celler låsta men inte tvingade förrän arket är skyddat), sedan låsa de specifika cellerna du vill skydda, och slutligen skydda arket för att tvinga låsningen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Utdataresultat**
Denna kod säkerställer att endast de angivna cellerna (A1 och B2 i detta exempel) är låsta, och att arket är skyddat för att genomdriva dessa inställningar. Alla andra celler i arket förblir upplåsta och redigerbara.

<br>
<img src="3.png" width=60% />
