---
title: Cifrado de archivos de Excel
type: docs
weight: 90
url: /es/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) te permite cifrar y proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits, considerándose un cifrado débil. Para un cifrado fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene CSP que ofrecen tipos de cifrado fuertes, como por ejemplo el 'Proveedor Criptográfico Fuerte de Microsoft'. Para darte una idea, los bancos utilizan un cifrado de 128 bits para encriptar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells para Python via .NET te permite cifrar y proteger con contraseña archivos de Excel de Microsoft con el tipo de cifrado que prefieras.

{{% /alert %}}

## **Usar Microsoft Excel**

Para configurar los ajustes de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**. Aparecerá un cuadro de diálogo.
1. Selecciona la pestaña **Seguridad**.
1. Ingresa una contraseña y haz clic en **Avanzado**.
1. Elige el tipo de cifrado y confirma la contraseña.

## **Cifrado con Aspose.Cells**

El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel usando la API Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Especificar la opción de Contraseña para modificar**

El siguiente ejemplo muestra cómo establecer la opción **Contraseña para modificar** de Microsoft Excel para un archivo existente usando la API Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Verificar la contraseña del archivo cifrado**

Para verificar la contraseña del archivo cifrado, Aspose.Cells para Python via .NET proporciona el método [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Estos métodos aceptan dos parámetros, el flujo del archivo y la contraseña que necesita ser verificada.
El siguiente fragmento de código muestra el uso del método [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) para verificar si la contraseña proporcionada es válida o no.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Cifrado/Descifrado de archivo ODS**

Aspose.Cells para Python via .NET permite cifrar y descifrar archivos ODS. El archivo ODS descifrado puede abrirse tanto en Excel como en OpenOffice, sin embargo, el archivo ODS cifrado solo puede abrirse en OpenOffice tras proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede mostrar una advertencia. Las opciones de cifrado no son aplicables para archivos ODS a diferencia de otros tipos de archivos. Para cifrar un archivo ODS, carga el archivo y establece el valor [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) a la contraseña real antes de guardarlo. El archivo ODS cifrado de salida solo puede abrirse en OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en el [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Una vez que el archivo está cargado, establece el valor de la cadena [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) como nulo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

