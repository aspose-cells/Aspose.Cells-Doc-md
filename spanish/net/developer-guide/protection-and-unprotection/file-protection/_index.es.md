---
title: Cifrar y Descifrar archivos de Excel
type: docs
weight: 10
url: /es/net/encrypt-and-decrypt-excel-files/
description: Cómo cifrar y descifrar archivos de Excel usando C#. Bloquear y desbloquear archivos de Excel.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) te permite cifrar y proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits, considerándose un cifrado débil. Para un cifrado fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene CSP que ofrecen tipos de cifrado fuertes, como por ejemplo el 'Proveedor Criptográfico Fuerte de Microsoft'. Para darte una idea, los bancos utilizan un cifrado de 128 bits para encriptar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells te permite cifrar y proteger con contraseña archivos de Microsoft Excel con el tipo de cifrado que desees.

{{% /alert %}}

## **Usar Microsoft Excel**

Para configurar los ajustes de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**. Aparecerá un cuadro de diálogo.
1. Selecciona la pestaña **Seguridad**.
1. Ingresa una contraseña y haz clic en **Avanzado**.
1. Elige el tipo de cifrado y confirma la contraseña.

## **Cifrar archivo de Excel con Aspose.Cells**

El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel utilizando la API de Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Especificar la opción de Contraseña para modificar**

El siguiente ejemplo muestra cómo establecer la opción de **Contraseña para modificar** en Microsoft Excel para un archivo existente utilizando la API de Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Descifrar archivo Excel con Aspose.Cells**
Es muy abrir un archivo de Excel protegido por contraseña y descifrarlo usando la API de Aspose.Cells como los siguientes códigos:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Temas avanzados**
- [Encriptar y Desencriptar archivos ODS](/cells/es/net/encrypt-and-decrypt-ods-files/)
- [Configurar Tipo de Encriptación Fuerte](/cells/es/net/setting-strong-encryption-type/)
- [Especificar Autor al Proteger la Escritura del Libro de Trabajo](/cells/es/net/specify-author-while-write-protecting-workbook/)
- [Verificar Contraseña de Archivos Encriptados](/cells/es/net/verify-password-of-encrypted-excel-and-ods-files/)

