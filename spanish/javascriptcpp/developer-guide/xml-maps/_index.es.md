---
title: Importar XML a libro de trabajo de Excel con JavaScript mediante C++
linktitle: Mapas XML
type: docs
weight: 210
url: /es/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importar datos desde archivos XML a Excel usando Aspose.Cells for JavaScript mediante C++.
---

{{% alert color="primary" %}}

Aspose.Cells permite importar el mapa XML dentro del libro usando el método [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Puedes importar Mapas XML usando Microsoft Excel con los siguientes pasos:

- Selecciona la pestaña **Desarrollador**
- Haz clic en **Importar** en la sección de XML y sigue los pasos requeridos.

Deberás proporcionar tus datos XML para completar la importación. Aquí tienes un [ejemplo de datos XML](5115037.txt) que puedes usar para pruebas.

{{% /alert %}}

## **Importar Mapa XML usando Microsoft Excel**

La siguiente captura de pantalla muestra cómo importar un Mapa XML usando Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importar mapa XML usando Aspose.Cells for JavaScript mediante C++**

El siguiente código de ejemplo muestra cómo utilizar el [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Genera el [archivo de Excel de salida](5115036.xlsx) como se muestra en esta captura de pantalla.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Agregar Mapa XML dentro del libro usando el método XmlMapCollection.add()](/cells/es/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportar datos XML vinculados al mapa XML dentro del libro](/cells/es/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Encontrar el nombre del elemento raíz del mapa XML](/cells/es/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Vincular celdas a elementos del mapa XML](/cells/es/javascript-cpp/link-cells-to-xml-map-elements/)
