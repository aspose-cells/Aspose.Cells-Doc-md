---
title: Establecer Tipo de Cifrado Fuerte
type: docs
weight: 60
url: /es/python-net/setting-strong-encryption-type/
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) te permite cifrar y proteger con contraseña hojas de cálculo. Utiliza algoritmos proporcionados por un Proveedor de Servicios Criptográficos. Un Proveedor de Servicios Criptográficos (o CSP) es un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es "Compatible con Office 97/2000". Este es un CSP con algunos problemas de seguridad conocidos públicamente. Las hojas de cálculo aseguradas con el cifrado "débil (XOR)" o con el tipo de cifrado "Compatible con Office 97/2000" pueden ser descifradas fácilmente.

Para superar este problema, utiliza uno de los tipos de cifrado fuerte proporcionados por Microsoft Excel. Puedes cambiar el tipo de cifrado al CSP más fuerte disponible. Para el cifrado fuerte, se requiere una longitud mínima de clave de 128 bits, por ejemplo, 'Proveedor Criptográfico Fuerte de Microsoft'.

También puedes cifrar y proteger con contraseña archivos de Excel con un tipo de cifrado fuerte usando la API Aspose.Cells para Python via .NET.

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


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SettingStrongEncryptionType-1.py" >}}

