---  
title: Encriptar y desencriptar archivos de Excel con Node.js vía C++  
linktitle: Cifrar y Descifrar archivos de Excel  
type: docs  
weight: 10  
url: /es/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Cómo encriptar y desencriptar archivos de Excel usando Node.js vía C++. Bloquear y desbloquear archivos de Excel.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) te permite cifrar y proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits, considerándose un cifrado débil. Para un cifrado fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene CSP que ofrecen tipos de cifrado fuertes, como por ejemplo el 'Proveedor Criptográfico Fuerte de Microsoft'. Para darte una idea, los bancos utilizan un cifrado de 128 bits para encriptar la conexión con sus sistemas de Banca por Internet.  

Aspose.Cells te permite cifrar y proteger con contraseña archivos de Microsoft Excel con el tipo de cifrado que desees.  
{{% /alert %}}  

## **Usar Microsoft Excel**  

Para configurar los ajustes de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):  

1. Desde el menú **Herramientas**, selecciona **Opciones**. Aparecerá un cuadro de diálogo.  
2. Selecciona la pestaña **Seguridad**.  
3. Ingresa una contraseña y haz clic en **Avanzado**  
4. Elija el tipo de cifrado y confirme la contraseña.  

## **Cifrar archivo Excel con Aspose.Cells for Node.js via C++**  

El siguiente ejemplo muestra cómo cifrar y proteger por contraseña un archivo Excel usando la API Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

### **Especificando la opción de contraseña para modificar**  

El siguiente ejemplo muestra cómo establecer la opción de **Contraseña para modificar** en Microsoft Excel para un archivo existente utilizando la API de Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Descifrar archivo Excel con Aspose.Cells for Node.js via C++**  
Es muy fácil abrir un archivo Excel protegido por contraseña y descifrarlo usando la API Aspose.Cells como se muestra en el siguiente código:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **Temas avanzados**  
- [Encriptar y Desencriptar archivos ODS](/cells/es/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Configurar Tipo de Encriptación Fuerte](/cells/es/nodejs-cpp/setting-strong-encryption-type/)  
- [Especificar Autor al Proteger la Escritura del Libro de Trabajo](/cells/es/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Verificar Contraseña de Archivos Encriptados](/cells/es/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


