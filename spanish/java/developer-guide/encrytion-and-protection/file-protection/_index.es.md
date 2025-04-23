---
title: Cifrar y Descifrar archivos de Excel
type: docs
weight: 40
url: /es/java/encrypt-and-decrypt-excel-files/
description: Cómo encriptar y desencriptar archivos de Excel usando Java. Bloquear y desbloquear archivos de Excel.
---

{{% alert color="primary" %}}
Microsoft Excel (97 - 365) te permite cifrar / proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por el Proveedor de Servicios Criptográficos. Un Proveedor de Servicios Criptográficos o CSP es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000" o "Cifrado Semanal (XOR)". También es importante elegir una longitud de clave de cifrado adecuada. Algunos Proveedores de Servicios Criptográficos no admiten más de 40 o 56 bits. Eso se considera un tipo de cifrado débil. Pero, para un tipo de cifrado fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene Proveedores de Servicios Criptográficos que ofrecen tipos de cifrado fuertes, por ejemplo, el 'Proveedor Criptográfico Fuerte de Microsoft'. Para darte una idea, el cifrado de 128 bits es lo que los bancos usan para cifrar la conexión con sus Sistemas de Banca por Internet. Aspose.Cells te permite cifrar / proteger con contraseña tus archivos de Excel con el tipo de cifrado deseado.

{{% /alert %}}

## **Usando MS Excel**

En MS Excel (por ejemplo, MS Excel 2003), para implementar la configuración de cifrado de archivos, puedes intentar:

- Desde el menú **Herramientas**, selecciona **Opciones**, y luego selecciona la pestaña **Seguridad**.
- Ingresa la **Contraseña para abrir** y haz clic en el botón **Avanzadas**.
- Elige el tipo de cifrado y confirma la contraseña.

![todo:image_alt_text](encrypting-excel-files_1.png)

**Figura: Cuadro de diálogo de Opciones**

![todo:image_alt_text](encrypting-excel-files_2.png)

**Figura: Cuadro de diálogo de Tipo de Cifrado**

## **Cifrado de archivo de Excel**
El siguiente ejemplo muestra cómo puedes cifrar/proteger con contraseña un archivo de Excel utilizando la API de Aspose.Cells.

### **Código de Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Descifrar archivo Excel con Aspose.Cells**
Es muy abrir un archivo de Excel protegido por contraseña y descifrarlo usando la API de Aspose.Cells como los siguientes códigos:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



{{< app/cells/assistant language="java" >}}
