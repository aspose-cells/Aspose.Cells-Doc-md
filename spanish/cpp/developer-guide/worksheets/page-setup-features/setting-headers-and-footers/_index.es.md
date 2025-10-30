---
title: Configurando encabezados y pies de página con C++
linktitle: Configuración de encabezados y pies de página
type: docs
weight: 30
url: /es/cpp/setting-headers-and-footers/
description: Este artículo explica cómo insertar programáticamente una imagen en el encabezado y pie de página de las hojas de Excel al configurar el encabezado y pie de página mediante comandos de script usando la API o biblioteca C++.
keywords: Insertar imagen en cabecera y pie de página de Excel en C++, configurar comandos de script para encabezado pie de página en Excel C++
---

{{% alert color="primary" %}}

Los encabezados y pies de página son las líneas de texto que se muestran debajo del margen superior o encima del margen inferior, respectivamente. También es posible agregar encabezados y pies de página a las hojas de cálculo. Los encabezados y pies de página pueden utilizarse para mostrar información útil como el número de página, el nombre del autor, el nombre del tema o la fecha y hora. Los encabezados y pies de página se gestionan mediante la configuración del diseño de página.

{{% /alert %}}

## **Configuración de encabezados y pies de página**

Aspose.Cells le permite agregar encabezados y pies de página a las hojas de cálculo en tiempo de ejecución, pero recomendamos configurar los encabezados y pies de página manualmente en un archivo pre-diseñado para imprimir. Puede utilizar Microsoft Excel como una herramienta GUI para configurar los encabezados y pies de página y ahorrar esfuerzo y tiempo de desarrollo. Aspose.Cells puede importar el archivo y guardar la configuración.

Para agregar encabezados y pies de página en tiempo de ejecución, Aspose.Cells proporciona llamadas de API especiales y comandos de script para formatear encabezados y pies de página.

### **Comandos de Script**

Los comandos de script son comandos especiales que le permiten configurar el formato de los encabezados y pies de página.

|**Comandos de Script**|**Descripción**|
| :- | :- |
|&P|Número de página actual|
|&G|Una imagen|
|&N|El número total de páginas|
|&D|La fecha actual|
|&T|La hora actual|
|&A|Nombre de la hoja de cálculo|
|&F|El nombre del archivo sin su ruta|
|&&Texto|Muestra &Texto. Por ejemplo: &&WO será mostrado como &WO|
|&"\<FontName>"|Representa un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representa el nombre de la fuente con estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de la fuente. Por ejemplo: “&14abc”. Sin embargo, si este comando va seguido de un número normal a imprimir en el encabezado, esto debe separarse con un carácter de espacio del tamaño de la fuente. Por ejemplo: “&14 123”.|

### **Establecer Encabezados y Pies de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) proporciona dos métodos, [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) y [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/), utilizados para agregar un encabezado y un pie de página a una hoja de trabajo. Estos métodos solo toman dos parámetros:

- **Sección** – la sección donde se debe colocar el encabezado o pie de página. Hay tres secciones: izquierda, centro y derecha, representadas respectivamente por 0, 1 y 2.
- **Script** – el script a utilizar para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Insertar una Imagen en un Encabezado o Pie de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) tiene dos métodos adicionales, [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) y [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/), utilizados para agregar imágenes en el encabezado y pie de página. Estos métodos toman los siguientes parámetros:

- **Sección** – la sección de encabezado o pie de página donde se colocará la imagen. Hay tres secciones, izquierda, centro y derecha, representadas por los valores 0, 1 y 2 respectivamente.
- **Arreglo de bytes** – los datos gráficos (los datos binarios deben escribirse en el búfer de un arreglo de bytes).

Después de ejecutar el código a continuación y abrir el archivo, verificar el encabezado de la hoja de trabajo mediante:

1. En el menú **Archivo**, seleccionar **Configurar Página**. Se mostrará un cuadro de diálogo.
1. Seleccionar la pestaña **Encabezado/Pie de página**.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
