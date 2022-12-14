---
title: Cifrar y descifrar archivos de Excel
type: docs
weight: 10
url: /es/python-java/encrypt-and-decrypt-excel-files/
description: Cómo cifrar y descifrar archivos de Excel usando Python. Bloquear y desbloquear archivos de Excel.
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) le permite cifrar y proteger con contraseña sus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits. Eso se considera un cifrado débil. Para un cifrado fuerte, se requiere una longitud de clave mínima de 128 bits. Microsoft Windows contiene CSP que también ofrecen tipos de cifrado fuertes, por ejemplo, el 'Microsoft Proveedor criptográfico fuerte'. Para que te hagas una idea, el cifrado de 128 bits es el que utilizan los bancos para cifrar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells para Python le permite encriptar y proteger con contraseña Microsoft archivos de Excel con el tipo de encriptación que desee.

{{% /alert %}}

## **Usando Microsoft Excel**

Para establecer la configuración de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1.  Desde el**Instrumentos** menú, seleccione**Opciones**Aparecerá un cuadro de diálogo.
1.  Selecciona el**Seguridad** pestaña.
1.  Introduzca una contraseña y haga clic en**Avanzado**
1. Elija el tipo de encriptación y confirme la contraseña.

## **Cifrado de archivo de Excel con Aspose.Cells**

El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel utilizando Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Descifrar archivo de Excel con Aspose.Cells**
Es muy bueno abrir un archivo de Excel protegido con contraseña y descifrarlo usando el Aspose.Cells API como los siguientes códigos:

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}


