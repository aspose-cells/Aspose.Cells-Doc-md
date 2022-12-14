---
title: Cifrar y descifrar archivos de Excel
type: docs
weight: 40
url: /es/java/encrypt-and-decrypt-excel-files/
description: Cómo cifrar y descifrar archivos de Excel usando Java. Bloquear y desbloquear archivos de Excel.
---
{{% alert color="primary" %}}
Microsoft Excel (97 - 365) le permite cifrar/proteger con contraseña sus hojas de cálculo. Utiliza algoritmos proporcionados por Crypto Service Provider. Un Crypto Service Provider o CSP es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000" o "Cifrado semanal (XOR)". También es importante elegir una longitud de clave de cifrado adecuada. Algunos de los proveedores de servicios criptográficos no admiten más de 40 o 56 bits. Eso se considera un tipo de encriptación débil. Pero, para el tipo de cifrado fuerte, se requiere una longitud de clave mínima de 128 bits. Microsoft Windows contiene proveedores de servicios criptográficos que también ofrecen tipos de cifrado fuertes, por ejemplo, el 'Microsoft Proveedor criptográfico fuerte'. Para dar una idea, la encriptación de 128 bits es la que usan los bancos para encriptar la conexión con sus Sistemas de Banca por Internet. Aspose.Cells le permite encriptar/proteger con contraseña sus archivos de Excel con el tipo de encriptación que desee.

{{% /alert %}}

## **Usando MS Excel**

En MS Excel (por ejemplo, MS Excel 2003), para implementar la configuración de cifrado de archivos, puede intentar:

-  Desde el**Instrumentos** menú, seleccione**Opciones** y, a continuación, seleccione el**Seguridad** pestaña.
-  Aporte**Contraseña para abrir** y haga clic en el**Avanzado** botón.
- Elija el tipo de encriptación y confirme la contraseña.

![todo:imagen_alternativa_texto](encrypting-excel-files_1.png)

**Figura: Diálogo de opciones**

![todo:imagen_alternativa_texto](encrypting-excel-files_2.png)

**Figura: cuadro de diálogo Tipo de cifrado**

## **Cifrado de archivo de Excel**
El siguiente ejemplo muestra cómo puede cifrar/proteger con contraseña un archivo de Excel utilizando el Aspose.Cells API.

### **Código de muestra:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingFiles-EncryptingFiles.java" >}}


## **Descifrar archivo de Excel con Aspose.Cells**
Es muy bueno abrir un archivo de Excel protegido con contraseña y descifrarlo usando el Aspose.Cells API como los siguientes códigos:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Decrypt-Excel-File.java" >}}



