---  
title: Establecer Tipo de Cifrado Fuerte con Node.js a través de C++  
linktitle: Establecer Tipo de Cifrado Fuerte  
type: docs  
weight: 60  
url: /es/nodejs-cpp/setting-strong-encryption-type/  
description: Aprenda cómo establecer tipos de cifrado fuerte para archivos Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) te permite cifrar y proteger con contraseña hojas de cálculo. Utiliza algoritmos proporcionados por un Proveedor de Servicios Criptográficos. Un Proveedor de Servicios Criptográficos (o CSP) es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000". Este es un CSP con algunos problemas de seguridad conocidos públicamente. Las hojas de cálculo aseguradas con el cifrado "débil (XOR)" o con el tipo de cifrado "Compatible con Office 97/2000" pueden ser descifradas fácilmente.

Para superar este problema, utiliza uno de los tipos de cifrado fuerte proporcionados por Microsoft Excel. Puedes cambiar el tipo de cifrado al CSP más fuerte disponible. Para el cifrado fuerte, se requiere una longitud mínima de clave de 128 bits, por ejemplo, 'Proveedor Criptográfico Fuerte de Microsoft'.

También puedes cifrar y proteger con contraseña archivos de Excel con un tipo de cifrado fuerte utilizando la API de Aspose.Cells.

{{% /alert %}}  
## **Aplicar cifrado con Microsoft Excel**  
Para implementar el cifrado de archivos en Microsoft Excel (por ejemplo 2007):

1. Desde el menú **Herramientas**, selecciona **Opciones**.  
1. Selecciona la pestaña **Seguridad**.  
1. Ingresa un valor para el campo **Contraseña para abrir**.  
1. Haz clic en **Avanzado**.  
1. Elige el tipo de cifrado y confirma la contraseña.  

## **Aplicar cifrado con Aspose.Cells**  
Los ejemplos de código a continuación aplican cifrado fuerte en un archivo y establecen una contraseña.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the Excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
